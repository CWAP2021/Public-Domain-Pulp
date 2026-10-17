"""Generate Decap's local-editor form definitions from the linked content schema."""
import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1];schema=json.loads((root/'content/approval/catalog.schema.json').read_text());defs=schema['$defs']
labels={'id':'Stable ID (keep after first save)','slug':'Page address slug','catalogTeaser':'Catalog description','publicationStatus':'Publication status','literaryIdentification':'Character / literary identification','prequelToBookId':'Prequel to book','playlistQrAssetId':'Playlist QR image','chronologicalPosition':'Story chronology position','position':'Publication / series position','isbn13':'ISBN-13','asin':'Amazon ASIN','coverAssetId':'Cover image','pageCount':'Pages (edition-specific)'}
relations={'publishingLineId':('lines','name'),'authorId':('authors','displayName'),'seriesId':('series','name'),'bookId':('books','title'),'prequelToBookId':('books','title'),'recommendedStartingBookId':('books','title'),'coverAssetId':('assets','id'),'playlistQrAssetId':('assets','id'),'photoAssetId':('assets','id'),'socialImageAssetId':('assets','id')}
def fields(properties):return [field(k,v) for k,v in properties.items()]
def field(name,node):
 if '$ref' in node:node=defs[node['$ref'].split('/')[-1]]
 if 'anyOf' in node:node=next((x for x in node['anyOf'] if x.get('type')!='null'),node['anyOf'][0]);node=defs[node['$ref'].split('/')[-1]] if '$ref'in node else node
 nullable=isinstance(node.get('type'),list) and 'null' in node['type'];t=node.get('type');t=next((x for x in t if x!='null'),'string') if isinstance(t,list) else t
 f=dict(name=name,label=labels.get(name,re.sub(r'(?<!^)(?=[A-Z])',' ',name).title()),required=not nullable)
 if name=='sourceIds':return dict(name=name,widget='hidden',default=[])
 if name in relations:
  collection,display=relations[name];return dict(**f,widget='relation',collection=collection,search_fields=[display,'id'],display_fields=[display],value_field='id')
 if 'enum' in node:f.update(widget='select',options=node['enum'])
 elif t=='object':f.update(widget='object',fields=fields(node['properties']),collapsed=name in ['approval','rightsReview','seo'])
 elif t=='array':
  item=node.get('items',{});f.update(widget='list')
  if '$ref' in item:item=defs[item['$ref'].split('/')[-1]]
  if name in ['publicationOrder','storyChronology']:f.update(widget='relation',collection='books',multiple=True,search_fields=['title','id'],display_fields=['title'],value_field='id',required=False)
  elif item.get('type')=='object':f['fields']=fields(item['properties'])
  else:f['field']=dict(name='item',label='Item',widget='text' if name=='paragraphs' else 'string')
 elif t in ['integer','number']:f.update(widget='number',value_type='int' if t=='integer' else 'float',min=node.get('minimum',0))
 elif t=='boolean':f.update(widget='boolean')
 elif name in ['path']:f.update(widget='image')
 elif node.get('format')=='date':f.update(widget='datetime',format='YYYY-MM-DD',date_format='YYYY-MM-DD',time_format=False)
 else:f.update(widget='text' if name in ['description','bio','hook','catalogTeaser','notes','scope','evidence'] else 'string')
 return f
collections=[]
for name,definition,label,display in [('books','book','Books','title'),('lines','line','Publishing lines','name'),('series','series','Series','name'),('authors','author','Authors / pen names','displayName'),('editions','edition','Editions and retailer links','id'),('assets','asset','Images','id')]:
 collections.append(dict(name=name,label=label,preview_path='books/{{slug}}/' if name=='books' else '',folder='content/'+name,create=True,extension='json',format='json',identifier_field='id',slug='{{id}}',summary='{{'+display+'}}',fields=fields(defs[definition]['properties'])))
collections.append(dict(name='journal',label='Journal links',folder='content/journal',create=True,extension='json',format='json',identifier_field='id',slug='{{id}}',fields=[dict(name=k,label=k.title(),widget='text' if k=='description' else 'string') for k in ['id','title','category','date','label','url','description']]))
site=json.loads((root/'content/settings/site.json').read_text());settingsFields=[dict(name=k,label=k.title(),widget='boolean' if isinstance(v,bool) else 'string') for k,v in site.items()]
collections.append(dict(name='settings',label='Site settings',files=[dict(name='site',label='Publisher settings',file='content/settings/site.json',fields=settingsFields)]))
config=dict(local_backend=True,backend={'name':'git-gateway'},media_folder='public/uploads',public_folder='/uploads',collections=collections,load_config_file=False)
(root/'public/admin/config.json').write_text(json.dumps(config,indent=2)+'\n')
print('Generated local Decap collections with author/series/book/asset relationship pickers.')
