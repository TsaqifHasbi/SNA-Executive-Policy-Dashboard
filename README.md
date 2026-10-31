# IndoBERT & SNA Intelligence Dashboard (IndoBERT_SNA_MT_PP)

Aplikasi Dashboard Analisis Sentimen berbasis **Deep Learning IndoBERT (Akurasi: 91.33%, Macro F1: 91.37%)** dan **Social Network Analysis (SNA by Sentiment)** lintas 7 kanal media sosial dan berita online.

## 🏛️ Topik Utama & Strategis:
1. **Sekolah Rakyat** (Topik Utama Skripsi: Pemantauan Fasilitas, Pendidikan, & Mutu Konstruksi)
2. **Makan Bergizi Gratis (MBG)**
3. **Koperasi Desa Merah Putih (KDMP)**

## 🚀 Fitur Utama Dashboard:
1. **Executive Summary & Dashboard PU**:
   - Volume, Reach (Jangkauan), Engagement, dan **Net Sentiment Score (NSS)** ala Kementerian Pekerjaan Umum.
   - Tren Harian & Rerata Bergerak 7 Hari (**7D Moving Average**).
   - Uji Kebermaknaan Statistik (**Two-Sample Z-Test**) untuk membedakan perubahan **NYATA** vs **DERAU**.
   - Analisis 4 Fungsi Framing (**Entman & Edelman**).
2. **SNA by Sentiment**:
   - Graf jejaring interaktif berbasis fisika (Pyvis) dengan pewarnaan sentimen (*🟢 Positif, 🔴 Negatif, ⚪ Netral*).
   - Metrik Sentralitas Aktor (In-Degree / Top Influencers, Out-Degree).
   - Ekspor graf ke format **Gephi (.GEXF)** untuk analisis resolusi tinggi.
3. **Platform Intelligence (7 Kanal)**:
   - Analisis mendalam per kanal: TikTok, YouTube, Twitter/X, Instagram, Threads, Facebook, dan Berita Online.
   - Deteksi konten viral terpopuler (paling banyak ditonton, disukai, dan direpost).
4. **Dual Word Clouds & Difusi Isu**:
   - **Buzz of Cloud**: Berdasarkan frekuensi kata yang paling banyak diucapkan.
   - **Word of Cloud**: Berdasarkan jangkauan (reach) kata yang paling luas menyebar.
5. **Evaluasi IndoBERT (Bab IV Skripsi)**:
   - Evaluasi lengkap: Akurasi Sentimen 91.33% (Macro F1 91.37%), Akurasi Emosi 91.78% (Macro F1 91.74%).
   - Visualisasi Heatmap Confusion Matrix 3x3.
   - Simulator prediksi teks baru (*Live Tester*).

## 🛠️ Cara Menjalankan:
1. Buka terminal PowerShell di folder ini:
   `ash
   cd c:\Users\Asus\OneDrive\Documents\Project_Streamlit\IndoBERT_SNA_MT_PP
   `
2. Jalankan Streamlit:
   `ash
   streamlit run app.py
   `
   *Atau cukup klik dua kali file un_dashboard.bat!*
