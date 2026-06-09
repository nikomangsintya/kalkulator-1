import streamlit as st

# Judul
st.set_page_config(
    page_title="Kalkulator FPB dan KPK",
    page_icon="🧮"
)

st.title("🧮 Kalkulator FPB dan KPK")
st.write("Menggunakan Algoritma Euclid")

# Fungsi FPB dengan langkah-langkah Euclid
def hitung_fpb(a, b):
    langkah = []

    while b != 0:
        q = a // b
        r = a % b

        langkah.append(f"{a} = {q} × {b} + {r}")

        a, b = b, r

    return a, langkah


# Input pengguna
a = st.number_input(
    "Masukkan bilangan pertama",
    min_value=1,
    step=1
)

b = st.number_input(
    "Masukkan bilangan kedua",
    min_value=1,
    step=1
)

# Tombol hitung
if st.button("Hitung"):

    fpb, langkah = hitung_fpb(int(a), int(b))

    kpk = abs(int(a) * int(b)) // fpb

    st.success(f"FPB = {fpb}")
    st.success(f"KPK = {kpk}")

    st.subheader("Langkah Algoritma Euclid")

    for langkah_ke, isi in enumerate(langkah, start=1):
        st.write(f"**Langkah {langkah_ke}**")
        st.code(isi)

    st.info(
        f"Karena sisa terakhir adalah 0, maka FPB({int(a)}, {int(b)}) = {fpb}"
    )
