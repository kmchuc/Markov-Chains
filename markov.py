"""Generate Markov text from text files."""
import random
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    f = open(file_path, 'r')
    f = f.read()

    #file_path.close()
    return f

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here

    list_of_words = text_string.split()

    i = 0
    for word in list_of_words:
        if i < (len(list_of_words) - 2):
            second_word = list_of_words[i+1] 
            third_word = list_of_words[i+2] 
            key = (word, second_word)

            if (word, second_word) in chains:
                chains[(key)].append(third_word)
            
            else:
                chains[(key)] = [third_word]
                i += 1
    
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
   # values = []

    # your code goes here

    key_list = list(chains.keys())

    length = len(key_list)
   
    for x in range(length):
        rand_index = random.randint(0, length)

    if len(words) == 0:
        random_key = key_list[rand_index]
        first_word = random_key[0]
        scnd_word = random_key[1]
        
        words.extend([first_word, scnd_word])
        print(words)
        values = chains[(words[-2], words[-1])]
        print(values)

    # #while True:
    # for key in key_list:
    #     print(key)
    #     if chains[key] == values:
    #         print("reached if clause")
    #         words = our_string.split(" ")
            
    #         values = chains[words[-2], words[-1]]
            
    #         new_value = choice(values)
    #         our_string = our_string + " " + new_value
        
    # return our_string


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

print(chains)
# Produce random text
random_text = make_text(chains)

print(random_text)
