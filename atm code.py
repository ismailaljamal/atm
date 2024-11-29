
def withdraw(withdrawal_ammount,balance):
    if withdrawal_ammount <= balance:
        print('جاري تنفيذ العملية')
        balance = balance - withdrawal_ammount
        print('استلام النقدية')
        return balance
    else:
        print('الرصيد غير كافي')

def deposit(deposit_ammount,balance):
    balance += deposit_ammount
    print('تم الايداع بنجاح')
    return balance
    

def balance_information(accounts,account_name):
    for key,value in accounts.items():
        if key == account_name:
            return value

def transformation(from_account,to_account,transfer_ammount,accounts):
    for key , value in accounts.items():
        if key == from_account:
            if transfer_ammount <= value:
                accounts[to_account] += transfer_ammount
                accounts[from_account] -= transfer_ammount
                print('تم التحويل بنجاح')
                return accounts
            else:
                print('الرصيد غير كافي')
                
    


accounts = {
    'mohamed':1000,
    'ahmed':5000,
    'ashraf':10000,
    'ward':20000
}

while True:
    account = input('we have 4 accounts, which account do you have?')
    for key,value in  accounts.items():
        if key == account:
            balance = value
    procces = input("""Choose which prossec do you need (withdraw / deposit / balance information /transformation)""")
    if procces == 'withdraw':
        withdraw_ammount = int(input('how much money do you want ?'))
        new_balance = withdraw(withdraw_ammount,balance)
        accounts[account] = new_balance
        
    elif procces == 'deposit':
        deposit_ammount = int(input('how much money do you want to deposit ?'))
        new_balance = deposit(deposit_ammount,balance)
        accounts[account] = new_balance
    elif  procces == 'balance information':
        check_balance = balance_information(accounts,account)
        print(f'your balance = {check_balance}')
    elif procces == 'transformation':
        to_account = input('which account do you want to transfer')
        transfer_ammount = int(input('how much money do you want to transfer ?'))
        new_accounts = transformation(account,to_account,transfer_ammount,accounts)
        accounts = new_accounts
    
        
    
    

    
