"""Make a complete file-browser preview and a clean downloadable source project."""
from pathlib import Path
import shutil,re,os,zipfile
root=Path(__file__).resolve().parents[1];dist=root/'dist';out=root/'preview/full-site'
if out.exists():shutil.rmtree(out)
shutil.copytree(dist,out)
def relative_url(url,current):
 if not url.startswith('/') or url.startswith('//'):return url
 path,sep,hashpart=url.partition('#');pathname,querysep,query=path.partition('?')
 target=out/pathname.lstrip('/')
 if pathname.endswith('/'):target=target/'index.html'
 elif target.is_dir():target=target/'index.html'
 rel=os.path.relpath(target,current.parent).replace(os.sep,'/')
 return rel+('?' +query if querysep else '')+('#'+hashpart if sep else '')
for p in out.rglob('*.html'):
 s=p.read_text()
 # Local-file previews cannot reliably display third-party subscription frames.
 # Keep the hosted site's native form; give the portable preview a usable link.
 s=re.sub(r'<iframe\b[^>]*src="https://publicdomainpulppress\.substack\.com/embed"[^>]*>\s*</iframe>', '<div style="padding:28px;border:1px solid #c5a880;border-radius:3px;margin-bottom:18px"><p style="margin-bottom:18px">Get new books, sample chapters, and news from Public Domain Pulp.</p><a class="button" href="https://substack.com/@publicdomainpulppress">Subscribe on Substack ↗</a></div>', s)
 s=re.sub(r'\b(href|src|action)="(/[^\"]*)"',lambda m:m[1]+'="'+relative_url(m[2],p)+'"',s)
 p.write_text(s)
for p in out.rglob('*.css'):
 s=p.read_text();s=re.sub(r'url\(([\"\x27]?)(/[^)\"\x27]+)\1\)',lambda m:'url('+m[1]+relative_url(m[2],p)+m[1]+')',s);p.write_text(s)
# Node project sources only; no dependencies, research notebooks, or obsolete prototypes.
files=[]
for folder in ['src','public','scripts','docs/website','content/books','content/series','content/authors','content/editions','content/assets','content/journal','content/settings','content/lines']:
 files += [p for p in (root/folder).rglob('*') if p.is_file() and (folder!='scripts' or p.name in ['check-content.mjs','check-site.mjs','create-cms-config.py','package-preview.py'])]
files += [root/'content/approval'/name for name in ['catalog.schema.json','catalog.draft.json']]
files += [root/name for name in ['package.json','pnpm-lock.yaml','pnpm-workspace.yaml','astro.config.mjs','netlify.toml','.gitignore','.env.example','README.md']]
files=[p for p in files if p.is_file() and p.suffix not in ['.pyc'] and '__pycache__' not in p.parts]
with zipfile.ZipFile(root/'PublicDomainPulp_Website_Source.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in dict.fromkeys(files):z.write(p,p.relative_to(root))
with zipfile.ZipFile(root/'PublicDomainPulp_Website_Preview.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in out.rglob('*'):
  if p.is_file():z.write(p,p.relative_to(out))
print('Created portable full-site preview, preview ZIP and source ZIP.')
