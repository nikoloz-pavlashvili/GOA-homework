start = int(input("shemoiyvane pirveli ricxvi"))
end = int(input("shemoiyvane bolo ricxvi"))


if end < start:
    print("ricxvi")
else:
    sum = 0  
    print("ricxvi")
    
    for i in range(start, end + 1):  
        print(i)
        sum += i
    
    print("all:", sum)
