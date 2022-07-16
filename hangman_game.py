import random


def select_word(path: str):
    with open(path, "r", encoding="utf-8") as file:
        data = file.read()
        words = data.split()

        word_pos = random.randint(0, len(words) - 1)
        return words[word_pos]


def run():
    lives = 10
    word = select_word("./files/data_hangman_game.txt")
    word_guess_list = ["_" for i in word]

    while True:
        print("¡Adivina la palabra!")
        print("".join(word_guess_list))

        if lives > 1:
            print("\nTe quedan", lives, "vidas\n")
        else:
            print("\nTe queda", lives, "vida\n")

        guess = input("Ingresa una letra o una palabra: ")

        if not guess.isalpha():
            print("Debe ser una letra o una palabra...")
            continue

        if guess == word:
            print("¡Ganaste! La palabra es:", word)
            break

        if guess in word:
            for pos, char in enumerate(word):
                if char == guess:
                    word_guess_list[pos] = guess

        if word == "".join(word_guess_list):
            print("¡Ganaste! La palabra es:", word)
            break

        if lives == 1:
            print("Has perdido...")
            print("La palabra era:", word)
            break

        lives -= 1


if __name__ == "__main__":
    run()
