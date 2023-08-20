from easynmt import EasyNMT

model = EasyNMT('opus-mt')

# 1. Read the contents of a text file to replace the `document` variable
with open('Server - Copy.srt', 'r', encoding='utf-8') as file:
    document = file.read()

# Translate the document to Spanish
translation = model.translate(document, target_lang='es')

# 2. Write the translated output to a new file called `result.txt`
with open('Server_es.srt', 'w', encoding='utf-8') as output_file:
    output_file.write(translation)