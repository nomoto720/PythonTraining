import codecs
text=input('何を記録しますか?>>')
with codecs.open('diary.txt','a','utf-8') as file:
    file.write(text+'\n')
