#!/usr/bin/env python3
"""LI-003A local-only static and browser checks. Requires beautifulsoup4 and playwright."""
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlsplit
import json, threading, sys, os
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent.parent/'web'
ROUTES=['index','sources','methodology','about','privacy','cookies','terms','data-policy']
LOCALES=['en','pl','nl']
PAGES=[(l,r,('' if l=='en' else l+'/')+r+'.html') for l in LOCALES for r in ROUTES]
def static():
    checks=0
    for lang,route,rel in PAGES:
        p=ROOT/rel; s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
        assert s.html['lang']==lang and len(s.find_all('h1'))==1,rel
        assert all(len(s.find_all(t))==1 for t in ('main','header','footer')),rel
        assert s.find('meta',attrs={'name':'robots'})['content']=='noindex, nofollow'
        assert s.select_one('a.skip-link')['href']=='#main-content'
        assert not s.find_all(['script','form','iframe','img']),rel
        if route in ROUTES[4:]: assert s.select_one('.draft-panel'),rel
        for a in s.find_all(['a','link']):
            h=a.get('href','')
            if h=='data:,': continue
            if h.startswith('#'): assert s.find(id=h[1:]); continue
            u=urlsplit(h); assert not u.scheme and not h.startswith('/'),(rel,h)
            d=(p.parent/u.path).resolve(); assert d.is_relative_to(ROOT) and d.is_file(),(rel,h)
            checks+=1
        langs=s.select('.locale-nav a'); assert {a['hreflang'] for a in langs}==set(LOCALES),rel
        for a in langs:
            assert (p.parent/a['href']).resolve()==(ROOT/('' if a['hreflang']=='en' else a['hreflang']+'/')/(route+'.html')).resolve(),rel
    return checks
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*a,**kw): super().__init__(*a,directory=str(ROOT),**kw)
    def translate_path(self,p): return super().translate_path(p[len('/LivingIndex'):] if p.startswith('/LivingIndex/') else p)
    def log_message(self,*args): pass

def browser_checks(out):
    from playwright.sync_api import sync_playwright
    server=ThreadingHTTPServer(('127.0.0.1',0),Handler);threading.Thread(target=server.serve_forever,daemon=True).start()
    base=f'http://127.0.0.1:{server.server_port}'; checks=ax=keyboard=zoom=0;errors=[]
    try:
        with sync_playwright() as pw:
            browser=pw.chromium.launch(executable_path=os.environ.get('CHROMIUM_PATH') or None)
            ctx=browser.new_context(reduced_motion='reduce');page=ctx.new_page();cdp=ctx.new_cdp_session(page)
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None)
            page.on('requestfailed',lambda r:errors.append(r.url+' failed'))
            page.on('response',lambda r:errors.append(f'{r.status}: {r.url}') if r.status>=400 else None)
            page.on('request',lambda r:errors.append('External: '+r.url) if not r.url.startswith(base+'/') and not r.url.startswith('data:') else None)
            for prefix in ('','/LivingIndex'):
                for lang,route,rel in PAGES:
                    for width in (320,768,1440):
                        page.set_viewport_size({'width':width,'height':900});page.goto(base+prefix+'/'+rel,wait_until='load')
                        assert page.locator('h1').count()==1
                        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(rel,width,'overflow')
                        assert page.evaluate('document.cookie === "" && localStorage.length === 0 && sessionStorage.length === 0'),rel
                        checks+=1
                        if width==768 and prefix=='':
                            roles=[n.get('role',{}).get('value') for n in cdp.send('Accessibility.getFullAXTree')['nodes'] if not n.get('ignored')]
                            assert all(r in roles for r in ('main','banner','contentinfo','heading','navigation')) and roles.count('navigation')==3,(rel,roles)
                            ax+=1
                        if route=='index' and prefix=='':
                            page.keyboard.press('Tab'); assert page.locator(':focus').get_attribute('class')=='skip-link',(rel,width)
                            assert page.locator(':focus').evaluate('(e)=>getComputedStyle(e).outlineStyle')!='none'
                            page.keyboard.press('Enter');assert page.locator(':focus').get_attribute('id')=='main-content'
                            page.keyboard.press('Tab');assert page.locator(':focus').get_attribute('href')=='methodology.html'
                            keyboard+=1
                            if lang=='en' and width in (320,1440):
                                page.goto(base+'/'+rel);page.screenshot(path=str(out/f'li003-home-{width}.png'),full_page=True)
                    if prefix=='':
                        page.set_viewport_size({'width':1280,'height':900});page.goto(base+'/'+rel);page.evaluate('document.body.style.zoom="200%"')
                        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(rel,'200% CSS zoom overflow')
                        zoom+=1
            assert not ctx.cookies(),ctx.cookies()
            assert not errors,errors
            page.set_viewport_size({'width':1440,'height':900});page.goto(base+'/pl/privacy.html');page.screenshot(path=str(out/'li003-privacy-pl.png'),full_page=True)
            browser.close()
    finally: server.shutdown();server.server_close()
    return dict(browser_page_viewport_checks=checks,accessibility_tree_checks=ax,keyboard_checks=keyboard,css_zoom_200_checks=zoom,network_console_storage_errors=errors)
if __name__=='__main__':
    out=Path(next((arg for arg in sys.argv[1:] if not arg.startswith('--')),str(ROOT.parent/'evidence')));out.mkdir(exist_ok=True,parents=True)
    r=dict(pages=len(PAGES),static_relative_links_assets=static())
    if '--static-only' not in sys.argv: r.update(browser_checks(out))
    print(json.dumps(r,indent=2));(out/'result.json').write_text(json.dumps(r,indent=2)+'\n')
