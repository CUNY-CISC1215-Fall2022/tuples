# A Markov text generator.
# It performs an analysis of an existing text, creating a dictionary
# mapping n-gram tuples to list of candidate next words that can be
# chosen randomly.

import random

# For the analysis, we're using a portion of the book Jane Eyre.
# You can go to Project Gutenberg (gutenberg.org) to get free
# public domain books and try the analysis yourself.
infile = open("jane_eyre.txt")

# Step 1: Extract all words from the book in order
words = []
# Iterate through lines in the book
for line in infile:
    line = line.strip()

    line_split = line.split(" ")
    # Iterate through words in the line
    for word in line_split:
        # Each word is appended to the words list individually.
        words.append(word)

# Step 2: Conduct an analysis. Find all pairs of words (a bigram),
# and whichever word comes next. This code uses bigrams. Try modifying
# it for unigrams and trigrams.
# The output dictionary maps a tuple of words to a list of candidate words.
#
# For example, the sentence "the cat in the hat" would be analyzed as:
#   {
#       ("the", "cat"): ["in"],
#       ("cat", "in"): ["the"],
#       ("in", "the"): ["hat"]
#   }
#
# If we were using unigrams, the dictionary would look like this:
#   {
#       "the": ["cat", "hat"],
#       "cat": ["in"],
#       "in": ["the"]
#   }
analysis = {}
# Use zip to construct a bigram: two prefixes and a candidate next word
for prefix, prefix2, next in zip(words, words[1:], words[2:]):
    bigram = (prefix, prefix2)

    if bigram not in analysis:
        analysis[bigram] = []

    analysis[bigram].append(next)


# Choose an initial random prefix and add it to the output
prefix = random.choice(list(analysis.keys()))
output = [prefix[0], prefix[1]]

# Generate 50 new words:
for i in range(50):
    # Select a list of candidates from the analysis dictionary
    candidates = analysis[prefix]
    # Pick one at random
    next = random.choice(candidates)
    # Add it to the output and construct a new prefix
    output.append(next)
    prefix = (prefix[1], next)

# Print all the output
print(" ".join(output))