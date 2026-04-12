class SystemDataMahasiswa:
    def __init__(self, user_data):
        self.datas = user_data  # list untuk menyimpan banyak mahasiswa

    def add_data(self, mahasiswa):
        while True:
            self.datas.append(mahasiswa)
            print("Data mahasiswa berhasil ditambahkan!\n")
            for i, value in enumerate(self.datas, start=0):
                    number_student= map(int, value[1].split())
                    NIM = list(number_student)
                    print(f"Nama: {value[0]}, NIM: {NIM[0]}, Jurusan: {value[2]}")
            messege = input("\nApakah Anda ingin menambahkan data mahasiswa lagi? (y/n): ")
            if messege.lower() == 'y':
                mahasiswa = input("Masukkan data mahasiswa (pisahkan dengan spasi): ").split()
                
            else:
                break

    def show_data(self):
        print(f"{"="*20} {"Data mahasiswa".center(20)} {"="*20}\n")
        for i, mhs in enumerate(self.datas, start=1):
            number_student= map(int, mhs[1].split())
            NIM = list(number_student)
            print(f"{i}. Nama: {mhs[0]}, NIM: {NIM[0]}, Jurusan: {mhs[2]}")
        print("\n", "="*60)

# Input user
input_data = input("Masukkan data mahasiswa (pisahkan dengan spasi): ")

# Pisahkan input menjadi bagian-bagian
data_mahasiswa = input_data.split()

# Buat objek SystemDataMahasiswa dan tambahkan data mahasiswa
system = SystemDataMahasiswa([])
system.add_data(data_mahasiswa)
system.show_data()