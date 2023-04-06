#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)
        self.last_transaction_amount = price * quantity

    def apply_discount(self):
        if self.discount:
            self.total *= (1 - (self.discount / 100))
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")
        return self.total

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        for _ in range(self.items.count(self.items[-1])):
            self.items.pop()



#! First attempt -- Close but no cigar:

# class CashRegister:
#     def __init__(self, discount=0, total=0):
#         self.total = total
#         self.items = []
#         if discount is None or type(discount) in (int, float):
#             self._discount = discount
#         else:
#             print("The discount must be an integer, float, or None.")

#     def get_discount(self):
#         return self._discount
    
#     def set_discount(self, discount):
#         if discount is None or type(discount) in (int, float):
#             self._discount = discount
#         else:
#             print("The discount must be an integer, float, or None.")

#     discount = property(get_discount, set_discount)

#     def add_item(self, title, price, quantity=1):
#         for _ in range(quantity):
#             self.items.append((title, price))
#         self.total += price * quantity
    
#     def apply_discount(self):
#         if self._discount:
#             self.total *= (1 - (self._discount / 100))
#             print(f"After the discount, the total comes to ${self.total:.0f}.")
#         else:
#             print("There is no discount to apply.")
#         return self.total
    
#     def void_last_transaction(self):
#         last_item = self.items.pop()
#         last_item_price, last_item_quantity = last_item[1], self.items.count(last_item)
#         self.total -= last_item_price * (last_item_quantity + 1)