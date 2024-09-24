import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

### Complete functions ###
def main():
    while sandwich_maker_instance.is_on:
        choice = input("What would you like? (small/medium/large  -  off/report): ").lower().strip()

        if choice == "off":
            sandwich_maker_instance.turn_off()
        elif choice == "report":
            sandwich_maker_instance.report()
        elif choice in recipes:
            sandwich_recipe_instance = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich_recipe_instance["ingredients"]):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, sandwich_recipe_instance["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich_recipe_instance["ingredients"])
            else:
                return
        else:
            print("Invalid option, please choose small, medium, large, report, or off.")

if __name__=="__main__":
    main()