# For the first time downloand, include the following two lines in the script
#import  nltk
#nltk.download()
# After that, a GUI will pop up. Choose to download "all" for all packages, and then click 'download.'
# This will give you all of the tokenizers, chunkers, other algorithms, and all of the corpora. If space is an issue, you can elect to selectively download everything manually.
#  The NLTK module will take up about 7MB, and the entire nltk_data directory will take up about 1.8GB, which includes your chunkers, parsers, and the corpora.

from nltk.tokenize import sent_tokenize, word_tokenize

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

print(sent_tokenize(EXAMPLE_TEXT))

print(word_tokenize(EXAMPLE_TEXT))
