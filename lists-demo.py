 # 1-  "Samsung S5,Samsung S6,Samsung S7,Samsung S8" elemanlarına sahip bir liste oluşturunuz.

from unittest import result


telefonlar = ["Samsung S5","Samsung S6","Samsung S7","Samsung S8"]

# 2-  Liste Kaç elemanlıdır ?
# result = len(telefonlar)
# 3-  Listenin ilk ve son elemanı nedir ?
# result = telefonlar[0]
# result2 = telefonlar[-1]


# 4-  "Samsung S5" değerini "Samsung S9" ile değiştirin.

# telefonlar[0] = "Samsung S9"

# result = telefonlar

# 5-  "Samsung S6" listenin bir elemanı mıdır ?

# result = "Samsung S6" in telefonlar

# 6-  Listenin -3 indeksindeki değer nedir ?

# result = telefonlar[-3]


# 7-  Listenin ilk 2 elemanını alın.

# result = telefonlar[0:3]

# 8-  Listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" değerlerini ekleyin.

# telefonlar[-1] = "Samsung S10"
# telefonlar[-2] = "Samsung S9"

# result =telefonlar

# 9-  Listenin üzerine "IPhone X" ve "IPhone XR" değerlerini ekleyin.

# result = telefonlar + ["Iphone x" , "Iphone XR"]

# 10- Listenin son elemanını silin.

# del telefonlar[-1]
# result = telefonlar

# 11- Liste elemanlarını tersten yazdırınız.

# result = telefonlar[::-1]

# 12- Aşağıdaki verileri bir liste içinde saklayınız.

   # studentA: Eren Güngörmez 2004 , (90,80,100)
   # studentB: Emirhan Güngörmez 2001 , (70, 60, 95)
   # studentC: Yiğit Güngörmez 2020 , (85, 90 ,100)
   
studentA = ["Eren" , "Güngörmez" , 2004, [90,80,100]]
studentB = ["Emirhan" , "Güngörmez", 2001, [70,60,95]]
studentC = ["Yiğit", "Güngörmez" ,2020, [85,90,100]]
 

# 13- Liste elemanlarını ekrana yazdırınız.

# result = studentA[0]

result = f"{studentA[0]} {studentA[1]} {2022-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)
