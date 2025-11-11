def get_total(products):
    total = 0
    for price in products.values():
        total += price
    return total

products = {}
n = int(input("Введите количество товара: "))

for i in range(1, n + 1):
    name = input(f"Введите название товара {i}: ")
    price = int(input(f"Введите цену товара {i}: "))
    products[name] = price

print(f"Всего товаров: {len(products)}")
print(f"Общая сумма: {get_total(products)}")