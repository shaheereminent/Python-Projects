import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
rn_letters = int(input("How many letters would you like in your password: "))
rn_symbols = int(input("How many symbols would you like: "))
rn_numbers = int(input("How many numbers would you like: "))

password_list = []
final_password = ""

for char in range(0, rn_letters):
    password_list.append(random.choice(letters))

for char in range(0, rn_symbols):
    password_list.append(random.choice(letters))

for char in range(0, rn_numbers):
    password_list.append(random.choice(letters))

random.shuffle(password_list)

for char in password_list:
    final_password += char

print(final_password)