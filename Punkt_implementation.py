import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer

def implementation(filename):
    f = open(filename, 'r')
    text = f.read()
    ends = []
    for start, end in PunktSentenceTokenizer().span_tokenize(text):
        ends += [end]
    return ends