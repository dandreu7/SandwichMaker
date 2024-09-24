class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns total calculated from coins inserted."""
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