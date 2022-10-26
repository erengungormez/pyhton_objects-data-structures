# key : value  // anahtar : değer

# 16 => bursa 34 => istanbul

# sehirler = ["bursa" , "istanbul"]

# plakalar = [16 , 34]

# print(plakalar[sehirler.index("bursa")])   // zor olan yöntem 


# ________________________________________________________________________________________


# plakalar = { "bursa" : 16 , "istanbul" : 34}

# print(plakalar["bursa"])
# print(plakalar["istanbul"])

# plakalar["erzurum"] = 25
# plakalar["bursa"] = "selam eren :)))"

# print(plakalar["erzurum"])

# print(plakalar)

# ________________________________________________________________________________________

users = {
    "erengungormez" : {
        "age" : 18,
        "roles" : ["admin" , "member"],
        "email" : "eren@gmail.com",
        "adress" : "bursa",
        "phone" : 2222222
    },
    "yiğitkağan" : {
        "age" : 2,
        "roles" : [ "member"],
        "email" : "yiğit@gmail.com",
        "adress" : "bursa",
        "phone" : 2222222
    }

}

print(users["erengungormez"]["roles"][0])