class User:
    def __init__(self, name = "Default", choice = "Espresso", payment = 0):
        self.user_name = name
        self.choice_of_drink = choice
        self.payment_bill = payment
    
        
    def get_user_name(self):
        return self.user_name


    def get_choice_of_drink(self):
        return self.choice_of_drink


    def get_payment_bill(self):
        return self.payment_bill
    
    
    def set_user_name(self, name):
        self.user_name = name
        
        
    def set_choice_of_drink(self, choice):
        self.choice_of_drink = choice
        
        
    def set_payment_bill(self, payment):
        self.payment_bill = payment
        
class CoffeeMachine(User):
    def __init__(self):
        super().__init__()
        self.remaining_coffee = 100
        self.remaining_sugar = 100
        self.remaining_milk = 100
        self.price_latte = 4
        self.price_cappucino = 5
        self.price_espresso = 3
        self.coffee_required_for_espresso = 15
        self.coffee_required_for_latte = 10
        self.coffee_required_for_cappucino = 12
        self.milk_required_for_espresso = 0
        self.milk_required_for_latte = 20
        self.milk_required_for_cappucino = 7
        
    
    def get_price_latte(self):
        return self.price_latte

    
    def get_price_cappucino(self):
        return self.price_cappucino
    
    
    def get_price_espresso(self):
        return self.price_espresso
    
    
    def get_price(self):
        if(self.choice_of_drink == "latte"):
            return self.get_price_latte()
        elif(self.choice_of_drink == "espresso"):
            return self.get_price_espresso()
        elif(self.choice_of_drink == "cappucino"):
            return self.get_price_cappucino()
    
    
    def vend_drink(self):
        if(self.choice_of_drink == "latte"):
            self.coffee_required = self.coffee_required_for_latte
            self.milk_required = self.milk_required_for_latte
            self.price = self.price_latte
        elif(self.choice_of_drink == "espresso"):
            self.coffee_required = self.coffee_required_for_espresso
            self.milk_required = self.milk_required_for_espresso
            self.price = self.price_espresso
        elif(self.choice_of_drink == "cappucino"):
            self.coffee_required = self.coffee_required_for_cappucino
            self.milk_required = self.milk_required_for_cappucino
            self.price = self.price_cappucino
        if(self.remaining_coffee >= self.coffee_required):
            self.remaining_coffee -= self.coffee_required
        else:
            print(f"We have run out of coffee! Our sincere apologies! Please collect your money: ${self.payment_bill}!")
            self.set_payment_bill(0)
            return
        if(self.payment_bill < self.price):
            while(self.payment_bill < self.price):
                rem = self.price - self.payment_bill
                self.exit_choice = int(input(f"You are ${rem} short. Do you want to vend or exit? Please enter 1 to continue, or any other number to exit: "))
                if(self.exit_choice != 1):
                    print("Thank you! Exitting now!")
                    exit(1)
                payment_add = float(input(f"Please add ${rem} more to vend. Please enter the amount being entered: "))
                self.payment_bill += payment_add
        choice_of_sugar = int(input("How many sugar cubes do you want? Please enter an integer: "))
        if(self.remaining_sugar >= choice_of_sugar):
            self.remaining_sugar -= choice_of_sugar
        else:
            choice_of_remaining_sugar = input(f"We only have {self.remaining_sugar} cubes left! Will these many be fine for you? Please enter Y or y for yes...otherwise please enter N or n for no: ")
            if(choice_of_remaining_sugar in ['Y', 'y']):
                self.remaining_sugar = 0
            else:
                print("Sorry for the inconvenience! We couldn't fulfil your sugar requirement!\n")
                return
        print(f"\nThank you for vending a/an {self.choice_of_drink} {self.user_name}! It was a pleasure serving you {self.user_name}.\n")
        self.payment_bill -= self.price
        if(self.payment_bill != 0):
            print(f"Please collect your change: ${format(self.payment_bill, ".2f")}\n")
            return
    
        
    def restock_coffee(self, n):
        if(n < 100 and n != 0):
            self.remaining_coffee += n
        elif(n == 100):
            self.remaining_coffee = 100
        else:
            print("Oops! You added too much! Coffee has been successfully been added to a 100 percent capacity!")
            self.remaining_coffee = 100
    
    
    def restock_milk(self, n):
        if(n < 100 and n != 0):
            self.remaining_milk += n
        elif(n == 100):
            self.remaining_milk = 100
        else:
            print("Oops! You added too much! Milk has been successfully been added to a 100 percent capacity!")
            self.remaining_milk = 100
        
        
    def restock_sugar(self, n):
        if(n < 100 and n != 0):
            self.remaining_sugar += n
        elif(n == 100):
            self.remaining_sugar = 100
        else:
            print("Oops! You added too much! Sugar has been successfully been added to a 100 percent capacity!")
            self.remaining_sugar = 100    
        
C = CoffeeMachine()        
while(1): 
    print("Hello! Welcome to the Coffee Machine!")

    user_name = input("What is your name? We will have that written on your cup! Please enter it here: ")
    C.set_user_name(user_name)

    user_choice = int(input("Please enter 1 if you want to have a Latte, 2 if you want to have an Espresso, and 3 if you want to have an Cappucino: "))
    if(user_choice == 1):
        C.set_choice_of_drink("latte")
    elif(user_choice == 2):
        C.set_choice_of_drink("espresso")
    elif(user_choice == 3):
        C.set_choice_of_drink("cappucino")
    elif(user_choice == 1975):
        print("\n\nYou have entered the maintenance mode!")
        while(1):
            maintenance_choice = int(input("Please enter 1 to add more coffee, 2 to enter more milk, or 3 to add more sugar cubes: "))
            if(maintenance_choice == 1):
                maintenance_value = float(input("Please enter the final percentage of coffee after addition: "))
                C.restock_coffee(maintenance_value)
                print(f"Coffee has been restocked to {C.remaining_coffee}%.")
            elif(maintenance_choice == 2):
                maintenance_value = float(input("Please enter the final percentage milk after addition: "))
                C.restock_milk(maintenance_value)
                print(f"Milk has been restocked to {C.remaining_milk}%.")
            elif(maintenance_choice == 3):
                maintenance_value = int(input("Please enter the final number of sugar cubes after addition: "))
                C.restock_sugar(maintenance_value)
                print(f"Sugar cubes have been restocked to {C.remaining_sugar}%.")
            else:
                print("Invalid value!")
            choice_maintenance = int(input("Please enter 1 if you want to exit maintenance mode. Enter any other number to continue maintenance mode: "))
            if(choice_maintenance == 1):
                print("Shutting Down to update settings!")
                exit(1)
    else:
        print("Wrong input! Please reinitiate!\n\n")
        continue

    user_payment = float(input(f"The price of the drink is ${C.get_price()} . Please enter the amount you are entering: $"))
    if(user_payment > 0):
        C.set_payment_bill(user_payment)
    else:
        print("No money entered! Terminating current order!")
        continue

    C.vend_drink()
    
    choice_main = input("Please enter \"Power Off\" if you want to shut the CoffeeMachine, otherwise just enter any character to continue: ")
    if(choice_main == "Power Off"):
        print("Shutting Off!")
        exit(1)
    else:
        print("\n\n")