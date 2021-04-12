'''
In the supermarket.py file, write a code that should achieve above tests through failing test, production test and the refractor test. 

'''

class Supermarket:
    def __init__(self, item, cart):
        self.item = item
        self.cart = cart

    
class Checkout:
        
    def shop(self):
        checkout_cart = Supermarket('', [])
        print('''
        Welcome to my supermarket, here you can add shopping items to your cart.
        When you are prompted to answer the questions simply type: yes or no and done when
        you are completed with your shopping cart.

        After adding the item you will be prompted to enter a price as well. Just use numbers.

        If you want to calculate the total of your cart simply type done, then type calculate when you 
        prompted to.

        HAPPY SHOPPING!
         ''')
        total_price = []
        user_input = input('Would you like to add items to the cart? ')
        if user_input != 'yes' and user_input != 'no':
            print('User input not valid. Type yes or no!')
            user_input = input('Would you like to add items to the cart? ')

            while user_input == 'yes':
                add_to_cart = input('Add to Cart: ')
                add_price = float(input(f'What is the price of {add_to_cart}? '))
                total_price.append(add_price)
                joined_value = add_to_cart + ' ' + str(add_price)
                checkout_cart.cart.append(joined_value)
                for i in checkout_cart.cart:
                    print(i)

                user_input = input('''
                If you are finish type done to get the total. 
                If you are NOT done type yes to continue: ''')
                if user_input == 'yes':
                    continue

                elif user_input == 'done':
                    get_total = input('Type calculate to get the total price of your items? ')
                    if get_total == 'calculate':
                        calculate = sum(total_price)
                        print(f'Your total price of your cart is {calculate}')
                        savings = input('To apply discount of 5 percent type save: ')
                        if savings == 'save':
                            divided_num = calculate / 100
                            percent = divided_num * 5
                            new_total = percent - calculate
                            print(f'Your new total is now {new_total}!')

                    break
                
        else:
            while user_input == 'yes':
                add_to_cart = input('Add to Cart: ')
                add_price = float(input(f'What is the price of the {add_to_cart}? '))
                total_price.append(add_price)
                joined_value = add_to_cart + ' ' + str(add_price)
                checkout_cart.cart.append(joined_value)
                for i in checkout_cart.cart:
                    print(i)

                user_input = input('''
                If you are finish type done to get the total. 
                If you are NOT done type yes to continue: ''')                
                if user_input == 'yes':
                    continue

                elif user_input == 'done':
                    get_total = input('Type calculate to get the total price of your items? ')
                    if get_total == 'calculate':
                        calculate = sum(total_price)
                        print(f'Your total price of your cart is {calculate}')
                        savings = input('To apply discount of 5 percent type save: ')
                        if savings == 'save':
                            divided_num = calculate / 100
                            percent = divided_num * 5
                            new_total =  calculate - percent 
                            print(f'Your new total is now {new_total}!')
                    break

        
        print('THANKS FOR SHOPPING!')
        return checkout_cart.cart




check_one = Checkout()
check_one.shop()