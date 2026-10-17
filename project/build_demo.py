import json
s=open('ipoteka_working.html',encoding='utf8').read()
def rep(a,b):
    global s
    assert a in s,'MISSING '+a[:70]; s=s.replace(a,b,1)

DEMO_CONTRACT={
 "loan_kind":"Ипотека на квартиру в новостройке","bank":"АО «Пример Банк» (выдуманный)","contract_date":"2023-03-15",
 "loan_amount":6200000,"property_price":7800000,"rate":9.6,"term_months":300,"payment_type":"аннуитетный","monthly_payment":54601,
 "program":None,"insurance":"Жизнь и здоровье заёмщика, после регистрации собственности ещё и сама квартира.","insurance_cost_year":24000,
 "rate_if_no_insurance":"+1 п.п. при отказе от страхования жизни","rate_increase_pp":1,"rate_increase_condition":"не продлить страхование жизни и здоровья",
 "early_repayment":"В любой день без комиссии, заявление в приложении за 1 рабочий день, минимальной суммы нет.",
 "rent_restrictions":"Пункт 4.1.9: сдавать квартиру в аренду и регистрировать в ней третьих лиц можно только с письменного согласия банка.",
 "rate_change":"Только при отказе от страхования жизни или если не оформить собственность в срок.","penalties":"0,06% от суммы просрочки за каждый день.",
 "schedule_balance":5945000,"schedule_balance_date":"2026-10-15","schedule_months_left":257,"tranches":None,
 "property_notes":"Дом сдан в июле 2026, акт приёма-передачи подписан, собственность ещё не оформлена.",
 "deadlines":[
  {"date":"2027-01-31","what":"Оформить право собственности на квартиру и передать банку закладную","penalty":"ставка вырастет на 2 п.п. до предоставления документов"},
  {"date":"2027-03-15","what":"Продлить полис страхования жизни и квартиры на следующий год","penalty":"ставка вырастет на 1 п.п."}],
 "red_flags":[
  {"title":"Ставка растёт сразу на 2 пункта","detail":"Если не оформить собственность к 31.01.2027, ставка поднимется до 11,6% (п. 4.3.2). Это плюс 8 тысяч к платежу каждый месяц."},
  {"title":"Страховку нужно продлевать каждый год","detail":"Банк повышает ставку уже со следующего платежа после окончания полиса (п. 4.1.7). Полис стоит продлевать заранее."},
  {"title":"Аренда только с согласия банка","detail":"Без письменного согласия банк вправе потребовать досрочного возврата всего кредита (п. 4.4.1)."}]}

DEMO_CONSULT="""### Главное про вашу ипотеку
Остаток 5 945 000 ₽ под 9,6%, платить ещё 21 год и 5 месяцев. Платёж 54 605 ₽, это 26% дохода семьи, нагрузка комфортная. Если ничего не менять, банк получит ещё около **8,1 млн ₽** процентов, и это без страховки.

### Что выгоднее именно вам
Доплата 5 000 ₽ в месяц с сокращением срока экономит около **2,1 млн ₽** процентов, ипотека закроется на 4 года 8 месяцев раньше. Сокращать платёж в вашем случае смысла мало: нагрузка и так невысокая, а экономия выйдет в разы меньше. Сейчас, в первые годы, каждый рубль доплаты работает сильнее всего.

### На что смотреть в договоре
- **Срок 31 января 2027.** До этой даты нужно оформить собственность и передать банку закладную. Опоздаете, ставка вырастет на 2 п.п., платёж станет около 62 765 ₽, это плюс 8 160 ₽ каждый месяц. Запишитесь в МФЦ уже в ноябре: регистрация и закладная занимают 3-5 недель.
- **Страховка жизни.** Без неё ставка +1 п.п., платёж вырос бы на 4 026 ₽, около 48 тысяч в год. Полис стоит 24 тысячи, держать его выгодно. Перед продлением в марте сравните цены у других аккредитованных страховых.
- **Досрочка** без комиссии и без минимальной суммы, заявление в приложении за день. Гасить можно хоть по 5 000.

### Сдача в аренду
Пункт 4.1.9: сдавать квартиру и прописывать жильцов можно только с письменного согласия банка. Если планируете сдавать, подайте заявление заранее и получите ответ на бумаге. Без согласия банк вправе потребовать вернуть весь кредит.

### Рефинансирование и вычет
Рефинансировать есть смысл, если найдёте ставку 8% и ниже: разница меньше 1,5 п.п. съестся расходами на переоформление. Вычет: квартира стоила 7,8 млн, за покупку вернётся 260 тысяч, за проценты до 390 тысяч. Право на вычет появилось с подписания акта в июле 2026, так что за 2026 год можно подать уже в начале 2027.

### План на ближайший месяц
- Записаться в МФЦ на регистрацию собственности и сразу заказать закладную в банке.
- Включить доплату 5 000 ₽ в месяц с сокращением срока.
- В январе подать 3-НДФЛ за 2026 год и направить возврат на досрочку.
- Поставить напоминание на март: сравнить цены страховки перед продлением."""

rep('<title>Ипотечный консультант</title>','<title>Ипотечный консультант (демо)</title>')
rep("const DEFAULTS={debt:4500000,rate:10.5,months:240,income:150000,extra:3000,ins:18000};","const DEFAULTS={debt:5945000,rate:9.6,months:257,income:210000,extra:5000,ins:24000};\nconst DEMO_CONTRACT="+json.dumps(DEMO_CONTRACT,ensure_ascii=False)+";\nconst DEMO_CONSULT="+json.dumps(DEMO_CONSULT,ensure_ascii=False)+";")
rep("const KEY='ipoteka-v1',XKEY='ipoteka-extra-v2',CKEY='ipoteka-contract-v1';","const KEY='demo-ipoteka-v1',XKEY='demo-ipoteka-extra-v2',CKEY='demo-ipoteka-contract-v1';")
rep("txPrice:'',txSalary:'',txPaid:'0'","txPrice:'7 800 000',txSalary:'120 000',txPaid:'0'")
# демо-плашка и подписи
rep('<div><b>Ипотечный консультант</b><span>персональный расчёт</span></div>','<div><b>Ипотечный консультант</b><span>демо-версия</span></div>')
rep('<div class="top">\n      <div>','<div class="top">\n      <div class="demo-pill">Демо: все данные и договор выдуманы</div>\n      <div style="flex-basis:100%;height:0"></div>\n      <div>')
rep('.mobile-only{display:none!important}','.mobile-only{display:none!important}\n.demo-pill{background:var(--yellow);color:var(--on-light);font-weight:600;font-size:12.5px;border-radius:999px;padding:4px 12px}')
rep('<div class="note" id="sampleNote" style="margin-top:12px">Сейчас стоят цифры для примера. Нажмите «Изменить данные» или загрузите договор во вкладке «Документы».</div>','<div class="note" id="sampleNote" style="margin-top:12px">Это демо: цифры взяты из выдуманного договора. Нажмите «Изменить данные» и подвигайте их, всё пересчитается сразу.</div>')
rep('<button class="btn ghost small" id="clearBtn" type="button">Очистить всё</button>','<button class="btn ghost small" id="clearBtn" type="button">Сбросить к примеру</button>')
rep('<p style="margin-bottom:8px">Удалятся все цифры, досрочки, разбор и консультация. Вернуть будет нельзя.</p>','<p style="margin-bottom:8px">Ваши изменения сотрутся, вернутся цифры примера.</p>')
rep('<div class="actions"><button class="btn danger small" id="clearYes" type="button">Да, очистить</button>','<div class="actions"><button class="btn danger small" id="clearYes" type="button">Да, сбросить</button>')
# демо-контракт и готовая консультация при запуске
rep("window.contract=fetchStore(CKEY);","window.contract=fetchStore(CKEY)||DEMO_CONTRACT;consultText=DEMO_CONSULT;el('consult').hidden=false;el('consult').innerHTML=md(DEMO_CONSULT);")
# без Claude: показываем пример разбора, а не заглушку
rep("function hideAI(){el('cUpload').hidden=true;el('cResult').hidden=true;el('cUnavailable').hidden=false;el('aiBar').hidden=true}",
"""function hideAI(){el('cUpload').hidden=true;el('cUnavailable').hidden=false;
  el('cUnavailable').textContent='Это демо: ниже пример того, что ИИ выписывает из договора за минуту. В рабочей версии сюда загружают договор и график платежей клиента, PDF, Word или фото страниц.';
  el('resetBtn').hidden=true;el('consultBtn').hidden=true;el('aiBar').querySelector('p').innerHTML='<b>Персональная консультация.</b> Ниже пример: так ИИ разбирает цифры и договор клиента. В рабочей версии она пишется заново по кнопке.';showContract()}""")
rep("  if(!w||!w.use){hideAI();el('reportBar').hidden=true;return}","  if(!w||!w.use){hideAI();return}")
rep("w.use('downloads').then(d=>{downloadsApi=d;el('reportBar').hidden=!d}).catch(()=>{el('reportBar').hidden=true});","w.use('downloads').then(d=>{downloadsApi=d}).catch(()=>{});")
# PDF без Claude: обычное скачивание
rep("    await downloadsApi.save({filename:'Ипотека расчёт и консультация.pdf',data:pdf.output('blob')});",
"""    const blob=pdf.output('blob'),fname='Ипотека расчёт и консультация (демо).pdf';
    if(downloadsApi)await downloadsApi.save({filename:fname,data:blob});
    else{const u=URL.createObjectURL(blob);const a=document.createElement('a');a.href=u;a.download=fname;document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(u),5000)}""")
# сброс: стереть и перезагрузить
rep("  el('clearYes').onclick=()=>{","  el('clearYes').onclick=()=>{try{[KEY,XKEY,CKEY].forEach(k=>localStorage.removeItem(k))}catch(e){}location.reload();return;")
open('ipoteka_demo_artifact.html','w',encoding='utf8').write(s)
# версия для хостинга: полный документ + приветственный экран с видео
import importlib.util,os
spec=importlib.util.spec_from_file_location('wp',os.path.join(os.path.dirname(os.path.abspath(__file__)),'welcome_patch.py'));wp=importlib.util.module_from_spec(spec);spec.loader.exec_module(wp)
s=wp.apply(s)
head='<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<meta name="description" content="Демо ипотечного консультанта: расчёт досрочки, рефинансирования и вычета, разбор договора ИИ, сроки и PDF-отчёт.">\n<meta property="og:title" content="Ипотечный консультант (демо)">\n<meta property="og:description" content="Расчёт досрочки, рефинансирования и вычета, разбор договора ИИ, сроки и PDF-отчёт.">\n<meta name="theme-color" content="#1a1d2e">\n</head>\n<body>\n'
open('ipoteka_demo_index.html','w',encoding='utf8').write(head+s+'\n</body>\n</html>\n')
print('ok',s.count('—'))
