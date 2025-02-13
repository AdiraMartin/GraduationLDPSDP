import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Graduation LDP & SDP",
    layout="wide",
    page_icon="🎓",
)

col1, col2, col3 = st.columns([1, 3, 1])

with col2:  # Kolom tengah untuk judul agar berada di tengah halaman
    st.markdown(
        "<h1 style='text-align: center; color: navy;'>🎓 Graduation Day 🎓</h1>",
        unsafe_allow_html=True,
    )

with col1:  # Kolom kanan untuk logo
    st.image("Print Gimmick Lulus.png", width=120)
    
st.markdown("<h2 style='text-align: center; color: darkblue;'>Leadership Development Program & Supervisor Development Program</h2>",
        unsafe_allow_html=True,
    )

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Data Graduation Feb 2025.csv")
    df["NIK"] = df["NIK"].astype(str).str.upper()  # Ubah semua NIK jadi huruf kapital
    return df

data = load_data()

# Buat form input di tengah
st.write("##")
st.markdown("<h3 style='text-align: center;'>Masukkan Data</h3>", unsafe_allow_html=True)

with st.form("cek_kelulusan", clear_on_submit=False):
    nik_input = st.text_input("Masukkan NIK", key="nik").strip().upper()  # Ubah input NIK ke huruf kapital
    nama_input = st.text_input("Masukkan Nama", key="nama").strip().title()  # Format nama jadi Title Case
    program_options = ["LDP Batch 5", "LDP Batch 6", "SDP Batch 1", "SDP Batch 2"]
    selected_program = st.selectbox("Pilih Program", program_options, key="program")

    # Tombol Cek Kelulusan
    submit_button = st.form_submit_button("Cek Kelulusan")

if submit_button:
    # Pengecualian untuk NIK HOAC21005
    if nik_input == "HOAC21005":
        selected_program = "LDP Batch 6"  # Override programnya
        lulus = True
    else:
        matched_data = data[(data['NIK'] == nik_input) & (data['Program'] == selected_program)]
        lulus = not matched_data.empty

    if lulus:
        nama_display = nama_input if nama_input else "Kamu"
        st.markdown(f"<h3 style='text-align: center; color: green;'> Yeaaayyy Selamat yaa {nama_display}! kamu lulus 🎉</h3>", unsafe_allow_html=True)

        # Tampilkan gambar berdasarkan program
        if "SDP" in selected_program:
            st.image("4.png", caption="Supervisor Development Program", use_container_width=True)
        elif "LDP" in selected_program:
            st.image("3.png", caption="Leadership Development Program", use_container_width=True)
    else:
        st.markdown("<h3 style='text-align: center; color: red;'>Maaf, data tidak ditemukan 😞</h3>", unsafe_allow_html=True)
        st.warning("Pastikan NIK dan Program yang Kamu masukkan sudah benar.")
