import glob
import bagofwords

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
temp= raw_input("Search It.")
#query=temp.strip().split(' ')  
stop_words = set(stopwords.words('english'))
 
word_tokens = word_tokenize(temp)
 
filtered_sentence = [w for w in word_tokens if not w in stop_words]
 
filtered_sentence = []
 
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
 
path = '/path/to/html/file/*.html'
files=glob.glob(path)
for file in files:
     bagofwords.assign(file,filtered_sentence)
     #print(file)

bagofwords.rst()
