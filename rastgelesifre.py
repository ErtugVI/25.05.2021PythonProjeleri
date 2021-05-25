from random import choice

karakterler = ["a","b","c","ç","d","e","f","g","h","A","B","C","Ç","D","E","F","G","H",0,1,2,3,4,5,6,7,8,9]

karaktersayisi = int(input("Şifrenizin kaç karakterli olacağını belirleyiniz."))

sifre = ""

for i in range(karaktersayisi):
    sifre += str(choice(karakterler))

print(sifre)
