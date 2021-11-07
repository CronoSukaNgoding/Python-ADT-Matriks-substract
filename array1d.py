import ctypes

# Implementasi ADT Array menggunakan module ctypes
class Array:
    # Buat array dengan ukuran size.
    def __init__(self, size):
        if (size <= 0):
            raise ValueError("Array harus mempunyai ukuran > 0")
        else:
            # Inisialiasi field-field
            self._size = size
            # Buat struktur array menggunakan module ctype.
            CArray = ctypes.py_object * size
            self._isi = CArray()
            # Inisialisasi setiap elemen.
            self.clear(None)

    # Mengembalikan ukuran dari array.
    # Diakses menggunakan fungsi len().
    def __len__(self):
        return self._size

    # Method getitem mendapatkan nilai dari elemen dengan indeks tertentu
    # menggunakan notasi subscript.
    # Contoh: arr[5] mengembalikan nilai elemen pada indeks ke-5.
    # Method ini menerima satu argument: 
    # indeks dari elemen yang ingin diakses nilainya.
    # Method ini mengembalikan nilai elemen dari indeks.
    def __getitem__(self, index):
        if (index < 0 or index >= len(self)):
            raise IndexError('Indeks harus dalam rentang yang valid.')
        else:
            return self._isi[index]

    # Method setitem(nilai) menetapkan nilai elemen
    # menggunakan notasi subscript. 
    # Contoh: arr[4] = 11.
    # Method ini menerima dua argument: 
    # (1) indeks - indeks dari elemen yang ingin ditetapkan nilainya; dan 
    # (2) nilai - nilai yang ingin ditugaskan ke elemen tersebut
    # Method ini tidak mengembalikan nilai.
    def __setitem__(self, index, nilai):
        if (index < 0 or index >= len(self)):
            raise IndexError('Indeks harus dalam rentang yang valid.')
        else:
            self._isi[index] = nilai

    # Method clear(nilai) membersihkan array dengan 
    # mengganti nilai setiap elemen array dengan nilai yang diberikan.
    # Method ini menerima satu argument: 
    # nilai yang ingin ditetepkan ke semua elemen.
    # Method ini tidak mengembalikan nilai.
    def clear(self, nilai):
        for i in range(len(self)):
            self._isi[i] = nilai

    # Method iterator() meng-traverse nilai-nilai elemen pada array.
    # Diakses menggunakan loop for.
    def __iter__(self):
        return _ArrayIterator(self._isi)

# Class iterator untuk ADT Array
class _ArrayIterator:
    def __init__(self, iniArray):
        self._refArray = iniArray
        self._curIndex = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curIndex < len(self._refArray):
            entry = self._refArray[self._curIndex]
            self._curIndex += 1
            return entry
        else:
            raise StopIteration
