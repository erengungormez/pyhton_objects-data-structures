from operator import index


message = "Hello There. My name is Eren Güngörmez"

# message = message.upper() ("upper" tüm harfleri büyük yazdırır.)
# message = message.lower() ("lower" tüm harfleri küçük yazdırır.)
# message = message.title() ("title" tüm kelimelerin baş harfi büyük harfler başlar.)
# message = message.capitalize() ("capitalize" cümlede sadece baş kelimenin ilk harfini büyük yazar.)
# message = message.strip() ("strip" cümlenin başında veya sonunda boşluk varsa ortadan kaldırır.)
# message = message.split() ("split" her boşluktan itibaren kelimelere ayırır)
# message = message.split(".") (noktalardan itibaren ayırır***)

# index = message.find("Eren") ("find" bir cümlede bir kelime bulmak istiyorsak)
# print(index) (Eren kelimesinin ilk harfinin hangi indeksde olduğunu belirtir negatif bir sayı çıkarsa o kelime cümlede yoktur)

# message = message.replace("Eren","Yiğit Kağan") ("replace" bir karakter yerine başka bir karakteri eklememizi sağlar)
# message = message.center(50) ("center" 50 satırlık bir alan belirler ve cümleyi bu alana ortalar)

print(message)
# print(message[2]) (split metoduyla ayırdığımız kelimelere indeks numarasıyla ulaşabiliriz)
