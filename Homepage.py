import streamlit as st

st.set_page_config(
    page_title="Matrix App",
    page_icon="❤️",
)
# JUDUL
st.title('MATRIX CALCULATOR 🧮')

def main():
    st.write("Selamat mencoba!🙌")
    
    st.write("- App 1: Determinant Matrix")
    st.write("- App 2: Eigenvalues Matrix")
    st.write("- App 3: Eigenvectors Matrix")
    st.write("- App 4: Perkalian Matrix")
    st.write("- App 5: Normalisasi Matrix")
    st.write("- App 6: Transpose Matrix")

    
if __name__ == '__main__':
    main()
