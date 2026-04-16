class SystemDataMahasiswa:
    def __init__(self, option, user_data):
        self.datas = user_data
        self.option = option

    def menu(self):
        while True:  # ➜ TAMBAHAN penting (loop menu)
            print(f"{'='*20} {'Menu'.center(20)} {'='*20}")
            print("1. Tambah data mahasiswa\n2. Tampilkan data mahasiswa\n3. Hapus data\n4. Keluar")
            print(f"{'='*60}")

            self.option = input("Pilih opsi (1/2/3): ")

            if self.option == '1':
                input_data = input("Masukkan data mahasiswa (pisahkan dengan spasi): ")
                data_mahasiswa = input_data.split()
                self.add_data(data_mahasiswa)

            elif self.option == '2':
                self.show_data()

            elif self.option == '3':
                self.delete_data()

            elif self.option == '4':
                print("Terima kasih telah menggunakan program ini!")
                break

    def add_data(self, mahasiswa):
        # ➜ HAPUS while True (biar tidak infinite loop)
        self.datas.append(mahasiswa)
        print("Data mahasiswa berhasil ditambahkan!\n")

        for i, value in enumerate(self.datas, start=0):
            number_student = map(int, value[1].split())
            NIM = list(number_student)
            print(f"Nama: {value[0]}, NIM: {NIM[0]}, Jurusan: {value[2]}")

    def show_data(self):
        print(f"{'='*20} {'Data mahasiswa'.center(20)} {'='*20}\n")
        for i, mhs in enumerate(self.datas, start=1):
            number_student = map(int, mhs[1].split())
            NIM = list(number_student)
            print(f"{i}. Nama: {mhs[0]}, NIM: {NIM[0]}, Jurusan: {mhs[2]}")
        print("\n", "="*60)

    def delete_data(self):
        self.show_data()
        try:
            index = int(input("Masukkan nomor data mahasiswa yang ingin dihapus: ")) - 1
            if 0 <= index < len(self.datas):
                del self.datas[index]
                print("Data mahasiswa berhasil dihapus!")
            else:
                print("Nomor data tidak valid.")
        except ValueError:
            print("Input tidak valid. Masukkan nomor yang benar.")


# Inisialisasi yang benar (HARUS 2 parameter)
system = SystemDataMahasiswa(None, [])

# Jalankan menu
system.menu()


