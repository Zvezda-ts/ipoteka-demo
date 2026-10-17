import sys,os,shutil,time
from playwright.sync_api import sync_playwright
MODE=sys.argv[1]  # h | v
DEMO='file://'+os.path.abspath('ipoteka_demo_index.html')
if MODE=='h': VP={'width':1280,'height':720}; DSF=1.5; SIZE={'width':1920,'height':1080}
else: VP={'width':405,'height':720}; DSF=2.6667; SIZE={'width':1080,'height':1920}
OVER=r"""
(()=>{const st=document.createElement('style');st.textContent=`
#fx-cur{position:fixed;left:0;top:0;width:22px;height:22px;border-radius:50%;background:rgba(243,228,107,.9);box-shadow:0 0 0 6px rgba(243,228,107,.25);z-index:99999;pointer-events:none;transform:translate(-50%,-50%);transition:transform .12s, opacity .3s}
#fx-cur.down{transform:translate(-50%,-50%) scale(.7)}
#fx-cap{position:fixed;left:50%;transform:translateX(-50%);__POS__;z-index:99998;background:rgba(36,34,58,.92);color:#fff;border:2px solid #9b7fd8;border-radius:16px;padding:14px 26px;font:700 __FS__px Onest,system-ui,sans-serif;text-align:center;max-width:92vw;box-shadow:0 20px 50px rgba(0,0,0,.5);opacity:0;transition:opacity .35s, transform .35s}
#fx-cap.on{opacity:1}
#fx-card{position:fixed;inset:0;z-index:100000;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;text-align:center;padding:30px;background:radial-gradient(circle at 70% 20%,#4b3596,#1a1d2e 65%);color:#fff;font-family:Onest,system-ui,sans-serif;opacity:0;transition:opacity .5s;pointer-events:none}
#fx-card.on{opacity:1}
#fx-card h1{margin:0;font-size:__H1__px;font-weight:800;line-height:1.1;letter-spacing:-.01em}
#fx-card p{margin:0;font-size:__P__px;color:#cdbdf0;max-width:900px}
#fx-card .url{background:#f3e46b;color:#24223a;font-weight:700;border-radius:999px;padding:10px 24px;font-size:__U__px}
#fx-card .logo{width:__L__px;height:__L__px;border-radius:22%;background:linear-gradient(135deg,#7a5cc4,#9b7fd8);display:grid;place-items:center}
`;document.head.appendChild(st);
const c=document.createElement('div');c.id='fx-cur';document.body.appendChild(c);
addEventListener('mousemove',e=>{c.style.left=e.clientX+'px';c.style.top=e.clientY+'px'},true);
addEventListener('mousedown',()=>c.classList.add('down'),true);addEventListener('mouseup',()=>c.classList.remove('down'),true);
const cap=document.createElement('div');cap.id='fx-cap';document.body.appendChild(cap);
const card=document.createElement('div');card.id='fx-card';document.body.appendChild(card);
window.fxCap=t=>{if(!t){cap.classList.remove('on');return}cap.classList.remove('on');setTimeout(()=>{cap.textContent=t;cap.classList.add('on')},180)};
window.fxCard=(h)=>{if(!h){card.classList.remove('on');return}card.innerHTML=h;card.classList.add('on')};
})();
"""
if MODE=='h': OVER=OVER.replace('__POS__','bottom:34px').replace('__FS__','26').replace('__H1__','64').replace('__P__','28').replace('__U__','26').replace('__L__','92')
else: OVER=OVER.replace('__POS__','top:16px').replace('__FS__','17').replace('__H1__','36').replace('__P__','18').replace('__U__','15').replace('__L__','72')
LOGO='<div class="logo"><svg width="55%" height="55%" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg></div>'

with sync_playwright() as p:
    b=p.chromium.launch()
    ctx=b.new_context(viewport=VP,device_scale_factor=DSF,record_video_dir='raw_'+MODE,record_video_size=SIZE)
    pg=ctx.new_page()
    pg.goto(DEMO); pg.wait_for_load_state('networkidle'); pg.evaluate(OVER)
    w=lambda ms: pg.wait_for_timeout(ms)
    def move_to(sel,steps=25,click=True):
        box=pg.locator(sel).first.bounding_box()
        x=box['x']+box['width']/2; y=box['y']+box['height']/2
        pg.mouse.move(x,y,steps=steps)
        if click: pg.mouse.down(); w(90); pg.mouse.up()
    def tab(name):
        loc=pg.locator(f'.tab[data-tab="{name}"]')
        loc.scroll_into_view_if_needed(); w(150)
        move_to(f'.tab[data-tab="{name}"]')
    cap=lambda t: pg.evaluate('t=>fxCap(t)',t)
    card=lambda h: pg.evaluate('h=>fxCard(h)',h)
    pg.mouse.move(VP['width']*0.6,VP['height']*0.5)
    card(LOGO+'<h1>Ипотечный консультант<br>на ИИ</h1><p>Разбор договора клиента и расчёт выгоды за пару минут</p>'); w(3000); card(None); w(600)
    # обзор
    cap('Сколько клиент переплачивает и сколько сэкономит'); w(1600)
    if MODE=='v': pg.locator('#extraRange').scroll_into_view_if_needed(); w(500)
    box=pg.locator('#extraRange').bounding_box(); y=box['y']+box['height']/2
    x0=box['x']+box['width']*0.1; x1=box['x']+box['width']*0.42
    pg.mouse.move(x0,y,steps=20); pg.mouse.down()
    for i in range(1,41): pg.mouse.move(x0+(x1-x0)*i/40,y); w(55)
    pg.mouse.up(); w(1400)
    if MODE=='v': pg.evaluate('scrollTo({top:0,behavior:"smooth"})'); w(900)
    # документы
    tab('docs'); cap('ИИ выписывает условия из договора: PDF, Word или фото'); w(2600)
    if MODE=='v': pg.evaluate('scrollTo({top:400,behavior:"smooth"})'); w(1500)
    # сроки
    tab('terms'); cap('Сроки с обратным отсчётом и пункты, где клиент теряет деньги'); w(2200)
    pg.evaluate('scrollTo({top:%d,behavior:"smooth"})'%(380 if MODE=='h' else 700)); w(2300)
    pg.evaluate('scrollTo({top:0,behavior:"smooth"})'); w(500)
    # рефинансирование
    tab('refi'); cap('Окупится ли рефинансирование'); w(900)
    move_to('#rfRate'); pg.keyboard.type('7,9',delay=160); w(1800)
    # вычет
    tab('tax'); cap('Налоговый вычет: сколько вернёт государство'); w(2400)
    # советы
    tab('tips'); cap('Персональная консультация и PDF-отчёт для клиента'); w(1500)
    pg.evaluate('scrollTo({top:%d,behavior:"smooth"})'%(420 if MODE=='h' else 900)); w(2400)
    cap(None); w(300)
    card(LOGO+'<h1>Соберу такую версию<br>под ваше агентство</h1><p>Ваш логотип и цвета, заявки с сайта, Telegram-бот</p><div class="url">zvezda-ts.github.io/ipoteka-demo</div>'); w(3800)
    vid=pg.video.path(); ctx.close(); b.close()
    shutil.move(vid,f'raw_{MODE}.webm'); print(vid)
