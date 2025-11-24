import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

re_order_letters = random.sample(letters, len(letters))
re_order_numbers = random.sample(numbers, len(numbers))
re_order_symbols = random.sample(symbols, len(symbols))

print("Welcome to the PyPassword Generator!")
rn_letters = int(input("How many letters would you like in your password: "))
rn_symbols = int(input("How many symbols would you like: "))
rn_numbers = int(input("How many numbers would you like: "))

password_merge = []
password_str_convert = ""

# Adding Re-Order Strings to Password (Password Merge)
for letter in range(0, rn_letters + 1):
    password_merge.append(re_order_letters[letter])

# Adding Re-Order Number to Password (Password Merge)
for number in range(0, rn_numbers + 1):
    password_merge.append(re_order_numbers[number])

# Adding Re-Order Symbols to Password (Password Merge)
for symbol in range(0, rn_symbols + 1):
    password_merge.append(re_order_symbols[symbol])

# Re-Ordering Collected Password (Password Merge)
re_order_password_merge = random.sample(password_merge, len(password_merge))

# Adding Re-Ordered Password to Final Password
for char in re_order_password_merge:
    
    password_str_convert += char
    
print(password_str_convert)
    
