def calculate_balance(initial_balance, *transactions):
    for i in transactions:
        initial_balance += i
        if initial_balance < 0:
            print('баланс ушел в минус!')
    print(initial_balance)
    return initial_balance
calculate_balance(100, -300)
