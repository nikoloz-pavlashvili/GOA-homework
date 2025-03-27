product1 = "apple"
product2 = "banana"
product3 = "cherry"


products = [product1, product2, product3]


new_product1 = input("შეიყვანეთ ახალი პროდუქტი 1: ")
new_product2 = input("შეიყვანეთ ახალი პროდუქტი 2: ")

# სიაში ბოლო ორი პროდუქტის დამატება
products(new_product1)
products(new_product2)


index = int(input("რომელ პროდუქტს გსურთ? (შეიყვანეთ ინდექსი): "))


print(f"თქვენ აირჩიეთ:")


new_product = input("ჩაანაცვლეთ პროდუქტი ახალი პროდუქტით: ")
products[index] = new_product


print("განახლებული პროდუქტის სია:")
