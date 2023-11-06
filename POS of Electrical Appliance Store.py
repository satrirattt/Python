items = []  # Store product items

def add_item():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter the number of products you want to add to the stock: "))

    new_item = {
        "name": name,
        "price": price,
        "stock": stock,
        "sold_quantity": 0
    }

    items.append(new_item)
    print("\nThe product has been added to the stock!")
    print(f"Added product: {name}, Price: {price}, Stock: {stock}\n")
    return new_item

def Product_stock():
    print("Products in stock:")
    for item in items:
        print(f"Name: {item['name']}")
        print(f"Price: {item['price']}")
        print(f"Stock: {item['stock']}\n")

def make_sale():
    name = input("Product name to sell: ")
    num_of_product = int(input("Number of products you want to sell: "))

    found_product = False
    for item in items:
        if item["name"] == name:
            if item["stock"] >= num_of_product:
                item["stock"] -= num_of_product
                item["sold_quantity"] += num_of_product
                print(f"Sold product: {name}, Price: {item['price']}, Amount: {num_of_product}")
                found_product = True
                break

    if not found_product:
        print("Product not found.")
    print()

def Generate_bill():
    print("Bill:")
    print("-------------------------------------------")
    print(":Product            Price           Total :")
    print("-------------------------------------------")
    total_bill = 0

    for item in items:
        if item['sold_quantity'] > 0:
            total_item_price = item['price'] * item['sold_quantity']
            total_bill += total_item_price
            print(f":{item['name']}\t\t   {item['price']:.2f}\t   {total_item_price:.2f}:")

    print("-------------------------------------------")
    print(f"Total: {total_bill:.2f} Bath\n")

while True:
    print("=======================================")
    print(":  POS of Electrical Appliance Store  :")
    print("=======================================")
    print(":1. Add a product to the stock        :")
    print(":2. Product stock                     :")
    print(":3. Make a sale                       :")
    print(":4. Generate a bill                   :")
    print(":5. Exit                              :")
    print("=======================================")
    print()
    choice = int(input("Enter your choice: "))
    print()

    if choice == 1:
        add_item()
        
    elif choice == 2:
        Product_stock()
        
    elif choice == 3:
        make_sale()

    elif choice == 4:
        Generate_bill()
        
    elif choice == 5:
        print("Exit Program...")
        break
