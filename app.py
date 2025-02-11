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
    return pd.read_csv("Data Graduation Feb 2025.csv", encoding="utf-8")

data = load_data()

# Cek apakah NIK ada di data
if nik_input:
    matched_data = data[(data['NIK'] == nik_input) & (data['Program'] == selected_program)]
    
    if not matched_data.empty:
        if "SDP Batch 1" in selected_program or "SDP Batch 2" in selected_program:
            st.image("3.png", caption="Selamat! Anda lulus dari SDP", use_column_width=True)
        elif "LDP Batch 5" in selected_program or "LDP Batch 6" in selected_program:
            st.image("4.png", caption="Selamat! Anda lulus dari LDP", use_column_width=True)
    else:
        st.warning("NIK tidak ditemukan dalam program yang dipilih.")
