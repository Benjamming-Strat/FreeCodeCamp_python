import numpy as np

class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name
        self.balance = 0
        self.withdraws = 0

    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount" : amount, "description": description})
        self.balance += amount


    def withdraw(self, amount, description=""):
        
        if self.check_funds(amount):
            self.withdraws += amount
            self.ledger.append({"amount" : -amount, "description": description})
            self.balance -= amount
            return True
        
        return False
        

    def get_balance(self):
        return self.balance

 
    #3 von food weg und 3 zu enter
    def transfer(self, category, amount):

        with_description = f'Transfer to {category.name}'

        if self.withdraw(amount,with_description):
            depo_description = f"Transfer from {self.name}" 
            category.deposit(amount, depo_description)
            return True
        return False
        

    def check_funds(self, amount):
        return self.balance >= amount

    def __str__(self) -> str:
        
        
        string = self.name.capitalize().center(30, "*")+ "\n"

        for ele in self.ledger:
            
            left = ele["description"][:23]
            right = '{0:.2f}'.format(ele["amount"])
            
            total = "Total: " + str(self.balance)

            adjustment = 30 - len(left)
            string += left + str(right).rjust(adjustment," ") +"\n"
              

        return string + total

def create_spend_chart(args: Category) -> str:
    
    #category_sorted = sorted([arg for arg in args],key= lambda item: item.withdraws, reverse=True)
    category_sorted = args
    category_sorted_names = list((map(lambda x: x.name.capitalize(), category_sorted)))
    print(category_sorted_names)
    withdraw_sum = sum([amount.withdraws for amount in category_sorted])
    print(withdraw_sum)
    percent_cat = [(100* amount.withdraws/withdraw_sum//10)*10 for amount in category_sorted]
    print(percent_cat)

    string = ""
    format_string_top = "{}" * (len(args))

    for i in range(10,-1,-1):
        
        string += "{:d}|".format(i*10).rjust(4) + format_string_top.format(*["  " if i*10>percent_cat[k] else  "o".rjust(2) if k==0  else "o".rjust(3)  \
            for k,c in enumerate(args)]) + "\n"
            
        

    string += "    " + ("---"*(len(args))).rjust(3*len(args))+"-" + "\n"
    max_name_len = max(map(len, category_sorted_names))
    format_string_botton = "    " + " {}" + "  {}"* (len(args)-1)

    for j in range(max_name_len):
        string += format_string_botton.format(*[c[j] if len(c)>j else " " for c in category_sorted_names]) + "  \n"

    return string


   
if __name__ == "__main__":
    food = Category("food")
    entertainment = Category("entertainment")
    clothing = Category("clothing")
    business = Category("business")


    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)

    #food.transfer(entertainment, 20,)

    print(food)
    
    print(create_spend_chart([business, food, entertainment]))


    
        
    


