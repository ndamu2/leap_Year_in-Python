year=int(input("what year do you want to start with?   "))
years=int(input("how many years do want to check?      "))
year +=0
for i in range (year, year+years):
    if year % 4 == 0:
        print(str(i)+"this is a leap year")
        i +=1
    else:
        print (str(i)+"isnt leap year")
        i +=1
