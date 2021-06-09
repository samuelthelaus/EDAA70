
class Account:
    def __init__(self, customer_id, account_nbr):
        self._customer_id = customer_id
        self._account_nbr = account_nbr
        self._balance = 0

    def get_customer_id(self):
        return self._customer_id

    def get_account_nbr(self):
        return self._account_nbr

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

    def __str__(self):
        return (
            f'Account(owner: {self._customer_id}, '
            f'nbr: {self._account_nbr}, '
            f'balance: {self._balance})'
        )

    def __repr__(self):
        return str(self)

    
class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}
        self.num_cust = 0
        self.num_acc = 0
    
    def add_customer(self, name):
        self.num_cust += 1
        self.customers[f'C{self.num_cust}'] = name
        return f'C{self.num_cust}'

    def get_customer_name(self, customer_id):
        if customer_id in self.customers:
            return self.customers[customer_id]
        return None

    def create_account(self, customer_id):
        if customer_id in self.customers:
            self.num_acc += 1
            self.accounts[self.num_acc] = Account(customer_id, self.num_acc)
            return self.num_acc
        return -1
    
    def get_account(self, account_nbr):
        if account_nbr in self.accounts:
            return self.accounts[account_nbr]
        return None
    
    def accounts_by_customer(self, customer_id):
        if customer_id in self.customers:
            return [account for key, account in self.accounts.items() if account.get_customer_id() == customer_id]
        return []
    
    def remove_account(self, account_nbr):
        if account_nbr in self.accounts:
            self.accounts.pop(account_nbr)
            return True
        return False
    
    def transfer(self, from_account_nbr, to_account_nbr, amount):
        if from_account_nbr in self.accounts and to_account_nbr in self.accounts:
            if self.accounts[from_account_nbr].withdraw(amount):
                self.account[to_account_nbr].deposit(amount)
                return True
        return False
    
    def total_balances(self):
        return sum([account.get_balance() for key, account in self.accounts.items()])
    
    def all_accounts(self):
        return list(self.accounts.values())
    
    def all_accounts_sorted_by_balance(self):
        balance_list = [account.get_balance() for key, account in self.accounts.items()]
        acc_num_list = list(self.accounts.keys())
        for i in range(len(balance_list)):
            min_index = i
            for j in range(i+1, len(balance_list)):
                if balance_list[j] < balance_list[min_index]:
                    min_index = j
            tmp_b = balance_list[i]
            tmp_a = acc_num_list[i]
            balance_list[i] = balance_list[min_index]
            acc_num_list[i] = acc_num_list[min_index]
            balance_list[min_index] = tmp_b
            acc_num_list[min_index] = tmp_a
        
        return [self.accounts[acc_num] for acc_num in acc_num_list[::-1]]




banken = Bank()

banken.add_customer('Stefan Holmgren')

banken.create_account('C1')
banken.create_account('C1')
banken.create_account('C1')

banken.accounts[1].deposit(200)
banken.accounts[2].deposit(100)
banken.accounts[3].deposit(150)

print(banken.accounts_by_customer('C1'))
print(banken.total_balances())
print(banken.all_accounts())
print(banken.all_accounts_sorted_by_balance())