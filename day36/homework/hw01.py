# ვქმნით სიტყვების სიას
words = ["კომპიუტერი", "ფანჯარა", "დინოზავრი", "სათამაშო", "პალინდრომი"]

i = 0

for word in words:
    if i % 2 == 0: 
        print(word[::-1])  
    else:
        print(word)  
    i += 1 