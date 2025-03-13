#6) მომხმარებელს შემოატანინეთ ქულა score და შეინახეთ ცვლადში, როგორც integer.
#შემდეგ, ქულის მიხედვით განსაზღვრეთ შეფასება (grade):
#A – თუ score მეტია 80-ზე
#B – თუ score მეტია 60-ზე
#C – თუ score მეტია 40-ზე
#D – თუ score მეტია 20-ზე
#F – თუ score 20-ზე ნაკლებია

score = int(input("შეიყვანე შენი ქულა აქ: "))
if score > 80:
    print("A")
if score > 60:
    print("B")
if score > 40:
    print("C")
if score < 20:
    print("D")
if score < 20:
    print("F")
