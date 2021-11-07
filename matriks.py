from substract_matriks import Matriks

def cetakMatriks(matriks):
    for brs in range(matriks.bykBaris()):
        for klm in range(matriks.bykKolom()):
            print(f'{matriks[brs, klm]: 4d}', end=' ')
        print()

def main():

    # Definisikan matrixA = | 6 7 |
    #                       | 8 9 |
    #                       | 1 0 |
    matrixA = Matriks(3, 2)
    matrixA[0, 0] = 6
    matrixA[0, 1] = 7
    matrixA[1, 0] = 8
    matrixA[1, 1] = 9
    matrixA[2, 0] = 1
    matrixA[2, 1] = 0


    # Definisikan matrixB = | 0 1 |
    #                       | 2 3 |
    #                       | 4 5 |
    matrixB = Matriks(3, 2)
    matrixB[0, 0] = 0
    matrixB[0, 1] = 1
    matrixB[1, 0] = 2
    matrixB[1, 1] = 3
    matrixB[2, 0] = 4
    matrixB[2, 1] = 5


    # Definisikan matrixC = | -1 -2 |
    #                       | 3   4 |
    matrixC = Matriks(2, 2)
    matrixC[0, 0] = -1
    matrixC[0, 1] = -2
    matrixC[1, 0] = 3
    matrixC[1, 1] = 4
    
    # Lakukan pengurangan matrixA - matrixB
    # menggunakan operasi substract dengan operator -.
    matrixS = matrixA - matrixB

    # Cetak selisih matriks
    print('MatrixA - MatrixB =')
    print()
    cetakMatriks(matrixS)
    print()
    
    # Uji pengurangan dua matriks berbeda ukuran
    print('Uji pengurangan dua matriks berbeda ukuran:')
    try:
        matrixT = matrixA - matrixC
        cetakMatriks(matrixT)
    except ValueError:
        print('Matriks yang diberikan tidak berukuran sama!')
        
main()