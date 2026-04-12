class Mobil:
          def __init__(self, merk, color):
                    self.merk = merk
                    self.color = color
          def info(self):
                    print(f"Mobil ini bermerk {self.merk} dan berwarna {self.color}")
mobil1 = Mobil("Toyota", "Merah")
mobil2 = Mobil("Honda", "Putih")
print(mobil1.info())
print(mobil2.info())