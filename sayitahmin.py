import random
aralık = random.randint(1,100)

for i in range(10):
    tahmin = int(input("Bir sayı tahmin ediniz. Doğru cevabı tahmin etmek için 5 hakkınız bulunmaktadır."))
    if(aralık > tahmin):
        print("Sayınızı yükseltiniz.")
    elif(aralık == tahmin):
        print("Tebrikler doğru sayıyı buldunuz!")
    else:
        print("Sayınızı düşürünüz.")

if(aralık != tahmin):
    print("Doğru sayıyı bulamadınız.")            

