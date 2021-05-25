sayi = int(input("Bir sayı giriniz."))

knm = 0

for i in range(2, sayi):
    if sayi % 2 == 0:
        knm = knm +1

if knm > 0:
    print("Girdiğiniz sayı asal değildir.") 
else:
     print("Girdiğiniz sayı asaldır.")       