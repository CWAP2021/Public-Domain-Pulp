import fs from 'node:fs';import path from 'node:path';import Ajv2020 from 'ajv/dist/2020.js';import addFormats from 'ajv-formats';
const read=p=>JSON.parse(fs.readFileSync(p,'utf8'));const folder=name=>fs.readdirSync(`content/${name}`).filter(p=>p.endsWith('.json')).map(p=>read(`content/${name}/${p}`));
const base=read('content/approval/catalog.draft.json');const settings=read('content/settings/site.json');
export const catalog={...base,settings:{...base.settings,contactEmail:settings.contactEmail},books:folder('books'),series:folder('series'),authors:folder('authors'),editions:folder('editions'),assets:folder('assets'),publishingLines:folder('lines')};
const ajv=new Ajv2020({allErrors:true,strict:false});addFormats(ajv);const validate=ajv.compile(read('content/approval/catalog.schema.json'));const errors=[];
if(!validate(catalog))errors.push(...validate.errors.map(e=>`${e.instancePath}: ${e.message}`));
const maps=Object.fromEntries(['books','authors','series','editions','assets','publishingLines'].map(k=>[k,new Map(catalog[k].map(x=>[x.id,x]))]));
for(const [name,map] of Object.entries(maps))if(map.size!==catalog[name].length)errors.push(`Duplicate ${name} IDs`);
const check=(kind,id,context)=>{if(id&&!maps[kind].has(id))errors.push(`${context}: missing ${kind} reference ${id}`);};
const slots=new Set();
for(const b of catalog.books){
 check('assets',b.coverAssetId,b.id);check('assets',b.playlistQrAssetId,b.id);check('books',b.prequelToBookId,b.id);
 for(const c of b.contributors)check('authors',c.authorId,b.id);
 for(const m of b.seriesMemberships){check('series',m.seriesId,b.id);if(m.position!=null){const key=`${m.seriesId}/${m.position}`;if(slots.has(key))errors.push(`Duplicate series position ${key}`);slots.add(key);}}
 if(!b.description.paragraphs.length||!b.description.hook)errors.push(`Incomplete description: ${b.id}`);
 if(!catalog.editions.some(e=>e.bookId===b.id))errors.push(`No editions: ${b.id}`);
 if(!/^\/books\/[a-z0-9-]+\/$/.test(b.seo.canonicalPath))errors.push(`Invalid canonical path: ${b.id}`);
}
for(const e of catalog.editions){check('books',e.bookId,e.id);if(['available','preorder'].includes(e.publicationStatus)&&!e.links.some(l=>l.kind==='retailer'&&l.verification==='destination-verified'))errors.push(`No verified retailer: ${e.id}`);if(e.isbn13&&[...e.isbn13].reduce((s,n,i)=>s+Number(n)*(i%2?3:1),0)%10)errors.push(`Invalid ISBN: ${e.id}`);}
for(const s of catalog.series){check('publishingLines',s.publishingLineId,s.id);for(const k of ['publicationOrder','storyChronology'])for(const id of s[k]||[])check('books',id,s.id);check('books',s.recommendedStartingBookId,s.id);}
for(const a of catalog.assets)if(!fs.existsSync(path.join('public',a.path)))errors.push(`Missing image ${a.path}`);
for(const kind of ['books','series','authors']){const slugs=catalog[kind].map(x=>x.slug);if(new Set(slugs).size!==slugs.length)errors.push(`Duplicate ${kind} slugs`);}
if(settings.newsletter!=='https://substack.com/@publicdomainpulppress')errors.push('Primary newsletter differs from publisher instruction');
if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(settings.contactEmail))errors.push('Invalid feedback recipient');
if(process.env.PDP_PRODUCTION==='true'||process.argv.includes('--launch')){
 for(const key of ['launchApproved','editorialApproved','rightsApproved','privacyApproved'])if(!settings[key])errors.push(`Launch approval pending: ${key}`);
 for(const b of catalog.books){if(!['publisher-approved','published'].includes(b.approval.state)||!['publisher-approved','published'].includes(b.description.approval.state))errors.push(`Publisher copy approval pending: ${b.id}`);if(b.rightsReview?.status!=='publisher-cleared')errors.push(`Rights review pending: ${b.id}`);}
 for(const a of catalog.assets)if(a.rightsStatus!=='publisher-cleared')errors.push(`Asset approval pending: ${a.id}`);
}
if(errors.length){console.error(errors.join('\n'));process.exit(1);}console.log(`Content validated: ${catalog.books.length} books, ${catalog.series.length} series, ${catalog.editions.length} editions.`);
