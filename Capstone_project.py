#Loading Library
import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt


# Import Dataset
Index_Cum_Return_Data =  pd.read_csv('index_cum_return_data.csv')
JKSE_Event_Data = pd.read_csv('jkse_event_data.csv')
Sectoral_2020 = pd.read_csv('sectoral2020_data.csv')
Sectoral_2022 = pd.read_csv('sectoral2022_data.csv')
Heatmap = pd.read_csv('heatmap.csv')
GDP = pd.read_csv('GDP.csv')
FDI = pd.read_csv('FDI.csv')

st.set_page_config(
    page_title = "Analisis Performa Pergerakan Indeks Saham Selama Tahun 2020-2023"
    ,layout='centered')

st.title("Analisis Performa Pergerakan Indeks Saham Selama Tahun 2020-2023")
stringHeader =  'Penulis : **Julyandri**'
st.markdown(stringHeader)

# Background & Hypothesis
st.write("""Belakangan ini, popularitas saham sebagai instumen investasi semakin meningkat 
        dikarenakan investasi saham bisa memberikan return yang besar. Di Indonesia, JKSE atau IHSG
        merupakan indeks yang digunakan Bursa Efek Indonesia untuk mengukur harga saham. Namun, 
        di negara lain memiliki nama indeks saham yang berbeda-beda seperti Thailand (SET Index), 
        Malaysia (KLSE) dan Filipina (PSEi). Pergerakan indeks saham pada umumnya sangat sensitif 
        terhadap kondisi perekonomian maupun issue-issue baik secara domestik maupun global.""")

st.write("""Hipotesa dalam project ini adalah semakin tinggi GDP nominal maka dapat meningkatkan 
        performa indeks saham suatu negara. GDP(Gross Domestic Product) atau PDB(Produk Domestik Bruto) adalah 
        perhitungan yang digunakan oleh suatu negara sebagai ukuran utama bagi aktivitas perekonomian. 
        Meningkatnya GDP menunjukkan naiknya kemampuan masyarakat untuk konsumsi sehingga dapat 
        meningkatkan penjualan perusahaan yang akan berdampak pada peningkatan performa indeks saham suatu negara.""")

st.write("""Selain itu, pada bulan Maret 2020, terjadi peristiwa covid-19 yang memberikan dampak negatif
        terhadap kinerja indeks saham indonesia secara bulanan dan pada bulan Febuari 2022, peristiwa invasi
        Russia-Ukraine tidak berdampak pada kinerja indeks saham secara bulanan dengan 
        Foreign Direct Investment sebagai indikator""")

st.write("""Analisis dalam project ini untuk menguji hipotesa tersebut dan melihat bagaimana 
        perbandingan performa dan korelasi indeks saham antar negara selama tahun 2020-2023 dan
        bagaimana pergerakan pasar saham Indonesia pada saat terjadi COVID-19 dan 
        invasi Russia-Ukraine""")

# GDP
st.subheader("GDP(Gross Domestic Product)")

Dropdown = st.selectbox("Pilih Tahun", GDP['Year'].unique())
df_dropdown_year = GDP[GDP['Year'] == Dropdown]
fig = px.bar(df_dropdown_year, x='GDP', y='Country', orientation='h',text='GDP')
fig.update_layout(title=f'GDP in Billions USD for the Year {Dropdown}',
                  xaxis_title='GDP',
                  yaxis_title='Country',
                  showlegend=False, yaxis={'categoryorder':'total ascending'}
                  )
st.plotly_chart(fig, use_container_width=True)

# Analysis
st.write("""Selama 4 tahun berturut-turut, Indonesia memiliki GDP nominal tertinggi dibandingkan
         ketiga negara tersebut""")

# Performance Index
st.subheader("Performance Index")

# Figure 1
fig1 = px.line(Index_Cum_Return_Data, x='Date',
              y='cum_return_pct', color='Name',
              title='Performance Index - Monthly Cumulative Returns',
              labels={'cum_return_pct':'Monthly Cumulative Returns (%)', })
fig1.update_layout(height=500,width=850,title_x=0.25)
st.plotly_chart(fig1)
# Analysis
st.write("""Berdasarkan grafik diatas,dapat dilihat bahwa secara kumulatif return 
         selama 2020-2023, JKSE memiliki return yang paling tinggi dan satu-satunya negara 
         yang bisa menghasilkan return positif dibanding dengan negara lainnya. Hal ini sejalan
         dengan hipotesa yang menyatakan tingginya GDP berdampak pada performa(return) index saham
         suatu negara yang semakin tinggi""")

# Covid-19 vs Russian Invasion of Ukraine
st.subheader("Covid-19 vs Russian Invasion of Ukraine")

# Figure 2
fig2 = make_subplots(rows=1, cols=2)

fig2.add_trace(
    go.Scatter(x=JKSE_Event_Data['Date'].loc[0:4], y=JKSE_Event_Data['Close'].loc[0:4],name="JKSE-Covid-19-Global Pandemic",line=dict(color='red')),
    row=1, col=1)

fig2.add_trace(
    go.Scatter(x=JKSE_Event_Data['Date'].loc[5:9], y=JKSE_Event_Data['Close'].loc[5:9],name="JKSE-Russian Invasion of Ukraine",
    line=dict(color='green')),row=1, col=2)
fig2.update_layout(height=500,width=850,title_text="Covid-19-Global Pandemic(Mar 2020) vs Russian Invasion of Ukraine(Feb 2022)"
                  ,title_x=0.075)
st.plotly_chart(fig2)
# Analysis
st.write("""Berdasarkan grafik diatas,dapat dilihat bahwa pada saat WHO mengumumkan covid-19 
         sebagai pandemi global pada bulan Maret 2020,JKSE menurun tajam dari bulan sebelumnya. 
         Namun disisi lain, pada saat invasi rusia ke ukraine pada bulan Febuari 2022,JKSE naik 
         cukup signifikan sampai 2 bulan kedepan""")

# Realization of Foreign Direct Investment in Indonesia
st.markdown("##### Realization of Foreign Direct Investment in Indonesia")
#Figure 2.1
fig2_1 = px.pie(FDI,values='Percentage',names='Country',title='Realization of Foreign Direct Invesment in Indonesia Q1-2022 in Billions USD')
fig2_1.update_layout(height=500,width=850,title_x=0.15)
st.plotly_chart(fig2_1)
# Analysis
st.write("""Besarnya Foreign Direct Investment(FDI) atau penanaman modal asing akan membawa sektor
        perdagangan di Indonesia semakin tumbuh dan tentunya meningkatkan perekonomian negara. Seperti
        yang kita ketahui bahwa kondisi perekonomian bisa dibilang sebagai salah satu faktor yang 
        berdampak pada naik turunnya harga saham.""")
         
st.write("""Ketika menambahkan indikator mengenai Foreign Direct Investment, terlihat bahwa top 5
        negara asing yang melakukan penanaman modal asing di Indonesia adalah Singapura,Hong Kong,
        China,Jepang dan Amerika sehingga tidak terdapat negara Russia maupun Ukraina 
        sehingga cenderung tidak berdampak pada indeks saham Indonesia secara harga bulanan""")

# Sectoral Indices
st.markdown("### Sectoral Indices")

# Figure 3 & Figure 4
fig3 = px.line(Sectoral_2020, x='Date',
              y='monthly_return', color='Sektoral',
              title='Performance - Sectoral Indices Monthly Return Due to Covid-19 - Global Pandemic (Mar 2020)',
              labels={'monthly_return':'Monthly Return (%)'})
fig3.update_layout(height=500,width=850,title_x=0.01)
st.plotly_chart(fig3, use_container_width=True)


fig4 = px.line(Sectoral_2022, x='Date',
              y='monthly_return', color='Sektoral',
              title='Performance - Sectoral Indices Monthly Return Due to Russian Invasion of Ukraine(Feb 2022)',
              labels={'monthly_return':'Monthly Return (%)', })
fig4.update_layout(height=500,width=850,title_x=0.01)
st.plotly_chart(fig4, use_container_width=True)
# Analysis
st.write("""Untuk melihat sektor apa saja yang paling terdampak atas kejadian tersebut maka 
         disajikan grafik diatas. Berdasarkan grafik tersebut, pada bulan Maret 2020, semua 
         sektoral kompak turun dengan penurunan paling dalam berada di sektor aneka industri 
         dan pada bulan Febuari 2022 meskipun JKSE naik, tetapi ada 2 sektor yang mengalami 
         penurunan yaitu kesehatan dan barang konsumen primer.""")

# Correlation Heatmap
st.subheader("Correlation Heatmap")

# Figure 5
fig5, ax = plt.subplots()
heatmap = sns.heatmap(Heatmap.corr(), ax=ax,annot=True,annot_kws={"size": 8})
heatmap.set_title('Correlation of All Stock Market Index', fontdict={'fontsize': 8})
fig5.set_size_inches(4, 2)
plt.xticks(fontsize=8)  
plt.yticks(fontsize=8)
cbar = heatmap.collections[0].colorbar
cbar.ax.tick_params(labelsize=8) 
st.write(fig5)
#Analysis
st.write("""JKSE dan SET.BK adalah dua indeks yang memiliki korelasi yang paling 
         tinggi yaitu sebesar 0,76.  Sedangkan JKSE dan KLSE memiliki korelasi negatif 
         sebesar -0.051""")

#Insight and Recommendation
with st.expander("**Insight and Recommendation**"):
    st.markdown("""
- JKSE atau yang biasa dikenal IHSG dapat mencetak cumulative return tertinggi 
sebesar 22.4% dari tahun 2020-2023 dibandingkan negara asia Tenggara lainnya. 
Ini dapat menjadi pertimbangan investor untuk memilih JKSE ketika ingin berinvestasi 
di negara Asia Tenggara dikarenakan memiliki return paling tinggi
- Pada saat WHO mengumumkan global pandemi pada bulan Maret 2020, JKSE mengalami 
penurunan dibandingkan bulan sebelumnya. Jika ditelusuri lebih lanjut, semua sektor 
mengalami penurunan namun sektor aneka industri mengalami penurunan paling tajam 
dibanding sektor lainnya. Pada bulan Febuari 2022, meskipun JKSE naik, tetapi ada 
2 sektor yang mengalami penurunan yaitu kesehatan dan barang konsumen primer. 
Sehingga, sektor-sektor tersebut dapat diperhatikan sebagai antisipasi/kewaspadaan 
investasi jika kedepannya terjadi kasus serupa
""")
    
#Contact
st.markdown("**Contact : julyandri78@gmail.com**")
