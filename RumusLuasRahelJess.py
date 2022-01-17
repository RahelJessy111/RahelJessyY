import os

def clearData():
    os.system('cls')

def menuBidang():
    clearData()
    while True:
        print("""
            <<<===Selamat Datang Di Program Kami===>>>
        Pilih Bidang Yang Akan Dihitung:
        1. Luas Segiempat
        2. Luas Segitiga
        3. Luas Lingkaran
        4. Kembali""","\n")
        inputAngka = int(input("Masukkan berupa angka: "))
        if inputAngka == 1:
            rumusSegiempat()
        elif inputAngka == 2:
            rumusSegitiga()
        elif inputAngka == 3:
            rumusLingkaran()
        elif inputAngka == 4:
            Kembali()

def rumusSegiempat():
    clearData()
    while True:
        print("""
            <<==Menghitung Luas Segiempat==>>""")
        Sisi=int(input("Berapa Sisi Yang Diketahui: "))
        luas= Sisi*Sisi
        print("Luas Segiempat adalah" ,str(luas))
        inputlagi=input('Apakah Anda Ingin Menghitung Lagi? tekan ya [y] or tidak [t]: ')
        if inputlagi == 'y' :
            rumusSegiempat()
        else:
            menuBidang()

def rumusSegitiga():
    clearData()
    while True:
        print("""
            <<==Menghitung Luas Segitiga==>>""")
        Alas=int(input("Berapa Alas Yang Diketahui: "))
        Tinggi=int(input("Berapa Tinggi Yang Diketahui: "))
        luas= 0.5 * Alas * Tinggi
        print("Luas Segitiga adalah ",str(luas))
        inputlagi=input('Apakah Anda Ingin Menghitung Lagi? tekan ya [y] or tidak [t]: ')
        if inputlagi == 'y' :
            rumusSegitiga()
        else:
            menuBidang()

def rumusLingkaran():
    clearData()
    print("""
        <<==Menghitung Luas Lingkaran==>>""")
    def rumusLingkaran(r):
        print("""
        <<==Menghitung Luas Lingkaran==>>""")
        return 3.14 * (r*r)
    r = input("Berapa Jari Jarinya: ")
    luas = rumusLingkaran(int(r))
    print("Luas Lingkaran adalah ",str(luas))
    inputlagi=input('Apakah Anda Ingin Menghitung Lagi? tekan ya [y] or tidak [t]: ')
    if inputlagi == 'y' :
        rumusLingkaran()
    else:
        menuBidang()

def Kembali():
    while True :
        clearData()
        inputlagi=input('Apakah Anda Ingin Keluar dari Program? tekan ya [y] or tidak [t]: ')
        if inputlagi == 'y' :
            print("Terima Kasih Sudah Mencoba Program Kami")
        else:
            menuBidang()
menuBidang()