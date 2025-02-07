class SystemOfBanks:
    __all_banks = []
    accounts = {}

    def add_bank(self,bank):
        if bank not in self.__all_banks:
            self.__all_banks.append(bank)
            self.accounts[bank] = []

    @classmethod
    def add_bank_account(self, bank, first_name, last_name, age, egn):
        if bank not in self.__all_banks:
            raise KeyError('Invalid bank!')
        self.accounts[(bank, first_name, last_name, age, egn)] = id((bank, first_name, last_name, age, egn))

        
class Person:
    def __init__(self, first_name, second_name, age, egn):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.egn = egn


class Customer(Person):
    def __init__(self, first_name, last_name, age, egn):
        super().__init__(first_name, last_name, age, egn)
        self.account_numbers = {}

    def open_bank_account(self, bank, first_name, last_name, age, egn):
        SystemOfBanks.add_bank_account(bank, first_name, last_name, age, egn)
        self.account_numbers[bank] = id((bank, first_name, last_name, age, egn))

    def check_avl(bank_name, account_number):
        return SystemOfBanks.accounts[(bank_name,account_number)]
    
    def close_bank(bank_name, account_number):
        pass




class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


banks = SystemOfBanks()
banks.add_bank('Unicredit bank')
banks.add_bank('Banka Intesa')
customer1 = Customer('Dimitar', 'Grigorov', 20, 451235)
print(customer1.egn)
customer1.open_bank_account('Unicredit bank', 'Dimitar', 'Grigorov', 20, 451235)
print(customer1.account_numbers['Unicredit bank'])