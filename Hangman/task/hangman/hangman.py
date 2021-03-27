import random


def main_menu():
    while True:
        command = input('Type "play" to play the game, "exit" to quit:')

        if command == 'play':
            return init_game()
        if command == 'quit':
            return None


def init_game(words=('python', 'java', 'kotlin', 'javascript'), lifes_counter=8):
    return game(random.choice(words), lifes_counter)


def is_input_letter_valid(letter):
    if len(letter) > 1:
        print("You should input a single letter")
        return False

    if not letter.isascii() or not letter.islower():
        print("Please enter a lowercase English letter")
        return False
    return True


def game(word, lifes_counter):
    guessed_word = '-' * len(word)
    guessed_letters = set()

    def is_letter_guessed(letter):
        if letter in guessed_letters:
            print("You've already guessed this letter")
            return False

        guessed_letters.add(letter)

        if letter not in word:
            print("That letter doesn't appear in the word")
            lifes_counter_decrease()
            return False

        guessed_word_change()
        return True

    def guessed_word_change():
        nonlocal guessed_word
        guessed_word = ''.join([i if i in guessed_letters else '-' for i in word])

    def lifes_counter_decrease():
        nonlocal lifes_counter
        lifes_counter -= 1

    def is_word_guessed():
        if '-' not in guessed_word:
            print(f"\n{word}\nYou guessed the word!\nYou survived!")
            return True

        return False

    def game_process():
        print("H A N G M A N")
        while lifes_counter > 0:
            letter = input(f"\n{guessed_word}\nInput a letter:")

            if is_input_letter_valid(letter) \
                    and is_letter_guessed(letter) \
                    and is_word_guessed():
                break

        else:
            print("You lost!")

    return game_process()


if __name__ == '__main__':
    main_menu()
