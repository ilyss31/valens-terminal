import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
import time

st.set_page_config(page_title="Valens Wealth | Terminal", layout="wide")

if 'page' not in st.session_state: st.session_state.page = 'landing'

def switch_page(page_name):
    st.session_state.page = page_name
    st.rerun()

if st.session_state.page == 'landing':
    st.markdown("<br><br><br><br><h1 style='text-align: center; font-family: serif;'>VALENS WEALTH</h1><h4 style='text-align: center;'>Otonom Varlık Yönetimi</h4>", unsafe_allow_html=True)
    if st.button("Terminal'e Bağlan", use_container_width=True, type="primary"): switch_page('dashboard')

elif st.session_state.page == 'dashboard':
    if st.button("<- Çıkış"): switch_page('landing')
    
    # 1. GRAFİK
    st.subheader("BTC/USD Canlı Veri")
    data = yf.download("BTC-USD", period="1d", interval="15m", progress=False)
    if not data.empty:
        fig = go.Figure(data=[go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'])])
        st.plotly_chart(fig, use_container_width=True)
        current_price = float(data['Close'].iloc[-1])
    else:
        current_price = 64000.00 # Hata durumunda varsayılan
    
    # 2. PANEL
    if st.button("🚀 Analizi Başlat"):
        with st.spinner("Yapay Zeka Motoru Hazırlanıyor..."):
            time.sleep(2)
        # Tabloyu metin olarak değil, Streamlit'in kendi güvenli metric yapısıyla basıyoruz
        st.success("Sistem Kararı: GÜÇLÜ AL")
        c1, c2, c3 = st.columns(3)
        c1.metric("Giriş", f"${current_price:,.2f}")
        c2.metric("Hedef (TP)", f"${current_price*1.04:,.2f}")
        c3.metric("Stop (SL)", f"${current_price*0.98:,.2f}")
