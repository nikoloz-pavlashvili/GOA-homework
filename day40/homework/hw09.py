word = input("შეიყვანეთ ნეისმიერი სიტყვა")

position = word.find('a')

if position != -1:
    print("პირველი 'a' არის პოზიცია", position)
else:
    print("'a' ამ სიტყვაში არ არის პოზიცია")
