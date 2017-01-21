# Made by wdhg
# github.com/wdhg

from string import ascii_letters, punctuation
from random import choice
import argparse

# Constant word types
NOUN, ADJECTIVE, VERB, ADVERB = "n", "a", "v", "A"
# Argument parsing
parser = argparse.ArgumentParser(description="A Memorable Password Generator")
parser.add_argument("-s",
                    "--struct",
                    nargs="+",
                    type=str,
                    default = [ADJECTIVE, NOUN, VERB, ADVERB],
                    choices = NOUN + ADJECTIVE + VERB + ADVERB,
                    required=False,
                    help="The structure of the password")
parser.add_argument("-c",
                    "--char",
                    dest = "use_char",
                    default = False,
                    action = "store_true",
                    help = "Generate a password with only characters")
parser.add_argument("-l",
                    "--length",
                    type = int,
                    default = 16,
                    help = "Length of random password")
parser.add_argument("-p",
                    "--punctuation",
                    dest = "use_punct",
                    default = False,
                    action = "store_true",
                    help = "Use punctuation")
# Getting words
nouns = open("nouns.txt").read().split()
adjectives = open("adjectives.txt").read().split()
verbs = open("verbs.txt").read().split()
adverbs = open("adverbs.txt").read().split()

def generate_char(length, use_punct=False):
    if use_punct:
        letters = ascii_letters + punctuation
    else:
        letters = ascii_letters
    return "".join(choice(letters) for _ in range(length))

def generate_word(structure):
    password = ""
    for word_type in structure:
        if word_type == NOUN:
            password += choice(nouns)
        elif word_type == ADJECTIVE:
            password += choice(adjectives)
        elif word_type == VERB:
            password += choice(verbs)
        elif word_type == ADVERB:
            password += choice(adverbs)
    return password

def main():
    args = parser.parse_args()

    if args.use_char:
        password = generate_char(args.length, args.use_punct)
    else:
        password = generate_word(args.struct)

    print(password)

if __name__ == "__main__":
    main()