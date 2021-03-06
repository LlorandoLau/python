import nltk,re,codecs
from nltk import *
def content_fraction(text):
    stopwords=nltk.corpus.stopwords.words('english')
    content=[w for w in text if w.lower() not in stopwords]
    return content

def name(text):
    names=nltk.corpus.names.words('male.txt')
    names=names+nltk.corpus.names.words('female.txt')
    content=[w for w in text if w not in names]
    return content

#提取英文单词并统计词频 消除标点
punctuation = '!,_~;:?."\''
def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation),'',text)
    return text.strip().lower()
f=codecs.open('The Fellowship of the Ring.txt','r','Utf-8')
x=f.read()
to=nltk.word_tokenize(x)
text=nltk.Text(to)
text.dispersion_plot(['Frodo','Gandalf','Bilbo','Strider','Sam'])

