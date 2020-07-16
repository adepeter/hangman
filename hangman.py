import random
from typing import Any, List


def to_string(list_obj: List) -> str:
    # convert a list to a string
    return ''.join(list_obj)


def to_list(string_obj: str) -> List:
    # convert a string to list
    return list(string_obj)


def get_random_word() -> str:
    # return a random shuffle of any word in the list to kick up game
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


def obfuscate_secret(secret_word: str, give_hint=False, replacer: str="*") -> str:
    """Use random module to strip out some letters from secret word.
    Returns an obfuscated word
    which hidden characters can be replaced in replacer parameter
    EG of returned secret could contain a mixture of letters and secrets
    Or totally hidden.
    """
    rand = random.randint(1, len(secret_word))
    if give_hint is False:
        secret_word = len(secret_word) * '*'
    for k in range(rand):
        to_string = random.choice(str(secret_word))
        secret_word = secret_word.replace(to_string, replacer)
    return secret_word

random_words_bank = get_random_word()
secret_text = obfuscate_secret(random_words_bank)
unscramble_secret = to_list(secret_text)

print('\n'.join(["---welcome to my hangman game---", "Please proceed with your name"]))

print()
username = input("Enter your name here please: ")

print()

print(f"The length of the secret letter you are about to \
guess is %d long and you have a total of 10 \
trials before the game ends." % len(secret_text))

print(f"Below is the obfuscated text {secret_text}")

start = 0
stop = 10
while start < stop:
    guess = input("Enter letter: ")
    start += 1
    if guess not in random_words_bank:
        message = f"'{guess}' doesnt match any character in the secret word"
        message += f"\tYou have {stop-start} chances left"
        print(message)
        if start == stop:
            print(f"Game stopped as you didnt hit the target after {stop} trials")
            break
    elif guess in secret_text:
        print(f"Guess is already among secret character. {stop-start} chances left")
        start = start
    else:
        if guess in random_words_bank:
            print(f"Hurray, you just got a guess!!! {stop-start} chances left")
            for k, v in enumerate(random_words_bank):
                if random_words_bank[k] == guess:
                    unscramble_secret[k] = guess
                    print('Hint: %s' % to_string(unscramble_secret))
            if "*" not in unscramble_secret and \
                    (to_string(unscramble_secret) == random_words_bank):
                print(f"Game successfully won after {start} trial")
                print("Secret word was %s" % random_words_bank)
                break
