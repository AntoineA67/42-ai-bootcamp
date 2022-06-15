# in the_bank.py

class Account(object):

	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount


class Bank(object):
	"""The bank"""
	def __init__(self):
		self.accounts = []

	def __find_account(self, account: str) -> Account:
		""" Search for account in bank accounts
			@account (string): account to find
			@return Account if found, else None
		"""
		if type(account) != str: return None
		acc = list(filter(lambda acc: 'name' in acc.__dict__ and acc.__dict__['name'] == account, self.accounts))
		if len(acc) != 1:
			return None
		return acc[0]

	@staticmethod
	def __check_account(account: Account) -> bool:
		""" Check if given account is valid or not and return the result
			@account: Account() to check
			@return True if account is valid, else False
		"""
		acc_dict = account.__dict__
		return	isinstance(account, Account)\
				and len(acc_dict) % 2 != 0\
				and all(not att.startswith('b') for att in acc_dict.keys())\
				and any(att.startswith('zip') or att.startswith('addr') for att in acc_dict.keys())\
				and 'name' in acc_dict.keys() and 'id' in acc_dict.keys() and 'value' in acc_dict.keys()\
				and isinstance(acc_dict['name'], str) and isinstance(acc_dict['id'], int) and isinstance(acc_dict['value'], (int, float))

	def add(self, new_account):
		""" Add new_account in the Bank
			@new_account: Account() new account to append
			@return True if success, False if an error occured
		"""
		if isinstance(new_account, Account) and new_account.name not in self.accounts:
			self.accounts.append(new_account)
			return True
		return False

	def transfer(self, origin, dest, amount):
		"""" Perform the fund transfer
			@origin: str(name) of the first account
			@dest: str(name) of the destination account
			@amount: float(amount) amount to transfer
			@return True if success, False if an error occured
		"""
		if type(origin) != str: raise TypeError('Origin account name should be a string')
		if type(dest) != str: raise TypeError('Dest account name should be a string')
		if type(amount) != float: raise TypeError('Amount to transfer should be a float')
		origin_acc, dest_acc = self.__find_account(origin), self.__find_account(dest) 
		if not origin_acc or not dest_acc:
			return False
		# print(origin_acc.name, '\t', dest_acc.name)
		if not self.__check_account(origin_acc) or not self.__check_account(dest_acc) or amount < 0 or amount > origin_acc.value:
			return False
		if origin != dest:
			origin_acc.transfer(-amount)
			dest_acc.transfer(amount)
		return True

	def fix_account(self, name):
		""" fix account associated to name if corrupted
			@name: str(name) of the account
			@return True if success, False if an error occured
		"""
		acc = self.__find_account(name)
		if not acc:
			return False
		if not hasattr(acc, 'id') or type(acc.id) != int:
			acc.__setattr__('id', Account.ID_COUNT)
			Account.ID_COUNT += 1
		if not hasattr(acc, 'addr') and not hasattr(acc, 'zip'):
			acc.__setattr__('addr', 'Unknown address')
		if not hasattr(acc, 'value') or not isinstance(acc.value, (int, float)):
			acc.__setattr__('value', 0.0)
		for att in acc.__dict__.keys():
			if att.startswith('b'): delattr(acc, att)
		if len(acc.__dict__) % 2 == 0:
			for att in acc.__dict__.keys():
				if att not in ('name', 'value', 'zip', 'addr', 'id') or (att == 'addr' and hasattr(acc, 'zip')) :
					delattr(acc, att)
					break
		if not self.__check_account(acc):
			print('Sorry, could not fix that account')
			return False
		return True
		
		
		
		