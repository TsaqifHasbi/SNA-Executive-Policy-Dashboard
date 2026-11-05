# MH Weekly Executive Monitoring Report Slides
# Recreating the exact 21-slide report layout and data

# pyrefly: ignore[missing-import]
import streamlit as st
import pandas as pd
# pyrefly: ignore[missing-import]
import plotly.graph_objects as go

from src.mh_style import (
    render_html,
    render_mh_top_bar,
    render_mh_title,
    render_kpi_chips,
    render_status_badge,
    render_callout_target,
    render_prioritas_banner,
    render_mh_footer,
    render_chapter_break
)

FOOTNOTE_SOURCE = "Sistem Pemantauan Harian proyek Kementerian PU (279) dan Menteri PU (280), Pemantau Delta, empat berkas analisis 28 Okt, media terbuka. Saringan aktif diterapkan."

# ==============================================================================
# SLIDE 1: COVER EDISI SPESIAL MINGGUAN
# ==============================================================================
def render_slide_1_cover(df=None, **kwargs):
    render_mh_top_bar(slide_num=None)
    
    col_left, col_right = st.columns([1.1, 0.9], gap="large")
    
    with col_left:
        html_title = """<div style="padding: 10px 0;">
<div style="font-size: 34px; font-weight: 800; color: #0F2942; line-height: 1.15; font-family:'Plus Jakarta Sans',sans-serif;">
Edisi Spesial<br><span style="color: #2563EB;">Mingguan</span>
</div>
<div style="font-size: 16px; font-weight: 700; color: #1E293B; margin: 12px 0 8px 0;">
Laporan Pekan 26 Okt-1 Nov untuk Pimpinan
</div>
<div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 16px;">
Sorotan khusus: panggung bergeser dari perkara Sumut ke air - Kali Angke, Karian, dan banjir awal musim. Dilengkapi empat berkas analisis (lembaga dan menteri), penanganan bencana, dan proyeksi 7 hari.
</div>
<div style="margin-bottom: 20px;">
<span style="background: #2563EB; color: #FFFFFF; font-weight: 700; font-size: 11px; padding: 4px 12px; border-radius: 20px; letter-spacing: 0.5px;">2 NOVEMBER 2026</span>
</div>
</div>"""
        render_html(html_title)
        
        # 4 KPI cards
        kpis_row = """<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
<div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
<div style="width: 8px; height: 8px; border-radius: 50%; background: #2563EB; margin-bottom: 6px;"></div>
<div style="font-size: 26px; font-weight: 800; color: #0F2942;">13%</div>
<div style="font-size: 11px; color: #64748B;">negatif lembaga, turun dari 20%</div>
</div>
<div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
<div style="width: 8px; height: 8px; border-radius: 50%; background: #2563EB; margin-bottom: 6px;"></div>
<div style="font-size: 26px; font-weight: 800; color: #0F2942;">19%</div>
<div style="font-size: 11px; color: #64748B;">negatif menteri, naik dari 12%</div>
</div>
<div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
<div style="width: 8px; height: 8px; border-radius: 50%; background: #2563EB; margin-bottom: 6px;"></div>
<div style="font-size: 26px; font-weight: 800; color: #0F2942;">200 rb</div>
<div style="font-size: 11px; color: #64748B;">tayangan video Kali Angke</div>
</div>
<div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
<div style="width: 8px; height: 8px; border-radius: 50%; background: #2563EB; margin-bottom: 6px;"></div>
<div style="font-size: 26px; font-weight: 800; color: #0F2942;">784 rb</div>
<div style="font-size: 11px; color: #64748B;">tayangan video jembatan tali Aceh</div>
</div>
</div>"""
        render_html(kpis_row)

    with col_right:
        # Chart 1: Percakapan tentang lembaga - negatif per hari
        render_html("""<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:12px 16px; margin-bottom:12px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:11px; font-weight:700; color:#475569; letter-spacing:0.5px; margin-bottom:6px; text-transform:uppercase;">PERCAKAPAN TENTANG LEMBAGA - NEGATIF PER HARI</div>
</div>""")
        
        dates = ['26 Okt', '27 Okt', '28 Okt', '29 Okt', '30 Okt', '31 Okt', '1 Nov']
        neg_counts = [99, 80, 35, 55, 45, 43, 10]
        
        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(
            x=dates, y=neg_counts,
            mode='lines+markers',
            line=dict(color='#2563EB', width=3),
            marker=dict(size=7, color='#2563EB')
        ))
        fig_line.update_layout(
            height=140,
            margin=dict(l=25, r=15, t=10, b=25),
            paper_bgcolor='#FFFFFF',
            plot_bgcolor='#FFFFFF',
            xaxis=dict(showgrid=False, tickfont=dict(size=9.5, color='#64748B')),
            yaxis=dict(showgrid=True, gridcolor='#F1F5F9', tickfont=dict(size=9, color='#64748B'), range=[0, 120])
        )
        st.plotly_chart(fig_line, use_container_width=True, config={'displayModeBar': False})
        
        # Chart 2: Sentimen Keseluruhan
        render_html("""<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:10px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:11px; font-weight:700; color:#475569; letter-spacing:0.5px; margin-bottom:4px; text-transform:uppercase;">SENTIMEN KESELURUHAN</div>
</div>""")
        
        fig_donut = go.Figure(data=[go.Pie(
            labels=['Positif', 'Netral', 'Negatif'],
            values=[34.1, 53.4, 12.5],
            hole=.65,
            marker_colors=['#10B981', '#64748B', '#EF4444'],
            textinfo='label+percent',
            textposition='outside',
            showlegend=False
        )])
        fig_donut.update_layout(
            height=170,
            margin=dict(l=10, r=10, t=10, b=10),
            paper_bgcolor='#FFFFFF'
        )
        st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})

    render_mh_footer(FOOTNOTE_SOURCE)


# ==============================================================================
# SLIDE 2: EXECUTIVE SUMMARY
# ==============================================================================
def render_slide_2_executive_summary(df=None, **kwargs):
    render_mh_top_bar(slide_num=2)
    render_mh_title(
        "Executive Summary",
        "Perkara mereda; panggung pindah ke air dan survei",
        "Enam temuan dari pemantauan (279, 280), empat berkas, Pemantau Delta, media. Pita biru: prioritas."
    )
    
    chips = [
        {"label": "Penyebutan Lembaga", "val": "2.935", "sub": "turun dari 3.375", "dot": "#2563EB", "val_color": "#2563EB"},
        {"label": "Positif Lembaga", "val": "34%", "sub": "turun dari 53%", "dot": "#10B981", "val_color": "#10B981"},
        {"label": "Negatif Lembaga", "val": "13%", "sub": "turun dari 20%", "dot": "#EF4444", "val_color": "#EF4444"},
        {"label": "Puncak Negatif", "val": "99", "sub": "lembaga, 26 Okt", "dot": "#EF4444", "val_color": "#EF4444"},
        {"label": "Negatif Menteri", "val": "19%", "sub": "naik dari 12%", "dot": "#10B981", "val_color": "#10B981"}
    ]
    render_kpi_chips(chips)
    
    # 6 Temuan Utama Grid
    findings_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:16px 20px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:13.5px; font-weight:700; color:#0F2942; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
<span style="width:8px; height:8px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Enam Temuan Utama Sepekan
</div>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px 24px;">
<div>
<div style="font-weight:700; font-size:12px; color:#1E293B; margin-bottom:2px;">1. Perkara Sumut mereda</div>
<div style="font-size:11px; color:#475569; line-height:1.45;">Negatif lembaga 99 pada 26 Okt (gema agenda KPK), lalu 35-55 per hari; X senyap sejak 30 Okt. Sepekan: 13% dari 2.935.</div>
</div>
<div>
<div style="font-weight:700; font-size:12px; color:#1E293B; margin-bottom:2px;">2. Video terbesar lahir dari air</div>
<div style="font-size:11px; color:#475569; line-height:1.45;">Susur Sungai Angke 200 rb tayang (31 Okt); Karian surut 121 rb (29 Okt); 'kali angke' muncul di 6 platform dalam sehari.</div>
</div>
<div>
<div style="font-weight:700; font-size:12px; color:#1E293B; margin-bottom:2px;">3. Menteri tertekan kolom komentar</div>
<div style="font-size:11px; color:#475569; line-height:1.45;">Negatif menteri 19% (178 dari 952), puncak 27% pada 29 Okt; Instagram 31% negatif, berita daring hanya 2%.</div>
</div>
<div>
<div style="font-weight:700; font-size:12px; color:#1E293B; margin-bottom:2px;">4. Sekolah Rakyat pengangkat terkuat</div>
<div style="font-size:11px; color:#475569; line-height:1.45;">Tiga unggahan teratas menteri bertema Sekolah Rakyat (2.293; 1.837; 1.524 keterlibatan); 153 sebutan, nada +69.</div>
</div>
<div>
<div style="font-weight:700; font-size:12px; color:#1E293B; margin-bottom:2px;">5. Tidak ada serangan terorganisir</div>
<div style="font-size:11px; color:#475569; line-height:1.45;">Pola serempak yang terukur hanya tagar internal #PU608 dan #SigapMembangun: 169 unggahan, 93 akun, puncak jam kerja.</div>
</div>
<div>
<div style="font-weight:700; font-size:12px; color:#1E293B; margin-bottom:2px;">6. Banjir datang, balai belum terlihat</div>
<div style="font-size:11px; color:#475569; line-height:1.45;">Video jembatan tali Aceh 784 rb tayang tanpa jawaban; banjir Aceh 1 Nov belum ada rilis balai. Hadir di NTT, Bandung, Kalbar.</div>
</div>
</div>
</div>"""
    render_html(findings_html)
    
    # PRIORITAS Box
    render_prioritas_banner([
        ("Rilis banjir Aceh-Sumbar", "BWS Sumatera I dan V: kegiatan, alat berat, dan air bersih dalam 24 jam."),
        ("Jadwal kerja lokasi kunjungan", "Kali Angke dan Cipaganti: tanggal pengerukan dan geobag, sebelum hujan menguji."),
        ("Jawab survei dengan capaian", "Sekolah Rakyat, irigasi Rp2,99 T, jalan perbatasan - lembar capaian tanpa polemik.")
    ])
    
    # Callout
    render_callout_target("Penentu pekan depan: apakah kerja di lokasi yang sudah viral - Kali Angke, Cipaganti, Aceh - terlihat sebelum hujan dan survei membingkainya sebagai janji.")
    render_mh_footer("Sumber: Proyek 279 dan 280, 26 Okt-1 Nov (ditarik 2 Nov 09.15 WIB; pembanding 19-25 Okt); berkas Topik, Framing (279), Isu Pos-Neg, Stakeholder (280) 28 Okt; Pemantau Delta; Antara, Kompas.com, Koran Jakarta.")


# ==============================================================================
# SLIDE 3: CHAPTER 01 - THE OVERVIEW
# ==============================================================================
def render_slide_3_chapter_1(df=None, **kwargs):
    render_chapter_break(
        1,
        "The Overview",
        "Volume dan nada sepekan untuk lembaga (279) dan menteri (280) dibanding pekan lalu, tujuh saluran, peta kata, dan isu positif-negatif menteri",
        1,
        [
            (4, "Overall Media & Social"),
            (5, "Platform Review - tujuh saluran"),
            (6, "Suara Teratas & Dua Awan Kata"),
            (7, "Isu Positif dan Negatif - Menteri PU")
        ]
    )
    render_mh_footer("Bab Pembuka Tinjauan Komprehensif")


# ==============================================================================
# SLIDE 5: PLATFORM REVIEW - TUJUH SALURAN
# ==============================================================================
def render_slide_5_platform_review(df=None, **kwargs):
    render_mh_top_bar(slide_num=5)
    render_mh_title(
        "Platform Review",
        "Instagram 69% perhatian; berita daring 53% volume",
        "Kiri: tujuh saluran lembaga (proyek 279) 26 Okt-1 Nov, urut keterlibatan. Kanan: emosi percakapan lembaga."
    )
    
    chips = [
        {"label": "Berita Daring", "val": "53%", "sub": "1.564; negatif 5%", "dot": "#64748B"},
        {"label": "Keterlibatan IG", "val": "771 rb", "sub": "69% dari total", "dot": "#2563EB", "val_color": "#2563EB"},
        {"label": "TikTok", "val": "272 rb", "sub": "24% keterlibatan", "dot": "#2563EB", "val_color": "#2563EB"},
        {"label": "Negatif X", "val": "30%", "sub": "turun dari 72%", "dot": "#EF4444", "val_color": "#EF4444"},
        {"label": "Marah", "val": "6%", "sub": "takut 5%", "dot": "#F59E0B", "val_color": "#F59E0B"}
    ]
    render_kpi_chips(chips)
    
    col_tbl, col_emo = st.columns([1.25, 0.75], gap="medium")
    
    with col_tbl:
        tbl_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Tujuh Saluran - Urut dari Keterlibatan
</div>
<table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:10px; font-weight:700; text-transform:uppercase;">
<th style="padding:6px 4px;">SALURAN</th>
<th style="padding:6px 4px;">PENYEBUTAN</th>
<th style="padding:6px 4px;">KETERLIBATAN ▼</th>
<th style="padding:6px 4px;">POSITIF</th>
<th style="padding:6px 4px;">CATATAN</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Instagram</td><td>650</td><td><strong>771 rb</strong></td><td style="color:#10B981; font-weight:600;">41%</td><td style="color:#64748B; font-size:10px;">29% negatif; Angke, Sekolah Rakyat</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">TikTok</td><td>84</td><td><strong>272 rb</strong></td><td style="color:#10B981; font-weight:600;">46%</td><td style="color:#64748B; font-size:10px;">Sekolah Rakyat, Tol Desari</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">YouTube</td><td>72</td><td>39,7 rb</td><td>22%</td><td style="color:#64748B; font-size:10px;">72% netral</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">X/Twitter</td><td>208</td><td>14,8 rb</td><td>34%</td><td style="color:#EF4444; font-size:10px;">30% negatif; senyap sejak 30 Okt</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Facebook</td><td>282</td><td>11,2 rb</td><td>38%</td><td style="color:#64748B; font-size:10px;">berbagi tautan; keluhan pasar</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Threads</td><td>75</td><td>8,0 rb</td><td style="color:#10B981; font-weight:600;">43%</td><td style="color:#64748B; font-size:10px;">13% negatif; satire mereda</td></tr>
<tr><td style="font-weight:600; padding:6px 4px;">Berita daring</td><td>1.564</td><td>4,6 rb</td><td>30%</td><td style="color:#64748B; font-size:10px;">686 media; negatif 5%</td></tr>
</tbody>
</table>
</div>"""
        render_html(tbl_html)

    with col_emo:
        render_html("""<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:6px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Suasana Emosi Percakapan (%)
</div>
</div>""")
        
        emos = ['Sedih', 'Terkejut', 'Takut', 'Marah', 'Percaya', 'Gembira', 'Menanti']
        vals = [2, 5, 5, 6, 13, 15, 54]
        
        fig_bar = go.Figure(go.Bar(
            x=vals, y=emos,
            orientation='h',
            marker=dict(color='#2563EB'),
            text=[f"{v}%" for v in vals],
            textposition='outside'
        ))
        fig_bar.update_layout(
            height=210,
            margin=dict(l=10, r=35, t=5, b=20),
            paper_bgcolor='#FFFFFF',
            plot_bgcolor='#FFFFFF',
            xaxis=dict(showgrid=True, gridcolor='#F1F5F9', range=[0, 65], tickfont=dict(size=9, color='#64748B')),
            yaxis=dict(tickfont=dict(size=10, color='#1E293B'))
        )
        st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})

    render_callout_target("Berita daring membawa volume (53%) dengan negatif 5%; Instagram membawa perhatian (69% keterlibatan) sekaligus 29% negatif. Negatif X turun dari 72% pekan lalu ke 30%.")
    render_mh_footer("Sumber: Proyek 279, 26 Okt-1 Nov (keterlibatan total 1.121.777; sentimen dan emosi per saluran). Emosi jijik 1% tidak ditampilkan.")


# ==============================================================================
# SLIDE 6: SUARA TERATAS & DUA AWAN KATA
# ==============================================================================
def render_slide_6_two_wordclouds(df=None, **kwargs):
    render_mh_top_bar(slide_num=6)
    render_mh_title(
        "Suara Teratas & Dua Awan Kata",
        "Kosakata bergeser ke air; negatif mengerucut ke Sumut",
        "Dua awan dari tabel 200 kata lembaga (279), 26 Okt-1 Nov. Kiri: frekuensi, warna = nada. Kanan: muatan negatif."
    )
    
    chips = [
        {"label": "Hijau Teratas", "val": "Sekolah", "sub": "Rakyat; 153; +69", "dot": "#10B981", "val_color": "#10B981"},
        {"label": "Merah Teratas", "val": "Proyek Jalan", "sub": "59; nada -53", "dot": "#EF4444", "val_color": "#EF4444"},
        {"label": "Kata Dianalisis", "val": "200 → 53", "sub": "setelah saringan", "dot": "#2563EB"},
        {"label": "Kata Negatif", "val": "10", "sub": "≥2 sebutan negatif", "dot": "#64748B"},
        {"label": "Dua Kata Teratas", "val": "69%", "sub": "dari sebutan negatif", "dot": "#2563EB"}
    ]
    render_kpi_chips(chips)
    
    c_cloud1, c_cloud2 = st.columns(2, gap="medium")
    
    with c_cloud1:
        cloud1_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:16px 18px; min-height:220px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:12px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Kata yang Paling Sering Muncul (53 kata)
</div>
<div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:10px 14px; text-align:center; padding:10px 0;">
<span style="font-size:26px; font-weight:800; color:#10B981;">Sekolah Rakyat</span>
<span style="font-size:24px; font-weight:800; color:#D97706;">Sumatera Utara</span>
<span style="font-size:18px; font-weight:700; color:#EF4444;">Proyek Jalan</span>
<span style="font-size:18px; font-weight:700; color:#059669;">Kali Angke</span>
<span style="font-size:16px; font-weight:700; color:#10B981;">Sumatera Barat</span>
<span style="font-size:14px; font-weight:600; color:#059669;">Air Bersih</span>
<span style="font-size:15px; font-weight:700; color:#D97706;">Bendung Polor</span>
<span style="font-size:13px; font-weight:600; color:#475569;">Tenaga Kerja</span>
<span style="font-size:13px; font-weight:600; color:#475569;">Tol Semarang-Demak</span>
<span style="font-size:12px; font-weight:600; color:#64748B;">Sumur Bor</span>
<span style="font-size:12px; font-weight:600; color:#EF4444;">Dugaan Korupsi</span>
<span style="font-size:11px; font-weight:500; color:#64748B;">Aceh Tenggara</span>
<span style="font-size:11px; font-weight:500; color:#64748B;">Bendungan Karian</span>
<span style="font-size:11px; font-weight:500; color:#64748B;">Commitment Fee</span>
</div>
</div>"""
        render_html(cloud1_html)

    with c_cloud2:
        cloud2_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:16px 18px; min-height:220px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:12px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Peta Muatan Negatif (10 kata)
</div>
<div style="display:flex; flex-direction:column; align-items:center; justify-content:center; gap:8px; text-align:center; padding:14px 0;">
<div style="font-size:12px; color:#94A3B8; font-weight:500;">Sulawesi Tenggara</div>
<div style="font-size:22px; font-weight:800; color:#EF4444;">Proyek Jalan</div>
<div style="font-size:30px; font-weight:900; color:#DC2626;">Sumatera Utara</div>
<div style="font-size:14px; font-weight:700; color:#EF4444;">Tenaga Ahli • Commitment Fee</div>
<div style="font-size:15px; font-weight:700; color:#B91C1C;">Aceh Tenggara</div>
<div style="font-size:11px; font-weight:600; color:#EF4444;">Dugaan Korupsi • Pembebasan Lahan</div>
</div>
</div>"""
        render_html(cloud2_html)

    # Note
    note_html = """<div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px; padding:10px 14px; margin-top:12px;">
<div style="font-size:11px; font-weight:700; color:#0F2942; margin-bottom:3px;">Saringan dan Cara Membaca</div>
<div style="font-size:10.5px; color:#64748B; line-height:1.4;">Dikeluarkan: nama lembaga dan unit, nama orang (tersangka, pejabat, menteri lain), partai, pemda, BUMN, media, topik kementerian lain. Varian ejaan digabung.</div>
</div>"""
    render_html(note_html)
    
    render_callout_target("Kosakata pekan ini milik sungai dan air - Kali Angke, Bendung Polor, sumur bor, air bersih; muatan negatif tetap mengerucut pada perkara jalan Sumatera Utara.")
    render_mh_footer("Sumber: Tabel term proyek 279, 200 kata teratas, 26 Okt-1 Nov. Nada = (positif - negatif) / sebutan.")


# ==============================================================================
# SLIDE 7: ISU POSITIF DAN NEGATIF - MENTERI PU
# ==============================================================================
def render_slide_7_issues_minister(df=None, **kwargs):
    render_mh_top_bar(slide_num=7)
    render_mh_title(
        "Isu Positif dan Negatif - Menteri PU",
        "Sekolah Rakyat mengangkat, survei kinerja menekan",
        "Berkas Isu Negatif-Positif Menteri PU (proyek 280), 22-28 Okt, ditambah data sepekan. Urut keterlibatan."
    )
    
    chips = [
        {"label": "Penyebutan", "val": "977", "sub": "berkas 22-28 Okt", "dot": "#10B981"},
        {"label": "Negatif X", "val": "58%", "sub": "62 penyebutan", "dot": "#EF4444", "val_color": "#EF4444"},
        {"label": "Berita Daring", "val": "84%", "sub": "positif; 264", "dot": "#2563EB", "val_color": "#2563EB"},
        {"label": "Negatif Pekan", "val": "19%", "sub": "178 dari 952", "dot": "#F59E0B"},
        {"label": "Positif Panel", "val": "39,4%", "sub": "netral 48,5%", "dot": "#10B981", "val_color": "#10B981"}
    ]
    render_kpi_chips(chips)
    
    col_pos, col_neg = st.columns(2, gap="medium")
    
    with col_pos:
        pos_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#10B981; display:inline-block;"></span>
Tema Positif
</div>
<table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:10px; font-weight:700; text-transform:uppercase;">
<th style="padding:6px 4px;">TEMA</th>
<th style="padding:6px 4px; text-align:right;">KETERLIBATAN ▼</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Sekolah Rakyat 'keterbatasan ekonomi' (IG, 28 Okt)</td><td style="text-align:right; font-weight:700; color:#10B981;">2.293</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Sekolah Rakyat hidupkan ekonomi (TikTok, 27 Okt)</td><td style="text-align:right; font-weight:700; color:#10B981;">1.837</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Jalan perbatasan Kalimantan 2.300 km (TikTok)</td><td style="text-align:right; font-weight:700;">1.560</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Tol Semarang-Demak 79,42% (Metro TV)</td><td style="text-align:right; font-weight:700;">723</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Uji pendaratan pesawat tempur di jalan tol</td><td style="text-align:right; font-weight:700;">353</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Preservasi jalan Aceh 80,77%</td><td style="text-align:right; font-weight:700;">212</td></tr>
<tr><td style="padding:6px 4px;">Jalan Lintas Utara Flores 472,48 km</td><td style="text-align:right; font-weight:700;">127</td></tr>
</tbody>
</table>
</div>"""
        render_html(pos_html)

    with col_neg:
        neg_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#EF4444; display:inline-block;"></span>
Tema Negatif
</div>
<table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:10px; font-weight:700; text-transform:uppercase;">
<th style="padding:6px 4px;">TEMA</th>
<th style="padding:6px 4px; text-align:right;">KETERLIBATAN ▼</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Survei IPO dalam video TikTok (25 Okt)</td><td style="text-align:right; font-weight:700; color:#EF4444;">1.881</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">'Raja' daftar menteri terburuk (IG, 26 Okt)</td><td style="text-align:right; font-weight:700; color:#EF4444;">1.864</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Rencana akses Tol Desari (TikTok, 27 Okt)</td><td style="text-align:right; font-weight:700;">837</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Judul '3 besar menteri terburuk' (Facebook)</td><td style="text-align:right; font-weight:700;">228</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Desakan reshuffle bersama survei (Facebook)</td><td style="text-align:right; font-weight:700;">145</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Komentar skeptis video Kali Angke (IG, 31 Okt)</td><td style="text-align:right; font-weight:700; color:#EF4444;">12 negatif</td></tr>
<tr><td colspan="2" style="padding:8px 4px; font-size:10px; color:#64748B; background:#FEF2F2; border-radius:4px; margin-top:4px;">Pekan 26 Okt-1 Nov: negatif menteri naik ke 19% (178 dari 952) dari 12%; Instagram 31% negatif, berita daring 2%.</td></tr>
</tbody>
</table>
</div>"""
        render_html(neg_html)

    render_callout_target("Sekolah Rakyat menjadi pengangkat terkuat menteri; penekan tetap survei kinerja, kini lewat kolom komentar Instagram, bukan pemberitaan.")
    render_mh_footer("Sumber: Berkas Analisis Isu Negatif dan Positif Menteri PU (280), 28 Okt, periode 22-28 Okt (977 sebutan; 350.906 keterlibatan).")


# ==============================================================================
# SLIDE 8: CHAPTER 02 - THE DEEP DIVE
# ==============================================================================
def render_slide_8_chapter_2(df=None, **kwargs):
    render_chapter_break(
        2,
        "The Deep Dive",
        "Empat berkas analisis - dua lembaga (279), dua menteri (280) - ditambah sorotan khusus pekan air, bencana, keserempakan, dan proyeksi intelijen",
        2,
        [
            (9, "Analisis Topik Utama - Kementerian PU"),
            (10, "Peta Pemangku Kepentingan - Menteri PU"),
            (11, "Sorotan Khusus: Pekan Air"),
            (12, "Analisis Framing - Kementerian PU"),
            (13, "Penanganan Bencana oleh Kementerian PU"),
            (14, "Keserempakan & Rekomendasi Intelijen (15)")
        ]
    )
    render_mh_footer("Bab Pendalaman Isu Strategis")


# ==============================================================================
# SLIDE 9: ANALISIS TOPIK UTAMA - KEMENTERIAN PU
# ==============================================================================
def render_slide_9_main_topics(df=None, **kwargs):
    render_mh_top_bar(slide_num=9)
    render_mh_title(
        "Analisis Topik Utama - Kementerian PU",
        "Perkara Sumut memimpin; kerja lapangan menyeimbangkan",
        "Berkas Topik Utama Kementerian PU (proyek 279), 22-28 Okt. Kiri: enam topik teratas. Kanan: bacaan dan pergerakan pekan ini."
    )
    
    chips = [
        {"label": "Penyebutan", "val": "3.010", "sub": "22-28 Okt", "dot": "#EF4444"},
        {"label": "Topik", "val": "10", "sub": "dari berkas", "dot": "#EF4444"},
        {"label": "Negatif", "val": "23%", "sub": "dari 3.010", "dot": "#F59E0B", "val_color": "#F59E0B"},
        {"label": "X Negatif", "val": "65%", "sub": "arena perkara", "dot": "#EF4444", "val_color": "#EF4444"},
        {"label": "TikTok Positif", "val": "77%", "sub": "label KPK positif", "dot": "#10B981", "val_color": "#10B981"}
    ]
    render_kpi_chips(chips)
    
    c_top, c_read = st.columns([1.15, 0.85], gap="medium")
    
    with c_top:
        topics_table = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Enam Topik Teratas - Urut Berkas
</div>
<table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:10px; font-weight:700;">
<th style="padding:6px 4px;">TOPIK ▼</th>
<th style="padding:6px 4px;">BUKTI</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">1. Korupsi BBPJN Sumut (KPK: 8 tersangka)</td><td style="color:#64748B; font-size:10.5px;">±156 sebutan; 'proyek jalan' 208; hampir semua negatif</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">2. Peran Gubernur Sumut, pergeseran Rp165 M</td><td style="color:#64748B; font-size:10.5px;">6.532 keterlibatan; bukan tersangka</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">3. Isu 'pesawat pribadi' dan perjalanan</td><td style="color:#EF4444; font-size:10.5px;">47 dari 48 sebutan negatif; seluruhnya X</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">4. Survei IPO 'menteri terburuk'</td><td style="color:#64748B; font-size:10.5px;">24 negatif dari 128 sebutan menteri</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">5. Jalan perbatasan Kalimantan 2.300 km</td><td style="color:#10B981; font-size:10.5px;">positif; TikTok 2.116 keterlibatan</td></tr>
<tr><td style="font-weight:600; padding:6px 4px;">6. Sekolah Rakyat, Tol Semarang-Demak, air</td><td style="color:#10B981; font-size:10.5px;">positif; 'sekolah rakyat' 96, tol 79,42%</td></tr>
</tbody>
</table>
</div>"""
        render_html(topics_table)

    with c_read:
        read_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Bacaan Berkas
</div>
<div style="background:#FEF2F2; border-left:3px solid #EF4444; padding:8px 10px; margin-bottom:10px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#991B1B;">Klaster hukum paling negatif</div>
<div style="font-size:10.5px; color:#7F1D1D; line-height:1.4;">BBPJN 101 negatif dari 119 sebutan; X memuat 49 dari 59 sebutan topik terbesar.</div>
</div>
<div style="background:#F0FDF4; border-left:3px solid #10B981; padding:8px 10px; margin-bottom:10px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#065F46;">Penyeimbang sudah tersedia</div>
<div style="font-size:10.5px; color:#064E3B; line-height:1.4;">Perbatasan, Sekolah Rakyat, pemulihan Sumatera berlabel positif, tetapi belum dipakai menjawab perkara.</div>
</div>
<div style="background:#EFF6FF; border-left:3px solid #2563EB; padding:8px 10px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#1E40AF;">Pekan ini: klaster hukum surut</div>
<div style="font-size:10.5px; color:#1E3A8A; line-height:1.4;">'Sumatera Utara' turun ke 198 sebutan (65 negatif) pada 26 Okt-1 Nov; X 1-2 sebutan per hari sejak 30 Okt.</div>
</div>
</div>"""
        render_html(read_html)

    render_callout_target("Berkas 22-28 Okt memotret puncak perkara; data pekan ini menunjukkan topik hukum surut dan kerja lapangan mengambil alih.")
    render_mh_footer("Sumber: Berkas Analisis Topik Utama Kementerian PU (279), 28 Okt, periode 22-28 Okt (3.010 sebutan; 1.949.916 keterlibatan).")


# ==============================================================================
# SLIDE 10: PETA PEMANGKU KEPENTINGAN - MENTERI PU
# ==============================================================================
def render_slide_10_stakeholder_mapping(df=None, **kwargs):
    render_mh_top_bar(slide_num=10)
    render_mh_title(
        "Peta Pemangku Kepentingan - Menteri PU",
        "Pihak berdaya tinggi perlu dikelola dari dekat",
        "Berkas Stakeholder Mapping (Power-Interest Grid) Menteri PU (proyek 280), 22-28 Okt. Kiri: kuadran. Kanan: risiko berbalik."
    )
    
    chips = [
        {"label": "Penyebutan", "val": "977", "sub": "22-28 Okt", "dot": "#EF4444"},
        {"label": "Berita Positif", "val": "84%", "sub": "dari 264 berita", "dot": "#10B981", "val_color": "#10B981"},
        {"label": "Negatif X", "val": "58%", "sub": "dari 62 sebutan", "dot": "#EF4444", "val_color": "#EF4444"},
        {"label": "Keluhan Nyata", "val": "2", "sub": "upah, ganti rugi", "dot": "#F59E0B"},
        {"label": "TikTok", "val": "189,6 rb", "sub": "keterlibatan, 31 unggahan", "dot": "#2563EB"}
    ]
    render_kpi_chips(chips)
    
    c_grid, c_risk = st.columns([1.1, 0.9], gap="medium")
    
    with c_grid:
        grid_table = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Kuadran Power-Interest - Urut Daya
</div>
<table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:10px; font-weight:700;">
<th style="padding:6px 4px;">KUADRAN ▼</th>
<th style="padding:6px 4px;">PIHAK DAN POSISI</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Kelola dekat: Presiden/Istana</td><td style="color:#64748B; font-size:10.5px;">30 positif, 0 negatif; desakan reshuffle di Facebook</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Kelola dekat: KPK</td><td style="color:#64748B; font-size:10.5px;">pengembangan perkara balai; status hukum ikut KPK</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Kelola dekat: lembaga survei, ASN PU</td><td style="color:#64748B; font-size:10.5px;">label 'terburuk'; isu pemecatan ASN bocor ke X</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Jaga puas: media nasional, BUMN karya</td><td style="color:#10B981; font-size:10.5px;">mendukung; Metro TV 44,2 rb tayang</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Beri informasi: warga terdampak</td><td style="color:#64748B; font-size:10.5px;">ganti rugi Demak, upah Sekolah Rakyat - <span style="color:#D97706; font-weight:700;">KLAIM</span></td></tr>
<tr><td style="font-weight:600; padding:6px 4px;">Pantau: Meta AI di Threads</td><td style="color:#64748B; font-size:10.5px;">'belum ada keterangan resmi' soal jet - <span style="color:#D97706; font-weight:700;">KLAIM</span></td></tr>
</tbody>
</table>
</div>"""
        render_html(grid_table)

    with c_risk:
        risk_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Risiko Berbalik
</div>
<div style="background:#FEF3C7; border-left:3px solid #F59E0B; padding:8px 10px; margin-bottom:10px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#92400E;">Istana</div>
<div style="font-size:10.5px; color:#78350F; line-height:1.4;">Akumulasi survei 'terburuk' dan desakan reshuffle dapat menggeser dukungan.</div>
</div>
<div style="background:#FEF2F2; border-left:3px solid #EF4444; padding:8px 10px; margin-bottom:10px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#991B1B;">Keluhan nyata</div>
<div style="font-size:10.5px; color:#7F1D1D; line-height:1.4;">Upah pekerja dan ganti rugi warga paling kredibel bila viral; keluhan upah identik muncul di 5 unggahan IG.</div>
</div>
<div style="background:#F1F5F9; border-left:3px solid #64748B; padding:8px 10px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#1E293B;">Kekosongan informasi</div>
<div style="font-size:10.5px; color:#334155; line-height:1.4;">Tanpa rilis terindeks, jawaban AI dan akun anonim mengisi isu perjalanan dinas.</div>
</div>
</div>"""
        render_html(risk_html)

    render_callout_target("Pihak penentu bukan pengkritik di X, tetapi Istana, KPK, dan warga dengan keluhan nyata - ketiganya dijawab dengan data, bukan bantahan.")
    render_mh_footer("Sumber: Berkas Stakeholder Mapping (Power-Interest Grid) Menteri PU (280), 28 Okt, periode 22-28 Okt (977 sebutan; 350.906 keterlibatan).")


# ==============================================================================
# SLIDE 11: SOROTAN KHUSUS: PEKAN INI AIR
# ==============================================================================
def render_slide_11_water_focus_timeline(df=None, **kwargs):
    render_mh_top_bar(slide_num=11)
    render_mh_title(
        "Sorotan Khusus: Pekan ini Air",
        "Dari perkara Sumut ke sungai, bendungan, banjir",
        "Sorotan khusus. Isu terbesar pekan ini menurut jangkauan: air - sungai, bendungan, banjir. Kronologi, lapis narasi, status."
    )
    
    chips = [
        {"label": "Kali Angke", "val": "200 rb", "sub": "tayangan, 31 Okt", "dot": "#EF4444"},
        {"label": "Karian", "val": "121 rb", "sub": "tayangan, 29 Okt", "dot": "#EF4444"},
        {"label": "Jembatan Tali", "val": "784 rb", "sub": "tayangan, tanpa jawaban", "dot": "#F59E0B"},
        {"label": "Negatif Menteri", "val": "27%", "sub": "puncak 29 Okt", "dot": "#2563EB"},
        {"label": "Platform", "val": "6", "sub": "'kali angke', 31 Okt", "dot": "#EF4444"}
    ]
    render_kpi_chips(chips)
    
    timeline_table = f"""<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Kronologi dan Lapis Narasi
</div>
<table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:10px; font-weight:700;">
<th style="padding:6px 4px; width:75px;">TANGGAL ▼</th>
<th style="padding:6px 4px;">PERISTIWA</th>
<th style="padding:6px 4px; width:95px;">LAPIS</th>
<th style="padding:6px 4px; width:100px;">STATUS</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:700; padding:6px 4px;">26 Okt</td><td>Negatif lembaga 99 (18%) - gema agenda KPK perkara jalan Sumut</td><td style="color:#D97706; font-weight:600;">HUKUM</td><td>{render_status_badge("MEREDA", "slate")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:700; padding:6px 4px;">29 Okt</td><td>IG Kompas.com: kampung tenggelam Bendungan Karian muncul saat surut; 121 rb tayang</td><td style="color:#D97706; font-weight:600;">BENDUNGAN</td><td>{render_status_badge("PANTAU", "amber")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:700; padding:6px 4px;">29 Okt</td><td>Kunjungan Maluku Utara, sumur bor Tidore; negatif menteri puncak 41 (27%)</td><td style="color:#D97706; font-weight:600;">MENTERI</td><td>{render_status_badge("PANTAU", "amber")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:700; padding:6px 4px;">30 Okt</td><td>Banjir bandang Cikalintu-Cipaganti, Bandung; tanggul jebol, 35 rumah terdampak</td><td style="color:#D97706; font-weight:600;">SUNGAI</td><td>{render_status_badge("BERJALAN", "green")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:700; padding:6px 4px;">31 Okt</td><td>Susur Sungai Angke bersama Gubernur Banten: 199.697 tayang, 'kali angke' di 6 platform</td><td style="color:#D97706; font-weight:600;">SUNGAI</td><td>{render_status_badge("BERLANJUT", "green")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:700; padding:6px 4px;">31 Okt</td><td>Komentar 'omon-omon', 'wisata air' di video Angke; 12 negatif</td><td style="color:#D97706; font-weight:600;">MENTERI</td><td>{render_status_badge("KLAIM", "amber")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:700; padding:6px 4px;">31 Okt</td><td>Video jembatan tali Gayo Lues 784 rb tayang; nama PU belum disebut</td><td style="color:#D97706; font-weight:600;">JEMBATAN</td><td>{render_status_badge("KURANG", "red")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:700; padding:6px 4px;">1 Nov</td><td>Banjir Pidie Jaya, Nagan Raya, Aceh Barat; PU tangani Cikalintu</td><td style="color:#D97706; font-weight:600;">SUNGAI</td><td>{render_status_badge("BARU", "blue")}</td></tr>
<tr><td style="font-weight:700; padding:6px 4px;">2 Nov</td><td>Geobag Cipaganti; Bupati Gayo Lues lapor banjir ke Menteri; irigasi Rp2,99 T</td><td style="color:#D97706; font-weight:600;">SUNGAI</td><td>{render_status_badge("BERJALAN", "green")}</td></tr>
</tbody>
</table>
</div>"""
    render_html(timeline_table)
    
    render_callout_target("Air memberi panggung terbesar pekan ini dan menunggu bukti kerja berikutnya; titik paling rawan adalah Aceh - viral menjelang setahun bencana, belum ada rilis balai.")
    render_mh_footer("Sumber: IG info Tangerang 31 Okt (199.697 tayang) dan Kompas.com 29 Okt (121.096); TikTok Inilah 31 Okt; Koran Jakarta, Majalah Lintas.")


# ==============================================================================
# SLIDE 12: ANALISIS FRAMING - KEMENTERIAN PU
# ==============================================================================
def render_slide_12_framing_analysis(df=None, **kwargs):
    render_mh_top_bar(slide_num=12)
    render_mh_title(
        "Analisis Framing - Kementerian PU",
        "Korupsi unggul emosi; pembangunan unggul volume",
        "Berkas Framing Entman & Edelman Kementerian PU (proyek 279), 22-28 Okt. Kiri: lima bingkai. Kanan: bingkai lawan dan tandingan."
    )
    
    chips = [
        {"label": "Penyebutan", "val": "3.010", "sub": "22-28 Okt", "dot": "#EF4444"},
        {"label": "Berita Positif", "val": "68%", "sub": "1.376 berita", "dot": "#10B981", "val_color": "#10B981"},
        {"label": "X Negatif", "val": "65%", "sub": "370 sebutan", "dot": "#EF4444", "val_color": "#EF4444"},
        {"label": "YouTube", "val": "54%", "sub": "negatif; 96 sebutan", "dot": "#F59E0B"},
        {"label": "TikTok", "val": "963,8 rb", "sub": "keterlibatan", "dot": "#2563EB"}
    ]
    render_kpi_chips(chips)
    
    c_f1, c_f2 = st.columns([0.9, 1.1], gap="medium")
    
    with c_f1:
        f1_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Lima Bingkai - Indikator Kata Kunci
</div>
<table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:10px; font-weight:700;">
<th style="padding:6px 4px;">BINGKAI</th>
<th style="padding:6px 4px; text-align:right;">SEBUTAN ▼</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">F1 Korupsi jalan Sumut - 'sumatera utara', negatif</td><td style="text-align:right; font-weight:700; color:#EF4444;">458</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">F2 Infrastruktur hadir - dua tagar resmi, positif</td><td style="text-align:right; font-weight:700; color:#10B981;">209</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">F4 Etika pejabat - 'pesawat pribadi', negatif</td><td style="text-align:right; font-weight:700; color:#EF4444;">48</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">F3 Negara memulihkan - satgas, banjir bandang</td><td style="text-align:right; font-weight:700;">47</td></tr>
<tr><td style="padding:6px 4px;">F5 Insiden layanan - Jembatan Ciloa, bus dinas</td><td style="text-align:right; font-weight:700;">280 rb tayang</td></tr>
</tbody>
</table>
</div>"""
        render_html(f1_html)

    with c_f2:
        f2_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Bingkai Lawan dan Narasi Tandingan
</div>
<table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:10px; font-weight:700;">
<th style="padding:6px 4px;">BINGKAI LAWAN</th>
<th style="padding:6px 4px;">NARASI TANDINGAN</th>
<th style="padding:6px 4px;">KANAL</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="color:#EF4444; font-weight:600; padding:6px 4px;">'Kementerian sarang korupsi'</td><td style="color:#1E293B;">Membersihkan diri: rotasi, audit, kanal vendor</td><td style="color:#64748B; font-size:10px;">Rilis, X</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="color:#EF4444; font-weight:600; padding:6px 4px;">'Aliran suap ke pusat' - KLAIM</td><td style="color:#1E293B;">Respons faktual, tanpa spekulasi</td><td style="color:#64748B; font-size:10px;">Berita</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="color:#EF4444; font-weight:600; padding:6px 4px;">'Elite naik jet, pegawai dipersulit'</td><td style="color:#1E293B;">Data moda dan biaya perjalanan</td><td style="color:#64748B; font-size:10px;">X, Threads</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="color:#EF4444; font-weight:600; padding:6px 4px;">'Menteri terburuk'</td><td style="color:#1E293B;">Metrik capaian, bukan bantahan</td><td style="color:#64748B; font-size:10px;">FB, IG</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="color:#64748B; padding:6px 4px;">Angka tanpa wajah</td><td style="color:#10B981; font-weight:600;">Wajah warga: Krayan, Lombok Barat</td><td style="color:#64748B; font-size:10px;">TikTok, Reels</td></tr>
<tr><td style="color:#64748B; padding:6px 4px;">Tagar hanya beredar internal</td><td style="color:#10B981; font-weight:600;">Tagar ramah publik, suara pihak ketiga</td><td style="color:#64748B; font-size:10px;">IG, TikTok</td></tr>
</tbody>
</table>
</div>"""
        render_html(f2_html)

    render_callout_target("Pesan tandingan dari berkas: 'Bersih dari dalam, membangun sampai ke tapal batas' - integritas dan pembangunan disajikan sebagai satu komitmen.")
    render_mh_footer("Sumber: Berkas Analisis Framing Media (Entman & Edelman) Kementerian PU (279), 28 Okt, periode 22-28 Okt (3.010 sebutan; 1.949.916 keterlibatan).")


# ==============================================================================
# SLIDE 13: PENANGANAN BENCANA OLEH KEMENTERIAN PU
# ==============================================================================
def render_slide_13_disaster_response(df=None, **kwargs):
    render_mh_top_bar(slide_num=13)
    render_mh_title(
        "Penanganan Bencana oleh Kementerian PU",
        "Hadir di NTT, Bandung, Kalbar; banjir Aceh belum",
        "Hanya kegiatan kementerian dan unitnya. Penanganan pemda, BPBD, TNI dicatat sebagai konteks."
    )
    
    chips = [
        {"label": "Gempa NTT", "val": "650", "sub": "aset pulih, 8 kab.", "dot": "#2563EB"},
        {"label": "Kegiatan Baru", "val": "5", "sub": "26 Okt-2 Nov", "dot": "#10B981", "val_color": "#10B981"},
        {"label": "Banjir Aceh", "val": "4", "sub": "kabupaten, tanpa balai", "dot": "#F59E0B"},
        {"label": "Krisis Air", "val": "42", "sub": "berita, 31 Okt-1 Nov", "dot": "#EF4444"},
        {"label": "Banjir-Gempa", "val": "53", "sub": "berita, 1-2 Nov", "dot": "#EF4444"}
    ]
    render_kpi_chips(chips)
    
    c_d1, c_d2 = st.columns([1.1, 0.9], gap="medium")
    
    with c_d1:
        d1_html = f"""<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Kegiatan Kementerian PU - Gempa, Banjir, Karhutla, Kekeringan
</div>
<div style="display:flex; flex-direction:column; gap:8px; font-size:11px;">
<div><strong>Gempa NTT:</strong> 650 infrastruktur pulih di 8 kabupaten; 59 rusak ringan ditangani, termasuk RSUD Aeramo (29 Okt) - {render_status_badge("BERJALAN", "green")}</div>
<div><strong>Banjir bandang Cikalintu-Cipaganti, Bandung (30 Okt):</strong> PU turun tangan; geobag dipasang cegah banjir susulan (1-2 Nov) - {render_status_badge("BERJALAN", "green")}</div>
<div><strong>Karhutla:</strong> sumur bor dangkal BWS Kalimantan I di Kubu Raya (30 Okt); saluran Riam Kanan 11,25 km (28 Okt) - {render_status_badge("BERJALAN", "green")}</div>
<div><strong>Kekeringan:</strong> sumur bor Tidore Kepulauan saat kunjungan Malut (29 Okt) - {render_status_badge("BERJALAN", "green")}; Jawa belum ada kegiatan baru - {render_status_badge("KURANG", "red")}</div>
<div><strong>Banjir Aceh-Sumbar 1 Nov (Pidie Jaya 17 desa, Nagan Raya 15 desa, Agam):</strong> belum ada kegiatan balai di berita - {render_status_badge("KURANG", "red")}</div>
</div>
</div>"""
        render_html(d1_html)

    with c_d2:
        d2_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Konteks Penanganan Pihak Lain (31 Okt-2 Nov)
</div>
<div style="font-size:11px; color:#475569; line-height:1.5; margin-bottom:10px;">
• Sumedang: sumur bor oleh Wakil Ketua DPR<br>
• Pati: TNI AL salurkan air bersih<br>
• Sampit: swasta 12.000 liter per hari<br>
• Atambua (NTT): ratusan KK krisis air<br>
• Anak Krakatau: abu ke Cilegon, warga diberi masker
</div>
<div style="background:#EFF6FF; border-left:3px solid #2563EB; padding:8px 10px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#1E40AF;">Insight</div>
<div style="font-size:10px; color:#1E3A8A; line-height:1.4;">Musim hujan sudah tiba di Sumatra dan Jawa Barat, sementara NTT, Maluku, dan Jawa Timur masih kering. Ruang krisis air Jawa diisi DPR, TNI, dan swasta; banjir Aceh baru sampai ke Menteri lewat laporan bupati (2 Nov).</div>
</div>
</div>"""
        render_html(d2_html)

    render_callout_target("Jarak terlebar pekan ini: banjir Aceh 1 Nov dan krisis air Jawa - keduanya belum memiliki rilis balai.")
    render_mh_footer("Sumber: Antara 29 Okt (gempa NTT); Koran Jakarta 1 Nov; Liputan7 30 Okt; Koran Jakarta 29 Okt; Kompas.com 1 Nov.")


# ==============================================================================
# SLIDE 14: KESEREMPAKAN & UJI ORGANIK
# ==============================================================================
def render_slide_14_bot_organic_audit(df=None, **kwargs):
    render_mh_top_bar(slide_num=14)
    render_mh_title(
        "Keserempakan & Uji Organik",
        "Tak ada serangan terkoordinasi; tagar internal serempak",
        "Penjelajah penyebutan, lintas platform, 26 Okt-1 Nov. Pengukuran untuk periksa ke dalam, bukan tindakan terhadap akun."
    )
    
    chips = [
        {"label": "Pola Diuji", "val": "6", "sub": "sepekan", "dot": "#EF4444"},
        {"label": "Terkoordinasi", "val": "1", "sub": "tagar internal", "dot": "#10B981"},
        {"label": "Serangan", "val": "0", "sub": "pola terkoordinasi", "dot": "#F59E0B"},
        {"label": "Kali Angke", "val": "6", "sub": "platform, 31 Okt", "dot": "#2563EB"},
        {"label": "Portal Teratas", "val": "2,4%", "sub": "37 dari 1.564 berita", "dot": "#2563EB"}
    ]
    render_kpi_chips(chips)
    
    patterns_table = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Pola Serempak - Urut dari Risiko
</div>
<table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:10px; font-weight:700;">
<th style="padding:6px 4px; width:75px;">ARAH</th>
<th style="padding:6px 4px;">POLA</th>
<th style="padding:6px 4px;">UKURAN</th>
<th style="padding:6px 4px;">PENILAIAN ▼</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="color:#EF4444; font-weight:700; padding:6px 4px;">KRITIK</td><td style="font-weight:600;">Ulang-cuit 'penetapan 8 tersangka'</td><td style="color:#64748B;">32 akun 26-28 Okt, 28 negatif, 0 keterlibatan</td><td>Agenda hukum; berhenti 29 Okt</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="color:#EF4444; font-weight:700; padding:6px 4px;">KRITIK</td><td style="font-weight:600;">Komentar keluhan upah identik</td><td style="color:#64748B;">1 teks di 5 unggahan IG (27-28 Okt)</td><td style="color:#D97706; font-weight:600;">Perlu cek lapangan</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="color:#10B981; font-weight:700; padding:6px 4px;">DUKUNG</td><td style="font-weight:600;">Tagar #PU608 dan #SigapMembangun</td><td style="color:#64748B;">169 unggahan, 93 akun, 32 teks kembar; puncak 12-15 WIB</td><td style="color:#EF4444; font-weight:600;">Terkoordinasi internal; rawan dibaca pendengung</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="color:#EF4444; font-weight:700; padding:6px 4px;">KRITIK</td><td style="font-weight:600;">Survei kinerja menteri</td><td style="color:#64748B;">daur 25-26 dan 31 Okt; FB, IG, Threads</td><td>Narasi turunan; organik</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="color:#64748B; font-weight:700; padding:6px 4px;">NETRAL</td><td style="font-weight:600;">Liputan Kali Angke</td><td style="color:#64748B;">6 platform pada 31 Okt; 102 unggahan, 68 akun</td><td style="color:#10B981; font-weight:600;">Organik, dipicu kunjungan</td></tr>
<tr><td style="color:#10B981; font-weight:700; padding:6px 4px;">DUKUNG</td><td style="font-weight:600;">Rilis Sekolah Rakyat dan P3TGAI</td><td style="color:#64748B;">5-6 platform per hari (26-28 Okt)</td><td>Sindikasi rilis; wajar</td></tr>
</tbody>
</table>
</div>"""
    render_html(patterns_table)
    
    render_callout_target("Satu-satunya pola terkoordinasi justru dari pihak sendiri: tagar internal serempak di jam kerja - perlu dipadukan dengan suara warga agar tidak dibaca sebagai pendengung.")
    render_mh_footer("Sumber: Penjelajah penyebutan (pencarian tagar, teks kembar, jam WIB), lintas platform, news-insight (1.564 berita, 686 media).")


# ==============================================================================
# SLIDE 15: REKOMENDASI INTELIJEN - PROYEKSI 7 HARI
# ==============================================================================
def render_slide_15_intelligence_projections(df=None, **kwargs):
    render_mh_top_bar(slide_num=15)
    render_mh_title(
        "Rekomendasi Intelijen - Proyeksi 7 Hari",
        "Ujian bergeser dari perkara ke banjir dan survei",
        "Sintesis pemantauan 279/280, empat berkas 28 Okt, Pemantau Delta, dan media. Skenario 7 hari dan tanda bahaya."
    )
    
    chips = [
        {"label": "Paling Mungkin", "val": "Banjir", "sub": "dan air; isu bergeser", "dot": "#10B981"},
        {"label": "Paling Berbahaya", "val": "Konvergensi", "sub": "banjir, survei, sidang", "dot": "#EF4444", "val_color": "#EF4444"},
        {"label": "Tidak Mungkin", "val": "Serangan", "sub": "terorganisir", "dot": "#64748B"},
        {"label": "Negatif Harian", "val": "10-15%", "sub": "proyeksi lembaga", "dot": "#EF4444"},
        {"label": "Review", "val": "9 Nov", "sub": "evaluasi mingguan", "dot": "#2563EB"}
    ]
    render_kpi_chips(chips)
    
    c_scen, c_warn = st.columns([0.9, 1.1], gap="medium")
    
    with c_scen:
        scen_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Tiga Skenario
</div>
<div style="background:#F0FDF4; border-left:3px solid #10B981; padding:8px 10px; margin-bottom:8px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#065F46;">Paling mungkin: panggung pindah ke air</div>
<div style="font-size:10px; color:#064E3B; line-height:1.4;">Negatif lembaga 10-15% per hari; banjir awal musim dan krisis air timur menentukan nada; perkara Sumut muncul hanya saat sidang.</div>
</div>
<div style="background:#FEF2F2; border-left:3px solid #EF4444; padding:8px 10px; margin-bottom:8px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#991B1B;">Paling berbahaya: konvergensi</div>
<div style="font-size:10px; color:#7F1D1D; line-height:1.4;">Banjir besar di lokasi kunjungan atau di Aceh tanpa balai hadir, bersamaan dengan survei kinerja dan fakta sidang menyebut pejabat pusat.</div>
</div>
<div style="background:#F1F5F9; border-left:3px solid #64748B; padding:8px 10px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#1E293B;">Tidak mungkin: serangan terorganisir</div>
<div style="font-size:10px; color:#334155; line-height:1.4;">Kaskade X berhenti sejak 29 Okt; serempak terbesar adalah liputan organik dan tagar internal.</div>
</div>
</div>"""
        render_html(scen_html)

    with c_warn:
        warn_table = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Tanda Bahaya dan Respons
</div>
<table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:10px; font-weight:700;">
<th style="padding:5px 4px;">TANDA</th>
<th style="padding:5px 4px;">AMBANG ▼</th>
<th style="padding:5px 4px;">RESPONS</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:5px 4px;">Banjir di lokasi kunjungan menteri</td><td style="color:#EF4444; font-weight:700;">1 kejadian</td><td>Jadwal kerja, foto progres</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:5px 4px;">Banjir Aceh-Sumbar tanpa rilis balai</td><td style="color:#EF4444; font-weight:700;">24 jam</td><td>Rilis BWS Sumatera I, V</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:5px 4px;">Negatif menteri harian</td><td style="color:#D97706; font-weight:700;">>25%, 2 hari</td><td>Balasan faktual di IG</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:5px 4px;">Pejabat pusat disebut di sidang</td><td style="color:#EF4444; font-weight:700;">1 kali</td><td>Pernyataan resmi</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:5px 4px;">Survei 'terburuk' dikutip ulang</td><td style="font-weight:700;">≥3 media</td><td>Lembar capaian</td></tr>
<tr><td style="padding:5px 4px;">Video infrastruktur rusak viral</td><td style="font-weight:700;">>100 rb tayang</td><td>Peta kewenangan, jadwal</td></tr>
</tbody>
</table>
</div>"""
        render_html(warn_table)

    render_callout_target("Dua tanda terdekat: hujan di Kali Angke dan Cipaganti, serta banjir Aceh tanpa rilis balai - keduanya dapat dijawab dengan jadwal kerja yang sudah ada.")
    render_mh_footer("Sumber: Analisis 26 Okt-1 Nov; berkas Topik, Framing (279), Isu Pos-Neg, Stakeholder (280) 28 Okt; Pemantau Delta 69, 94.")


# ==============================================================================
# SLIDE 16: CHAPTER 03 - THE ACTION
# ==============================================================================
def render_slide_16_chapter_3(df=None, **kwargs):
    render_chapter_break(
        3,
        "The Action",
        "Dua laporan harian, daftar pantau dengan unit penanggung jawab, prioritas tindakan, dan catatan metodologi",
        3,
        [
            (17, "Laporan Harian 1 November"),
            (18, "Laporan Harian 2 November"),
            (19, "Daftar Pantau Sepekan"),
            (20, "Prioritas Tindakan & Metodologi")
        ]
    )
    render_mh_footer("Bab Implementasi & Rencana Aksi")


# ==============================================================================
# SLIDE 17: LAPORAN HARIAN 1 NOVEMBER
# ==============================================================================
def render_slide_17_daily_nov1(df=None, **kwargs):
    render_mh_top_bar(slide_num=17)
    render_mh_title(
        "Laporan Harian 1 November",
        "Minggu sepi; banjir Aceh dan keluhan pasar mengemuka",
        "1 November (Minggu), hari penuh terakhir. Kiri: apa yang tercatat. Kanan: temuan."
    )
    
    chips = [
        {"label": "Lembaga", "val": "168", "sub": "negatif 6%", "dot": "#2563EB"},
        {"label": "Menteri", "val": "69", "sub": "negatif 12%", "dot": "#EF4444"},
        {"label": "Banjir-Gempa", "val": "53", "sub": "berita, 1-2 Nov", "dot": "#EF4444"},
        {"label": "Unggahan Teratas", "val": "351", "sub": "keterlibatan, keluhan pasar", "dot": "#F59E0B"},
        {"label": "Kegiatan Baru", "val": "2", "sub": "Cikalintu, edukasi", "dot": "#10B981"}
    ]
    render_kpi_chips(chips)
    
    c_p1, c_l1 = st.columns([1.1, 0.9], gap="medium")
    
    with c_p1:
        p1_table = f"""<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Peristiwa 1 November
</div>
<table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:10px; font-weight:700;">
<th style="padding:6px 4px;">ISI</th>
<th style="padding:6px 4px; width:90px;">STATUS</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Keluhan pedagang Pasar Ngawen, Blora: pasar baru dibangun tak sesuai harapan (FB, 351)</td><td>{render_status_badge("KLAIM", "amber")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Kementerian PU tangani banjir bandang Cikalintu, Bandung</td><td>{render_status_badge("POSITIF", "green")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Banjir Pidie Jaya 17 desa, Nagan Raya 15 desa, Aceh Barat 3 kecamatan</td><td>{render_status_badge("BARU", "blue")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Edukasi 'Bendungan, Bendung, Sumur Bor' (IG resmi, 5,3 rb tayang)</td><td>{render_status_badge("POSITIF", "green")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="padding:6px 4px;">Mudik gratis Nataru dan perluasan akses transportasi (topik teratas)</td><td>{render_status_badge("KONTEKS", "slate")}</td></tr>
<tr><td style="padding:6px 4px;">Krisis air Sumedang, Pati, Sampit diisi DPR, TNI, swasta</td><td>{render_status_badge("KURANG", "red")}</td></tr>
</tbody>
</table>
</div>"""
        render_html(p1_table)

    with c_l1:
        l1_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Pelajaran dari 1 November
</div>
<div style="background:#FEF2F2; border-left:3px solid #EF4444; padding:8px 10px; margin-bottom:8px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#991B1B;">Mutu bangunan jadi bahan kritik</div>
<div style="font-size:10px; color:#7F1D1D; line-height:1.4;">Keluhan pasar Blora menjadi unggahan teratas; pemilik proyek perlu dicek sebelum dikaitkan ke PU.</div>
</div>
<div style="background:#FEF3C7; border-left:3px solid #F59E0B; padding:8px 10px; margin-bottom:8px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#92400E;">Banjir datang lebih cepat dari rilis</div>
<div style="font-size:10px; color:#78350F; line-height:1.4;">53 berita banjir-gempa dalam sehari; kegiatan balai baru tercatat di Bandung.</div>
</div>
<div style="background:#F0FDF4; border-left:3px solid #10B981; padding:8px 10px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#065F46;">Edukasi bekerja di hari sepi</div>
<div style="font-size:10px; color:#064E3B; line-height:1.4;">Unggahan penjelasan bendungan dan sumur bor menjadi teratas di dua proyek.</div>
</div>
</div>"""
        render_html(l1_html)

    render_callout_target("Hari libur tanpa agenda menteri; nada ditentukan keluhan mutu bangunan dan banjir awal musim di Sumatra.")
    render_mh_footer("Sumber: Proyek 279 dan 280, 1 Nov; Pemantau Delta 69 dan 94; Kompas.com, CNN Indonesia, RRI.")


# ==============================================================================
# SLIDE 18: LAPORAN HARIAN 2 NOVEMBER
# ==============================================================================
def render_slide_18_daily_nov2(df=None, **kwargs):
    render_mh_top_bar(slide_num=18)
    render_mh_title(
        "Laporan Harian 2 November",
        "Senin pagi: irigasi Rp2,99 T dan geobag Cipaganti",
        "2 November, tarikan pagi (s.d. 09.15 WIB). Belum dipakai untuk menyimpulkan arah hari ini."
    )
    
    chips = [
        {"label": "Lembaga", "val": "20", "sub": "pagi; 0 negatif", "dot": "#2563EB"},
        {"label": "Menteri", "val": "9", "sub": "pagi; 0 negatif", "dot": "#EF4444"},
        {"label": "Laporan Banjir", "val": "1", "sub": "Gayo Lues ke Menteri", "dot": "#EF4444"},
        {"label": "Irigasi", "val": "Rp2,99 T", "sub": "P3TGAI 2027", "dot": "#10B981", "val_color": "#10B981"},
        {"label": "Lokasi", "val": "13.296", "sub": "sasaran irigasi", "dot": "#2563EB"}
    ]
    render_kpi_chips(chips)
    
    c_p2, c_f2 = st.columns([1.1, 0.9], gap="medium")
    
    with c_p2:
        p2_table = f"""<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Kabar Pagi 2 November
</div>
<table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:10px; font-weight:700;">
<th style="padding:6px 4px; width:55px;">JAM ▼</th>
<th style="padding:6px 4px;">ISI</th>
<th style="padding:6px 4px; width:75px;">ARAH</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:700; padding:6px 4px;">08.18</td><td>Rp2,99 T irigasi 2027 (P3TGAI) sasar 13.296 lokasi; usulan dibuka</td><td>{render_status_badge("POSITIF", "green")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:700; padding:6px 4px;">06.45</td><td>Bupati Gayo Lues laporkan banjir Desa Badak kepada Menteri PU</td><td>{render_status_badge("PANTAU", "amber")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:700; padding:6px 4px;">06.40</td><td>PU pasang geobag di Cipaganti, Bandung, cegah banjir susulan</td><td>{render_status_badge("POSITIF", "green")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:700; padding:6px 4px;">06.00</td><td>Kementerian PU cetak 41.824 tenaga kerja konstruksi; pemanfaatan BIM dan AI</td><td>{render_status_badge("POSITIF", "green")}</td></tr>
<tr><td style="font-weight:700; padding:6px 4px;">05.19</td><td>Unggahan FB kunjungan Menteri di Maluku Utara (63 keterlibatan)</td><td>{render_status_badge("KONTEKS", "slate")}</td></tr>
</tbody>
</table>
</div>"""
        render_html(p2_table)

    with c_f2:
        f2_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Perlu Diikuti Hari Ini
</div>
<div style="background:#FEF3C7; border-left:3px solid #F59E0B; padding:8px 10px; margin-bottom:8px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#92400E;">Banjir Gayo Lues</div>
<div style="font-size:10px; color:#78350F; line-height:1.4;">Laporan bupati ke Menteri perlu dijawab balai dengan kegiatan di lapangan.</div>
</div>
<div style="background:#F0FDF4; border-left:3px solid #10B981; padding:8px 10px; margin-bottom:8px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#065F46;">Irigasi Rp2,99 T</div>
<div style="font-size:10px; color:#064E3B; line-height:1.4;">Rilis besar pertama pekan ini; siapkan peta lokasi agar tidak dibaca janji.</div>
</div>
<div style="background:#EFF6FF; border-left:3px solid #2563EB; padding:8px 10px; border-radius:3px;">
<div style="font-weight:700; font-size:11px; color:#1E40AF;">Hujan di Bandung dan Tangerang</div>
<div style="font-size:10px; color:#1E3A8A; line-height:1.4;">Geobag Cipaganti dan normalisasi Angke diuji hujan pekan ini.</div>
</div>
</div>"""
        render_html(f2_html)

    render_callout_target("Pagi tenang dengan kabar baik - irigasi dan geobag; tugas hari ini menautkan kabar itu ke wilayah yang sedang banjir.")
    render_mh_footer("Sumber: Proyek 279/280, 2 Nov s.d. 09.15 WIB (20 dan 9 sebutan); FajarAsia, Posmo, Majalah Lintas.")


# ==============================================================================
# SLIDE 19: DAFTAR PANTAU SEPEKAN
# ==============================================================================
def render_slide_19_watch_list(df=None, **kwargs):
    render_mh_top_bar(slide_num=19)
    render_mh_title(
        "Daftar Pantau Sepekan",
        "Sembilan butir: tiga baru, dua mereda",
        "Butir yang perlu diikuti unit, urut dari prioritas. Klaim dicatat sebagai klaim."
    )
    
    chips = [
        {"label": "Butir", "val": "9", "sub": "diikuti", "dot": "#2563EB"},
        {"label": "Baru", "val": "3", "sub": "sejak 31 Okt", "dot": "#EF4444"},
        {"label": "Klaim", "val": "1", "sub": "perlu cek", "dot": "#F59E0B"},
        {"label": "Kurang", "val": "2", "sub": "belum ada rilis", "dot": "#EF4444"},
        {"label": "Mereda", "val": "2", "sub": "perkara, jet", "dot": "#10B981"}
    ]
    render_kpi_chips(chips)
    
    watch_table = f"""<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Butir Pantau - Urut dari Prioritas
</div>
<table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:10px; font-weight:700;">
<th style="padding:6px 4px;">BUTIR</th>
<th style="padding:6px 4px;">UNIT</th>
<th style="padding:6px 4px; width:110px;">STATUS ▼</th>
<th style="padding:6px 4px;">LANGKAH</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Banjir Aceh-Sumbar (Gayo Lues, Pidie Jaya, Agam)</td><td style="color:#64748B;">SDA (BWS Sumatera)</td><td>{render_status_badge("BARU - TINGGI", "red")}</td><td style="color:#1E293B;">Rilis kegiatan 24 jam</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Kali Angke dan Cipaganti diuji hujan</td><td style="color:#64748B;">BBWS C2, Citarum</td><td>{render_status_badge("BARU", "blue")}</td><td style="color:#1E293B;">Jadwal kerja terbuka</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Irigasi Rp2,99 T, 13.296 lokasi</td><td style="color:#64748B;">SDA + Humas</td><td>{render_status_badge("BARU", "blue")}</td><td style="color:#1E293B;">Peta lokasi</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Survei kinerja menteri (IPO, IndocPolls)</td><td style="color:#64748B;">Pimpinan + Humas</td><td>{render_status_badge("BERLANJUT", "amber")}</td><td style="color:#1E293B;">Lembar capaian</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Krisis air Jawa, NTT, Maluku</td><td style="color:#64748B;">SDA + Cipta Karya</td><td>{render_status_badge("KURANG", "red")}</td><td style="color:#1E293B;">Rilis sumur bor</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Jembatan viral pascabencana Aceh</td><td style="color:#64748B;">Bina Marga</td><td>{render_status_badge("KURANG", "red")}</td><td style="color:#1E293B;">Peta kewenangan</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Keluhan Pasar Ngawen, Blora; upah pekerja</td><td style="color:#64748B;">Cipta Karya + Setjen</td><td>{render_status_badge("KLAIM", "amber")}</td><td style="color:#1E293B;">Cek pemilik proyek</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Perkara BBPJN Sumut; sidang Tipikor</td><td style="color:#64748B;">Pimpinan + Itjen</td><td>{render_status_badge("MEREDA", "slate")}</td><td style="color:#1E293B;">Pantau jadwal</td></tr>
<tr><td style="font-weight:600; padding:6px 4px;">Isu 'pesawat pribadi'</td><td style="color:#64748B;">Humas</td><td>{render_status_badge("MEREDA", "slate")}</td><td style="color:#1E293B;">Data siap pakai</td></tr>
</tbody>
</table>
</div>"""
    render_html(watch_table)
    
    render_callout_target("Butir teratas lahir dari air - banjir Aceh, hujan di lokasi kunjungan, irigasi; perkara Sumut kini butir paling tenang.")
    render_mh_footer("Sumber: Analisis 26 Okt-2 Nov; berkas 28 Okt; Pemantau Delta 67, 69, 75, 94; Kompas.com, Pojoksatu, Koran Jakarta.")


# ==============================================================================
# SLIDE 20: PRIORITAS TINDAKAN & METODOLOGI
# ==============================================================================
def render_slide_20_priorities_methodology(df=None, **kwargs):
    render_mh_top_bar(slide_num=20)
    render_mh_title(
        "Prioritas Tindakan & Metodologi",
        "Enam tindakan; balai di depan, data per proyek terpisah",
        "Kiri: tindakan urut dari paling mendesak. Kanan: sumber data dan batasnya."
    )
    
    chips = [
        {"label": "Sumber", "val": "5", "sub": "jenis", "dot": "#2563EB"},
        {"label": "Lembaga (279)", "val": "2.935", "sub": "penyebutan", "dot": "#2563EB"},
        {"label": "Menteri (280)", "val": "952", "sub": "penyebutan", "dot": "#2563EB"},
        {"label": "Berkas Dibaca", "val": "4", "sub": "28 Okt", "dot": "#10B981"},
        {"label": "Klaim", "val": "1", "sub": "belum terverifikasi", "dot": "#F59E0B"}
    ]
    render_kpi_chips(chips)
    
    c_act, c_meth = st.columns([1.0, 1.0], gap="medium")
    
    with c_act:
        act_html = f"""<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Enam Tindakan Prioritas
</div>
<table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:10px; font-weight:700;">
<th style="padding:6px 4px;">TINDAKAN</th>
<th style="padding:6px 4px; width:80px;">WAKTU</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">1. Rilis kegiatan banjir Aceh-Sumbar</td><td>{render_status_badge("SEGERA", "red")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">2. Jadwal kerja Kali Angke, Cipaganti</td><td>{render_status_badge("SEGERA", "red")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">3. Peta lokasi irigasi Rp2,99 T</td><td>{render_status_badge("SEGERA", "red")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">4. Rilis sumur bor krisis air timur</td><td>{render_status_badge("PEKAN INI", "amber")}</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">5. Lembar capaian untuk daur survei</td><td>{render_status_badge("PEKAN INI", "amber")}</td></tr>
<tr><td style="font-weight:600; padding:6px 4px;">6. Padukan tagar internal dengan suara warga</td><td>{render_status_badge("PEKAN INI", "amber")}</td></tr>
</tbody>
</table>
</div>"""
        render_html(act_html)

    with c_meth:
        meth_html = """<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px 16px; box-shadow:0 1px 3px rgba(0,0,0,0.02);">
<div style="font-size:12.5px; font-weight:700; color:#0F2942; margin-bottom:10px; display:flex; align-items:center; gap:6px;">
<span style="width:7px; height:7px; border-radius:50%; background:#2563EB; display:inline-block;"></span>
Sumber dan Batasnya
</div>
<table style="width:100%; border-collapse:collapse; font-size:10.5px; text-align:left;">
<thead>
<tr style="border-bottom:1.5px solid #CBD5E1; color:#64748B; font-size:9.5px; font-weight:700;">
<th style="padding:6px 4px;">SUMBER</th>
<th style="padding:6px 4px;">CAKUPAN DAN BATAS</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Proyek Lembaga (279)</td><td style="color:#64748B;">Kementerian PU: 2.935 penyebutan, 7 saluran</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Proyek Menteri (280)</td><td style="color:#64748B;">Menteri PU: 952 penyebutan; khusus halaman menteri</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Berkas analisis</td><td style="color:#64748B;">279: Topik, Framing. 280: Isu Pos-Neg, Stakeholder (22-28 Okt)</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Pemantau Delta</td><td style="color:#64748B;">Banjir-Gempa (53 berita) dan Kekeringan (42), 31 Okt-2 Nov</td></tr>
<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600; padding:6px 4px;">Media terbuka</td><td style="color:#64748B;">Antara, Kompas.com, Koran Jakarta, RRI - uji silang</td></tr>
<tr><td style="font-weight:600; padding:6px 4px;">Saringan</td><td style="color:#64748B;">Bahasa asing, luar negeri, dinas PUPR, pemda, kementerian lain</td></tr>
</tbody>
</table>
</div>"""
        render_html(meth_html)

    render_callout_target("Tiga tindakan pertama dapat diselesaikan hari ini oleh balai dan Humas dengan data yang sudah ada.")
    render_mh_footer("Keyakinan: TERBUKTI = minimal dua sumber sepakat; KLAIM = belum terverifikasi. Tarikan 2 Nov 09.15 WIB; pembanding pekan 19-25 Okt.")


# ==============================================================================
# SLIDE 21: CLOSING SUMMARY
# ==============================================================================
def render_slide_21_closing_summary(df=None, **kwargs):
    html = """<div style="background:#0F2942; border-radius:12px; padding:45px 30px; text-align:center; color:#FFFFFF; margin:20px 0; box-shadow:0 4px 12px rgba(0,0,0,0.1);">
<div style="margin-bottom:24px;">
<span style="background:#F6B100; color:#0F172A; font-weight:800; font-size:16px; padding:6px 14px; border-radius:6px; letter-spacing:0.8px;">MH</span>
</div>
<div style="font-size:22px; font-weight:700; color:#FFFFFF; max-width:850px; margin:0 auto 24px auto; line-height:1.6; font-family:'Plus Jakarta Sans',sans-serif;">
Pekan ini perkara Sumut mereda - negatif lembaga turun dari 20% ke 13% - dan panggung pindah ke air: Kali Angke yang ditonton 200 ribu kali, Karian yang surut, dan banjir awal musim. Pekan depan ditentukan oleh siapa yang lebih dulu hadir saat hujan turun.
</div>
<div style="border-top:1px solid rgba(255,255,255,0.15); width:180px; margin:24px auto 16px auto;"></div>
<div style="font-size:12px; color:#94A3B8; font-weight:500;">
Tim Monitoring Harian - Edisi Spesial Mingguan untuk Pimpinan, 26 Oktober-1 November 2026
</div>
</div>"""
    render_html(html)
