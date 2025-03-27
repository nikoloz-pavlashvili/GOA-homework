#7) მომხმარებელს შემოაყვანინეთ წინადადება, შემდეგ for ციკლისა და პირობითი განცხადებების საშვალებით დაბეჭდეთ ჯერ ხმოვნების, შემდეგ კი თანხმოვნების რაოდენობა (ხმოვნებად ჩათვალეთ სიმბოლოები: a, e, i, o, u ხოლო სხვა ყველა თანხმოვნად)

sentence = input("შეიყვანეთ წინადადება: ")

xmovani = "aeiou"

xmovnebis_raodenoba = 0
tanxmovnebis_raodenoba = 0

for char in sentence.lower():
    if char.isalpha(): 
        if char in xmovani:
            xmovnebis_raodenoba += 1
        else:
            tanxmovnebis_raodenoba += 1

print("ხმოვნების რაოდენობა:", xmovnebis_raodenoba)
print("თანხმოვნების რაოდენობა:", tanxmovnebis_raodenoba)