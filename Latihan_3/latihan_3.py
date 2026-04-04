# Buat fitur login yang memiliki max 3x kesempatan untuk login
username_account = input("Masukkan username: ")
password_account = input("Masukkan password: ")
message_confirm = input("Apakah Anda ingin mencoba login lagi? (y/n): ") 

def login(username, password, messege):
          i = 0
          chance_login = 3
          
          while i <= 3:
                    if username == "admin" and password == "admin123":
                              print(f"Anda telah berhasil login! Selamat datang {username}!")
                    elif username != "admin" or password != "admin123" or i != 0:
                              chance_login -= 1
                              print(f"Username atau password salah! Kesempatan login: {chance_login}x lagi")
                              if chance_login == 0:
                                        print("Anda telah kehabisan kesempatan untuk login. Silakan coba lagi nanti.")
                                        break
                    if messege == "n":
                              print("Terima kasih telah menggunakan aplikasi ini.")
                              break
                    elif messege == "y":
                              username = input("Masukkan username: ")
                              password = input("Masukkan password: ")
                              messege = input("Apakah Anda ingin mencoba login lagi? (y/n):")
                              i += 1
my_login = login(username_account, password_account, message_confirm)
print(my_login)