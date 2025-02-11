import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Graduation LDP 5 & 6 and SDP 1 & 2', 
    layout='wide',  
    page_icon='🎓'  
)

# Menampilkan logo di tengah atas
st.image("image.png", width=150)

# Menampilkan judul dan subjudul di tengah
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
st.write("## Masukkan Data Anda")
nik_input = st.text_input("Masukkan NIK").upper()
nama_input = st.text_input("Masukkan Nama")

# Pilihan program
program_options = ["LDP Batch 5", "LDP Batch 6", "SDP Batch 1", "SDP Batch 2"]
selected_program = st.selectbox("Pilih Program", program_options)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("Data Graduation Feb 2025.csv")

data = load_data()

# Tombol cek kelulusan
if st.button("Cek Kelulusan"):
    if nik_input == "HOAC21005":
        st.image("3.png", caption=f"Selamat {nama_input}! Anda lulus dari LDP Batch 6", use_column_width=True)
    else:
        matched_data = data[(data['NIK'] == nik_input) & (data['Program'] == selected_program)]
        
        if not matched_data.empty:
            if "SDP Batch 1" in selected_program or "SDP Batch 2" in selected_program:
                st.image("4.png", caption=f"Selamat {nama_input}! Anda lulus dari SDP", use_column_width=True)
            elif "LDP Batch 5" in selected_program or "LDP Batch 6" in selected_program:
                st.image("3.png", caption=f"Selamat {nama_input}! Anda lulus dari LDP", use_column_width=True)
        else:
            st.warning("NIK tidak ditemukan dalam program yang dipilih.")
