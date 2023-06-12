import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Matrix App",
    page_icon="❤️",
)

def main():
    st.sidebar.success("Pilihlah Operasi")
    app_choice = None  # Inisialisasi variabel app_choice

    app_choice = st.sidebar.radio("Pilih Operasi yang ingin Anda lakukan", 
                                  ("Determinant Matrix", 
                                   "Eigenvalues Matrix", 
                                   "Eigenvectors Matrix", 
                                   "Perkalian Matrix",
                                   "Normalisasi Matrix",
                                   "Transpose Matrix"))

    # Tampilkan konten sesuai pilihan
    #DETERMINAN MATRIX
    if app_choice == "Determinant Matrix":
        st.title('Determinant Matrix')
        
        def matrix_determinant(matrix):
            result = np.linalg.det(matrix)
            return result

        # Input matrix
        st.subheader("Matrix")
        rows = st.number_input("Jumlah baris", min_value=1, step=1, value=2)
        cols = st.number_input("Jumlah kolom", min_value=1, step=1, value=2)

        matrix = st.empty()
        matrix_values = []

        for i in range(rows):
            row = []
            for j in range(cols):
                value = st.number_input(f"Masukkan nilai pada posisi ({i}, {j})")
                row.append(value)
            matrix_values.append(row)

        matrix_values = np.array(matrix_values)
        matrix.dataframe(matrix_values)

        # Menampilkan perhitungan matrix determinant
        if st.button("Calculate Determinant"):
            result = matrix_determinant(matrix_values)
            st.subheader("Determinant")
            st.write(result)

    #EIGENVALUES MATRIX
    elif app_choice == "Eigenvalues Matrix":
        st.title('Eigenvalues Matrix')

        def matrix_eigenvalues(matrix):
            eigenvalues = np.linalg.eigvals(matrix)
            return eigenvalues

        # Input matrix
        st.subheader("Matrix")
        rows = st.number_input("Jumlah baris", min_value=1, step=1, value=2)
        cols = st.number_input("Jumlah kolom", min_value=1, step=1, value=2)

        matrix = st.empty()
        matrix_values = []

        for i in range(rows):
            row = []
            for j in range(cols):
                value = st.number_input(f"Masukkan nilai pada posisi ({i}, {j})")
                row.append(value)
            matrix_values.append(row)

        matrix_values = np.array(matrix_values)
        matrix.dataframe(matrix_values)

        # Menampilkan eigenvalue calculation
        if st.button("Calculate Eigenvalues"):
            eigenvalues = matrix_eigenvalues(matrix_values)
            st.subheader("Eigenvalues")
            for i, eigenvalue in enumerate(eigenvalues):
                st.write(f"Eigenvalue {i+1}: {eigenvalue}")

    #EIGENVECTORS MATRIX
    elif app_choice == "Eigenvectors Matrix":
        st.title('Eigenvectors Matrix')

        def matrix_eigenvectors(matrix):
            eigenvalues, eigenvectors = np.linalg.eig(matrix)
            return eigenvalues, eigenvectors

        # Input matrix
        st.subheader("Matrix")
        rows = st.number_input("Jumlah baris", min_value=1, step=1, value=2)
        cols = st.number_input("Jumlah kolom", min_value=1, step=1, value=2)

        matrix = st.empty()
        matrix_values = []

        for i in range(rows):
            row = []
            for j in range(cols):
                value = st.number_input(f"Masukkan nilai pada posisi ({i}, {j})")
                row.append(value)
            matrix_values.append(row)

        matrix_values = np.array(matrix_values)
        matrix.dataframe(matrix_values)

        # Menampilkan eigenvector calculation
        if st.button("Calculate Eigenvectors"):
            eigenvalues, eigenvectors = matrix_eigenvectors(matrix_values)
            st.subheader("Eigenvectors")
            for i, eigenvector in enumerate(eigenvectors.T):
                st.write(f"Eigenvector {i+1}: {eigenvector}")

    #PERKALIAN MATRIX
    elif app_choice == "Perkalian Matrix":
        st.title('Perkalian Matrix')

        def matrix_multiplication(matrix_a, matrix_b):
            result = np.dot(matrix_a, matrix_b)
            return result

        # Input matrix A
        st.subheader("Matrix A")
        rows_a = st.number_input("Jumlah baris (Matrix A)", min_value=1, step=1, value=2, key="rows_a")
        cols_a = st.number_input("Jumlah kolom (Matrix A)", min_value=1, step=1, value=2, key="cols_a")

        matrix_a = st.empty()
        matrix_a_values = []

        for i in range(rows_a):
            row = []
            for j in range(cols_a):
                value = st.number_input(f"Masukkan nilai pada posisi ({i}, {j})", key=f"value_a_{i}_{j}")
                row.append(value)
            matrix_a_values.append(row)

        matrix_a_values = np.array(matrix_a_values)
        matrix_a.dataframe(matrix_a_values)

        # Input matrix B
        st.subheader("Matrix B")
        rows_b = st.number_input("Jumlah baris (Matrix B)", min_value=1, step=1, value=2, key="rows_b")
        cols_b = st.number_input("Jumlah kolom (Matrix B)", min_value=1, step=1, value=2, key="cols_b")

        matrix_b = st.empty()
        matrix_b_values = []

        for i in range(rows_b):
            row = []
            for j in range(cols_b):
                value = st.number_input(f"Masukkan nilai pada posisi ({i}, {j})", key=f"value_b_{i}_{j}")
                row.append(value)
            matrix_b_values.append(row)

        matrix_b_values = np.array(matrix_b_values)
        matrix_b.dataframe(matrix_b_values)

        # Menampilkan hasil matrix multiplication
        if st.button("Multiply"):
            result = matrix_multiplication(matrix_a_values, matrix_b_values)
            st.subheader("Result")
            st.dataframe(result)

    # NORMALISASI MATRIX
    elif app_choice == "Normalisasi Matrix":
        st.title('Normalisasi Matrix')

        def normalize_matrix(matrix):
            max_value = np.max(matrix)
            min_value = np.min(matrix)
            normalized_matrix = (matrix - min_value) / (max_value - min_value)
            return normalized_matrix

        # Input matrix size
        matrix_size = st.number_input("Masukkan ukuran matriks:", min_value=1, step=1, value=3)

        # Input matrix elements
        matrix = []
        for i in range(matrix_size):
            row = []
            for j in range(matrix_size):
                element = st.number_input(f"Masukkan nilai pada posisi ({i}, {j}):", value=0.0)
                row.append(element)
            matrix.append(row)

        # Normalize matrix
        normalized_matrix = normalize_matrix(matrix)

        # Display original and normalized matrix
        st.subheader("Original Matrix:")
        st.write(np.array(matrix))
        st.subheader("Normalized Matrix:")
        st.write(normalized_matrix)

    #TRANSPOSE MATRIX
    elif app_choice == "Transpose Matrix":
        st.title('Transpose Matrix')

        def matrix_transpose(matrix):
            result = np.transpose(matrix)
            return result

        # Input matrix
        st.subheader("Matrix")
        rows = st.number_input("Jumlah baris", min_value=1, step=1, value=2)
        cols = st.number_input("Jumlah kolom", min_value=1, step=1, value=2)

        matrix = st.empty()
        matrix_values = []

        for i in range(rows):
            row = []
            for j in range(cols):
                value = st.number_input(f"Masukkan nilai pada posisi ({i}, {j})")
                row.append(value)
            matrix_values.append(row)

        matrix_values = np.array(matrix_values)
        matrix.dataframe(matrix_values)

        # Menampilkan hasil matrix transpose
        if st.button("Transpose"):
            result = matrix_transpose(matrix_values)
            st.subheader("Transposed Matrix")
            st.dataframe(result)


if __name__ == '__main__':
    main()
