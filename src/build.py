# Wonder Nails build. Fonts: Sentient via Fontshare's own stylesheet (api.fontshare.com), nothing self-hosted. Design: Desire's mock (05-mockup/output/mock.html; brief Rev 2). Codor's job here is the live build, not a new layout.
import json, html, os
from PIL import Image
R='/workspace/sites/wonder-nails/'; B='/wonder-nails/'; SITE='https://answerfirstai-ai.github.io/wonder-nails/'
SRC='/workspace/clients/la-salon-wonder-nails/05-mockup/output/img/'; OUT=R+'assets/img/p/'; os.makedirs(OUT,exist_ok=True)
TEL='tel:+12136260315'; PHONE='(213) 626-0315'; IGH='wonder_nails_little_tokyo'; IG='https://www.instagram.com/wonder_nails_little_tokyo/'; DM='https://ig.me/m/wonder_nails_little_tokyo'
MAPS='https://www.google.com/maps/place/Wonder+Nails/data=!4m7!3m6!1s0x80c2c78119125139:0x593a7c165cf02c7f!8m2!3d34.0505137!4d-118.2414434!16s%2Fg%2F11g1kry8ds!19sChIJOVESGYHHwoARfyzwXBZ8Olk'
POST={'g':'DDf3A-yPxWP','h':'DDf3A-yPxWP','a':'DDf3A-yPxWP','b':'DQFotyEEl5F','l':'DAy86A0TzUL'}  # post each set came from (photos/social/manifest.csv)
def exp(name,widths):
  im=Image.open(SRC+name+'.jpg').convert('RGB'); ws=sorted({min(w,im.width) for w in widths})
  for w in ws:
    p=f'{OUT}{name}-{w}'
    if not os.path.exists(p+'.avif'):
      r=im if w==im.width else im.resize((w,round(im.height*w/im.width)),Image.LANCZOS); r.save(p+'.webp',quality=82); r.save(p+'.avif',quality=60)
  return dict(n=name,ws=ws,w=im.width,h=im.height)
IMG={n:exp(n,w) for n,w in {'galaxy':[480,800,1206],'holiday':[1206],'holiday-wide':[480,800,1206],'green-aura':[480,800,868],'galaxy-detail':[480,800,904],
 'burgundy':[480,800,1440],'burgundy-wide':[480,800,1200,1440],'lavender':[480,800,1427]}.items()}
def pic(n,alt,sizes,lazy=True,hi=False,style=''):
  d=IMG[n]; ss=lambda e:', '.join(f'{B}assets/img/p/{n}-{w}.{e} {w}w' for w in d['ws']); mid=d['ws'][min(1,len(d['ws'])-1)]
  at=(' fetchpriority="high"' if hi else '')+(' loading="lazy"' if lazy else '')+(f' style="{style}"' if style else '')
  return f'<picture><source type="image/avif" srcset="{ss("avif")}" sizes="{sizes}"><img src="{B}assets/img/p/{n}-{mid}.webp" srcset="{ss("webp")}" sizes="{sizes}" width="{d["w"]}" height="{d["h"]}" alt="{html.escape(alt)}"{at}></picture>'
# sets for the step-closer dialog: i -> big file, alt, caption, post
SETS=[('galaxy','Blue-black galaxy almond nails with silver flecks on white fur','Blue-black galaxy set.','g'),
 ('holiday','Dark green almond nails with dots, red nails with a tree, and a candy cane accent','Green and red holiday set.','h'),
 ('green-aura','Green aura almond nails with gold rims','Green aura with gold rims.','a'),
 ('burgundy','Short square burgundy nails with colour-block accent nails','Burgundy with colour-block accents.','b'),
 ('lavender','Lavender and white ombre nails on white fur','Lavender and white ombre.','l')]
VIEW=[dict(s=f'{B}assets/img/p/{n}-{IMG[n]["ws"][-1]}.webp',a=a,c=c,p=f'https://www.instagram.com/p/{POST[k]}/') for n,a,c,k in SETS]
def ext(href,text,cls=''): return f'<a{" class=%s"%chr(34)+cls+chr(34) if cls else ""} href="{href}" target="_blank" rel="noopener">{text}<span class="sr"> (opens in a new tab)</span></a>'
dm=ext(DM,'Message on Instagram','link')
CRED=ext(IG,'Photos: @'+IGH)
btn=lambda cls='',t='Call':f'<a class="btn{cls}" href="{TEL}">{t}</a>'
body=f'''<header>
  <a class="mark" href="#top">Wonder Nails</a>
  <nav aria-label="Sections"><a href="#sets">Sets</a><a href="#hours">Hours</a><a href="#visit">Visit</a></nav>
  {btn()}
</header>
<main id="top">
<section class="hero">
  <div class="hd"><h1>Wonder Nails</h1>
  <p class="tag">A nail salon in Little Tokyo, open every day.</p></div>
  <div class="left">
    <figure class="h-sq"><button class="print" data-i="4" aria-label="Look closer: lavender and white ombre set">{pic('lavender','Lavender and white ombre nails on white fur','(max-width:900px) 40vw, 16vw',lazy=False)}</button></figure>
    <div class="say">
      <p class="lede">A nail salon on East 1st Street in Little Tokyo, open every day.</p>
      <div class="acts">{btn('',f'Call {PHONE}')}<a class="link" href="#visit">Directions</a></div>
    </div>
  </div>
  <figure class="h-tall"><button class="print" data-i="0" aria-label="Look closer: blue-black galaxy set">{pic('galaxy','Blue-black galaxy almond nails with silver flecks on white fur','(max-width:900px) 72vw, min(31vw,600px)',lazy=False,hi=True)}</button></figure>
  <figure class="h-wide"><button class="print" data-i="3" aria-label="Look closer: burgundy set with colour-block accents">{pic('burgundy-wide','Short square burgundy nails with colour-block accent nails','(max-width:900px) 100vw, 36vw',lazy=False)}</button></figure>
  <p class="credit">Galaxy set, burgundy colour-block, lavender ombre. {CRED}</p>
</section>

<section class="sets" id="sets">
  <h2>Five small wonders</h2>
  <p class="intro fade">Every set here is from our Instagram, @{IGH}. Tap one to look closer.</p>
  <figure class="a1 fade"><button class="print" data-i="2" aria-label="Look closer: green aura set">{pic('green-aura','Green aura almond nails with gold rims','(max-width:900px) 72vw, min(33vw,430px)')}</button><figcaption>Green aura with gold rims.</figcaption></figure>
  <figure class="a2 fade"><button class="print" data-i="1" aria-label="Look closer: green and red holiday set">{pic('holiday-wide','Dark green almond nails with dots, red nails with a tree, and a candy cane accent','(max-width:900px) 100vw, min(46vw,600px)')}</button><figcaption>Green and red holiday set, with dots and a tree.</figcaption></figure>
  <p class="b-text fade">Blue-black with silver flecks, like a night sky. Call to ask what we can do for you today.</p>
  <figure class="b-print fade"><button class="print" data-i="0" aria-label="Look closer: galaxy set">{pic('galaxy-detail','Close view of blue-black galaxy almond nails','(max-width:900px) 60vw, 22vw')}</button><figcaption>Galaxy set, closer.</figcaption></figure>
</section>

<section class="hours" id="hours">
  <div class="t fade">
    <h2>Open every day</h2>
    <ul><li>Monday to Saturday, 10 to 7:30</li><li>Sunday, 10 to 6</li></ul>
    <div class="acts">{btn('',f'Call {PHONE}')}{dm}</div>
    <p class="note">Hours per the Google listing; call to confirm.</p>
  </div>
  <figure class="p fade"><button class="print" data-i="3" aria-label="Look closer: burgundy set">{pic('burgundy','Burgundy short square nails with colour-block accent nails','(max-width:900px) 60vw, 24vw',style='object-position:50% 40%')}</button></figure>
</section>

<section class="visit" id="visit">
  <figure class="w"><button class="print" data-i="0" aria-label="Look closer: galaxy set">{pic('galaxy','Blue-black galaxy almond nails','(max-width:900px) 100vw, 600px',style='aspect-ratio:16/10;object-position:50% 72%')}</button></figure>
  <div class="t">
    <h2>244 E 1st St, Little Tokyo</h2>
    <p>Call {PHONE} or get directions.</p>
    <div class="acts">{btn(' on-olive')}{ext(MAPS,'Directions','link')}{dm}</div>
  </div>
</section>
</main>
<footer><p>Wonder Nails · {ext(IG,'@'+IGH)} · <a href="{TEL}">{PHONE}</a></p><p>{CRED}. Hours per the Google listing; call to confirm.</p></footer>

<dialog id="view" aria-label="Closer look">
  <div class="close-view">
    <img id="vimg" src="" alt="">
    <div class="vbar"><p id="vcap"><span id="vtxt"></span> <a id="vlink" href="" target="_blank" rel="noopener">Photo: @wonder_nails_little_tokyo<span class="sr"> (opens Instagram)</span></a></p><div class="nav"><button id="prev" aria-label="Previous set">Previous</button><button id="next" aria-label="Next set" autofocus>Next</button><button id="x">Close</button></div></div>
  </div>
</dialog>
<script>window.WN_SETS={json.dumps(VIEW)}</script>'''
LD={"@context":"https://schema.org","@type":"NailSalon","@id":SITE+"#salon","name":"Wonder Nails","url":SITE,"telephone":"+1-213-626-0315","image":SITE+"assets/img/og.jpg",
 "address":{"@type":"PostalAddress","streetAddress":"244 E 1st St","addressLocality":"Los Angeles","addressRegion":"CA","postalCode":"90012","addressCountry":"US"},
 "geo":{"@type":"GeoCoordinates","latitude":34.0505137,"longitude":-118.2414434},"hasMap":MAPS,"areaServed":"Little Tokyo, Los Angeles","sameAs":[IG]}
TITLE='Wonder Nails | Nail Salon in Little Tokyo, Los Angeles'
DESC='Wonder Nails, 244 E 1st St in Little Tokyo, Los Angeles. Call (213) 626-0315 or message on Instagram.'
def page(path,body,title=TITLE,extra='',robots=''):
  return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(DESC)}">{robots}<link rel="canonical" href="{SITE}{path}">
<meta name="theme-color" content="#b4c0c9"><meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(DESC)}"><meta property="og:url" content="{SITE}{path}"><meta property="og:image" content="{SITE}assets/img/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Blue-black galaxy almond nails with silver flecks on white fur"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{B}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://api.fontshare.com"><link rel="preconnect" href="https://cdn.fontshare.com" crossorigin>
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=sentient@300,400,500&display=swap">{extra}
<link rel="stylesheet" href="{B}assets/css/site.css">
<script>document.documentElement.className+=' js'</script>
<script type="application/ld+json">{json.dumps(LD,ensure_ascii=False)}</script></head><body>{body}
<script src="{B}assets/js/site.js" defer></script></body></html>'''
d=IMG['galaxy']
pre=f'<link rel="preload" as="image" type="image/avif" imagesrcset="{", ".join(f"{B}assets/img/p/galaxy-{w}.avif {w}w" for w in d["ws"])}" imagesizes="(max-width:900px) 72vw, min(31vw,600px)" fetchpriority="high">'
open(R+'index.html','w').write(page('',body,extra=pre))
nf=f'<header><a class="mark" href="{B}">Wonder Nails</a><span></span>{btn()}</header><main><section class="hours"><div class="t"><h2>That page is not here.</h2><div class="acts"><a class="btn" href="{B}">Back to the sets</a></div></div></section></main>'
nf=nf.replace('<script','<script')
open(R+'404.html','w').write(page('404.html',nf,title='Page not found | Wonder Nails',robots='<meta name="robots" content="noindex">').replace(f'<link rel="canonical" href="{SITE}404.html">',''))
open(R+'sitemap.xml','w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{SITE}</loc><lastmod>2026-10-23</lastmod></url></urlset>')
open(R+'robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n'); open(R+'.nojekyll','w').write('')
# favicon + OG image (1200x630 crop of the hero set: source is 1206px wide, so no resampling up)
open(R+'assets/img/favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" fill="#2c3620"/><path d="M6 9l4.2 14L16 12l5.800 11L26 9" stroke="#e3e2da" stroke-width="2.600" stroke-linejoin="round" stroke-linecap="round" fill="none"/></svg>')
g=Image.open(SRC+'galaxy.jpg').convert('RGB'); y=int(os.environ.get('OGY','330')); g.crop((3,y,1203,y+630)).save(R+'assets/img/og.jpg',quality=84,optimize=True)
print('built')
