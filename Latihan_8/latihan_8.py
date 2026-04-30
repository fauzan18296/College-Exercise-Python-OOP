class Kelas:
          def __init__(self, nama_dosen, nama_mk, jumlah_mahasiswa):
                    self.nama_dosen = nama_dosen
                    self.nama_mk = nama_mk
                    self.jumlah_mahasiswa = jumlah_mahasiswa

class Mahasiswa(Kelas):
          def __init__(self, nama_mahasiswa, nim, prodi):
                    self.nama_mahasiswa = nama_mahasiswa
                    self.nim = nim
                    self.prodi = prodi
                    self.nama_dosen = "Budi"
                    self.nama_mk = "Pemrograman Object Oriented"
                    self.jumlah_mahasiswa = 30

mahasiswa1 = Mahasiswa("Andi", "123456", "Informatika")


print("="*10, "kelas".upper(), "="*10)
print("Nama Dosen:", mahasiswa1.nama_dosen)
print("Nama Mata Kuliah:", mahasiswa1.nama_mk)
print("Jumlah Mahasiswa:", mahasiswa1.jumlah_mahasiswa)

print("\n","="*10, "mahasiswa".upper(), "="*10)
print("Nama Mahasiswa:", mahasiswa1.nama_mahasiswa)
print("NIM:", mahasiswa1.nim)
print("Program Studi:", mahasiswa1.prodi)