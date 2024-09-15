### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slice
            "ham": 4,  # slice
            "cheese": 4,  # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  # slice
            "ham": 6,  # slice
            "cheese": 8,  # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  # slice
            "ham": 8,  # slice
            "cheese": 12,  # ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  # slice
    "ham": 18,  # slice
    "cheese": 24,  # ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources
        self.is_on = True

    def check_resources(self, ingredients):
        """Returns True when the order can be made, False if ingredients are insufficient."""
        for ingredient, amount in ingredients.items():
            if self.machine_resources[ingredient] < amount:
                print(f"Sorry! There is not enough {ingredient} for your sandwich!")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins for payment.")
        dollars = int(input("How many dollars ($1)? ")) * 1.00
        half_dollars = int(input("How many half dollars ($0.5)? ")) * 0.50
        quarters = int(input("How many quarters ($0.25)? ")) * 0.25
        nickels = int(input("How many nickels ($0.05)? ")) * 0.05
        total = dollars + half_dollars + quarters + nickels
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Transaction successful. Here is ${change} in change.")
            else:
                print("Transaction successful.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount
        print(f"Your {sandwich_size} sandwich is ready. Bon appetit!!!")

    def report(self):
        """Prints a report of the current resources."""
        print("Current Inventory: ")
        for resource, amount in self.machine_resources.items():
            print(f"{resource}: {amount}")

    def turn_off(self):
        """Turns off the machine."""
        self.is_on = False
        print("Sandwich Machine is now off. Have a good day!")


### Make an instance of SandwichMachine class and write the rest of the codes ###
sandwichShop = SandwichMachine(resources)

def order_sandwich():
    while sandwichShop.is_on:
        choice = input("What would you like? (small/medium/large  -  off/report): ").lower().strip()

        if choice == "off":
            sandwichShop.turn_off()
        elif choice == "report":
            sandwichShop.report()
        elif choice in recipes:
            sandwich_recipe = recipes[choice]
            if sandwichShop.check_resources(sandwich_recipe["ingredients"]):
                coins = sandwichShop.process_coins()
                if sandwichShop.transaction_result(coins, sandwich_recipe["cost"]):
                    sandwichShop.make_sandwich(choice, sandwich_recipe["ingredients"])
            else:
                return
        else:
            print("Invalid option, please choose small, medium, large, report, or off.")

if __name__ == '__main__':
    order_sandwich()
