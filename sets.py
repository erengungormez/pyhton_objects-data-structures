teams = {'Fenerbahçe', 'Galatasaray' , 'Beşiktaş'}

# print(teams[0])  indekslenemez

for x in teams:
    print(x)
    
teams.add("Barcelona")   #  'add' metoduyla  barcelonayı tek bir eleman şekilde ekle 
teams.update(["Real Madrid" , "PSG" , "Liverpool"])  #  'update' metoduyla liste şeklinde ekle 
teams.remove("PSG")  # 'remove' metoduyla listeden silmeyi gerçekleştirir
teams.pop() # 'pop' ilk elemanı listeden siler
teams.clear() # 'clear' tüm elemanları silmeye yarayan metod    


print(teams)


