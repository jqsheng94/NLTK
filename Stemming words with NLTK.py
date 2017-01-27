from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

for w in example_words:
    print(ps.stem(w))

new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text)

print(' '.join([ps.stem(i) for i in words]))

new_text2 = "I am only swimming today whereas he swims everyday"
words2 = word_tokenize(new_text2)

print(' '.join([ps.stem(i) for i in words2]))
