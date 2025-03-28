colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]

index = int(input("შეიყვანეთ ფერი (0-დან 3-მდე): "))  
if 0 <= index < len(colors):
    new_color = input("შეიყვანეთ ახალი ფერი: ")
    colors[index] = new_color 
    print("განახლებული სია:", colors)
else:
    print("არასწორი ინდექსი! გთხოვთ, შეიყვანოთ 0-დან 3-მდე რიცხვი.")