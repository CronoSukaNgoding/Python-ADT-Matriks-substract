from array1d import Array

# Implementasi ADT Array 2 Dimensi
class Array2D:
    # Buat array 2-D dengan ukuran numBaris x numKolom
    # Mendefinisikan sebuah field berupa array 1-D yang masing-masing
    # elemennya mereferensikan array 1-D yang berisi nilai-nilai pada kolom-kolom
    # dari sebuah baris.
    def __init__(self, bykBaris, bykKolom):
        # Buat array 1-D untuk menyimpan array referensi untuk setiap baris.
        self._arrBaris = Array(bykBaris)

        # Buat array 1-D untuk setiap baris dari array 2-D.
        for i in range(bykBaris):
            self._arrBaris[i] = Array(bykKolom)

    # Mengembalikan banyaknya baris dalam array 2-D.
    def bykBaris(self):
        return len(self._arrBaris)

    # Mengembalikan banyaknya kolom dalam array 2-D.
    def bykKolom(self):
        return len(self._arrBaris[0])

    # Membersihkan array dengan menetapkan setiap element dengan nilai yang diberikan.
    def clear(self, nilai):
        for baris in range(self.bykBaris()):
            self._arrBaris[baris].clear(nilai)

    # Mendapatkan isi dari elemen pada posisi [i, j].
    # Diakses menggunakan notasi subscript: arr2D[i, j]
    def __getitem__(self, indeksTuple):
        # jika argumen yang diberikan bukan dua indeks (brs, klm)
        # raise ValueError
        if len(indeksTuple) != 2:
            raise IndexError('Indeks tidak valid.')
        else:
            brs = indeksTuple[0]
            klm = indeksTuple[1]
            
            # Jika brs dan klm tidak valid raise IndexError
            if brs < 0 or brs >= self.bykBaris() \
                or klm < 0 or klm >= self.bykKolom():
                raise IndexError('Indeks tidak valid.')
            else:
                arr1D = self._arrBaris[brs]
                elm = arr1D[klm]
                return elm

    # Menetapkan nilai dari elemen pada posisi [i, j].
    # Diakses menggunakan notasi subscript: arr2D[i, j] = nilai.
    def __setitem__(self, indexTuple, nilai):
        if len(indexTuple) != 2:
            raise IndexError('Indeks tidak valid.')
        else:
            brs = indexTuple[0]
            klm = indexTuple[1]
            # Jika brs dan klm tidak valid raise IndexError
            if brs < 0 or brs >= self.bykBaris() \
                or klm < 0 or klm >= self.bykKolom():
                raise IndexError('Indeks tidak valid.')
            else:
                arr1D = self._arrBaris[brs]
                arr1D[klm] = nilai
            
    