carts = {}


def add_item(customer_id, item_name, price, quantity):
    if customer_id not in carts:
        carts[customer_id] = {}

    if item_name in carts[customer_id]:
        carts[customer_id][item_name]['quantity'] += quantity
    else:
        carts[customer_id][item_name] = {'price': price, 'quantity': quantity}
    print(f"{quantity}, {item_name}(s) for customer {customer_id}.")


def remove_item(customer_id, item_name, quantity):
    if customer_id not in carts or item_name not in carts[customer_id]:
        print(f"Item {item_name} not found in the cart of the customer {customer_id}")
        return
    if carts[customer_id][item_name]['quantity'] <= quantity:
        del carts[customer_id][item_name]
    else:
        carts[customer_id][item_name]['quantity'] -= quantity
        print(f"{quantity} {item_name}(s) removed from customers' {customer_id} shopping cart.")



def display_cart(customer_id):
    if customer_id in carts:
        print(f"Shopping cart for customer {customer_id}.")
        for item, quantity in carts[customer_id].items():
            print(f'{item}, {quantity}')
        print(f'Total Price: ${calculate_total(customer_id):.2f}')
    else:
        print(f"Cannot be found for customer {customer_id}!!!")


add_item(100, "Chair", 40, 4)
add_item(152, "TV", 1500, 1)

remove_item(100, "Chair", 2)
display_cart(100)
add_item(100, "Microwave oven", 140, 1)

calculate_total(100)