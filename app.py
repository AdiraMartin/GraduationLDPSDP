import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Graduation LDP 5 & 6 and SDP 1 & 2', 
    layout='wide',  
    page_icon='🎓'  
)

# Layout dua kolom
col1, col2 = st.columns((0.12, 1))  # Sedikit perbesar kolom logo agar lebih proporsional

# Menampilkan judul dan subjudul di sebelah kanan (col2)
with col2:
    st.markdown(
        "<h1 style='text-align: center; color: navy;'>🎓 Graduation Day </h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h2 style='text-align: center; color: darkblue;'>Leadership Development Program Batch 5 & 6</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h2 style='text-align: center; color: darkblue;'>Supervisor Development Program Batch 1 & 2</h2>",
        unsafe_allow_html=True,
    )

# Input kolom untuk NIK dan Nama
st.sidebar.header("Input Data")
nik_input = st.sidebar.text_input("Masukkan NIK")
nama_input = st.sidebar.text_input("Masukkan Nama")

# Pilihan program
program_options = ["LDP Batch 5", "LDP Batch 6", "SDP Batch 1", "SDP Batch 2"]
selected_program = st.sidebar.selectbox("Pilih Program", program_options)

# Load data
@st.cache_data
def load_data():
    return pd.read_excel("Data Graduation Feb 2025.csv")

data = load_data()
data
