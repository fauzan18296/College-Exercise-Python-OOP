import random

class SimpleGames:
        score = 0
        def __init__(self, health):
                        self.health = health
        def attack(self):
                user_attack_types = ["Gunting", "Batu", "Kertas"]
                komputer_choice = random.choice(user_attack_types)
                user_choice = input("Pilih salah satu: Gunting, Batu, Kertas: ")
                i = 0
                while i <= self.health:
                        for j in range(len(user_attack_types)):
                                        if user_attack_types[j] == user_choice:
                                                if user_attack_types[j] == komputer_choice:
                                                        print("Seri!")
                                                        SimpleGames.score += 0
                                                elif (user_attack_types[j] == "Gunting" and komputer_choice == "Kertas") or (user_attack_types[j] == "Batu" and komputer_choice == "Gunting") or (user_attack_types[j] == "Kertas" and komputer_choice == "Batu"):
                                                        print("Komputer memilih:", komputer_choice)
                                                        print("Kamu menang!")
                                                        SimpleGames.score += 1
                                                else:
                                                        print("Komputer memilih:", komputer_choice)
                                                        print("Kamu kalah!")
                                                        self.health -= 1
                                                        SimpleGames.score -= 1

                        choice_message = "Apakah kamu ingin bermain lagi? (y/n): "
                        play_again = input(choice_message)
                        if play_again.lower() == 'y':
                                user_attack_types = ["Gunting", "Batu", "Kertas"]
                                komputer_choice = random.choice(user_attack_types)
                                user_choice = input("Pilih salah satu: Gunting, Batu, Kertas: ")
                                i += 1
                        elif play_again.lower() == 'n':
                                print("Terima kasih sudah bermain game ini.")
                                print(f"Permainan Selesai!Skor akhir kamu: {SimpleGames.score} Health kamu: {games.health}")
                                break
games = SimpleGames(3)
games.attack()