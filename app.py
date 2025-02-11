import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Graduation LDP & SDP",
    layout="wide",
    page_icon="🎓",
)

# Judul halaman
st.markdown(
    "<h1 style='text-align: center; color: navy;'>🎓 Graduation Day </h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h2 style='text-align: center; color: darkblue;'>Leadership Development Program & Supervisor Development Program</h2>",
    unsafe_allow_html=True,
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("Data Graduation Feb 2025.csv")

data = load_data()

# Buat form input di tengah
st.write("##")
st.markdown("<h3 style='text-align: center;'>Masukkan Data Anda</h3>", unsafe_allow_html=True)

with st.form("cek_kelulusan", clear_on_submit=False):
    nik_input = st.text_input("Masukkan NIK", key="nik")
    nama_input = st.text_input("Masukkan Nama", key="nama")
    
    # Pilihan program
    program_options = ["LDP Batch 5", "LDP Batch 6", "SDP Batch 1", "SDP Batch 2"]
    selected_program = st.selectbox("Pilih Program", program_options, key="program")

    # Tombol Cek Kelulusan
    submit_button = st.form_submit_button("Cek Kelulusan")

if submit_button:
    matched_data = data[(data['NIK'] == nik_input) & (data['Program'] == selected_program)]

    if not matched_data.empty:
        st.markdown("<h3 style='text-align: center; color: green;'>Selamat! Anda lulus 🎉</h3>", unsafe_allow_html=True)
        
        # Tampilkan gambar berdasarkan program
        if "SDP" in selected_program:
            st.image("4.png", caption="Supervisor Development Program", use_column_width=True)
        elif "LDP" in selected_program:
            st.image("3.png", caption="Leadership Development Program", use_column_width=True)
    else:
        st.markdown("<h3 style='text-align: center; color: red;'>Maaf, data tidak ditemukan 😞</h3>", unsafe_allow_html=True)
        st.warning("Pastikan NIK dan Program yang Anda masukkan sudah benar.")
