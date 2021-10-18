import random

words_file = open("words.txt", "r")
# splitlines removes the new lines, so ["act\n","word\n"] is instead ["act","word"]
words_list = words_file.read().splitlines()

# Select a random word then seperate the characters into a list of '_'
selected_word = words_list[random.randint(0, len(words_list)-1)]
encrypted_word = list("_"*len(selected_word))
wrong_guesses_list = []
max_wrong_guesses = 8


def print_encrypted_word():
    encrypted_word_as_string = ""
    for c in encrypted_word:
        encrypted_word_as_string += c
    print(encrypted_word_as_string)


# find all instance of char and return in a nice list (Not meant to be used for longer than 1 character)
def find_all(u_str, char):
    last_index = 0
    index_list = []
    found_index = u_str.find(char, last_index)
    while found_index != -1:
        last_index = found_index + 1
        index_list.append(found_index)
        found_index = u_str.find(char, last_index)
    return index_list


def guess(user_char):
    if user_char in wrong_guesses_list:
        print("You have already guessed this, try again.")
        return

    found_indexes = find_all(selected_word, user_char)

    if len(found_indexes) > 0:
        for i in found_indexes:
            encrypted_word[i] = user_char
    else:
        wrong_guesses_list.append(user_char)

    wrong_guesses_list_as_string = ""
    for c in wrong_guesses_list:
        wrong_guesses_list_as_string += c + ","

    print("Wrong guesses: " + wrong_guesses_list_as_string)
    print_encrypted_word()


print()
print_encrypted_word()
print("You have " + str(max_wrong_guesses) + " wrong guesses.")

game_won = False
user_input = ""
while len(wrong_guesses_list) < max_wrong_guesses and not game_won:
    user_input = input("\nPlease enter your guess: ")

    if user_input.lower() == "quit":
        break

    if len(user_input) != 1:
        print("Invalid input.")
        continue

    print()
    guess(user_input)

    if "_" not in encrypted_word:
        game_won = True


print()
if game_won:
    print("Game complete, you win!")
else:
    print("Game lost :(")
print("The word was: " + selected_word)

