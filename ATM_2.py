import random
import validation as vd


database = {
    7433883157: ['Ezra', 'Samuel', 'ezra@gmail.com', 'abc', 1000],
    8351212934: ['Seyi', 'Onifade', 'seyi@gmail.com', 'xyluz', 2000],
    5427320962: ['Abas', 'Ekwere', 'abas@yahoo.com', 'king', 3000]

}


def init():
    print('========Welcome to BankPHP========')

    have_account = int(input('Do you have an account with us? 1 (Yes); 2 (No) \n'))

    if have_account == 1:
        login()
        
    elif have_account == 2:
        register()

    else:
        print('Invalid option selected')
        init()

def login():
        
    user_account_number = input('Enter your Account Number \n')

    valid_account_number = vd.account_number_validation(user_account_number)

    if valid_account_number:

        user_password = input('Enter your Password \n')

    for account_number, user_details in database.items():
        if account_number == int(user_account_number):
            if user_details[3] == user_password:
                bank_operation(user_details)
        
    try_again = input('Invalid account or password. Do you want to try again or register?\
        \n 1. (Try Again) \n 2. (Register) \n 3. Enter any other character to exit. \n')
    if try_again == '1':
        login()
    elif try_again == '2':
        register()
    else:
        exit_operation()


def register():

    print('*****KINDLY REGISTER HERE*****')
    first_name = input('Enter your first name: \n')
    if first_name.isalpha():
        last_name = input('Enter your last name: \n')
        if last_name.isalpha():
            email = input('Enter your email address: \n')
            password = input('Create a password for yourself \n')

        else:
            print('Last name must be letters.')
            register()
    else:
        print('Last name must be letters.')
        register()
    

    
    account_number = generate_account_number()
    
    database[account_number] = [first_name, last_name, email, password, 0]
    
    print(f'Your Account Number is: {account_number}')

    return login()


def bank_operation(user):
    print('Welcome %s %s' %(user[0], user[1]))
    selected_option = int(input('What would you like to do?\
    \n 1. Deposit \n 2. Withdrawal \n 3. Logout \n 4. Exit \n'))
    
    if selected_option == 1:
        deposit_operation(user)
    elif selected_option == 2:
        withdrawal_operation(user)
    elif selected_option == 3:
        logout_operation()
    elif selected_option == 4:
        exit_operation()
    else:
        print('Invalid option selected. Please try again!')
        bank_operation(user)


def deposit_operation(user):

    account_balance = get_account_balance(user)
    deposit_amount = int(input('How much do you intend to deposit? \n'))
    account_balance += deposit_amount
    print(f'\nDeposit Successful. Your current balance is: {account_balance}')
    another_operation = input('Do you want to perform another operation? \
    \n If YES, Enter "1". \n If NO, Enter any other character to exit \n')
    if another_operation == '1':
        bank_operation(user)
    else:
        exit_operation()
        

def withdrawal_operation(user):

    account_balance = get_account_balance(user)
    withdrawal_amount = int(input('How much do you intend to withdraw? \n'))
    if account_balance >= withdrawal_amount:
        account_balance -= withdrawal_amount
    else:
        print(f'Your current balance is: {account_balance}. Try a lower amount.')
        withdrawal_amount = int(input('How much do you intend to withdraw? \n'))
    print(f'\n Withdrawal Successful. Your account balance is: {account_balance}')
    another_operation = input('\nDo you want to perform another operation? \
    \n If YES, Enter "1". \n If NO, Enter any other character to exit \n')
    if another_operation == '1':
        bank_operation(user)
    else:
        exit_operation()

def logout_operation():
    login()

def exit_operation():
    exit()

def generate_account_number():
    return random.randint(1000000000, 9999999999)

def get_account_balance(user_details):
    return user_details[4]

init()