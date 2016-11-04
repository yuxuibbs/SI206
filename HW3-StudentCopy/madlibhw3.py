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


# first 150 tokens
tokens = text2[0:149]
print("TOKENS")
print(tokens)
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
print("TAGGED TOKENS")
print(tagged_tokens)

tagmap = {"NN":"a noun",
          "CC":"a coordinating conjunction",
          "VB":"a verb",
          "JJ":"an adjective", 
          "UH":"an interjection"}
substitution_probabilities = {"NN":.15,"CC":.1,"VB":.1,"JJ":.1, "UH":.1}


print("\n\nEND*******")
