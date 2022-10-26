numbers = [1, 10 , 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "a", "s"]

# val = min(numbers)
# val = max(numbers)
# val = max(letters)   #alfabetik olarak max min değerler veriyor.
# val = min(letters)

# val = numbers[3:6]

# numbers[3] = 2004

# numbers.append(49) #en sona bir şey eklemek istediğimizde "append"
# numbers.append(233573243574)
# numbers.insert(1,2004) # seçtiğimiz indeks numarası yerine bir şey eklemek istediğimiz zaman "insert"
# numbers.pop(1) # seçili indeksden bir şey silmek istediğimiz zaman "pop"
# numbers.remove(5) # verilen kelimeyi bulur ve siler. "remove"
# numbers.sort() #sayıarı sıralar "sort"
# letters.sort() # alfabetik olarak sıralar
# numbers.reverse() # tam tersine çevirir.
# letters.reverse()


print(len(numbers))
print(len(letters))

print(numbers.count(10))
print(letters.count("a")) # a harfini bulur ve kaç tane olduğunu yazdırır

numbers.clear()

print(numbers)

