def account_number_validation(account_number):

    if account_number:

        if len(str(account_number)) == 10:
            
            try:
                int(account_number)
                return True
            except ValueError:
                print('Invalid Account Number. Account Number should be integer.') 
                return False

        else:
            print('Account Number must be 10 digits')

    else:
        print('Account Number is a required field')
        return False
