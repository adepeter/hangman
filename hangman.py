import random
from typing import Any, List


def to_string(list_obj: List) -> str:
    return ''.join(list_obj)


def to_list(string_obj: str) -> List:
    return list(string_obj)


def get_random_word() -> str:
    secret_words = [
        "oluwaseun",
        "peter",
        "wap",
        "yahoo",
        "youtube",
        "programming",
        "django",
        "strawberry"
    ]
    return random.choice(secret_words)


def obfuscate_secret(secret_word: str, replacer: str="*") -> str:
    rand = random.randint(1, len(secret_word))
    for k in range(rand):
        to_string = random.choice(str(secret_word))
    secret_word = secret_word.replace(to_string, replacer)
    return secret_word

random_words_bank = get_random_word()
secret_text = obfuscate_secret(random_words_bank)
unscramble_secret = to_list(secret_text)

print('\n'.join(["---welcome to my hangman game---", "Please proceed with your name"]))

print()
username = input("Enter your name here pls: ")

print()

print(f"The length of the secret letter you are about to \
guess is %d long and you have a total of 10\
trials before the game ends." % len(secret_text))

print(f"Below is the obfuscated text {secret_text}")

start = 0
stop = 10
while start < stop:
    guess = input("Enter letter: ")
    start += 1
    if guess not in random_words_bank:
        message = f"'{guess}' doesnt match any character in the secret word"
        message += f"You have {stop-start} chances left"
        print(message)
    elif guess in secret_text:
        print(f"Guess is already among secret character. {stop-start} chances left")
    else:
        if guess in random_words_bank:
            print("Hurray, you just got a guess")
            for k, v in enumerate(random_words_bank):
                if random_words_bank[k] == guess:
                    unscramble_secret[k] = guess
            if "*" not in unscramble_secret and \
                    (to_string(unscramble_secret) == random_words_bank):
                print(f"Game successfully won after {start} trial")
                print("Secret word was %s" % random_words_bank)
                break
        else:
            print(f"Game stopped as you didnt hit the target after {stop} trials")
