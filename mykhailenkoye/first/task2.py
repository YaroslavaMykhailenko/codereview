'''
Вивести на екран слова,що починаються з великої літери(з довільного тексту)
'''
my_text ='Який-небудь текст. Текст є довільним'
my_text = my_text.split()
index_text =0

while index_text<len(my_text):
    my_text[index_text] = my_text[index_text].upper()
index_text +=1

print(my_text)
