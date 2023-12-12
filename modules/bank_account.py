from decimal import Decimal
from modules.log import Log
from modules.utils import datetime_encoder
import json

class Bank_Account:

  venue = "Country Side Bank"
  id = 0

  def __init__(self, 
    balance = 0.0, 
    status = "available", # available | locked | closed 
    account_profile = "bronce", # bronce | silver | gold  | platinum
    currency = "USD") -> None:
    
    # Create consecutive account id
    Bank_Account.id += 1
    self.account_id = Bank_Account.id
    
    # Create account meta-data
    self.account_transactions = []
    self.balance = Decimal(balance)
    self.status = status
    self.account_profile = account_profile
    self.currency = currency

    Log("Create savings account", self.account_id, self.account_transactions)

  # Get historical transactions
  def get_transaction_logs(self, how_many = 2) -> list:
    Log("Get transaction logs", self.account_id, self.account_transactions)
    return json.dumps(self.account_transactions[:-how_many], default=datetime_encoder, indent=2)
  
  # Check current account's balance
  def check_balance(self) -> float:
    Log("Check balance", self.account_id, self.account_transactions)
    return Decimal(self.balance)
  
  # TODO: Lock account
  def freeze_account(self) -> bool:
    Log("Frezze account", self.account_id, self.account_transactions)
    pass

  # TODO: Transfer money to another account
  def transfer_money(self) -> None:
    Log("Transfer money", self.account_id, self.account_transactions)
    pass

  # Add money to the savings account
  def deposit_money(self, amount) -> float:
    Log("Deposit money", self.account_id, self.account_transactions)
    self.balance += Decimal(amount)
    return Decimal(self.balance)
  