# in the_bank.py
class Bank(object):
"""The bank"""
def __init__(self):
self.accounts = []
def add(self, new_account):
""" Add new_account in the Bank
@new_account: Account() new account to append
@return True if success, False if an error occured
"""
# test if new_account is an Account() instance and if
# it can be appended to the attribute accounts
# ... Your code ...
self.accounts.append(new_account)
def transfer(self, origin, dest, amount):
"""" Perform the fund transfer
@origin: str(name) of the first account
@dest: str(name) of the destination account
@amount: float(amount) amount to transfer
@return True if success, False if an error occured
"""
# ... Your code ...
def fix_account(self, name):
""" fix account associated to name if corrupted
@name: str(name) of the account
@return True if success, False if an error occured
"""
# ... Your code ...