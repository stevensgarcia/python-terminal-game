from decimal import Decimal
from modules.log import Log
from modules.utils import datetime_encoder
import json

class Bank_Account:

  venue = "Country Side Bank"
  id = 0

  def __init__(self, 
    balance = 0.0, 
    status = "active", # active | locked | closed 
    account_profile = "bronce", # bronce | silver | gold  | platinum
    currency = "USD") -> None:
    
    # Create consecutive account id
    Bank_Account.id += 1
    self.account_id = Bank_Account.id
    
    # Create account meta-data
    self.account_transactions_storage = []
    self.balance = Decimal(balance)
    self.status = status
    self.account_profile = account_profile
    self.currency = currency

    Log("Create savings account", self.account_id, self.account_transactions_storage)

  #############################################################################
  # ACCOUNT HISTORY
  #############################################################################

  # Get historical transactions
  def get_transaction_logs(self, how_many = 2) -> list:
    Log("Get transaction logs", self.account_id, self.account_transactions_storage)

    def statement() -> list:
      json_logs = json.dumps(self.account_transactions_storage[:-how_many], 
        default=datetime_encoder, indent=2)
      return json_logs
    
    return self.validate_account_status(statement)
  
  # Check current account's balance
  def check_balance(self) -> float:
    Log("Check balance", self.account_id, self.account_transactions_storage)

    def statement():
      return Decimal(self.balance)
    
    return self.validate_account_status(statement)

  #############################################################################
  # CHANGE ACCOUNT STATUS
  #############################################################################

  # Unlock/Lock savings account
  def lock_account(self) -> str:
    Log("Lock account", self.account_id, self.account_transactions_storage)
    self.status = "locked"
    return self.status
  
  def unlock_account(self) -> str:
    Log("Unlock account", self.account_id, self.account_transactions_storage)

    if not self.is_locked(): 
      print(f"Your account is already {self.status.upper()}")
    else:
      self.status = "active"

    return self.status

  # Check account status: active | locked | closed
  def check_account_status(self) -> str:
    Log("Check account status", self.account_id, self.account_transactions_storage)
    return self.status
  
  def is_locked(self) -> bool:
    if self.status != "active":
      return True
    else:
      return False

  # Helper function to validate if the account is locked, so then the requested
  # action can be perfomed
  def validate_account_status(self, statement):
    if not self.is_locked():
      return statement()
    else:
      print("\n#################################################################")
      print(f"Account is {self.status}. \nYou cann't deposit right now!. Please **ACTIVATE** your account first.")
      print("#################################################################\n")
      return False
  
  #############################################################################
  # ACCOUNT MONEY TRANSACTIONS
  #############################################################################

  # Add money to the savings account
  def deposit_money(self, amount) -> float:
    Log("Deposit money", self.account_id, self.account_transactions_storage)

    def statement():
      self.balance += Decimal(amount)
      return self.balance
    
    self.validate_account_status(statement)
      
  # TODO: Transfer money to another account
  # def transfer_money(self) -> None:
  #   Log("Transfer money", self.account_id, self.account_transactions_storage)
  #   pass

  # TODO: Withrow money
  # def withrow_money(self) -> None:
  #   Log("Withrow money", self.account_id, self.account_transactions_storage)
  #   pass