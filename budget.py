class Category:
    
    def __init__(self, category):
        self.category = category
        self.ledger = []
    
    def __str__(self):
        wline = self.category.center(30, '*') + "\n"
        for list_item in self.ledger:
            a = f"{list_item['description'][:23]:23}{list_item['amount']:7.2f}"
           wline += a +"\n"
        wline += 'Total: ' + str(self.get_balance())
        return wline
 
    
    def withdraw(self, amount, description=''):
        temp = {}
        if self.check_funds(amount):
            temp['amount'] = -amount
            temp['description'] = description
            self.ledger.append(temp)
            return True
        return False
        
           
    def deposit(self, amount, description=''):
        temp = {}
        temp['amount'] = amount
        temp['description'] = description
        self.ledger.append(temp)
        
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
        
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return(balance)
        
        
    def transfer(self, amount, expense_cat):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + expense_cat.category)
            expense_cat.deposit(amount, "Transfer from " + self.category)
            return True
        return False
    



def create_spend_chart(categories):
    spend = []
    for category in categories:
        temp = 0
        for item in category.ledger: 
            if item['amount'] < 0:
                temp += abs(item['amount'])
        spend.append(temp)
    total = sum(spend)
    percentage = [i/total * 100 for i in spend]
    
    pc = "Percentage spent by category"
    for i in range(100, -1, -10):
         pc += "\n" + str(i).rjust(3) + "|"
        for a in percentage:
            if a > i:
                 pc += " o "
            else:
                 pc += "   "
         pc += " "
   pc += "\n" + "    "

    for i in percentage:
         pc += "-"*3
   pc += "-"
    
    category_length = []
    for category in categories:
        cat_lenght.append(len(category.category))
    maximum_length = max( category_length)
    
    for y in range(maximum_length):
        pc += "\n    "
        for c in range(len(categories)):
            if y <  category_length[c]:
                pc += " " + categories[c].category[y] + " "
            else:
                pc += "   "
        pc += " "

    return pc
