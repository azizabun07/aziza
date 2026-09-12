def calculate_balance(initial_balance: int|float, *transactions: int|float):
    for i in transactions:
        initial_balance += i
        print(initial_balance)
        if initial_balance < 0:
            print('баланс ушел в минус!')
            return initial_balance

calculate_balance(100, -400)
