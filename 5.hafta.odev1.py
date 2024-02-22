
#1
def daire_alani(alan):
    pi=int(input("pi degerini giriniz:"))
    r=int(input("r degerini giriniz:"))
    alan = pi * r ** 2
    return alan
alan=daire_alani(1)
print(alan)


#2

def faktoriyel(N):
    sonuc=1
    for i in range(1,N+1):
        sonuc=sonuc*i
    return sonuc
girilen_sayi = int(input("Bir sayı girin: "))
deger = faktoriyel(girilen_sayi)
print(girilen_sayi,"!=", deger)


#3
def yas(dogum_yili):
    yasi=2024-dogum_yili
    return yasi
dogum_yili=int(input("lutfen dogum yilinizi giriniz:"))
yasi=yas(dogum_yili)
print(f"Su an {yasi} yasindasiniz")

#4
def emekli(dogum_yili, isim):
    yas=2024- dogum_yili
    if yas >=65:
        print("Emeklisiniz.")
    else:
        kalan_yiliniz=65 - yas
        print("{isim} emeklilik icin {kalan_yiliniz} yil kaldi!")
dogum_yili = int(input("Doğum yılını girin: "))
isim = input("Adınızı girin: ")
emekli_durumu = emekli(dogum_yili, isim)
print(emekli_durumu)