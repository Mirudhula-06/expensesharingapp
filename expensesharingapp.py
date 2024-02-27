class User:
    def __init__(self, username):
        self.username = username
        self.balance = 0
    def add_expense(self,amount):
        self.balance +=amount
    def settle_balance(self,amount):
        self.balance -=amount
class Expense:
    def __init__(self, description, amount, paid_by, users):
        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.users = users
    def split_expense(self):
        num_users=len(self.users)
        per_person_amount=self.amount/num_users
        for user in self.users:
            if user != self.paid_by:
                user.add_expense(per_person_amount)
        self.paid_by.add_expense(-self.amount)
class ExpenseManager:
    def __init__(self):
        self.users = {}
    def add_user(self, username):
        self.users[username] = User(username)
    def add_expense(self, description, amount, paid_by, users):
        expense = Expense(description, amount, self.users[paid_by], [self.users[user] for user in users])
        expense.split_expense()
    def get_balance(self, user):
        return self.users[user].balance
if __name__ == "__main__":
    manager = ExpenseManager()
    manager.add_user("amirtha")
    manager.add_user("banumathi")
    manager.add_user("saranyaa")
    manager.add_expense("Dinner", 600, "amirtha", ["banumathi", "saranyaa"])
    manager.add_expense("Groceries", 250, "banumathi", ["amirtha", "saranyaa"])
    manager.add_expense("Shopping",300,"saranyaa",["amirtha","banumathi"])
    print("amirtha's balance:", manager.get_balance("amirtha"))
    print("banumathi's balance:", manager.get_balance("banumathi"))
    print("saranyaa's balance:",manager.get_balance('saranyaa'))
