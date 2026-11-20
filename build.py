# Podgląd mixhurt.com.pl (okrojony sklep TREG na wspólnym motywie z treg.pl - umowa § 2 ust. 4).
# Styl bazowy: ../Treg_koncept/src.html (wspólny motyw), nadpisany kolorem i znakiem z logo mixhurt.
# Nazwy, ceny i dostępność: aquaholm.pl (wg klienta obowiązujące), sprawdzone 20.11.2026.
import re, html as H
E = H.escape
treg = open('../Treg_koncept/src.html', encoding='utf-8').read()
STYL = re.search(r'<style>(.*?)</style>', treg, re.S).group(1)
STYL = STYL.replace('{{BADGE_STYLE}}', open('badge_style.part', encoding='utf-8').read().replace('<style>', '').replace('</style>', ''))
BLUE = '#3a50e6'
# znak z logo mixhurt: koło przecięte trzema poziomymi soczewkami
def znak(kol=BLUE, bg='#fff'):
    return (f'<svg viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="47" fill="{kol}"/>'
            f'<path d="M22 27Q50 13 78 27Q50 41 22 27Z" fill="{bg}"/><path d="M12 50Q50 33 88 50Q50 67 12 50Z" fill="{bg}"/><path d="M22 73Q50 59 78 73Q50 87 22 73Z" fill="{bg}"/></svg>')
def logo(tekst, kol=BLUE, bg='#fff'):
    return (f'<svg viewBox="0 0 330 100" role="img" aria-label="mixhurt"><circle cx="50" cy="50" r="47" fill="{kol}"/>'
            f'<path d="M22 27Q50 13 78 27Q50 41 22 27Z" fill="{bg}"/><path d="M12 50Q50 33 88 50Q50 67 12 50Z" fill="{bg}"/><path d="M22 73Q50 59 78 73Q50 87 22 73Z" fill="{bg}"/>'
            f'<rect x="121" y="8" width="4" height="84" fill="{kol}"/>'
            f'<text x="146" y="66" fill="{tekst}" font-family="Archivo,Arial,sans-serif" font-size="50" font-weight="400" letter-spacing="1">mixhurt</text></svg>')
import urllib.parse
ZN_URI = 'data:image/svg+xml,' + urllib.parse.quote(znak().replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"'))
open('img/favicon.svg', 'w', encoding='utf-8').write(znak().replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"'))

STYL += f'''
:root{{--aq:{BLUE};--aqd:#2b3fc4;--aqn:#0d1640;--apv:{BLUE};--apvd:#2b3fc4;--logo:{BLUE};--g:#eef1f6;--line:#d9dee8}}
.kw,.kw.aq,.kw.apv{{border:0;background:url("{ZN_URI}") center/contain no-repeat;width:.7em;height:.7em}}
.btn.aq::after,.btn.ciem::after{{border:0;width:16px;height:16px;background:url("{ZN_URI.replace('3a50e6', 'ffffff').replace('fill%3D%22%23fff%22', 'fill%3D%22%233a50e6%22')}") center/contain no-repeat}}
.btn.biel{{background:#fff;color:var(--aqn)}}.btn.biel::after{{width:16px;height:16px;background:url("{ZN_URI}") center/contain no-repeat}}.btn.biel:hover{{background:#e8ecfd}}
/* pierwszy ekran: granat z logo, tekst + zdjęcia w natywnym rozmiarze (brak zdjęć >= 1920 px, zob. RESEARCH.md) */
.mh{{position:relative;background:#0d1640;color:#fff;overflow:hidden}}
.mh::before{{content:"";position:absolute;right:-12vw;top:50%;width:62vw;aspect-ratio:1;transform:translateY(-50%);border-radius:50%;background:radial-gradient(circle at 50% 50%,#1b2a86 0,#14206a 60%,transparent 61%)}}
.mh .wrap{{position:relative;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.08fr);gap:clamp(28px,4vw,90px);align-items:center;min-height:calc(100svh - var(--hh));padding:clamp(40px,5vw,90px) 0}}
.mh .zn{{display:block;width:clamp(54px,4vw,84px);margin-bottom:clamp(18px,1.8vw,30px)}}
.mh h1{{font-size:clamp(38px,3.9vw,84px);font-stretch:90%;max-width:16ch;line-height:1.03}}
.mh p{{max-width:46ch;font-size:clamp(18px,1.25vw,23px);margin-top:clamp(16px,1.6vw,26px);color:#e1e5fb}}
.mh .akc{{display:flex;flex-wrap:wrap;gap:12px;margin-top:clamp(26px,2.4vw,40px)}}
.mh .cn{{display:flex;flex-wrap:wrap;gap:8px 26px;margin-top:clamp(24px,2.4vw,40px);font-weight:600;font-size:clamp(15px,.95vw,18px)}}
.mh .cn span{{display:inline-flex;align-items:center;gap:10px}}.mh .cn span::before{{content:"";width:14px;height:14px;background:url("{ZN_URI.replace('3a50e6', 'ffffff').replace('fill%3D%22%23fff%22', 'fill%3D%22%230d1640%22')}") center/contain no-repeat}}
.mh .fot{{position:relative;margin:0;padding-bottom:clamp(50px,6vw,120px)}}
.mh .fot .w{{width:100%;max-width:1600px;aspect-ratio:16/9;object-fit:cover;border-radius:50% 50% 50% 50% / 14% 14% 14% 14%;box-shadow:0 30px 70px rgba(0,0,0,.35)}}
.mh .fot .b{{position:absolute;left:-4%;bottom:0;width:min(40%,320px);background:#fff;padding:10px;border-radius:12px;box-shadow:0 18px 40px rgba(0,0,0,.35)}}
@media (max-width:900px){{.mh .wrap{{grid-template-columns:1fr;min-height:0;padding:44px 0 36px}}.mh::before{{width:120vw;right:-50vw;top:70%}}.mh .fot{{padding-bottom:56px}}.mh .fot .b{{width:38%;left:0}}}}
/* zakupy: mocna sekcja */
.zak{{background:#0d1640;color:#dfe3fa}}.zak h2{{color:#fff}}.zak .lead{{color:#c9cff4}}
.zak .info4 h3{{color:#fff;border-bottom-color:#5b6ce9}}.zak .info4 li::before{{border:0;width:12px;height:12px;top:.5em;background:url("{ZN_URI.replace('3a50e6', '8e9cf5').replace('fill%3D%22%23fff%22', 'fill%3D%22%230d1640%22')}") center/contain no-repeat}}
.firma2{{display:grid;grid-template-columns:1fr 1fr;gap:clamp(28px,4vw,80px);align-items:start}}
.firma2 .dane{{margin-top:18px;color:var(--mut);font-size:.95rem}}
@media (max-width:900px){{.firma2{{grid-template-columns:1fr}}}}
.mapa iframe{{width:100%;height:100%;border:0}}
'''

ZAM = ('zam', 'Na zamówienie, realizacja 30 dni'); JEST = ('jest', 'Dostępna'); BRAK = ('brak', 'Brak w magazynie')
WANNY = [
    ('w9014', 4, 1200, 600, 'Wanna A9014 Premium Line', '170 x 80 x 58 cm, dysze obrotowe, podgrzewacz wody, wodospad, Bluetooth, pilot', '6 990', '10 900', JEST, 'Wanna z hydromasażem A9014'),
    ('w9011', 3, 1200, 600, 'Wanna narożna A9011 Premium Line', '150 x 150 x 58 cm, Bluetooth, podgrzewacz wody, USB, pilot', '7 490', '11 900', JEST, 'Narożna wanna z hydromasażem A9011'),
    ('w8008', 4, 1200, 600, 'Wanna A9008 Premium Line', '180 x 120 x 59 cm, dysze obrotowe, podgrzewacz wody, wodospad, Bluetooth, pilot', '7 490', '11 900', ZAM, 'Biała prostokątna wanna z hydromasażem A9008'),
    ('w8008c', 4, 1200, 600, 'Czarna wanna A9008C Premium Line', '180 x 120 x 59 cm, dysze obrotowe, podgrzewacz wody, wodospad, Bluetooth, pilot', '7 490', '11 900', ZAM, 'Czarna prostokątna wanna z hydromasażem A9008C'),
    ('w9001', 4, 1200, 600, 'Wanna A9001 Premium Line', '170 x 78 x 60 cm, dysze obrotowe, podgrzewacz wody, wodospad, Bluetooth, pilot', '6 990', '11 250', ZAM, 'Prostokątna wanna z hydromasażem A9001'),
]
BIEZNIE = [
    ('futura', 1, 640, 360, 'Bieżnia APV8000 Futura Prestige 6 KM', 'ekran dotykowy Android 15,6", silnik 6 KM, pas 145 x 58 cm', '4 990', '7 290', ZAM, 'Bieżnia elektryczna APVsport APV8000 Futura Prestige'),
    ('premium', 1, 640, 360, 'Bieżnia APV8000 Premium Line 6 KM', 'ekran dotykowy Android 10,1", silnik 6 KM, pas 145 x 58 cm', '4 990', '7 290', ZAM, 'Bieżnia elektryczna APVsport APV8000 Premium Line'),
    ('top', 1, 640, 360, 'Bieżnia APV8000 Top Quality 6 KM', 'ekran dotykowy Android 10,1", silnik 6 KM, pas 145 x 58 cm', '4 990', '7 290', ZAM, 'Bieżnia elektryczna APVsport APV8000 Top Quality'),
    ('pas', 1, 640, 360, 'Pas piersiowy telemetryczny', 'pomiar tętna w czasie treningu na bieżni APV8000', '125', '139', JEST, 'Pas piersiowy do pomiaru tętna'),
    ('zestaw', 1, 640, 360, 'Zestaw dodatków do APV8000', 'masażer, twister, 2 hantle, rama do brzuszków, mata pod bieżnię, olej silikonowy', '499', '800', BRAK, 'Zestaw dodatków do bieżni APV8000'),
]

def karta(k, n, wd, wm, nazwa, opis, cena, stara, dost, alt):
    zd = []
    for i in range(1, n + 1):
        f = (lambda w: f'img/{k}-{i}-{w}.webp') if n > 1 else (lambda w: f'img/{k}-{w}.webp')
        a = 'src' if i == 1 else 'data-src'
        zd.append(f'<button class="zd" type="button" data-lb="{f(wd)}" aria-label="Powiększ zdjęcie {i} z {n}">'
                  f'<img {a}="{f(wm)}" width="600" height="450" loading="lazy" decoding="async" alt="{E(alt)}{"" if i == 1 else f", zdjęcie {i}"}"></button>')
    kropki = ''.join(f'<i{" class=on" if i == 0 else ""}></i>' for i in range(n)) if n > 1 else ''
    strz = '<span class="gs"><button type="button" class="gp" aria-label="Poprzednie zdjęcie"></button><button type="button" class="gn" aria-label="Następne zdjęcie"></button></span>' if n > 1 else ''
    st = f'<s>{stara} zł</s>' if stara else ''
    kup = '<button type="button" class="dok" data-kosz>Dodaj do koszyka</button>' if dost[0] != 'brak' else '<a class="dok pyt" href="#kontakt">Zapytaj o termin</a>'
    return (f'<article class="prod">\n  <div class="gal" data-grupa><div class="gt">{"".join(zd)}</div>{strz}<div class="kr" aria-hidden="true">{kropki}</div></div>\n'
            f'  <div class="pin"><h3><span class="kw"></span>{E(nazwa)}</h3><p class="po">{E(opis)}</p>\n'
            f'  <p class="dost {dost[0]}"><span class="b" aria-hidden="true"></span>{dost[1]}</p>\n'
            f'  <p class="cena"><b>{cena} zł</b>{st}</p>{kup}</div>\n</article>')

TEL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M3 5h18v14H3zM3 6l9 7 9-7"/></svg>'
PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><path d="M12 11.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z"/></svg>'

strona = f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Wanny z hydromasażem i bieżnie elektryczne | mixhurt.com.pl</title>
<meta name="description" content="Sklep mixhurt.com.pl: wanny z hydromasażem Aquaholm Premium Line i bieżnie elektryczne APVsport APV8000. Raty 0%, PayPo, BLIK, serwis w całym kraju. Tel. 503 538 038.">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="preload" as="image" href="img/ta-hero-1600.webp" imagesrcset="img/ta-hero-800.webp 800w, img/ta-hero-1600.webp 1600w" imagesizes="(max-width:760px) 100vw, 60vw" fetchpriority="high">
<link rel="preload" as="font" type="font/woff2" href="fonts/archivo-rdzen.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="fonts/archivo-pl.woff2" crossorigin>
<style>{STYL}</style>
</head>
<body>
<a class="skip" href="#tresc">Przejdź do treści</a>
<header class="top" id="top">
  <div class="wrap">
    <a class="logo" href="#start" aria-label="mixhurt, strona główna">{logo('#2a2f45')}</a>
    <nav class="menu" id="menu" aria-label="Menu" style="margin-left:auto">
      <a href="#wanny">Wanny z hydromasażem</a>
      <a href="#bieznie">Bieżnie elektryczne</a>
      <a href="#zakupy">Dostawa i serwis</a>
      <a href="#kontakt">Kontakt</a>
    </nav>
    <a class="tel" href="tel:+48503538038"><span>pon.-pt. 9:00-18:00</span>503 538 038</a>
    <a class="mtel" href="tel:+48503538038" aria-label="Zadzwoń: 503 538 038">{TEL}</a>
    <button class="burger" id="burger" type="button" aria-label="Otwórz menu" aria-expanded="false" aria-controls="menu"><span></span></button>
  </div>
</header>

<main id="tresc">
<section class="mh" id="start" aria-labelledby="h1">
  <div class="wrap">
    <div>
      <span class="zn">{znak('#ffffff', '#0d1640')}</span>
      <h1 id="h1">Wanny z hydromasażem i bieżnie elektryczne w jednym sklepie</h1>
      <p>Wanny Aquaholm Premium Line i bieżnie APVsport APV8000 od firmy TREG z Bielska Podlaskiego. Zamówienie przez sklep, telefon albo WhatsApp.</p>
      <div class="akc"><a class="btn aq" href="#wanny">Zobacz wanny</a><a class="btn biel" href="#bieznie">Zobacz bieżnie</a></div>
      <div class="cn"><span>Raty 0% i PayPo</span><span>Serwis w całym kraju</span><span>Dostawa kurierem</span></div>
    </div>
    <figure class="fot"><img class="w" src="img/ta-hero-1600.webp" srcset="img/ta-hero-800.webp 800w, img/ta-hero-1600.webp 1600w" sizes="(max-width:900px) 92vw, 50vw" width="1600" height="900" fetchpriority="high" decoding="async" alt="Narożna wanna z hydromasażem Aquaholm z podświetloną wodą"><img class="b" src="img/futura-640.webp" width="640" height="559" loading="lazy" decoding="async" alt="Bieżnia elektryczna APVsport APV8000 Futura Prestige"></figure>
  </div>
</section>

<section class="sek" id="wanny" aria-labelledby="h-wanny">
  <div class="wrap">
    <div class="sg">
      <div>
        <h2 id="h-wanny"><span class="kw"></span>Wanny z hydromasażem</h2>
        <p class="lead">Seria Aquaholm Premium Line: prostokątne i narożne, białe i czarne. W większości modeli dysze obrotowe, podgrzewacz wody, wodospad, Bluetooth i pilot.</p>
      </div>
      <div class="nav" data-nav="tw"><button type="button" data-k="-1" aria-label="Poprzednie wanny"></button><button type="button" data-k="1" aria-label="Następne wanny"></button></div>
    </div>
    <div class="tor" id="tw" data-tor>
{chr(10).join(karta(*x) for x in WANNY)}
    </div>
    <div class="pod"><p>Modele oznaczone „na zamówienie” mają czas realizacji 30 dni.</p><p class="zrodlo">Nazwy, ceny i dostępność z aquaholm.pl, sprawdzone 20.11.2026.</p></div>
  </div>
</section>

<section class="sek szary" id="bieznie" aria-labelledby="h-bieznie">
  <div class="wrap">
    <div class="sg">
      <div>
        <h2 id="h-bieznie"><span class="kw"></span>Bieżnie elektryczne</h2>
        <p class="lead">APVsport APV8000 z silnikiem 6 KM, pasem biegowym 145 x 58 cm i dotykowym ekranem Android, do tego pas do pomiaru tętna i zestaw dodatków.</p>
      </div>
      <div class="nav" data-nav="tb"><button type="button" data-k="-1" aria-label="Poprzednie bieżnie"></button><button type="button" data-k="1" aria-label="Następne bieżnie"></button></div>
    </div>
    <div class="tor" id="tb" data-tor>
{chr(10).join(karta(*x) for x in BIEZNIE)}
    </div>
    <div class="pod"><p>Bieżnie APV8000 realizujemy na zamówienie w 30 dni.</p><p class="zrodlo">Nazwy, ceny i dostępność z aquaholm.pl, sprawdzone 20.11.2026.</p></div>
  </div>
</section>

<section class="sek zak" id="zakupy" aria-labelledby="h-zak">
  <div class="wrap">
    <div class="sg"><div><h2 id="h-zak">Dostawa, płatności i serwis</h2><p class="lead">Zasady ze sklepu i regulaminu, tak samo dla wanien i bieżni.</p></div></div>
    <div class="info4">
      <div><h3>Dostawa</h3><ul><li>Kurierem, także przesyłki nadwymiarowe i bardzo ciężkie</li><li>W Polsce zwykle 1 dzień roboczy od nadania (deklaracja firmy kurierskiej)</li><li>Koszt dostawy doliczany według cennika</li></ul></div>
      <div><h3>Płatności</h3><ul><li>Raty 0%</li><li>PayPo: zapłata po 30 dniach</li><li>BLIK i przelew</li><li>Gotówką przy odbiorze</li></ul></div>
      <div><h3>Gwarancja i serwis</h3><ul><li>Dokument gwarancyjny, instrukcja montażu i obsługi w komplecie</li><li>Serwis gwarancyjny i pogwarancyjny w całym kraju, 33 punkty serwisowe</li><li>Magazyn części zamiennych</li></ul></div>
      <div><h3>Zwroty</h3><ul><li>14 dni na odstąpienie od umowy</li><li>Zwrot pieniędzy w ciągu 7 dni roboczych</li><li>Przesyłkę sprawdza się przy kurierze</li></ul></div>
    </div>
  </div>
</section>

<section class="sek" id="kontakt" aria-labelledby="h-kontakt">
  <div class="wrap firma2">
    <div>
      <h2 id="h-kontakt">Zadzwoń albo napisz</h2>
      <div class="kd">
        <a href="tel:+48503538038">{TEL}<span><b>503 538 038</b>poniedziałek-piątek 9:00-18:00</span></a>
        <a href="mailto:kontakt@mixhurt.com.pl">{MAIL}<span><b>kontakt@mixhurt.com.pl</b>odpowiadamy w dni robocze</span></a>
        <a href="https://wa.me/48660489335" target="_blank" rel="noopener">{TEL}<span><b>WhatsApp 660 489 335</b>pytania o model, termin i dostawę</span></a>
      </div>
      <p class="dane">Sprzedawca: TREG Łukasz Pawluczuk, ul. 30 Lipca 2, 17-100 Bielsk Podlaski, NIP 543-200-95-88, REGON 200140166.</p>
    </div>
    <div class="mapa" id="mapa" data-src="https://www.google.com/maps?q=ul.+30+Lipca+2,+17-100+Bielsk+Podlaski&amp;output=embed"></div>
  </div>
</section>
</main>

<footer class="stopka">
  <div class="wrap">
    <div class="g">
      <div><a class="logo" href="#start" aria-label="mixhurt">{logo('#ffffff', '#8e9cf5', '#1e2124')}</a><p style="margin-top:14px">Wanny z hydromasażem Aquaholm i bieżnie elektryczne APVsport. Sklep firmy TREG z Bielska Podlaskiego.</p></div>
      <div><h4>Sklep</h4><ul><li><a href="#wanny">Wanny z hydromasażem</a></li><li><a href="#bieznie">Bieżnie elektryczne</a></li><li><a href="#bieznie">Akcesoria do bieżni</a></li></ul></div>
      <div><h4>Zakupy</h4><ul><li><a href="#zakupy">Dostawa i płatności</a></li><li><a href="#zakupy">Gwarancja i serwis</a></li><li><a href="#zakupy">Zwroty</a></li></ul></div>
      <div><h4>Kontakt</h4><ul><li><a href="tel:+48503538038">503 538 038</a></li><li><a href="mailto:kontakt@mixhurt.com.pl">kontakt@mixhurt.com.pl</a></li><li>ul. 30 Lipca 2, Bielsk Podlaski</li></ul></div>
    </div>
    <div class="dol"><span>© <span id="rok">2026</span> TREG Łukasz Pawluczuk</span>{open('badge_link.part', encoding='utf-8').read().strip()}</div>
  </div>
</footer>
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Powiększone zdjęcie"><button class="x" type="button" aria-label="Zamknij"></button><button class="p" type="button" aria-label="Poprzednie zdjęcie"></button><img alt=""><p></p><button class="n" type="button" aria-label="Następne zdjęcie"></button></div>
<script src="app.js" defer></script>
<script src="wa.js" data-firma="mixhurt" data-kolor="#0d1640" defer></script>
</body>
</html>
'''
assert '{{' not in strona
open('index.html', 'w', encoding='utf-8').write(strona)
print('ok', len(strona))
