"""""
for i in range (1,10):
    if i %2==0:
        print(f"{i} bir çift sayı")
    else:
        print(f"{i} bir tek sayı")

"""""
"""""
#Örnek 14:  1 den 100 e kadar olan sayılardan aynı anda 3 ve 5 e tam bölünen sayıları alt alta yazdıran python kodunu yazınız.
for i in range (1,101):
    if i %3==0 and i%5==0:
        print(i)
"""""
"""""
#Örnek 15:  Klavyeden girilen sayıya kadar olan sayıları alt alta yazdıran python kodunu yazınız.
sayi = int(input("sayı giriniz : "))
k = 1
while k <= sayi:
    print(k)
    k+=1
"""""
""""
#Örnek 17:  Klavyeden girilen bir metnin harflerini alt alta yazdıran python kodunu yazınız.
yazi = str(input("bir kelime yazınız :"))
for i in yazi:
    print(i)
#2.yol
metin=input("Metni Giriniz: ")
sayac=0
while sayac < len(metin):
  print(metin[sayac])
  sayac += 1
"""
""""
#Örnek 18:  Klavyeden girilen iki sayı arasındaki sayıları toplayan python kodunu yazınız.
toplam=0
sayi1=int(input('1. Sayıyı Giriniz: '))
sayi2=int(input('2. Sayıyı Giriniz: '))
for i in range(sayi1+1,sayi2):
      toplam = toplam + i
print("{0} ile {1} arasındaki sayıların toplamı : {2}".format(sayi1,sayi2,toplam))
"""

""""
#Örnek 19:  Klavyeden girilen sayının asal sayı olup olmadığını bulan python kodunu yazınız.
asalSayi= int(input("sayı girin :"))
for i in range(2,asalSayi):
    if  not asalSayi%i ==0:
        print("sayınız {}.Yani asal.".format(asalSayi))
        break
    else:
        print("sayınız {}.Yani asal değil.".format(asalSayi))
        break
#2.yol
sayac=0
sayi=input('Bir Sayı Giriniz: ')
for i in range(2,int(sayi)):
  if(int(sayi)%i==0):
    sayac+=1
    break
if(sayac!=0):
  print("Girilen Sayı Asal Değil")
else:
  print("Girilen Sayı Asal")
"""
""""
#Örnek 20:  Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.
toplam = 0
toplam1= 0
num = int(input("sayı girin : "))
for i in range(1,num):
    if i%2==0:
        toplam = toplam + i
    elif not i%2==0:
        toplam1=toplam1+i
print(f"{num}'a kadar olan çift sayıların toplamı {toplam}.")
print(f"{num}'a kadar olan tek sayıların toplamı {toplam1}.")

#Örnek 25:  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan çift sayıların ortalamasını bulan python kodunu yazınız.
num = int(input("başlangıç sayısını girin : "))
num1 = int(input("bitiş sayısını girin : "))
toplam = 0
çiftSayi = 0
for i in range(num+1,num1):
    if i%2==0:
        toplam +=i
        çiftSayi+=1
        ortalama = toplam/çiftSayi


print("çift sayı ortalaması : {}".format(int(ortalama)))
"""
"""
#Örnek 27:  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan sayıların ortalamasını bulan python kodunu yazınız.
num = int(input("başlangıç sayısını girin : "))
num1 = int(input("bitiş sayısını girin : "))
toplam = 0
adet = 0
for i in range(num+1,num1):
    toplam +=i
    adet+=1
    (ortalama)=int(toplam/adet)
print("ortalama : {}".format(ortalama))
"""
""""
#Örnek 28:  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan sayıların toplamını bulan python kodunu yazınız.
num = int(input("başlangıç sayısını girin : "))
num1 = int(input("bitiş sayısını girin : "))
toplam = 0
for i in range(num+1,num1):
    toplam+=i
print(toplam)
"""
"""
#Örnek 46:  Klavyeden girilen sayıya kadar olan çift sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.
num = int(input("sayı giriniz : "))
toplam = 0
while toplam < num:
    for i in range(0,num):
        if i%2==0:
            toplam+=i
print(toplam)
"""

""""
#ünlü ve ünsüz harf bulma
def ünlüHarf(cümle):
    sayi=0
    for i in cümle:
        if i in "aeıioöuü":
            sayi+=1
    return sayi
def ünsüzHarf(cümle):
    sayi1=0
    for i in cümle:
        if i in "qwrtypğsdfghjklşzxcvbnmç":
            sayi1+=1
    return sayi1
metin=input("cümle girin : ")
print(f"ünlü harf : {ünlüHarf(metin)} ve ünsüz harf : {ünsüzHarf(metin)}")
"""






























































