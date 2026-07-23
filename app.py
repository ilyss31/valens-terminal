<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Valens Wealth | Quant Terminal</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Inter:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet"/>
<style>
*{margin:0;padding:0;box-sizing:border-box;}
:root{
  --navy:#050b14;--navy-panel:#0b1523;--navy-panel-2:#0e1a2c;
  --gold:#D4AF37;--gold-bright:#F0D77B;--gold-dim:rgba(212,175,55,0.15);
  --white:#FFFFFF;--ivory:#ECEAE3;--muted:#8B93A7;
  --success:#3FAE6A;--danger:#C0453B;--border-gold:rgba(212,175,55,0.22);
}
html,body{height:100%;background:radial-gradient(ellipse at top,#0c1a30 0%,var(--navy) 65%);color:var(--white);font-family:'Inter',sans-serif;overflow:hidden;}

/* ===== NAVBAR ===== */
.navbar{display:flex;align-items:center;justify-content:space-between;background:linear-gradient(180deg,#0a1526 0%,#060d18 100%);border-bottom:1px solid var(--border-gold);padding:0 20px;height:54px;flex-shrink:0;}
.navbar-brand{display:flex;align-items:center;gap:10px;}
.navbar-logo{height:38px;width:auto;filter:drop-shadow(0 0 8px rgba(212,175,55,0.35));}
.navbar-name{font-family:'Playfair Display',serif;font-size:18px;color:var(--white);line-height:1.1;}
.navbar-name span{color:var(--gold);}
.navbar-sub{font-size:9px;color:var(--gold);letter-spacing:2.5px;}
.navbar-tabs{display:flex;}
.navbar-tab{color:var(--muted);font-size:12.5px;padding:0 16px;height:54px;display:flex;align-items:center;cursor:pointer;border-bottom:2px solid transparent;transition:all .2s;white-space:nowrap;}
.navbar-tab:hover{color:var(--white);background:rgba(212,175,55,0.04);}
.navbar-tab.active{color:var(--white);border-bottom:2px solid var(--gold);font-weight:600;}
.navbar-right{display:flex;align-items:center;gap:14px;}
.navbar-clock{text-align:right;font-family:'IBM Plex Mono',monospace;font-size:12px;color:var(--white);}
.navbar-date{color:var(--muted);font-size:9.5px;}
.live-badge{display:flex;align-items:center;gap:5px;background:rgba(63,174,106,0.12);border:1px solid rgba(63,174,106,0.3);border-radius:4px;padding:3px 8px;font-size:10px;color:var(--success);font-family:'IBM Plex Mono',monospace;}
.live-dot{width:6px;height:6px;border-radius:50%;background:var(--success);animation:pulse-dot 1.6s infinite;}
@keyframes pulse-dot{0%,100%{opacity:1;}50%{opacity:0.25;}}

/* ===== LAYOUT ===== */
.terminal{display:flex;height:calc(100vh - 54px);overflow:hidden;}

/* ===== CHART AREA ===== */
.chart-area{flex:1;display:flex;flex-direction:column;overflow:hidden;border-right:1px solid var(--border-gold);}
.chart-header{display:flex;align-items:center;justify-content:space-between;padding:7px 14px;border-bottom:1px solid var(--border-gold);background:rgba(11,21,35,0.7);flex-shrink:0;gap:10px;}
.chart-sym-block{display:flex;align-items:center;gap:10px;}
.chart-symbol{font-family:'IBM Plex Mono',monospace;font-size:15px;font-weight:600;color:var(--white);}
.chart-pair{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--gold);background:rgba(212,175,55,0.1);border:1px solid var(--border-gold);border-radius:4px;padding:2px 7px;}
.tf-tabs{display:flex;gap:2px;}
.tf-tab{font-family:'IBM Plex Mono',monospace;font-size:10.5px;padding:3px 9px;border-radius:4px;cursor:pointer;color:var(--muted);border:1px solid transparent;transition:all .15s;}
.tf-tab:hover{color:var(--white);}
.tf-tab.active{color:var(--gold);border-color:var(--border-gold);background:rgba(212,175,55,0.08);}
.inst-btns{display:flex;gap:4px;flex-wrap:wrap;}
.inst-btn{background:rgba(212,175,55,0.06);border:1px solid var(--border-gold);border-radius:4px;color:var(--muted);font-size:10px;padding:3px 8px;cursor:pointer;font-family:'IBM Plex Mono',monospace;transition:all .15s;}
.inst-btn:hover,.inst-btn.active{color:var(--gold);background:rgba(212,175,55,0.12);border-color:var(--gold);}

/* Price strip */
.price-strip{display:flex;align-items:center;gap:18px;padding:5px 14px;background:rgba(5,11,20,0.85);border-bottom:1px solid var(--border-gold);flex-shrink:0;}
.price-main{font-family:'IBM Plex Mono',monospace;font-size:20px;font-weight:600;color:var(--white);}
.price-up{color:var(--success);font-size:11.5px;font-family:'IBM Plex Mono',monospace;}
.price-down{color:var(--danger);font-size:11.5px;font-family:'IBM Plex Mono',monospace;}
.price-meta{color:var(--muted);font-size:9.5px;letter-spacing:1px;}
.sr-badges{display:flex;gap:6px;margin-left:auto;}
.sr-badge{font-family:'IBM Plex Mono',monospace;font-size:9.5px;padding:2px 7px;border-radius:3px;font-weight:600;}
.sr-res{background:rgba(192,69,59,0.15);border:1px solid rgba(192,69,59,0.35);color:#e07070;}
.sr-sup{background:rgba(63,174,106,0.15);border:1px solid rgba(63,174,106,0.35);color:#70c890;}

.chart-frame{flex:1;position:relative;overflow:hidden;}
.chart-frame iframe{width:100%;height:100%;border:none;}
/* S/R overlay lines drawn over the chart */
.sr-overlay{position:absolute;inset:0;pointer-events:none;z-index:5;}
.sr-line{position:absolute;left:0;right:0;height:0;border-top:1px dashed;display:flex;align-items:center;}
.sr-line.res{border-color:rgba(192,69,59,0.55);}
.sr-line.sup{border-color:rgba(63,174,106,0.55);}
.sr-line-tag{position:absolute;right:8px;transform:translateY(-50%);font-family:'IBM Plex Mono',monospace;font-size:9px;font-weight:600;padding:1px 6px;border-radius:3px;letter-spacing:0.3px;}
.sr-line.res .sr-line-tag{background:rgba(192,69,59,0.9);color:#fff;}
.sr-line.sup .sr-line-tag{background:rgba(63,174,106,0.9);color:#04140b;}

/* News ticker */
.news-ticker-bar{background:linear-gradient(90deg,#0a1526,#060d18);border-top:1px solid var(--border-gold);height:30px;display:flex;align-items:center;overflow:hidden;flex-shrink:0;}
.news-ticker-label{background:var(--gold);color:var(--navy);font-size:9.5px;font-weight:700;letter-spacing:1.5px;padding:0 10px;height:100%;display:flex;align-items:center;flex-shrink:0;white-space:nowrap;}
.news-ticker-track{overflow:hidden;flex:1;height:100%;display:flex;align-items:center;}
.news-ticker-inner{display:flex;white-space:nowrap;animation:ticker-scroll 80s linear infinite;}
@keyframes ticker-scroll{0%{transform:translateX(0);}100%{transform:translateX(-50%);}}
.news-ticker-item{display:inline-flex;align-items:center;gap:7px;padding:0 20px;font-size:10.5px;}
.news-src{color:var(--gold);font-weight:700;font-size:9.5px;}
.news-text{color:var(--ivory);}
.news-time{color:var(--muted);font-family:'IBM Plex Mono',monospace;font-size:9px;}
.news-sep{color:var(--border-gold);}

/* ===== RIGHT PANEL ===== */
.right-panel{width:310px;flex-shrink:0;display:flex;flex-direction:column;overflow:hidden;background:linear-gradient(180deg,#0a1220 0%,#050b14 100%);}
.panel-scroll{overflow-y:auto;flex:1;}
.panel-scroll::-webkit-scrollbar{width:3px;}
.panel-scroll::-webkit-scrollbar-thumb{background:var(--border-gold);}

/* Quant Engine */
.panel-section{padding:10px 12px;border-bottom:1px solid var(--border-gold);}
.panel-title{font-family:'Playfair Display',serif;font-size:12.5px;color:var(--gold);margin-bottom:8px;display:flex;align-items:center;gap:5px;}
.ind-row{margin-bottom:7px;}
.ind-top{display:flex;justify-content:space-between;font-size:11px;margin-bottom:3px;}
.ind-name{color:var(--white);font-weight:600;}
.ind-desc{color:var(--muted);}
.ind-pct{color:var(--gold);font-family:'IBM Plex Mono',monospace;font-size:10.5px;font-weight:600;}
.ind-bar-bg{background:rgba(212,175,55,0.1);border-radius:3px;height:3.5px;overflow:hidden;}
.ind-bar-fill{background:linear-gradient(90deg,var(--gold),var(--gold-bright));height:100%;border-radius:3px;transition:width 1.2s ease;}

/* Key Events */
.events-section{padding:10px 12px;border-bottom:1px solid var(--border-gold);}
.event-card{background:rgba(212,175,55,0.05);border:1px solid var(--border-gold);border-radius:7px;padding:8px 10px;margin-bottom:7px;}
.event-card:last-child{margin-bottom:0;}
.event-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;}
.event-name{color:var(--gold);font-weight:700;font-size:10.5px;letter-spacing:0.3px;}
.event-date{color:var(--muted);font-family:'IBM Plex Mono',monospace;font-size:9px;}
.event-impact{font-size:9px;font-weight:700;letter-spacing:0.5px;padding:1px 5px;border-radius:3px;}
.event-impact.bull{background:rgba(63,174,106,0.2);color:var(--success);border:1px solid rgba(63,174,106,0.3);}
.event-desc{color:var(--ivory);font-size:10px;line-height:1.45;margin-bottom:6px;}
.event-scenarios{display:flex;flex-direction:column;gap:3px;}
.scenario{display:flex;gap:6px;font-size:9.5px;line-height:1.4;padding:3px 6px;border-radius:4px;}
.scenario.bull-s{background:rgba(63,174,106,0.08);border-left:2px solid var(--success);}
.scenario.bear-s{background:rgba(192,69,59,0.08);border-left:2px solid var(--danger);}
.scenario-icon{flex-shrink:0;font-weight:700;}
.scenario.bull-s .scenario-icon{color:var(--success);}
.scenario.bear-s .scenario-icon{color:var(--danger);}
.scenario-text{color:var(--ivory);}

/* Smart Money Flow */
.smf-section{padding:10px 12px;border-bottom:1px solid var(--border-gold);}
.smf-scroll{max-height:120px;overflow:hidden;position:relative;}
.smf-inner{display:flex;flex-direction:column;gap:4px;animation:smf-scroll 20s linear infinite;}
@keyframes smf-scroll{0%{transform:translateY(0);}100%{transform:translateY(-50%);}}
.smf-item{background:rgba(212,175,55,0.04);border:1px solid rgba(212,175,55,0.1);border-radius:5px;padding:5px 8px;}
.smf-header{display:flex;justify-content:space-between;margin-bottom:2px;}
.smf-actor{color:var(--gold);font-weight:700;font-size:9.5px;letter-spacing:0.3px;}
.smf-time{color:var(--muted);font-family:'IBM Plex Mono',monospace;font-size:9px;}
.smf-action{color:var(--ivory);font-size:10px;line-height:1.35;}
.smf-action .buy{color:var(--success);font-weight:700;}
.smf-action .sell{color:var(--danger);font-weight:700;}
.smf-conclusion{margin-top:3px;padding:3px 6px;background:rgba(212,175,55,0.07);border-radius:3px;font-size:9.5px;color:var(--gold-bright);line-height:1.35;}

/* AI Signal */
.signal-section{padding:10px 12px;}
.signal-card{border-radius:9px;overflow:hidden;border:1px solid var(--gold);box-shadow:0 0 28px rgba(212,175,55,0.22),0 0 55px rgba(212,175,55,0.08);animation:signal-glow 3s ease-in-out infinite;}
@keyframes signal-glow{0%,100%{box-shadow:0 0 28px rgba(212,175,55,0.22),0 0 55px rgba(212,175,55,0.08);}50%{box-shadow:0 0 42px rgba(212,175,55,0.38),0 0 80px rgba(212,175,55,0.15);}}
.signal-header-bar{background:linear-gradient(90deg,#7a5f1c,var(--gold),#7a5f1c);color:var(--navy);text-align:center;padding:6px;font-weight:700;letter-spacing:3px;font-size:9.5px;}
.signal-body{background:radial-gradient(ellipse at center,#12213a 0%,var(--navy-panel) 75%);padding:12px 14px;text-align:center;}
.signal-decision-buy{color:var(--success);font-size:24px;font-weight:700;font-family:'Playfair Display',serif;text-shadow:0 0 18px rgba(63,174,106,0.5);}
.signal-decision-sell{color:var(--danger);font-size:24px;font-weight:700;font-family:'Playfair Display',serif;text-shadow:0 0 18px rgba(192,69,59,0.5);}
.signal-decision-neutral{color:var(--gold);font-size:24px;font-weight:700;font-family:'Playfair Display',serif;}
.signal-asset{color:var(--muted);font-size:9.5px;letter-spacing:1.5px;margin-top:2px;}
.signal-confidence{color:var(--gold-bright);font-size:11.5px;margin-top:5px;font-weight:600;}
.signal-levels{display:flex;justify-content:space-between;margin-top:9px;padding-top:7px;border-top:1px solid var(--border-gold);}
.signal-level{text-align:center;flex:1;}
.signal-level-label{color:var(--muted);font-size:8.5px;letter-spacing:1px;}
.signal-level-value{color:var(--white);font-family:'IBM Plex Mono',monospace;font-size:11.5px;margin-top:2px;font-weight:600;}

/* ===== PAGE VIEWS ===== */
.page-view{display:none;flex:1;flex-direction:column;overflow:hidden;}
.page-view.active{display:flex;}
.page-content{flex:1;overflow-y:auto;padding:24px;display:flex;flex-direction:column;gap:16px;}
.page-content::-webkit-scrollbar{width:4px;}
.page-content::-webkit-scrollbar-thumb{background:var(--border-gold);}
.page-card{background:linear-gradient(155deg,var(--navy-panel-2),var(--navy-panel));border:1px solid var(--border-gold);border-radius:10px;padding:18px 20px;}
.page-card-title{font-family:'Playfair Display',serif;color:var(--gold);font-size:16px;margin-bottom:12px;padding-bottom:8px;border-bottom:1px solid var(--border-gold);}
.page-card p,.page-card li{color:var(--ivory);font-size:13px;line-height:1.7;}
.page-card ul{padding-left:18px;}
.page-card li{margin-bottom:4px;}
.stat-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:4px;}
.stat-box{background:rgba(212,175,55,0.06);border:1px solid var(--border-gold);border-radius:7px;padding:12px;text-align:center;}
.stat-val{font-family:'IBM Plex Mono',monospace;font-size:18px;font-weight:600;color:var(--gold);}
.stat-lbl{color:var(--muted);font-size:10px;letter-spacing:1px;margin-top:3px;}
.form-row{display:flex;flex-direction:column;gap:5px;margin-bottom:12px;}
.form-label{color:var(--muted);font-size:11px;letter-spacing:1px;}
.form-input{background:rgba(212,175,55,0.06);border:1px solid var(--border-gold);border-radius:5px;color:var(--white);font-family:'IBM Plex Mono',monospace;font-size:13px;padding:7px 10px;outline:none;}
.form-input:focus{border-color:var(--gold);}
.btn-gold{background:transparent;border:1.5px solid var(--gold);color:var(--gold);border-radius:6px;font-weight:600;letter-spacing:0.6px;padding:8px 18px;cursor:pointer;font-size:12px;transition:all .2s;}
.btn-gold:hover{background:var(--gold);color:var(--navy);}
.research-item{padding:10px 0;border-bottom:1px solid var(--border-gold);}
.research-item:last-child{border-bottom:none;}
.research-src{color:var(--gold);font-size:10px;font-weight:700;margin-bottom:3px;}
.research-title{color:var(--white);font-size:13px;margin-bottom:3px;}
.research-summary{color:var(--muted);font-size:11.5px;line-height:1.5;}
</style>
</head>
<body>

<!-- NAVBAR -->
<div class="navbar">
  <div class="navbar-brand">
    <img class="navbar-logo" src="https://cdn.abacus.ai/images/0f498010-a0a5-4cf2-98cd-491f08add03c.png" alt="Valens Wealth"/>
    <div>
      <div class="navbar-name">Valens <span>Wealth</span></div>
      <div class="navbar-sub">QUANT TERMINAL v2.0</div>
    </div>
  </div>
  <div class="navbar-tabs">
    <div class="navbar-tab" onclick="showPage('portfolio')">Portfolio</div>
    <div class="navbar-tab active" id="tab-signals" onclick="showPage('signals')">Signals</div>
    <div class="navbar-tab" onclick="showPage('research')">Research</div>
    <div class="navbar-tab" onclick="showPage('settings')">Settings</div>
    <div class="navbar-tab" onclick="showPage('account')">Account</div>
  </div>
  <div class="navbar-right">
    <div class="live-badge"><span class="live-dot"></span>LIVE</div>
    <div class="navbar-clock">
      <div id="clock">--:--:-- EST</div>
      <div class="navbar-date" id="dateline">--</div>
    </div>
  </div>
</div>

<!-- ===== SIGNALS PAGE (default) ===== -->
<div class="page-view active" id="page-signals">
  <div class="terminal">

    <!-- CHART AREA -->
    <div class="chart-area">
      <div class="chart-header">
        <div class="chart-sym-block">
          <div class="chart-symbol" id="sym-label">XAU/USD</div>
          <div class="chart-pair" id="sym-pair">GOLD · OZ</div>
        </div>
        <div class="tf-tabs">
          <div class="tf-tab" onclick="setTF(this,'1')">1M</div>
          <div class="tf-tab" onclick="setTF(this,'5')">5M</div>
          <div class="tf-tab" onclick="setTF(this,'15')">15M</div>
          <div class="tf-tab" onclick="setTF(this,'60')">1H</div>
          <div class="tf-tab" onclick="setTF(this,'240')">4H</div>
          <div class="tf-tab active" onclick="setTF(this,'D')">1D</div>
        </div>
        <div class="inst-btns">
          <div class="inst-btn active" id="btn-XAUUSD" onclick="setInstrument('OANDA:XAUUSD','XAUUSD','XAU/USD','Gold Spot · OZ','4,053.98','4,129.35')">XAU/USD</div>
          <div class="inst-btn" id="btn-SPX500" onclick="setInstrument('SP:SPX','SPX500','SPX500','S&P 500 Index','5,312.46','5,289.20')">SPX</div>
          <div class="inst-btn" id="btn-NDX100" onclick="setInstrument('NASDAQ:NDX','NDX100','NDX100','Nasdaq 100','18,742.60','18,690.10')">NDX</div>
          <div class="inst-btn" id="btn-BTCUSD" onclick="setInstrument('COINBASE:BTCUSD','BTCUSD','BTC/USD','Bitcoin · USD','66,140.00','65,200.00')">BTC/USD</div>
          <div class="inst-btn" id="btn-EURUSD" onclick="setInstrument('FX:EURUSD','EURUSD','EUR/USD','Euro · Dollar','1.0812','1.0845')">EUR/USD</div>
          <div class="inst-btn" id="btn-AAPL" onclick="setInstrument('NASDAQ:AAPL','AAPL','AAPL','Apple Inc.','189.84','187.20')">AAPL</div>
        </div>
      </div>

      <div class="price-strip">
        <div>
          <div class="price-meta" id="price-label-top">GOLD SPOT · XAU/USD · OZ</div>
          <div class="price-main" id="live-price">4,053.98</div>
        </div>
        <div id="price-change" class="price-down">▼ -75.37 (-1.83%)</div>
        <div class="sr-badges" id="sr-badges">
          <span class="sr-badge sr-res">R3: 4,155</span>
          <span class="sr-badge sr-res">R2: 4,118</span>
          <span class="sr-badge sr-res">R1: 4,085</span>
          <span class="sr-badge sr-sup">S1: 4,040</span>
          <span class="sr-badge sr-sup">S2: 4,000</span>
          <span class="sr-badge sr-sup">S3: 3,960</span>
        </div>
        <div style="color:var(--muted);font-size:9.5px;margin-left:8px;" id="price-time">As of --:--</div>
      </div>

      <div class="chart-frame">
        <iframe id="tv-chart"
          src="https://s.tradingview.com/widgetembed/?frameElementId=tv_chart&symbol=OANDA%3AXAUUSD&interval=D&hidesidetoolbar=0&symboledit=0&saveimage=0&toolbarbg=050b14&studies=RSI%40tv-basicstudies%2CMACD%40tv-basicstudies%2CVolume%40tv-basicstudies&theme=dark&style=1&timezone=Etc%2FUTC&withdateranges=1&hideideas=1&locale=en"
          allowtransparency="true" frameborder="0" scrolling="no">
        </iframe>
        <!-- S/R overlay lines drawn on top of the chart -->
        <div class="sr-overlay" id="sr-overlay"></div>
      </div>

      <div class="news-ticker-bar">
        <div class="news-ticker-label">📡 LIVE FEED</div>
        <div class="news-ticker-track">
          <div class="news-ticker-inner" id="ticker-inner"></div>
        </div>
      </div>
    </div>

    <!-- RIGHT PANEL -->
    <div class="right-panel">
      <div class="panel-scroll">

        <!-- QUANT ENGINE -->
        <div class="panel-section">
          <div class="panel-title">⚙️ AI Quant Engine</div>
          <div id="quant-indicators"></div>
        </div>

        <!-- KEY EVENTS -->
        <div class="events-section">
          <div class="panel-title">📅 Key Events This Week</div>

          <div class="event-card">
            <div class="event-header">
              <span class="event-name">🇪🇺 ECB Faiz Oranı Kararı</span>
              <span class="event-impact bull">🔥 HIGH IMPACT</span>
            </div>
            <div class="event-date">Perşembe, 23 Tem · 15:15 (TSİ) · Beklenti %2.40</div>
            <div class="event-desc" style="margin-top:5px;">Avrupa Merkez Bankası faiz kararı ve 15:45'teki basın açıklaması. Lagarde'ın tonu EUR/USD ve dolaylı olarak Altın'ı hareketlendirecek.</div>
            <div class="event-scenarios">
              <div class="scenario bull-s">
                <span class="scenario-icon">▲ BUY</span>
                <span class="scenario-text">ECB %2.40'ta sabit tutar + Lagarde "şahin" (hawkish) konuşursa → EUR/USD 1.0880'e yükselir, Dolar zayıflar, Altın 4,085 direncini test eder.</span>
              </div>
              <div class="scenario bear-s">
                <span class="scenario-icon">▼ SELL</span>
                <span class="scenario-text">Lagarde "güvercin" (dovish) ve indirim sinyali verirse → EUR/USD 1.0740'a düşer, Dolar güçlenir, Altın 4,000 desteğine baskı görür.</span>
              </div>
            </div>
          </div>

          <div class="event-card">
            <div class="event-header">
              <span class="event-name">🇺🇸 US İşsizlik Başvuruları</span>
              <span class="event-impact bull">🔥 HIGH IMPACT</span>
            </div>
            <div class="event-date">Perşembe, 23 Tem · 15:30 (TSİ) · Beklenti 211K</div>
            <div class="event-desc" style="margin-top:5px;">ABD Haftalık İşsizlik Hakları Başvuruları. Açıklanan: 187K (önceki 209K). İşgücü piyasası verisi Fed faiz beklentilerini doğrudan etkiliyor.</div>
            <div class="event-scenarios">
              <div class="scenario bull-s">
                <span class="scenario-icon">▲ BUY</span>
                <span class="scenario-text">Başvurular &lt; 200K gelirse (güçlü istihdam) → Fed'in faiz sabit tutma ihtimali artar, Dolar güçlenir. SPX 5,340 direncine yönelir.</span>
              </div>
              <div class="scenario bear-s">
                <span class="scenario-icon">▼ SELL</span>
                <span class="scenario-text">Başvurular &gt; 220K gelirse (zayıf istihdam) → Resesyon endişesi, faiz indirim beklentisi. Altın safe-haven alımıyla 4,118'e yükselir.</span>
              </div>
            </div>
          </div>

          <div class="event-card">
            <div class="event-header">
              <span class="event-name">🇹🇷 TCMB Faiz Kararı</span>
              <span class="event-impact bull">🔥 HIGH IMPACT</span>
            </div>
            <div class="event-date">Perşembe, 23 Tem · 14:00 (TSİ) · Politika Faizi %37.00</div>
            <div class="event-desc" style="margin-top:5px;">TCMB bir hafta vadeli repo faizi %37.00'da sabit. Gecelik borçlanma %35.50, gecelik faiz %40.00. USD/TRY ve BIST için kritik.</div>
            <div class="event-scenarios">
              <div class="scenario bull-s">
                <span class="scenario-icon">▲ BUY</span>
                <span class="scenario-text">Faiz %37'de sabit + şahin metin → TL güçlenir, USD/TRY geriler. BIST100 bankacılık hisseleri toparlanır.</span>
              </div>
              <div class="scenario bear-s">
                <span class="scenario-icon">▼ SELL</span>
                <span class="scenario-text">Beklenmedik faiz indirimi sinyali → TL baskı altına girer, USD/TRY yükselir. Yatırımcı gram altına yönelir.</span>
              </div>
            </div>
          </div>
        </div>

        <!-- SMART MONEY FLOW -->
        <div class="smf-section">
          <div class="panel-title">🏦 Smart Money Flow</div>
          <div class="smf-scroll">
            <div class="smf-inner" id="smf-inner"></div>
          </div>
        </div>

        <!-- AI SIGNAL -->
        <div class="signal-section">
          <div class="panel-title">🤖 AI Signal</div>
          <div class="signal-card">
            <div class="signal-header-bar">ACTIVE SIGNAL</div>
            <div class="signal-body">
              <div id="signal-decision" class="signal-decision-sell">🔴 SELL</div>
              <div class="signal-asset" id="signal-asset">Gold Spot · XAU/USD</div>
              <div class="signal-confidence" id="signal-conf">76% CONFIDENCE</div>
              <div class="signal-levels">
                <div class="signal-level">
                  <div class="signal-level-label">ENTRY</div>
                  <div class="signal-level-value" id="sig-entry">4,053.98</div>
                </div>
                <div class="signal-level">
                  <div class="signal-level-label">STOP LOSS</div>
                  <div class="signal-level-value" id="sig-stop">4,090.00</div>
                </div>
                <div class="signal-level">
                  <div class="signal-level-label">TARGET</div>
                  <div class="signal-level-value" id="sig-target">4,000.00</div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</div>

<!-- ===== PORTFOLIO PAGE ===== -->
<div class="page-view" id="page-portfolio">
  <div class="page-content">
    <div class="page-card">
      <div class="page-card-title">📊 Portfolio Overview</div>
      <div class="stat-grid">
        <div class="stat-box"><div class="stat-val" style="color:var(--success)">+18.4%</div><div class="stat-lbl">YTD RETURN</div></div>
        <div class="stat-box"><div class="stat-val">$4.2M</div><div class="stat-lbl">AUM</div></div>
        <div class="stat-box"><div class="stat-val" style="color:var(--success)">2.31</div><div class="stat-lbl">SHARPE RATIO</div></div>
        <div class="stat-box"><div class="stat-val" style="color:var(--danger)">-6.2%</div><div class="stat-lbl">MAX DRAWDOWN</div></div>
        <div class="stat-box"><div class="stat-val">87%</div><div class="stat-lbl">WIN RATE</div></div>
        <div class="stat-box"><div class="stat-val">142</div><div class="stat-lbl">TOTAL TRADES</div></div>
      </div>
    </div>
    <div class="page-card">
      <div class="page-card-title">📈 Open Positions</div>
      <p style="color:var(--muted);font-size:12px;">Connect your broker API to display live positions. Supported: Interactive Brokers, Alpaca, Binance, Bybit.</p>
    </div>
    <div class="page-card">
      <div class="page-card-title">🏆 Allocation</div>
      <ul>
        <li>Gold (XAU/USD) — 35%</li>
        <li>US Equities (SPX/NDX) — 30%</li>
        <li>Crypto (BTC/ETH) — 20%</li>
        <li>Forex (EUR/USD) — 10%</li>
        <li>Cash — 5%</li>
      </ul>
    </div>
  </div>
</div>

<!-- ===== RESEARCH PAGE ===== -->
<div class="page-view" id="page-research">
  <div class="page-content">
    <div class="page-card">
      <div class="page-card-title">🔬 Institutional Research</div>
      <div class="research-item">
        <div class="research-src">GOLDMAN SACHS · Jul 22, 2025</div>
        <div class="research-title">Gold Target Raised to $2,700 — Structural Bull Case Intact</div>
        <div class="research-summary">Central bank demand, de-dollarization flows and Fed pivot expectations underpin a multi-year bull market in gold. GS raises 12-month target from $2,500 to $2,700/oz.</div>
      </div>
      <div class="research-item">
        <div class="research-src">JP MORGAN · Jul 21, 2025</div>
        <div class="research-title">S&P 500 Year-End Target: 5,800 — AI Earnings Cycle Accelerating</div>
        <div class="research-summary">Mega-cap tech earnings beats driving index higher. JPM sees AI capex cycle sustaining above-trend EPS growth through 2026. Overweight US equities.</div>
      </div>
      <div class="research-item">
        <div class="research-src">MORGAN STANLEY · Jul 20, 2025</div>
        <div class="research-title">Bitcoin Institutional Adoption — ETF Inflows Hit Record $2.1B Weekly</div>
        <div class="research-summary">Spot BTC ETF inflows accelerating post-halving. MS sees $80,000 as next key resistance. Institutional allocation to crypto rising from 1% to 3-5% of portfolios.</div>
      </div>
    </div>
    <div class="page-card">
      <div class="page-card-title">📐 Technical Analysis — XAU/USD</div>
      <p>Weekly structure remains bullish above $2,350 (200-week MA). Key resistance cluster at $2,450–$2,480 (previous ATH zone). A weekly close above $2,480 opens path to $2,600+. RSI(14) at 68 — approaching overbought but not yet exhausted on weekly timeframe.</p>
    </div>
  </div>
</div>

<!-- ===== SETTINGS PAGE ===== -->
<div class="page-view" id="page-settings">
  <div class="page-content">
    <div class="page-card">
      <div class="page-card-title">⚙️ Risk Parameters</div>
      <div class="form-row"><label class="form-label">SWING TAKE PROFIT (%)</label><input class="form-input" type="number" value="2.5" step="0.1"/></div>
      <div class="form-row"><label class="form-label">SWING STOP LOSS (%)</label><input class="form-input" type="number" value="1.2" step="0.1"/></div>
      <div class="form-row"><label class="form-label">SCALP TARGET (× ATR14)</label><input class="form-input" type="number" value="1.5" step="0.1"/></div>
      <div class="form-row"><label class="form-label">SCALP STOP (× ATR14)</label><input class="form-input" type="number" value="1.0" step="0.1"/></div>
      <button class="btn-gold">Save Parameters</button>
    </div>
    <div class="page-card">
      <div class="page-card-title">🔔 Alert Settings</div>
      <div class="form-row"><label class="form-label">EMAIL ALERTS</label><input class="form-input" type="email" placeholder="your@email.com"/></div>
      <div class="form-row"><label class="form-label">SIGNAL THRESHOLD (min confidence %)</label><input class="form-input" type="number" value="75" step="5"/></div>
      <button class="btn-gold">Save Alerts</button>
    </div>
    <div class="page-card">
      <div class="page-card-title">🌐 Language & Display</div>
      <div style="display:flex;gap:10px;margin-top:4px;">
        <button class="btn-gold">English</button>
        <button class="btn-gold">Türkçe</button>
      </div>
    </div>
  </div>
</div>

<!-- ===== ACCOUNT PAGE ===== -->
<div class="page-view" id="page-account">
  <div class="page-content">
    <div class="page-card">
      <div class="page-card-title">👤 Account</div>
      <div class="stat-grid" style="grid-template-columns:repeat(2,1fr);">
        <div class="stat-box"><div class="stat-val" style="font-size:14px;">INSTITUTIONAL</div><div class="stat-lbl">TIER</div></div>
        <div class="stat-box"><div class="stat-val" style="color:var(--success);font-size:14px;">ACTIVE</div><div class="stat-lbl">STATUS</div></div>
      </div>
    </div>
    <div class="page-card">
      <div class="page-card-title">🔗 Broker Integration</div>
      <p style="margin-bottom:12px;">Connect your brokerage account for live order execution and position tracking.</p>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">
        <button class="btn-gold">Interactive Brokers</button>
        <button class="btn-gold">Alpaca</button>
        <button class="btn-gold">Binance</button>
        <button class="btn-gold">Bybit</button>
      </div>
    </div>
    <div class="page-card">
      <div class="page-card-title">🔐 Security</div>
      <div class="form-row"><label class="form-label">API KEY</label><input class="form-input" type="password" placeholder="••••••••••••••••"/></div>
      <div class="form-row"><label class="form-label">API SECRET</label><input class="form-input" type="password" placeholder="••••••••••••••••"/></div>
      <button class="btn-gold">Update Credentials</button>
    </div>
  </div>
</div>

<script>
// ===== CLOCK =====
function updateClock(){
  const now=new Date();
  const est=new Date(now.toLocaleString('en-US',{timeZone:'America/New_York'}));
  const h=String(est.getHours()).padStart(2,'0'),m=String(est.getMinutes()).padStart(2,'0'),s=String(est.getSeconds()).padStart(2,'0');
  document.getElementById('clock').textContent=h+':'+m+':'+s+' EST';
  const months=['January','February','March','April','May','June','July','August','September','October','November','December'];
  document.getElementById('dateline').textContent=months[est.getMonth()]+' '+est.getDate()+', '+est.getFullYear();
  document.getElementById('price-time').textContent='As of '+h+':'+m+' EST';
}
setInterval(updateClock,1000);updateClock();

// ===== PAGE NAVIGATION =====
const pages=['signals','portfolio','research','settings','account'];
function showPage(name){
  pages.forEach(p=>{
    const pv=document.getElementById('page-'+p);
    if(pv) pv.classList.toggle('active',p===name);
  });
  document.querySelectorAll('.navbar-tab').forEach((t,i)=>{
    t.classList.toggle('active',pages[i]===name);
  });
}

// ===== CHART CONTROL =====
let currentSymbol='TVC:GOLD',currentInterval='D';
function buildChartUrl(sym,interval){
  return 'https://s.tradingview.com/widgetembed/?frameElementId=tv_chart&symbol='+encodeURIComponent(sym)+'&interval='+interval+'&hidesidetoolbar=0&symboledit=0&saveimage=0&toolbarbg=050b14&studies=RSI%40tv-basicstudies%2CMACD%40tv-basicstudies%2CVolume%40tv-basicstudies&theme=dark&style=1&timezone=Etc%2FUTC&withdateranges=1&hideideas=1&locale=en';
}
function setTF(el,interval){
  document.querySelectorAll('.tf-tab').forEach(t=>t.classList.remove('active'));
  el.classList.add('active');currentInterval=interval;
  document.getElementById('tv-chart').src=buildChartUrl(currentSymbol,currentInterval);
}

const srLevels={
  'XAUUSD':['R3: 2,480','R2: 2,455','R1: 2,432','S1: 2,398','S2: 2,375','S3: 2,350'],
  'SPX500':['R3: 5,450','R2: 5,380','R1: 5,340','S1: 5,280','S2: 5,220','S3: 5,150'],
  'NDX100':['R3: 19,200','R2: 18,950','R1: 18,800','S1: 18,600','S2: 18,400','S3: 18,100'],
  'BTCUSD':['R3: 75,000','R2: 73,500','R1: 72,800','S1: 71,000','S2: 69,500','S3: 67,000'],
  'EURUSD':['R3: 1.0920','R2: 1.0880','R1: 1.0850','S1: 1.0780','S2: 1.0740','S3: 1.0700'],
  'AAPL':['R3: 198','R2: 194','R1: 192','S1: 187','S2: 184','S3: 180'],
};
const signals={
  'XAUUSD':{dec:'🟢 STRONG BUY',cls:'signal-decision-buy',conf:'91% CONFIDENCE',entry:'2,418.30',stop:'2,389.10',target:'2,478.60',asset:'Gold Spot · XAU/USD'},
  'SPX500':{dec:'🟢 STRONG BUY',cls:'signal-decision-buy',conf:'94% CONFIDENCE',entry:'5,312.46',stop:'5,248.20',target:'5,445.80',asset:'S&P 500 · SPX500'},
  'NDX100':{dec:'🟢 BUY',cls:'signal-decision-buy',conf:'88% CONFIDENCE',entry:'18,742.60',stop:'18,520.00',target:'19,100.00',asset:'Nasdaq 100 · NDX100'},
  'BTCUSD':{dec:'🟢 BUY',cls:'signal-decision-buy',conf:'82% CONFIDENCE',entry:'72,140.00',stop:'70,800.00',target:'74,500.00',asset:'Bitcoin · BTC/USD'},
  'EURUSD':{dec:'🔴 SELL',cls:'signal-decision-sell',conf:'78% CONFIDENCE',entry:'1.0812',stop:'1.0860',target:'1.0740',asset:'Euro · EUR/USD'},
  'AAPL':{dec:'🟢 BUY',cls:'signal-decision-buy',conf:'85% CONFIDENCE',entry:'189.84',stop:'186.20',target:'195.50',asset:'Apple Inc. · AAPL'},
};

function setInstrument(tvSym,key,symLabel,pairLabel,price,prev){
  currentSymbol=tvSym;
  document.querySelectorAll('.inst-btn').forEach(b=>b.classList.remove('active'));
  const btn=document.getElementById('btn-'+key);
  if(btn)btn.classList.add('active');
  document.getElementById('sym-label').textContent=symLabel;
  document.getElementById('sym-pair').textContent=pairLabel;
  document.getElementById('price-label-top').textContent=pairLabel.toUpperCase();
  document.getElementById('live-price').textContent=price;
  const p=parseFloat(price.replace(/,/g,'')),pv=parseFloat(prev.replace(/,/g,''));
  const ch=p-pv,chp=(ch/pv)*100;
  const el=document.getElementById('price-change');
  el.className=ch>=0?'price-up':'price-down';
  el.textContent=(ch>=0?'▲ +':'▼ ')+ch.toFixed(2)+' ('+(chp>=0?'+':'')+chp.toFixed(2)+'%)';
  // SR levels
  const sr=srLevels[key]||[];
  const badges=document.getElementById('sr-badges');
  badges.innerHTML=sr.map((l,i)=>`<span class="sr-badge ${i<3?'sr-res':'sr-sup'}">${l}</span>`).join('');
  // Signal
  const s=signals[key]||signals['XAUUSD'];
  document.getElementById('signal-decision').textContent=s.dec;
  document.getElementById('signal-decision').className=s.cls;
  document.getElementById('signal-conf').textContent=s.conf;
  document.getElementById('sig-entry').textContent=s.entry;
  document.getElementById('sig-stop').textContent=s.stop;
  document.getElementById('sig-target').textContent=s.target;
  document.getElementById('signal-asset').textContent=s.asset;
  document.getElementById('tv-chart').src=buildChartUrl(currentSymbol,currentInterval);
}

// ===== INDICATORS =====
let indicators=[
  {name:'RSI',desc:'68 — Overbought',pct:85},
  {name:'MACD',desc:'Bullish Crossover',pct:72},
  {name:'EMA 50/200',desc:'Golden Cross Approaching',pct:65},
  {name:'Bollinger Bands',desc:'Width Expansion',pct:78},
  {name:'Volume',desc:'Surge Detected',pct:88},
  {name:'VWAP',desc:'Price Above',pct:74},
];
function renderIndicators(inds){
  document.getElementById('quant-indicators').innerHTML=inds.map(i=>`
    <div class="ind-row">
      <div class="ind-top">
        <span><span class="ind-name">${i.name}</span> <span class="ind-desc">— ${i.desc}</span></span>
        <span class="ind-pct">${i.pct}%</span>
      </div>
      <div class="ind-bar-bg"><div class="ind-bar-fill" style="width:${i.pct}%"></div></div>
    </div>`).join('');
}
renderIndicators(indicators);
setInterval(()=>{
  indicators=indicators.map(i=>({...i,pct:Math.min(99,Math.max(10,Math.round(i.pct+(Math.random()-0.5)*3)))}));
  renderIndicators(indicators);
},5000);

// ===== SMART MONEY FLOW =====
const smfData=[
  {actor:'BRIDGEWATER',time:'14:38',action:'<span class="buy">BUY</span> 12,400 lots — Gold Futures (GC)',conclusion:'Macro hedge fund accumulation at support. Bullish confluence with EMA200 bounce.'},
  {actor:'BLACKROCK',time:'14:21',action:'<span class="buy">BUY</span> 8,200 lots — Gold Futures (GC)',conclusion:'Safe-haven rotation. Aligns with DXY weakness & Fed rate pause signals.'},
  {actor:'CITADEL',time:'14:05',action:'<span class="sell">SELL</span> 5,600 lots — Nasdaq 100 (NQ)',conclusion:'Tech profit-taking post-earnings. MACD bearish divergence on 4H confirms.'},
  {actor:'RENAISSANCE',time:'13:52',action:'<span class="buy">BUY</span> 3,100 lots — BTC Perpetual',conclusion:'Quant model re-entry above 200-day MA. Volume surge +180% above avg.'},
  {actor:'TWO SIGMA',time:'13:40',action:'<span class="sell">SELL</span> 9,800 lots — EUR/USD',conclusion:'USD strength on jobs data. Price broke below VWAP — sellers in control.'},
  {actor:'MILLENNIUM',time:'13:28',action:'<span class="buy">BUY</span> 6,700 lots — Apple (AAPL)',conclusion:'Institutional accumulation pre-earnings. RSI reset from oversold.'},
  {actor:'POINT72',time:'13:15',action:'<span class="buy">BUY</span> 4,400 lots — S&P 500 (ES)',conclusion:'Momentum continuation. Golden Cross confirmed on daily — trend intact.'},
  {actor:'D.E. SHAW',time:'13:02',action:'<span class="sell">SELL</span> 2,900 lots — Gold Futures (GC)',conclusion:'Short-term overbought (RSI 74). Bollinger upper band breach — mean reversion risk.'},
];
function renderSMF(data){
  const doubled=[...data,...data];
  document.getElementById('smf-inner').innerHTML=doubled.map(d=>`
    <div class="smf-item">
      <div class="smf-header"><span class="smf-actor">🏛 ${d.actor}</span><span class="smf-time">${d.time} EST</span></div>
      <div class="smf-action">${d.action}</div>
      <div class="smf-conclusion">📊 ${d.conclusion}</div>
    </div>`).join('');
}
renderSMF(smfData);

// ===== NEWS TICKER =====
const newsItems=[
  {src:'BLOOMBERG',text:'Fed signals cautious stance on rate cuts amid sticky inflation data',time:'14:42'},
  {src:'REUTERS',text:'Gold surges past $2,400 — central bank demand hits record quarterly high',time:'14:38'},
  {src:'WSJ',text:'S&P 500 hits fresh all-time high as tech earnings beat expectations',time:'14:31'},
  {src:'FT',text:'Bridgewater increases equity exposure — Dalio cites "structural bull market"',time:'14:25'},
  {src:'CNBC',text:'Bitcoin breaks $72,000 resistance — institutional inflows at record pace',time:'14:19'},
  {src:'BARRONS',text:'Apple Q2 earnings: EPS $1.89 vs $1.72 est — services revenue up 14%',time:'14:12'},
  {src:'MARKETWATCH',text:'EUR/USD slides below 1.0820 as ECB holds rates, signals dovish pivot',time:'14:06'},
  {src:'BLOOMBERG',text:'FOMC Minutes due Wednesday — markets pricing 68% chance of September cut',time:'13:58'},
  {src:'REUTERS',text:'US GDP Q2 flash estimate Thursday — consensus at +2.1% annualized',time:'13:51'},
  {src:'FT',text:'OPEC+ maintains output cuts — Brent crude holds above $88/barrel',time:'13:44'},
  {src:'WSJ',text:'Treasury yields fall 8bps as inflation expectations moderate',time:'13:37'},
  {src:'CNBC',text:'Goldman Sachs raises Gold target to $2,700 — structural bull case intact',time:'13:30'},
];
function buildTicker(items){
  const doubled=[...items,...items];
  return doubled.map(n=>`<span class="news-ticker-item"><span class="news-src">${n.src}</span><span class="news-text">${n.text}</span><span class="news-time">${n.time}</span><span class="news-sep"> · </span></span>`).join('');
}
document.getElementById('ticker-inner').innerHTML=buildTicker(newsItems);
</script>
</body>
</html>
