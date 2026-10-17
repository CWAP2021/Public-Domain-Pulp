import {live,site} from '../data/catalog';
export function GET(){return new Response(live?`User-agent: *\nAllow: /\nDisallow: /admin/\nSitemap: ${site.url}/sitemap.xml\n`:'User-agent: *\nDisallow: /\n',{headers:{'Content-Type':'text/plain'}});}
