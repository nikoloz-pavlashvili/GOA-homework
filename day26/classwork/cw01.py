#2) შექმენით პროგრამა, რომელშიც მომხმარებელს შემოატანინებთ ქულას, შემდეგ კი if განხადების საშვალებით გამოუტანთ 2 შესაძლო შედეგს: "You have passed" ან "You failed"

score=input('enter your score')
if int (score)>=100:
    print('you passed')
if int(score)< 100:
    print('you failed')
