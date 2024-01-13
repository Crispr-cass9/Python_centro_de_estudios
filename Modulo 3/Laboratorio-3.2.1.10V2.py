user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in ["A", "E", "I", "O", "U"]:
        continue
    print(letter)

