import nltk

import pandas as pd
import re
from pymorphy2 import MorphAnalyzer
from nltk.corpus import stopwords
nltk.download('stopwords')


#nltk.download('stopwords')
print(1)
qw = pd.read_excel('321.xlsx')
df=qw.description
print(2)
patterns = "[A-Za-z0-9!#$%&'()*+,./:;<=>?@[\]^_`{|}~—\"\-]+"
stopwords_ru = stopwords.words("russian")
morph = MorphAnalyzer()

print(3)
def lemmatize(doc):
    doc = re.sub(patterns, ' ', doc)
    tokens = []
    for token in doc.split():
        if token and token not in stopwords_ru:
            token = token.strip()
            token = morph.normal_forms(token)[0]
            #print(token)
            tokens.append(token)
    if len(tokens) > 2:
        return tokens
    return None
q=[]
k=0
data = df.apply(lemmatize)

qw['ert']=data;
#print(zx)


print(a)
qw.to_excel("32100.xlsx")


# from collections import defaultdict
# word_freq = defaultdict(int)
# for tokens in data.iloc[:]:
#     for token in tokens:
#         word_freq[token] += 1
#
# print(word_freq)