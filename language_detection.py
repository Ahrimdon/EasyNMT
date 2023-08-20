from easynmt import EasyNMT

model = EasyNMT('opus-mt')

#Translate several sentences to English
sentences = ['Dies ist ein Satz in Deutsch.',   #This is a German sentence
             '这是一个中文句子',    #This is a chinese sentence
             'Esta es una oración en español.'] #This is a spanish sentence

print(model.translate(sentences, target_lang='en'))