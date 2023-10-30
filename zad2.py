def load_items():
    items = {}
    with open('prices.txt', 'r') as file:
        for line in file:
            name, quantity, price = line.split()
            items[name] = {'quantity': int(quantity), 'price': float(price)}
    return items

def print_items(items):
    for name, info in items.items():
        print(f'Название: {name}, Количество: {info["quantity"]}, Цена за ед.: {info["price"]}')

def add_to_cart(items, cart):
    print_items(items)
    name = input("Введите название товара, который вы хотите добавить в корзину: ")
    if name in items:
        quantity = int(input("Введите количество товара, которое вы хотите добавить в корзину: "))
        if quantity <= items[name]['quantity']:
            if name in cart:
                cart[name]['quantity'] += quantity
            else:
                cart[name] = {'quantity': quantity, 'price': items[name]['price']}
            items[name]['quantity'] -= quantity
        else:
            print("Недостаточное количество товара на складе.")
    else:
        print("Товар не найден.")

def calculate_total(cart):
    total = 0
    for info in cart.values():
        total += info['quantity'] * info['price']
    return total

def main():
    items = load_items()
    cart = {}
    while True:
        print("1. Добавить товар в корзину")
        print("2. Рассчитать общую стоимость заказа")
        print("3. Выход")
        choice = input("Введите ваш выбор: ")
        if choice == '1':
            add_to_cart(items, cart)
        elif choice == '2':
            total = calculate_total(cart)
            print(f'Ваш заказ: {cart}')
            print(f'Общая стоимость заказа: {total}')
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")
main()
