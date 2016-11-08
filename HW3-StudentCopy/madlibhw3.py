# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text


# code based on madlib_generatorP3.py
print("START*******")


import nltk 
from nltk.book import text2
from nltk import word_tokenize,sent_tokenize
import random


# first 150 tokens
tokens = text2[0:149]
tagged_tokens = nltk.pos_tag(tokens)
print("Original text:", " ".join(tokens))

tagmap = {"NN":"a noun",
          "CC":"a coordinating conjunction",
          "VB":"a verb",
          "JJ":"an adjective", 
          "UH":"an interjection"}
substitution_probabilities = {"NN":.15,"CC":.1,"VB":.1,"JJ":.1, "UH":.1}


def spaced(word):
    if word in [",", ".", "?", "!", ":"]:
        return word
    else:
        return " " + word

final_words = []


for (word, tag) in tagged_tokens:
    if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
        final_words.append(spaced(word))
    else:
        new_word = input("Please enter %s:\n" % (tagmap[tag]))
        final_words.append(spaced(new_word))

print("New text:", " ".join(final_words))


print("\n\nEND*******")
