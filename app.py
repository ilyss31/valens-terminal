import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import time
import random
import feedparser

# Sayfa yapılandırması en başta olmalı
st.set_page_config(page_title="Valens Wealth", layout="wide", initial_sidebar_state="expanded", page_icon="💎")

# --- SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = 'landing'
if 'lang' not in st.session_state: st.session_state.lang = 'EN'

# --- DİL ÇEVİRİLERİ ---
t_data = {
    "EN": {
        "btn": "Connect to Valens Terminal →", "title": "VALENS WEALTH | QUANT TERMINAL",
        "live": "LIVE DATA", "market": "Market", "start": "🚀 Start Bot",
        "price": "Current Price", "rsi": "RSI (14)", "macd": "MACD", "mom": "Momentum"
    },
    "TR": {
        "btn": "Valens Terminal'e Bağlan →", "title": "VALENS WEALTH | QUANT TERMINAL",
        "live": "CANLI VERİ", "market": "Piyasa", "start": "🚀 Botu Başlat",
        "price": "Güncel Fiyat", "rsi": "RSI (14)", "macd": "MACD", "mom": "Momentum"
    }
}
t = t_data[st.session_state.lang]

# --- CSS (Tasarım) ---
st.markdown("""
    <style>
    .stApp { background: radial-gradient(ellipse at top, #10254E 0%, #060D1C 68%); color: #ECE9E2; }
    .ticker-wrap { width: 100%; background-color: rgba(10,24,48,0.8); border-bottom: 1px solid #C9A961; padding: 10px 0; overflow: hidden; white-space: nowrap; }
    .ticker-text { display: inline-block; padding-left: 100%; animation: ticker 30s linear infinite; color: #ECE9E2; font-family: 'IBM Plex Mono'; }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }
    </style>
""", unsafe_allow_html=True)

# --- SAYFA MANTIĞI ---
if st.session_state.page == 'landing':
    st.markdown("<br><br><h1 style='text-align:center;'>VALENS WEALTH</h1>", unsafe_allow_html=True)
    if st.button(t['btn'], use_container_width=True, type="primary"):
        st.session_state.page = 'dashboard'
        st.rerun()

elif st.session_state.page == 'dashboard':
    # Haber Bandı
    st.markdown(f'<div class="ticker-wrap"><div class="ticker-text">[VALENS AI] System Online • {t["live"]} • Market activity monitored...</div></div>', unsafe_allow_html=True)
    
    # Sidebar
    symbol = st.sidebar.selectbox("Symbol", ["BTC-USD", "ETH-USD"])
    if st.sidebar.button("Back to Home"):
        st.session_state.page = 'landing'
        st.rerun()

    # Dashboard
    st.title(t['title'])
    
    # Veri + Grafik (Hata önleyici try-except)
    try:
        df = yf.download(symbol, period="1d", interval="15m", progress=False)
        if not df.empty:
            price = float(df['Close'].iloc[-1])
            st.metric(t['price'], f"${price:,.2f}")
            
            fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
            st.plotly_chart(fig, use_container_width=True)
            
            if st.button(t['start']):
                st.write("AI Analizi yapılıyor...")
                time.sleep(1)
                st.success("Sistem hazır: Analiz raporu üretildi.")
        else:
            st.error("Veri çekilemedi.")
    except Exception as e:
        st.error(f"Sistem hatası: {e}")
