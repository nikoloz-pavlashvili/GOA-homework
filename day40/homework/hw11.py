text = "This is a sample string for testing"

word = input("შეიყვანე ნებისმიერი სიტყვა")

position = text.find(word)

if position != -1:
    print("პოზიცია არის ეს", position)
else:
    print("word not found")
