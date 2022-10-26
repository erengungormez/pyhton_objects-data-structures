""" 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içine saklayanız

2- Öğrenci numarısını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin"""


ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci isim: ")
surname = input("öğrenci soyisim: ")
phone = input("telefon no: ")

# ogrenciler[number] = {
#     "ad" : name,
#     "soyad" : surname,
#     "telefon" : phone
# }

ogrenciler.update({
    number : {
        "ad" : name,
        "soyisim" : surname,
        "telefon" : phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci isim: ")
surname = input("öğrenci soyisim: ")
phone = input("telefon no: ")
ogrenciler.update({
    number : {
        "ad" : name,
        "soyisim" : surname,
        "telefon" : phone
    }
})

ogrenciler.update({
    number : {
        "ad" : name,
        "soyisim" : surname,
        "telefon" : phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci isim: ")
surname = input("öğrenci soyisim: ")
phone = input("telefon no: ")
ogrenciler.update({
    number : {
        "ad" : name,
        "soyisim" : surname,
        "telefon" : phone
    }
})

print("*"*50)

print(ogrenciler)

ogrNo = input("öğrenci no: ")

ogrenci = ogrenciler[ogrNo]

print(f"Aradığınız {ogrNo} nolu öğrencinin adı {ogrenci['ad']},  {ogrenci['soyisim']} ve telefononu ise {ogrenci['telefon']}")