import random
import datetime


class Dictionary:
    def __init__(self):
        try:
            with open('dictionary.txt', 'r') as f:
                self.data = list(f.read().split())
        except FileNotFoundError:
            print("Nie znaleziono pliku")

    def choose_word(self, diff):
        word = 0
        if diff == 1:
            easy = [word for word in self.data if len(word) <= 4]
            word = random.choice(easy)
        elif diff == 2:
            medium = [word for word in self.data if 4 < len(word) <= 6]
            word = random.choice(medium)
        elif diff == 3:
            hard = [word for word in self.data if len(word) > 6]
            word = random.choice(hard)
        return word


class Validator:

    @staticmethod
    def check_word(word):
        if type(word) is str:
            if len(set(word)) == len(word):
                return 1
            else:
                return 0
        else:
            return 0


class Stats:
    bulls = 0
    cows = 0


class Engine:
    dict = Dictionary()
    val = Validator()
    stat = Stats()
    temp_att = 10
    attempts = 10
    difficulty = 1

    def change_attempts(self, att):
        self.attempts = att
        self.temp_att = att
        return self.attempts, self.temp_att

    def bull_cow_count(self, user, word):
        self.stat.bulls = 0
        self.stat.cows = 0
        for (user_char, word_char) in zip(user, word):
            if user_char in word:
                if user_char == word_char:
                    self.stat.bulls += 1
                else:
                    self.stat.cows += 1
        return self.stat.bulls, self.stat.cows

    def win(self, bulls, word):
        if bulls == len(word):
            print(f"Zgadłeś!\nIlość podjętych prób {self.temp_att - self.attempts + 1}.")
            return 1
        else:
            return 0

    def stats(self, att, bulls, cows):
        self.attempts = att - 1
        print(f"Bulls: {bulls} Cows: {cows}\nLiczba prób do końca: {self.attempts}")
        self.stat.bulls = 0
        self.stat.cows = 0
        return self.attempts, self.stat.bulls, self.stat.cows

    def add_word(self, word):
        if self.val.check_word(word):
            with open('dictionary.txt', 'a+') as f2:
                f2.write(f"\n{word}")
                f2.seek(0)
                self.dict.data = list(f2.read().split())
                print("Izogram dodany do bazy\n")
                return word
        else:
            print("Podane słowo nie jest izogramem")
            return False

    def export_score(self):
        with open("highscore.txt", "a") as f1:
            if self.attempts > 0:
                f1.write(f"Data gry:{datetime.datetime.now()}\n"
                         f"Poziom trudności: {self.difficulty}\n"
                         f"Liczba prób: {self.attempts}\n"
                         f"Wygrana po tylu próbach:{self.temp_att - self.attempts + 1}\n"
                         f"BULLS: {self.stat.bulls} COWS: {self.stat.cows}\n\n")
            else:
                f1.write(f"Data gry:{datetime.datetime.now()}\n"
                         f"Poziom trudności: {self.difficulty}\n"
                         f"Liczba prób: {self.temp_att}\n"
                         f"Przegrana\n\n")
            print("Wynik zapisany\n")

    def play(self):
        self.attempts = self.temp_att
        word = self.dict.choose_word(self.difficulty)
        if word == 0:
            exit(1)
        while self.attempts > 0:
            print("Zgaduj")
            user = str(input())
            if not self.val.check_word(user):
                print("Podane słowo nie jest izogramem")
            else:
                self.bull_cow_count(user, word)
                if self.win(self.stat.bulls, word) == 1:
                    break
                else:
                    self.stats(self.attempts, self.stat.bulls, self.stat.cows)
        if self.attempts == 0:
            print("Przegrałeś")
