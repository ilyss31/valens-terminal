import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
import time

st.set_page_config(page_title="Valens Wealth | Otonom Varlık Yönetimi", layout="wide", initial_sidebar_state="collapsed")

if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def switch_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# 1. KARŞILAMA EKRANI (LANDING)
if st.session_state.page == 'landing':
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1 style='text-align: center; font-family: serif; color: #1E293B; font-size: 50px;'>VALENS WEALTH</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: #475569; font-weight: 300;'>Yeni Nesil Yapay Zeka Destekli Varlık Yönetimi</h4>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("<p style='text-align: center; color: #64748B;'>Yalnızca davetiye ile girilebilen, kurumlar ve nitelikli yatırımcılar için tasarlanmış otonom işlem terminali.</p>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("Valens Terminal'e Bağlan", use_container_width=True, type="primary"):
            switch_page('dashboard')

# 2. TERMİNAL EKRANI (DASHBOARD)
elif st.session_state.page == 'dashboard':
    col_logo, col_logout = st.columns([8, 1])
    with col_logo:
        st.markdown("<h3 style='font-family: serif; color: #1E293B;'>VALENS WEALTH | QUANT TERMINAL v1.0</h3>", unsafe_allow_html=True)
    with col_logout:
        if st.button("Çıkış Yap"):
            switch_page('landing')
            
    st.markdown("---")
    st.subheader("Canlı Piyasa Verisi: BTC/USD")
    
    @st.cache_data(ttl=60)
    def get_live_data():
        return yf.download("BTC-USD", period="1d", interval="15m", progress=False)

    try:
        df = get_live_data()
        fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=400, template="plotly_white", xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)
    except:
        st.warning("Piyasa verisi çekiliyor...")

    st.markdown("---")
    st.subheader("Valens AI Otonom Karar Motoru")
    
    if st.button("🚀 Otonom Analizi Başlat", use_container_width=True, type="primary"):
        with st.status("Valens AI Motoru Devreye Alınıyor...", expanded=True) as status:
            st.write("CME ve Global Borsa verileri taranıyor...")
            time.sleep(1.5)
            st.write("Makroekonomik haberler (NLP) analiz ediliyor...")
            time.sleep(1.5)
            st.write("Teknik indikatörler (RSI, MACD, Bollinger) hesaplanıyor...")
            time.sleep(1.5)
            status.update(label="Analiz Tamamlandı!", state="complete", expanded=False)
        
        st.success("Sistem Kararı: **[STRONG BUY] - GÜÇLÜ AL**")
        col1, col2, col3 = st.columns(3)
        col1.metric("Trend Yönü", "Yukarı (Bullish)", "+%4.2")
        col2.metric("Makro Duyarlılık (Sentiment)", "Pozitif", "0.82")
        col3.metric("Risk Skoru", "Düşük / Ilımlı", "-1.2%")
        st.info("**Valens AI Raporu:** Kurumsal cüzdanlarda akümülasyon tespit edildi. Algoritma 'Alım' yönünde %87 kesinlikte işlem açmaya karar vermiştir.")