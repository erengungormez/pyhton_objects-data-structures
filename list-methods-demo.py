from operator import index
from re import X


isimler = ['Ada','Yiğit','Hasan','Beril']
yaslar = [1998, 2000, 1998, 1987]
listeler = (yaslar , isimler)

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.

# isimler.append("Cenk")


# 2-  "Sena" değerini listenin başına ekleyiniz.

# isimler.insert(0,"Sena")

# 3-  "Yiğit" ismini listeden siliniz.

# isimler.remove("Yiğit")

# 4-  "Yiğit" isminin indeksi nedir ?

# index = isimler.index("Yiğit")
# print(index)

# 5-  "Beril" listenin bir elemanı mıdır ?

# result = "Beril" in isimler
# print(result)

# 6-  Liste elemanlarını ters çevirin.

# isimler.reverse()
# yaslar.reverse()

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.

# isimler.sort()

# 8-  yaslar listesini rakamsal büyüklüğe göre sıralayınız.

# yaslar.sort()

# 9-  s = "IPhone X,IPhone XR" karakter dizisini listeye çeviriniz.

# s = ["Iphone X" , "Iphone XR"]
# s.append("çalışıyor")
# print(s)

# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir ?
# min = min(yaslar)
# max = max(yaslar)
# print(max,min)

# 11- yaslar dizisinde kaç tane 1998 değeri vardır ?

# print(yaslar.count(1998))

# 12- yaslar dizisinin tüm elemanlarını siliniz.
# yaslar.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

Markalar = []

marka = input("Marka : ")
Markalar.append(marka)

marka2 = input("Marka : ")
Markalar.append(marka2)

marka3 = input("Marka : ")
Markalar.append(marka3)

print(Markalar)

print(yaslar)