cart = []

def add_item(item):
    cart.append(item)
    print(f'{item} added to the cart')


def remove_item(item):
    if item in cart:
        cart.remove(item)
        print(f'removed {item} from cart ')
    else:
        print('sorry cannot remove the item')

def show_cart():
    if cart:
        print("here's your cart")
        for item in cart:
            print(item)
        else:
            print('Your cart is empty')


def clearCart():
    cart.clear()
    print('Your cart is empty')



def main():
    done=False
    while not done:
        ans=input("quit/add/remove/show/clear :").lower()

        if ans == "quit":
            print("Thanks for visiting us")
            show_cart()
            done=True

        elif ans== "add":
            item=input("what would you like to add to the cart").title()
            add_item(item)
        elif ans=="remove":
            show_cart()
            item=input("what would you like to remove from the cart").title()
            remove_item(item)
        elif ans=="show":
            show_cart()
        elif ans == "clear":
            clearCart()
        else:
            print("Sorry , no such option")



main()



    


