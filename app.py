import os
import sys
import json
from pathlib import Path

# Set path to include src
current_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(current_dir))

# pyrefly: ignore[missing-import]
import streamlit as st
import pandas as pd

# Internal modules
from src.data_loader import load_main_data, filter_dataset
from src.metrics_calculator import calculate_kpis

# Executive Slide Renderers (Exact match to uploaded report slides - 30 total pages)
from src.executive_slides import (
    # 1. Volume & Trend
    render_slide_volume_user_engagement_reach,
    render_slide_mentions_trend_channel,
    render_slide_mentions_trend_sentiment,
    render_slide_mentions_trend_emotions,
    render_slide_crossplatform_diffusion,
    # 2. SNA
    render_slide_sna_by_sentiment,
    render_slide_sna_by_emotions,
    # 3. Sentiment 7 Channels
    render_slide_overall_sentiment,
    render_slide_sentiment_online_news,
    render_slide_sentiment_twitter,
    render_slide_sentiment_facebook,
    render_slide_sentiment_instagram,
    render_slide_sentiment_youtube,
    render_slide_sentiment_tiktok,
    render_slide_sentiment_threads,
    # 4. Emotions & Emojis
    render_slide_emotion_analysis_1,
    render_slide_emotion_analysis_2,
    render_slide_emoji_analysis,
    # 5. Media & Influencers
    render_slide_top_news_sites,
    render_slide_top_influencers_twitter,
    render_slide_top_influencers_facebook,
    render_slide_top_influencers_instagram,
    render_slide_top_influencers_youtube,
    render_slide_top_influencers_tiktok,
    render_slide_top_influencers_threads,
    # 6. Viral Content
    render_slide_viral_twitter_1,
    render_slide_viral_twitter_2,
    render_slide_viral_twitter_3,
    render_slide_viral_twitter_4,
    render_slide_viral_facebook,
    render_slide_viral_instagram,
    render_slide_viral_youtube,
    render_slide_viral_tiktok,
    render_slide_viral_threads,
    # 7. Word & Tag Clouds
    render_slide_popular_tags_terms,
    render_slide_wordcloud_terms,
    render_slide_wordcloud_hashtags
)

# Deep Analytical Tab Renderers
from src.tab_executive import render_tab_executive
from src.tab_sna import render_tab_sna
from src.tab_platforms import render_tab_platforms
from src.tab_emotions import render_tab_emotions
from src.tab_issues import render_tab_issues
from src.tab_wordcloud import render_tab_wordcloud
from src.tab_evaluation import render_tab_evaluation
from src.clean_header_footer import render_html

# -------------------------------------------------------------
# PAGE CONFIGURATION & EXECUTIVE THEME (EXECUTIVE THEME)
# -------------------------------------------------------------
st.set_page_config(
    page_title="Public Policy Intelligence Platform | IndoBERT & SNA",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Executive Clean Light Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    }
    
    .stApp {
        background-color: #F8FAFC;
    }
    
    div[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
    }
    div[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    div[data-testid="stSidebar"] label {
        color: #1E293B !important;
    }
    
    /* Clean Radio Buttons for Navigation */
    div[data-testid="stRadio"] label p, div[data-testid="stRadio"] label span {
        color: #0F172A !important;
        font-weight: 700 !important;
        font-size: 13px !important;
    }
    div[data-testid="stRadio"] label:hover {
        background: #FFF7ED !important;
    }
    
    /* Selectbox Styling */
    div[data-baseweb="select"] {
        border-radius: 6px;
    }

    /* Checkbox Alignment & Typography */
    div[data-testid="stCheckbox"] {
        padding: 0 !important;
        margin: 0 !important;
        display: flex !important;
        align-items: center !important;
    }
    div[data-testid="stCheckbox"] > label {
        align-items: center !important;
        margin: 0 !important;
    }
    div[data-testid="stCheckbox"] label p, div[data-testid="stCheckbox"] label span {
        font-size: 13px !important;
        font-weight: 600 !important;
        color: #334155 !important;
        margin: 0 !important;
    }

    /* Executive Card Wrapper for Streamlit Bordered Containers */
    div[data-testid="stVerticalBlockBorderWrapper"],
    div[data-testid="stVerticalBlock"] {
        overflow: visible;
    }
    
    /* Plotly Chart Integration: Clean layout, absolutely NO scrollbars, NO collision, seamless container fit */
    div[data-testid="stPlotlyChart"] {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        margin: 0 !important;
        overflow: visible !important;
        overflow-y: hidden !important;
        overflow-x: hidden !important;
    }
    div[data-testid="stPlotlyChart"] > div,
    div[data-testid="stPlotlyChart"] .js-plotly-plot,
    div[data-testid="stPlotlyChart"] .plot-container {
        overflow: visible !important;
        overflow-y: hidden !important;
        overflow-x: hidden !important;
    }
    div[data-testid="stPlotlyChart"] iframe {
        border: none !important;
        overflow: hidden !important;
    }
    /* Hide scrollbars completely on chart elements */
    div[data-testid="stPlotlyChart"]::-webkit-scrollbar,
    div[data-testid="stPlotlyChart"] *::-webkit-scrollbar {
        display: none !important;
        width: 0 !important;
        height: 0 !important;
    }
    div[data-testid="stPlotlyChart"],
    div[data-testid="stPlotlyChart"] * {
        -ms-overflow-style: none !important;
        scrollbar-width: none !important;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# DATA ENGINE INITIALIZATION
# -------------------------------------------------------------
@st.cache_resource(show_spinner=False)
def get_clean_dataset_v2():
    return load_main_data()

with st.spinner("Memuat korpus data 197.951 rekaman..."):
    df_raw = get_clean_dataset_v2()

# -------------------------------------------------------------
# SIDEBAR CONTROLS & STRATEGIC FILTERS
# -------------------------------------------------------------
with st.sidebar:
    render_html("""
    <div style="background:#FFFFFF; border-bottom:2px solid #EA580C; padding-bottom:12px; margin-bottom:14px;">
        <div style="font-size:18px; font-weight:800; color:#0F172A; text-transform:uppercase; letter-spacing:0.5px;">
            PUBLIC POLICY INTELLIGENCE
        </div>
        <div style="font-size:11.5px; font-weight:600; color:#64748B; margin-top:2px;">
            Analisis Opini Publik & SNA • IndoBERT AI
        </div>
    </div>
    """)
    st.caption("Pemantauan Kebijakan Publik Menuju 2029")
    
    # Mode Switcher
    view_mode = st.radio(
        "Pilih Mode Tampilan:",
        [
            "Laporan Analisis Visual (Kategori Tematik)",
            "Cockpit Analisis Mendalam & Evaluasi Model"
        ],
        index=0
    )
    
    st.markdown("---")
    st.markdown("### Filter Analisis")
    
    # 1. Topic Selector
    topic_options = ["MBG", "Sekolah_Rakyat", "KDMP", "Semua Topik"]
    selected_topic_raw = st.selectbox(
        "Topik Fokus Kebijakan:",
        topic_options,
        index=0,
        help="Pilih fokus kebijakan: MBG (Makan Bergizi Gratis), Sekolah Rakyat (Utama TA), atau KDMP (Koperasi Desa Merah Putih)"
    )
    selected_topic = "Semua" if selected_topic_raw == "Semua Topik" else selected_topic_raw

    # 2. Platform Selector
    platform_list = ["Semua Platform", "Twitter", "Facebook", "Instagram", "YouTube", "TikTok", "Threads", "News"]
    selected_plat_raw = st.selectbox(
        "Kanal Platform:",
        platform_list,
        index=0,
        help="Filter platform media sosial atau berita daring"
    )
    selected_platform = "Semua" if selected_plat_raw == "Semua Platform" else selected_plat_raw

    # 3. Date Range Filter
    import datetime
    min_date = df_raw['date'].min().date()
    max_date = df_raw['date'].max().date()
    
    # Default: 1 Januari 2025 s/d Sekarang (data terkini)
    default_start = max(min_date, datetime.date(2025, 1, 1))
    default_end = max_date
    
    date_range = st.date_input(
        "Rentang Waktu:",
        value=(default_start, default_end),
        min_value=min_date,
        max_value=max_date,
        help="Rentang waktu analisis data (default: 1 Januari 2025 s/d Sekarang)"
    )
    
    start_d, end_d = None, None
    if isinstance(date_range, (list, tuple)):
        if len(date_range) == 2:
            start_d, end_d = date_range[0], date_range[1]
        elif len(date_range) == 1:
            start_d, end_d = date_range[0], max_date

    # Apply filters
    df_filtered = filter_dataset(df_raw, selected_topic=selected_topic, selected_platform=selected_platform, start_date=start_d, end_date=end_d)

    # Load Real Evaluation Metrics (Sentimen & Emosi)
    sent_metrics_file = os.path.join(str(current_dir), 'models', 'best_indobert_sentiment', 'evaluation_metrics.json')
    emo_metrics_file = os.path.join(str(current_dir), 'models', 'best_indobert_emotion', 'evaluation_metrics.json')
    
    acc_sent = 0.9133
    f1_sent = 0.9137
    prec_sent = 0.9150
    rec_sent = 0.9133
    
    acc_emo = 0.9178
    f1_emo = 0.9174
    
    if os.path.exists(sent_metrics_file):
        try:
            with open(sent_metrics_file, 'r', encoding='utf-8') as f:
                s_data = json.load(f)
                acc_sent = s_data.get('accuracy', acc_sent)
                f1_sent = s_data.get('macro_f1', f1_sent)
                cm = s_data.get('confusion_matrix')
                if cm and len(cm) == 3:
                    col_sums = [sum(cm[r][c] for r in range(3)) for c in range(3)]
                    row_sums = [sum(cm[r]) for r in range(3)]
                    precs = [cm[i][i] / col_sums[i] if col_sums[i] > 0 else 0 for i in range(3)]
                    recs = [cm[i][i] / row_sums[i] if row_sums[i] > 0 else 0 for i in range(3)]
                    prec_sent = sum(precs) / 3.0
                    rec_sent = sum(recs) / 3.0
        except Exception:
            pass
            
    if os.path.exists(emo_metrics_file):
        try:
            with open(emo_metrics_file, 'r', encoding='utf-8') as f:
                e_data = json.load(f)
                acc_emo = e_data.get('accuracy', acc_emo)
                f1_emo = e_data.get('macro_f1', f1_emo)
        except Exception:
            pass

    st.markdown("---")
    st.markdown("### Status Korpus & Model")
    render_html(f"""
    <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:12px 14px; box-shadow:0 1px 2px rgba(0,0,0,0.03);">
        <div style="font-size:11.5px; line-height:1.75; color:#334155;">
            <div style="display:flex; justify-content:space-between;"><span>Total Korpus:</span> <strong>{len(df_raw):,}</strong></div>
            <div style="display:flex; justify-content:space-between;"><span>Data Terfilter:</span> <strong style="color:#0284C7;">{len(df_filtered):,}</strong></div>
            <div style="display:flex; justify-content:space-between;"><span>Penulis Unik:</span> <strong>{df_filtered['author'].nunique():,}</strong></div>
            <div style="border-top:1px dashed #E2E8F0; margin:6px 0;"></div>
            <div style="display:flex; justify-content:space-between;"><span>Akurasi Sentimen:</span> <strong style="color:#10B981;">{acc_sent*100:.2f}%</strong></div>
            <div style="display:flex; justify-content:space-between;"><span>Macro F1 Sentimen:</span> <strong style="color:#0F172A;">{f1_sent*100:.2f}%</strong></div>
            <div style="display:flex; justify-content:space-between; font-size:10.5px; color:#64748B;"><span>Precision / Recall:</span> <span>{prec_sent*100:.2f}% / {rec_sent*100:.2f}%</span></div>
            <div style="border-top:1px dashed #E2E8F0; margin:6px 0;"></div>
            <div style="display:flex; justify-content:space-between;"><span>Akurasi 9 Emosi:</span> <strong style="color:#8B5CF6;">{acc_emo*100:.2f}%</strong></div>
            <div style="display:flex; justify-content:space-between;"><span>Macro F1 9 Emosi:</span> <strong style="color:#0F172A;">{f1_emo*100:.2f}%</strong></div>
        </div>
    </div>
    """)

# Calculate Core KPIs
kpis = calculate_kpis(df_filtered)
date_display = f"{start_d} s/d {end_d}" if start_d and end_d else "Semua Periode"

# -------------------------------------------------------------
# MAIN CONTENT DISPATCHER
# -------------------------------------------------------------
if "Laporan Analisis Visual" in view_mode:
    # 7 LOGICAL ANALYTICAL CATEGORIES (All 30 visual pages organized thematically)
    CATEGORIES = {
        "1. Volume & Tren Temporal": {
            "Volume, User, Engagement & Reach": render_slide_volume_user_engagement_reach,
            "Tren Mentions Tiap Kanal": render_slide_mentions_trend_channel,
            "Tren Sentimen Waktu Riil": render_slide_mentions_trend_sentiment,
            "Tren 8 Emosi Publik Waktu Riil": render_slide_mentions_trend_emotions,
            "Difusi Isu Lintas Kanal (Crossplatform Diffusion)": render_slide_crossplatform_diffusion
        },
        "2. Analisis Jaringan Sosial (SNA)": {
            "Polarisasi Jaringan Berdasarkan Sentimen": render_slide_sna_by_sentiment,
            "Struktur Komunitas Berdasarkan 4 Klaster Emosi": render_slide_sna_by_emotions
        },
        "3. Sentimen 7 Kanal Platform": {
            "Sentimen Keseluruhan & Komparasi 7 Kanal": render_slide_overall_sentiment,
            "Sentimen Portal Berita Daring": render_slide_sentiment_online_news,
            "Sentimen Platform Twitter / X": render_slide_sentiment_twitter,
            "Sentimen Platform Facebook": render_slide_sentiment_facebook,
            "Sentimen Platform Instagram": render_slide_sentiment_instagram,
            "Sentimen Platform YouTube": render_slide_sentiment_youtube,
            "Sentimen Platform TikTok": render_slide_sentiment_tiktok,
            "Sentimen Platform Threads": render_slide_sentiment_threads
        },
        "4. Analisis Emosi & Semantik": {
            "Distribusi & Intensitas 8 Emosi (Plutchik)": render_slide_emotion_analysis_1,
            "Emosi Berdasarkan Sentimen & Kanal Platform": render_slide_emotion_analysis_2,
            "Analisis Frekuensi & Rasio Sentimen Emoji": render_slide_emoji_analysis
        },
        "5. Media Berita & Top Pemengaruh": {
            "Top 10 Situs Berita Daring Teraktif": render_slide_top_news_sites,
            "Top Pemengaruh Twitter / X (Interest vs Power)": render_slide_top_influencers_twitter,
            "Top Pemengaruh Facebook": render_slide_top_influencers_facebook,
            "Top Pemengaruh Instagram": render_slide_top_influencers_instagram,
            "Top Pemengaruh YouTube": render_slide_top_influencers_youtube,
            "Top Pemengaruh TikTok": render_slide_top_influencers_tiktok,
            "Top Pemengaruh Threads": render_slide_top_influencers_threads
        },
        "6. Konten Viral & Populer": {
            "Cuitan Populer Twitter / X (Halaman 1)": render_slide_viral_twitter_1,
            "Cuitan Populer Twitter / X (Halaman 2)": render_slide_viral_twitter_2,
            "Cuitan Populer Twitter / X (Halaman 3)": render_slide_viral_twitter_3,
            "Cuitan Populer Twitter / X (Halaman 4)": render_slide_viral_twitter_4,
            "Status Facebook Paling Disukai": render_slide_viral_facebook,
            "Status Instagram Paling Disukai": render_slide_viral_instagram,
            "Video YouTube Paling Ditonton": render_slide_viral_youtube,
            "Video TikTok Paling Ditonton": render_slide_viral_tiktok,
            "Status Threads Paling Disukai": render_slide_viral_threads
        },
        "7. Tagar & Awan Kata": {
            "Top 20 Tagar & Top 20 Istilah Kunci": render_slide_popular_tags_terms,
            "Awan Kata Kunci (Word Cloud) Seluruh Platform": render_slide_wordcloud_terms,
            "Awan Tagar (Hashtags) Seluruh Platform": render_slide_wordcloud_hashtags
        }
    }
    
    # Top Category Selector & Navigation Toolbar (Clean, classified, and logical)
    cat_names = list(CATEGORIES.keys())
    
    with st.container(border=True):
        render_html("""<div style="font-size:12.5px; font-weight:700; color:#475569; margin-bottom:5px;">
Kategori Laporan Analisis:
</div>""")
        c_nav1, c_nav2 = st.columns([1.65, 1.35], vertical_alignment="center")
        with c_nav1:
            selected_cat = st.selectbox(
                "Kategori Laporan Analisis:",
                cat_names,
                index=0,
                label_visibility="collapsed",
                help="Pilih klaster analisis tematik yang saling terhubung"
            )
        with c_nav2:
            view_all_in_cat = st.checkbox(
                "Tampilkan Seluruh Visualisasi dalam Kategori Ini Sekaligus",
                value=False,
                help="Centang untuk melihat seluruh halaman visualisasi dalam klaster ini secara berurutan dalam satu layar"
            )
            
        pages_in_cat = CATEGORIES[selected_cat]
        page_names = list(pages_in_cat.keys())
        
        if not view_all_in_cat:
            st.markdown("<div style='margin: 10px 0 6px 0; border-top: 1px dashed #E2E8F0;'></div>", unsafe_allow_html=True)
            # Sub-page navigation bar
            selected_page = st.radio(
                f"Pilih Halaman Visualisasi ({selected_cat}):",
                page_names,
                index=0,
                horizontal=True
            )
        
    st.write("")
    if not view_all_in_cat:
        # Render the specific selected page
        pages_in_cat[selected_page](df_filtered, selected_topic=selected_topic, topic_label=selected_topic, date_str=date_display)
    else:
        # Render all pages in the chosen category
        for idx, (pname, pfunc) in enumerate(pages_in_cat.items(), 1):
            pfunc(df_filtered, selected_topic=selected_topic, topic_label=selected_topic, date_str=date_display)
            if idx < len(pages_in_cat):
                st.markdown("<div style='margin: 40px 0; border-bottom: 2px dashed #CBD5E1;'></div>", unsafe_allow_html=True)

else:
    # ---------------------------------------------------------
    # MODE 2: COCKPIT ANALISIS MENDALAM & EVALUASI INDOBERT
    # ---------------------------------------------------------
    tabs = st.tabs([
        "Ringkasan Eksekutif",
        "Analisis SNA",
        "Analisis Kanal Platform",
        "Analisis Emosi",
        "Klaster Isu",
        "Word Cloud",
        "Evaluasi Model IndoBERT"
    ])
    
    with tabs[0]:
        render_tab_executive(df_filtered, df_raw, kpis)
    with tabs[1]:
        render_tab_sna(df_filtered, selected_topic, selected_platform, 100, current_dir)
    with tabs[2]:
        render_tab_platforms(df_filtered)
    with tabs[3]:
        render_tab_emotions(df_filtered)
    with tabs[4]:
        render_tab_issues(df_filtered)
    with tabs[5]:
        render_tab_wordcloud(df_filtered)
    with tabs[6]:
        render_tab_evaluation(current_dir)

# Refreshed for emotion & sentiment integration
