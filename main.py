import time, os, FileTools as FT


def format():
    acc_dict = {}
    file = 'accounts.txt'

    content = FT.readFile(file, 'rl')
    for user in content:
        user = str(user).split(' : ')

        user[1] = [user[1][1:5], user[1][7:-1]]
        acc_dict[user[0]] = user[1]
    return acc_dict


def val(acc_dict, option, *val):
    val = list(*val)
    match option:
        case 'acc':
            name, pin = val[0], val[1]
            while name not in acc_dict:
                name = input('Enter the name for the account: ')

            while pin != acc_dict[name][0]:
                try:
                    pin = int(input('\nEnter the pin for the user: '))

                    if pin == int(acc_dict[name][0]) and type(pin) == int:
                        return True
                
                except:
                    print('\nInvalid pin.')
                    time.sleep(1.5)
                    os.system('cls')
            return True

        case 'deposit':
            amount = val[0]
            while type(amount) != int:
                try:
                    amount = int(input('\nEnter the amount of money to deposit: '))

                    if amount > 0:
                        return amount
                    amount = ''
                
                except:
                    print('\nInvalid deposit amount.')
                    time.sleep(1.5)
                    os.system('cls')
            return amount

        case 'withdraw':
            name, amount = val[0], val[1]
            while type(amount) != int:
                try:
                    amount = int(input("Enter the amount of money to withdraw: "))

                    if amount >= 0 and int(acc_dict[name][1]) < amount:
                        return amount
                    amount = ''
                
                except:
                    print('\nInvalid withdraw amount.')
                    time.sleep(1.5)
                    os.system('cls')
            return amount


def deposit(name, amount, acc_dict):
    temp = int(acc_dict[name][1])
    temp += amount
    acc_dict[name] = [acc_dict[name][0], temp]

    FT.writeFile('accounts.txt', '\n'.join([f'{i} : {[int(acc_dict[i][0]), int(acc_dict[i][1])]}' for i in acc_dict]))
    return format()


def withdraw(name, amount, acc_dict):
    temp = int(acc_dict[name][1])
    temp -= amount
    acc_dict[name] = [acc_dict[name][0], temp]

    FT.writeFile('accounts.txt', '\n'.join([f'{i} : {[int(acc_dict[i][0]), int(acc_dict[i][1])]}' for i in acc_dict]))
    return format()


def view_acc(name, acc_dict):
    print(f'Name: {name}\nPin: {acc_dict[name][0]}\nMoney: {acc_dict[name][1]}')


def main():
    # Implement functions
    acc_dict = format()

    name = input('What is the name for the account: ')
    pin = input("Enter the pin number for the account: ")
    inSystem = val(acc_dict, 'acc', [name, pin])
    while inSystem:
        os.system('cls')
        option = input("Would you like to view, depsoit, or withdraw from your account (1, 2, 3, 4): ")

        while option not in ['1', '2', '3', '4']:
            option = input("Would you like to view, depsoit, withdraw from your account, or exit (1, 2, 3, 4): ")

        if option == '1':
            os.system('cls')
            view_acc(name, acc_dict)
            time.sleep(5)

        elif option == '2':
            amount = ''
            amount = val(acc_dict, 'deposit', [amount])
            acc_dict = deposit(name, amount, acc_dict)

            print("The money has been deposited")
            time.sleep(3)

        elif option == '3':
            amount = ''
            amount = val(acc_dict, 'deposit', [amount])
            acc_dict = withdraw(name, amount, acc_dict)
            
            print("The money has been withdrawed")
            time.sleep(3)

        else:
                os.system('cls')
                print("Goodbye")
                inSystem = False


if __name__ == '__main__':
    main()