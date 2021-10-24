replacements = (',',';', ':', '. ', '!', '(', ')', '"', "'", '\\', '/', '[', ']',"''",'  '," .",'.')
word = input()

for i in replacements:
    word = word.replace(i,' ')
    
word = word.split()


