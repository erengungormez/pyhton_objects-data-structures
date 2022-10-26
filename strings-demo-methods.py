import http
from re import T


website = "http://www.erengungormez.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
# basla = "   Hello World   "
# sonuc = basla.strip()

# 2- 'www.erengungormez.com' içindeki erengungormez bilgisi haricindeki her karakteri silin.

# sonuc ="www.erengungormez.com".strip("w.com")


# 3- 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın.

# sonuc = kursAdi.lower()

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a')) kaç tane olduğunu sayıyor

# sonuc = website.count("e") ()

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?

# sonuc = website.startswith("www") False
# sonuc = website.startswith("http") True
# sonuc = website.endswith("com") True

# 6- 'website' içinde '.com' ifadesi var mı?

# sonuc = website.find(".com") True


# 7- 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

# sonuc = kursAdi.isalpha() False
# sonuc = kursAdi.isdigit() False

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

# islem = "contents"
# sonuc = islem.center(50,"*")


# 9- 'kursAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

# sonuc = kursAdi.replace(" ","-")

# 10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin

# result = "Hello World"
# sonuc = result.replace("World", "There")

# 11-'kursAdi' karakter dizisini boşluk karakterlerinden ayırın.

# sonuc = kursAdi.split()

# print(sonuc)