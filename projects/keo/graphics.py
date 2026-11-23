"""Đồ hoạ video quảng cáo keo PELI — style công trình mạnh mẽ, màu thương hiệu cam + gold.
Chạy: python3 graphics.py <work_dir>  (tạo <work_dir>/overlay.html)"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "pipeline", "gfx"))
from lib import load_captions, _ff

W = sys.argv[1]
ASSETS = os.path.abspath(os.path.join(W, "assets"))
TOTAL = 99.4
HOOK_END = 2.4
caps = load_captions(os.path.join(HERE, "transcript.json"), os.path.join(HERE, "lines.txt"),
                     hide_before=HOOK_END, total=TOTAL)

ORANGE, GOLD = "#ff6a00", "#ffc21a"


def el(t0, t1, x, y, html, anim="slam", w=None, cls=""):
    style = f"left:{x}px;top:{y}px;" + (f"width:{w}px;" if w else "")
    return f'<div class="el {cls}" data-a="{anim}" data-t0="{t0}" data-t1="{t1}" style="{style}">{html}</div>'

R = lambda t, inner, cls="": f'<div class="rv {cls}" data-t="{t}">{inner}</div>'
img = lambda name, h: f'<img src="file://{ASSETS}/{name}.png" style="height:{h}px;display:block">'

def plate(text, cls=""):
    return f'<div class="plate {cls}">{text}</div>'

def section(n, title, sub):
    return (f'<div class="sect"><div class="sn">{n}</div><div class="st"><div class="stt">{title}</div>'
            f'<div class="sts">{sub}</div></div></div><div class="haz" style="width:560px;height:16px;margin-top:6px"></div>')

def chip(t, text, cls=""):
    return R(t, f'<span class="chip {cls}">{text}</span>', "inl")

def row(t, mark, text, cls=""):
    return R(t, f'<div class="row {cls}"><span class="mk">{mark}</span><span>{text}</span></div>')

def step(t, n, text):
    return R(t, f'<div class="step"><span class="num">{n}</span><span class="stx">{text}</span></div>')


E = []
# ---------- HOOK: hiện đủ ngay từ 0s ----------
E.append(el(-1, HOOK_END, 0, 150, '<div class="hook">'
            '<div class="haz" style="height:26px"></div>'
            '<div class="hk1">KEO SILICONE PELI</div>'
            '<div class="hk2"><span class="g">P300</span> <span class="vs">HAY</span> <span class="g">P500</span>?</div>'
            '<div class="hk3">CHỌN ĐÚNG KEO · LÀM MỘT LẦN LÀ CHẮC</div>'
            '<div class="haz" style="height:26px"></div></div>', anim="none", w=1080))

# ---------- 01 · P300 ----------
E.append(el(2.5, 26.3, 40, 110, section("01", "PELI P300", "KEO GỐC ACID"), anim="slideL"))
E.append(el(3.4, 8.3, 40, 330,
            row(3.5, "✔", "KHÔ RẤT NHANH") + row(4.5, "✔", "BÁM CỰC CHẮC TRÊN KÍNH") + row(6.6, "✔", "GIÁ THÀNH HỢP LÝ"),
            anim="slideL", cls="list"))
E.append(el(8.6, 18.4, 600, 760, '<div class="pcard blue">' + img("p300", 470) + '<div class="ptag">PELI P300</div></div>', anim="slideR"))
E.append(el(9.8, 18.4, 40, 330, '<div class="plate dark sm">DÙNG ĐỂ</div>'
            + row(11.0, "▸", "TRÁM KÍNH TRONG NHÀ") + row(13.5, "▸", "KHE KÍNH · CỬA KÍNH") + row(15.8, "▸", "SỬA CHỮA NHỎ · NHANH GỌN"),
            anim="slideL", cls="list"))
E.append(el(18.8, 26.2, 60, 330, '<div class="warn"><div class="wh">⚠ LƯU Ý</div>'
            + R(20.3, '<div class="wl">Mùi chua nhẹ lúc mới bơm</div>')
            + R(24.4, '<div class="wl"><b class="x">✕</b> Không dùng trên kim loại dễ bị ăn mòn</div>') + '</div>',
            anim="slam", w=960))

# ---------- 02 · P500 ----------
E.append(el(26.6, 52.0, 40, 110, section("02", "PELI P500", "KEO TRUNG TÍNH"), anim="slideL"))
E.append(el(28.9, 36.0, 40, 330,
            row(29.3, "✔", "KHÔNG MÙI") + row(30.2, "✔", "KHÔNG ĂN MÒN") + row(31.1, "✔", "BÁM ĐƯỢC RẤT NHIỀU BỀ MẶT"),
            anim="slideL", cls="list"))
E.append(el(32.9, 36.0, 40, 1130, '<div class="chips">' + chip(33.1, "NHÔM") + chip(33.6, "KÍNH") + chip(34.0, "BÊ TÔNG")
            + chip(34.6, "GỖ") + chip(34.9, "ĐÁ") + chip(35.3, "PVC") + '</div>', anim="none", w=1000))
E.append(el(36.2, 46.6, 590, 790, '<div class="pcard green">' + img("p500", 420) + '<div class="ptag">PELI P500</div></div>', anim="slideL"))
E.append(el(37.2, 46.6, 40, 330, plate("TRONG NHÀ & NGOÀI TRỜI", "gold"), anim="slam"))
E.append(el(40.1, 46.6, 40, 470, '<div class="list">' + row(40.8, "▸", "LẮP CỬA NHÔM, CỬA KÍNH")
            + row(43.2, "▸", "TRÁM KHE TƯỜNG, KHUNG CỬA") + row(45.2, "▸", "BỀ MẶT KIM LOẠI") + '</div>', anim="slideR", w=1000))
E.append(el(46.9, 52.0, 40, 330, '<div class="cmp">'
            + R(47.4, '<div class="cl ok"><b>✔</b> AN TOÀN · ĐA NĂNG HƠN</div>')
            + R(49.4, '<div class="cl slow"><b>◷</b> KHÔ CHẬM HƠN P300 MỘT CHÚT</div>') + '</div>', anim="slideL", w=1000))

# ---------- 03 · MẸO THI CÔNG ----------
E.append(el(52.1, 71.6, 40, 110, section("03", "MẸO THI CÔNG", "LÀM ĐẸP · BỀN · KHÔNG PHẢI SỬA"), anim="slideL"))
E.append(el(54.6, 71.6, 40, 330, '<div class="steps">'
            + step(56.9, "1", "VỆ SINH BỀ MẶT THẬT SẠCH") + step(58.9, "2", "BƠM KEO ĐỀU TAY")
            + step(61.4, "3", "VUỐT NHẸ 1 ĐƯỜNG CHO GỌN") + step(66.7, "4", "ĐỦ THỜI GIAN ĐÓNG RẮN") + '</div>',
            anim="none", w=1000))

# ---------- CHỐT ----------
E.append(el(71.8, 74.6, 0, 300, '<div class="stamp"><div class="haz" style="height:22px"></div>'
            '<div class="stx2">CHỐT LẠI</div><div class="sts2">CHỌN KEO NÀO?</div><div class="haz" style="height:22px"></div></div>',
            anim="slam", w=1080))
E.append(el(74.7, 93.4, 30, 120, '<div class="vs2">'
            '<div class="side s300" data-on="74.7" data-off="83.3">' + img("p300", 330)
            + '<div class="sname">P300 <small>ACID</small></div>'
            + R(76.8, '<div class="sl">✔ KHÔ NHANH</div>') + R(77.8, '<div class="sl">▸ KÍNH TRONG NHÀ</div>')
            + R(79.2, '<div class="sl">▸ SỬA CHỮA NHỎ</div>') + '</div>'
            '<div class="vsb">VS</div>'
            '<div class="side s500" data-on="83.3" data-off="999">' + img("p500", 330)
            + '<div class="sname">P500 <small>TRUNG TÍNH</small></div>'
            + R(84.7, '<div class="sl">✔ KHÔNG MÙI</div>') + R(85.8, '<div class="sl">▸ MỌI BỀ MẶT</div>')
            + R(89.5, '<div class="sl">▸ BỀN LÂU DÀI</div>') + '</div></div>', anim="slam", w=1020))

# ---------- KẾT ----------
E.append(el(93.6, TOTAL + 1, 0, 0, '<div class="endbg"></div>', anim="fade", w=1080))
E.append(el(93.7, TOTAL + 1, 0, 170, '<div class="end"><div class="haz" style="height:24px"></div>'
            '<div class="e1">CHỌN ĐÚNG KEO</div><div class="e2">ĐÚNG NHU CẦU</div>'
            + R(96.6, '<div class="e3">TIẾT KIỆM · ĐỠ CÔNG SỬA ĐI SỬA LẠI</div>')
            + '<div class="eprod">' + img("p300", 380) + img("p500", 380) + '</div>'
            '<div class="ebrand">PELI <span>SILICONE SEALANT</span></div>'
            '<div class="haz" style="height:24px"></div></div>', anim="slam", w=1080))


# ---------- build ----------
fonts = "".join(_ff(n, f"{fam}-{sub}-{w}-normal.woff2", w)
                for n, fam, w in [("Oswald", "oswald", 700), ("Oswald", "oswald", 600),
                                  ("BVP", "be-vietnam-pro", 700), ("BVP", "be-vietnam-pro", 800), ("BVP", "be-vietnam-pro", 900)]
                for sub in ("vietnamese", "latin"))
css = fonts + f"""
html,body{{margin:0;width:1080px;height:1920px;background:transparent;overflow:hidden}}
*{{box-sizing:border-box}}
.el{{position:absolute;opacity:0;will-change:transform}}
.haz{{width:100%;background:repeating-linear-gradient(-45deg,{GOLD} 0 26px,#141414 26px 52px);box-shadow:0 4px 10px rgba(0,0,0,.4)}}
.g{{background:linear-gradient(180deg,#fff3b0 0%,{GOLD} 45%,#c98a00 100%);-webkit-background-clip:text;color:transparent;
   -webkit-text-stroke:3px #1a1200;filter:drop-shadow(0 6px 0 #000)}}
.hook{{width:1080px;background:linear-gradient(180deg,rgba(10,10,10,.88),rgba(10,10,10,.78));padding:0 0 0;text-align:center}}
.hk1{{font-family:Oswald;font-weight:700;font-size:64px;color:#fff;letter-spacing:6px;padding-top:28px}}
.hk2{{font-family:Oswald;font-weight:700;font-size:200px;line-height:1.02;color:#fff;letter-spacing:2px}}
.hk2 .vs{{font-size:110px;color:{ORANGE};vertical-align:middle;-webkit-text-stroke:0}}
.hk3{{display:inline-block;margin:6px 0 30px;font-family:BVP;font-weight:900;font-size:46px;color:#111;background:{ORANGE};padding:10px 26px;
   transform:skewX(-8deg)}}
.sect{{display:flex;align-items:stretch;filter:drop-shadow(0 8px 14px rgba(0,0,0,.45))}}
.sn{{font-family:Oswald;font-weight:700;font-size:96px;line-height:1;color:#111;background:linear-gradient(180deg,#ffe07a,{GOLD} 50%,#d99a00);
   padding:14px 22px 10px}}
.st{{background:#121212;padding:12px 28px 10px;border-left:8px solid {ORANGE}}}
.stt{{font-family:Oswald;font-weight:700;font-size:70px;line-height:1;color:#fff;letter-spacing:1px}}
.sts{{font-family:BVP;font-weight:800;font-size:32px;color:{ORANGE};letter-spacing:2px;margin-top:6px}}
.list .row{{margin:0 0 14px}}
.row{{display:inline-flex;align-items:center;gap:16px;background:rgba(14,14,14,.86);border-left:10px solid {ORANGE};
   padding:12px 26px 12px 18px;font-family:BVP;font-weight:900;font-size:46px;color:#fff;box-shadow:0 8px 18px rgba(0,0,0,.4)}}
.row .mk{{display:inline-flex;align-items:center;justify-content:center;width:58px;height:58px;background:{GOLD};color:#111;font-size:36px}}
.rv{{opacity:0}} .rv.inl{{display:inline-block}}
.plate{{display:inline-block;white-space:nowrap;font-family:Oswald;font-weight:700;font-size:56px;color:#111;background:{ORANGE};padding:8px 26px;
   transform:skewX(-8deg);box-shadow:0 8px 18px rgba(0,0,0,.45)}}
.plate.gold{{background:linear-gradient(180deg,#ffe07a,{GOLD} 50%,#d99a00)}}
.plate.dark{{background:#111;color:{GOLD}}} .plate.sm{{font-size:40px;margin-bottom:14px}}
.pcard{{position:relative;padding:26px 30px 0;background:linear-gradient(160deg,rgba(255,255,255,.96),rgba(235,235,235,.96));
   border:8px solid {GOLD};outline:6px solid #111;box-shadow:0 20px 40px rgba(0,0,0,.55)}}
.pcard img{{filter:drop-shadow(0 10px 12px rgba(0,0,0,.35))}}
.ptag{{position:absolute;left:-14px;right:-14px;bottom:-30px;text-align:center;font-family:Oswald;font-weight:700;font-size:54px;
   color:#fff;background:{ORANGE};border:5px solid #111;padding:2px 0}}
.warn{{background:rgba(14,14,14,.9);border:8px solid {ORANGE};padding:22px 34px 26px;box-shadow:0 16px 34px rgba(0,0,0,.5);
   background-image:linear-gradient(rgba(14,14,14,.9),rgba(14,14,14,.9))}}
.wh{{font-family:Oswald;font-weight:700;font-size:84px;color:{GOLD};line-height:1.1}}
.wl{{font-family:BVP;font-weight:800;font-size:46px;color:#fff;margin-top:12px;line-height:1.25}}
.wl .x{{display:inline-block;background:#e0311b;color:#fff;padding:0 14px;margin-right:10px}}
.chips{{display:flex;flex-wrap:wrap;gap:16px}}
.chip{{display:inline-block;font-family:Oswald;font-weight:700;font-size:58px;color:#111;background:linear-gradient(180deg,#ffe07a,{GOLD} 50%,#d99a00);
   padding:6px 28px;border:5px solid #111;box-shadow:0 8px 16px rgba(0,0,0,.45)}}
.cmp .cl{{display:inline-block;font-family:BVP;font-weight:900;font-size:50px;padding:16px 28px;margin-bottom:16px;box-shadow:0 10px 20px rgba(0,0,0,.45)}}
.cl b{{margin-right:12px}}
.cl.ok{{background:{GOLD};color:#111}} .cl.slow{{background:#121212;color:#fff;border-left:12px solid {ORANGE}}}
.steps .step{{display:flex;align-items:center;gap:0;margin-bottom:18px;box-shadow:0 10px 20px rgba(0,0,0,.45)}}
.num{{flex:none;width:110px;height:104px;display:flex;align-items:center;justify-content:center;font-family:Oswald;font-weight:700;
   font-size:78px;color:#111;background:linear-gradient(180deg,#ffe07a,{GOLD} 50%,#d99a00)}}
.stx{{flex:1;height:104px;display:flex;align-items:center;padding:0 28px;font-family:BVP;font-weight:900;font-size:46px;color:#fff;
   background:rgba(14,14,14,.88);border-right:12px solid {ORANGE}}}
.stamp{{width:1080px;background:rgba(10,10,10,.85);text-align:center}}
.stx2{{font-family:Oswald;font-weight:700;font-size:190px;line-height:1.05;color:{ORANGE};-webkit-text-stroke:3px #000;padding-top:16px}}
.sts2{{font-family:BVP;font-weight:900;font-size:60px;color:{GOLD};padding-bottom:26px}}
.vs2{{display:flex;align-items:flex-start;justify-content:space-between}}
.side{{width:455px;background:rgba(14,14,14,.9);border:7px solid #444;padding:20px 18px 22px;display:flex;flex-direction:column;align-items:center;
   transition:none;box-shadow:0 16px 34px rgba(0,0,0,.5)}}
.side.on{{border-color:{GOLD};background:rgba(14,14,14,.94)}}
.side.dim{{filter:grayscale(.7) brightness(.55)}}
.sname{{font-family:Oswald;font-weight:700;font-size:76px;color:#fff;line-height:1;margin:14px 0 10px}}
.sname small{{font-size:34px;color:{ORANGE};letter-spacing:1px}}
.sl{{font-family:BVP;font-weight:900;font-size:38px;color:#111;background:{GOLD};padding:6px 16px;margin-top:10px;white-space:nowrap}}
.vsb{{align-self:center;margin-top:-120px;font-family:Oswald;font-weight:700;font-size:80px;color:#fff;background:{ORANGE};width:110px;height:110px;
   border-radius:50%;display:flex;align-items:center;justify-content:center;border:6px solid #111;z-index:2;margin-left:-40px;margin-right:-40px}}
.endbg{{width:1080px;height:1920px;background:radial-gradient(ellipse at 50% 40%,rgba(30,20,10,.75),rgba(8,8,8,.92))}}
.end{{width:1080px;text-align:center}}
.e1{{font-family:Oswald;font-weight:700;font-size:150px;line-height:1.05;color:#fff;padding-top:30px}}
.e2{{font-family:Oswald;font-weight:700;font-size:150px;line-height:1.05;background:linear-gradient(180deg,#fff3b0,{GOLD} 45%,#c98a00);
   -webkit-background-clip:text;color:transparent}}
.e3{{display:inline-block;margin-top:18px;font-family:BVP;font-weight:900;font-size:44px;color:#111;background:{ORANGE};padding:12px 26px}}
.eprod{{display:flex;justify-content:center;gap:40px;margin:46px 0 28px}}
.eprod img{{filter:drop-shadow(0 16px 20px rgba(0,0,0,.6))}}
.ebrand{{font-family:Oswald;font-weight:700;font-size:96px;color:{ORANGE};letter-spacing:4px;margin-bottom:34px}}
.ebrand span{{color:#fff;font-size:48px;letter-spacing:6px;vertical-align:middle}}
#cap{{position:absolute;left:40px;right:40px;top:1560px;text-align:center;font-family:BVP;font-weight:900;font-size:76px;color:#fff;
   text-transform:uppercase;-webkit-text-stroke:10px #000;paint-order:stroke fill;text-shadow:0 6px 0 rgba(0,0,0,.55);white-space:nowrap}}
#cap .k{{color:{GOLD}}}
"""

js = """
const CAPS=%s; const KEYS=/^(PELI|P300|P500|ACID|KÍNH|NHÔM|KHÔ|NHANH|KHÔNG|MÙI|BỀN|SẠCH|ĐÓNG|RẮN)$/i;
const els=[...document.querySelectorAll('.el')];
const cl=x=>Math.max(0,Math.min(1,x)), ease=x=>1-Math.pow(1-x,3);
const back=x=>{const c1=2.2,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
window.setT=function(t){
  for(const e of els){
    const t0=+e.dataset.t0,t1=+e.dataset.t1,an=e.dataset.a;
    if(t<t0-0.01||t>t1+0.01){e.style.opacity=0;continue}
    const a=an==='none'?1:cl((t-t0)/0.28), b=cl((t1-t)/0.18);
    let tr='';
    if(an==='slam') tr=`scale(${a<1?1.35-0.35*ease(a):1})`;
    else if(an==='slideL') tr=`translateX(${(1-ease(a))*-700}px)`;
    else if(an==='slideR') tr=`translateX(${(1-ease(a))*700}px)`;
    e.style.opacity=Math.min(an==='slam'?cl(a*2.5):ease(a),b); e.style.transform=tr+` translateY(${(1-b)*-20}px)`;
    for(const r of e.querySelectorAll('.rv')){
      const p=cl((t-(+r.dataset.t))/0.22);
      r.style.opacity=p; r.style.transform=`translateX(${(1-ease(p))*-60}px) scale(${p<1?0.85+0.15*back(p):1})`;
    }
    for(const s of e.querySelectorAll('.side')){
      const on=t>=+s.dataset.on&&t<+s.dataset.off; s.classList.toggle('on',on); s.classList.toggle('dim',!on);
    }
  }
  const cap=document.getElementById('cap');
  const c=CAPS.find(c=>t>=c[0]&&t<c[2]);
  if(c&&t<93.6){const p=cl((t-c[0])/0.1);
    cap.innerHTML=c[1].split(' ').map(w=>KEYS.test(w.replace(/[,.?!]/g,''))?`<span class="k">${w}</span>`:w).join(' ');
    cap.style.opacity=p;cap.style.transform=`scale(${0.8+0.2*back(p)})`}
  else cap.style.opacity=0;
};
""" % json.dumps(caps, ensure_ascii=False)

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head>
<body>{''.join(E)}<div id="cap"></div><script>{js}</script></body></html>"""
open(os.path.join(W, "overlay.html"), "w").write(html)
print(len(E), "elements,", len(caps), "captions")
