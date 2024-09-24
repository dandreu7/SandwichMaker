class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources
        self.is_on = True

    def check_resources(self, ingredients):
        """Returns True when the order can be made Returns False if ingredients are insufficient."""
        for ingredient, amount in ingredients.items():
            if self.machine_resources[ingredient] < amount:
                print(f"Sorry! There is not enough {ingredient} for your sandwich!")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from resources."""
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