num = [3, 5, 7, 56, 15, 22, 19, 6, 13, 4, 2, 12, 18, 11, 20]  
even = 0 
odd = 0  
for number in num:
    if number % 2 == 0: even += 1 
    else: odd += 1 
print("even:", even)
print("odd", odd)