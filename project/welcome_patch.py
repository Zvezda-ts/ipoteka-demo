# Вставляет приветственный экран с видео-петлёй в версию демо для сайта (index.html)
WEL_CSS='''
.wel{position:fixed;inset:0;z-index:200;background:rgba(12,13,24,.78);backdrop-filter:blur(6px);display:flex;align-items:center;justify-content:center;padding:max(16px,env(safe-area-inset-top,0px)) max(16px,env(safe-area-inset-right,0px)) max(16px,env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px))}
.wel-box{background:var(--side);border:1px solid var(--line);border-radius:18px;max-width:880px;width:100%;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.6);display:flex;flex-direction:column}
.wel-box video{width:100%;max-width:100%;height:auto;aspect-ratio:16/9;display:block;background:#1a1d2e url(poster.jpg) center/cover no-repeat;object-fit:cover}
.wel-body{padding:20px 24px 24px;display:flex;flex-wrap:wrap;gap:14px 20px;align-items:center;justify-content:space-between}
.wel-body h2{margin:0;font-size:22px;font-weight:700} .wel-body p{margin:4px 0 0;color:var(--muted);font-size:14.5px;max-width:52ch}
.howbtn{display:flex;align-items:center;gap:8px;justify-content:center}
@media (max-width:900px){.howbtn{display:none}}
'''
WEL_HTML='''<div class="wel" id="welcome" hidden role="dialog" aria-modal="true" aria-labelledby="welT">
  <div class="wel-box">
    <video id="welVid" width="1280" height="720" src="loop.mp4" poster="poster.jpg" autoplay muted loop playsinline preload="auto" aria-label="Как работает дашборд"></video>
    <div class="wel-body">
      <div><h2 id="welT">Ипотечный консультант на ИИ</h2><p>Разбор договора клиента и расчёт выгоды за пару минут. Дальше демо на выдуманном договоре, всё можно нажимать и двигать.</p></div>
      <button class="btn main" id="welGo" type="button">Открыть демо</button>
    </div>
  </div>
</div>
'''
WEL_JS='''
(function(){const W=el('welcome'),V=el('welVid');
  const open=()=>{W.hidden=false;try{V.currentTime=0;const pr=V.play();if(pr&&pr.catch)pr.catch(()=>{})}catch(e){}setTimeout(()=>el('welGo').focus(),50)};
  const close=()=>{W.hidden=true;try{V.pause()}catch(e){}try{localStorage.setItem('demo-welcome-seen','1')}catch(e){}};
  el('welGo').onclick=close;W.addEventListener('click',e=>{if(e.target===W)close()});
  addEventListener('keydown',e=>{if(e.key==='Escape'&&!W.hidden)close()});
  el('howBtn').onclick=open;
  let seen=false;try{seen=!!localStorage.getItem('demo-welcome-seen')}catch(e){}
  if(!seen)open();
})();
'''
def apply(s):
    s=s.replace('@media (prefers-reduced-motion:reduce)',WEL_CSS+'@media (prefers-reduced-motion:reduce)',1)
    s=s.replace('<div id="report" aria-hidden="true"></div>',WEL_HTML+'<div id="report" aria-hidden="true"></div>',1)
    s=s.replace('<div class="clearbox">','<button class="btn sec small howbtn" id="howBtn" type="button">▶ Как это работает</button>\n      <div class="clearbox">',1)
    s=s.replace('(function initAI(){',WEL_JS+'\n(function initAI(){',1)
    assert s.count('welcome')>=2 and 'howBtn' in s
    return s
