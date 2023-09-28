def hitung_nilai_akhir(UTS, UAS):
    nilai_akhir = (UTS + UAS) / 2
    return nilai_akhir


def hitung_nilai_akhir_semua_mahasiswa(data_mahasiswa):
    data_nilai_akhir = {} 
    for nama, nilai in data_mahasiswa.items():
        UTS, UAS = nilai['UTS'], nilai['UAS']
        nilai_akhir = hitung_nilai_akhir(UTS, UAS)
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir


def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))


def main():
    data_mahasiswa = {
        'MahasiswaA': {'UTS': 60, 'UAS': 90},
        'MahasiswaB': {'UTS': 89, 'UAS': 98},
        'MahasiswaC': {'UTS': 90, 'UAS': 50},
    }

    data_nilai_akhir = hitung_nilai_akhir_semua_mahasiswa(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)


if __name__ == "__main__":
    print("Kegiatan 3")
    main()