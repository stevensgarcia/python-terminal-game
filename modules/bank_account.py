from decimal import Decimal
from modules.log import Log
from modules.utils import datetime_encoder
import json
import csv

class Bank_Account:

  venue = "Country Side Bank"
  id = 0

  def __init__(self,
    owner,
    balance = 0.0, 
    status = "active", # active | locked | closed 
    account_profile = "bronce", # bronce | silver | gold  | platinum
    currency = "USD") -> None:
    
    # Create consecutive account id
    Bank_Account.id += 1
    self.account_id = Bank_Account.id
    
    # Create account meta-data
    self.owner = owner
    self.account_transactions_storage = []
    self.balance = Decimal(balance)
    self.status = status
    self.account_profile = account_profile
    self.currency = currency

    Log("Create savings account", self.account_id, self.account_transactions_storage)

  def __repr__(self) -> str:
    return f"This account belongs to {self.owner.name} and has a balance of {self.balance} {self.currency}"

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
  
  # Export transaction logs to CSV file
  def export_csv(self) -> None:
    Log("Export Logs to CSV", self.account_id, self.account_transactions_storage)
    
    with open(f"{self.account_id}.csv", "w") as file:

      fields = ['action', 'account_id', 'timestamp']
      writer = csv.DictWriter(file, fieldnames=fields)

      writer.writeheader()

      for log in self.account_transactions_storage:
        writer.writerow({
          "action": log["action"],
          "account_id": log["account_id"],
          "timestamp": log["timestamp"]
        })

  #############################################################################
  # CHANGE ACCOUNT STATUS
  #############################################################################

  # Unlock/Lock savings account
  def lock_account(self) -> str:
    Log("Lock account", self.account_id, self.account_transactions_storage)

    if self.is_locked(): 
      print(f"Your account is already {self.status.upper()}")
    else:
      self.status = "locked"
      print(f"Your account was succesfully {self.status.upper()}")

    return self.status
  
  def unlock_account(self) -> str:
    Log("Unlock account", self.account_id, self.account_transactions_storage)

    if not self.is_locked(): 
      print(f"Your account is already {self.status.upper()}")
    else:
      self.status = "active"
      print(f"Your account was succesfully changed to {self.status.upper()}")

    return self.status

  # Check account status: active | locked | closed
  def check_account_status(self) -> str:
    Log("Check account status", self.account_id, self.account_transactions_storage)
    return self.status
  
  # Check if account is already locked
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
      return Decimal(self.balance)
    
    self.validate_account_status(statement)

  # Withrow money at ATM
  def withrow_money(self, amount) -> float:
    Log("Withrow money", self.account_id, self.account_transactions_storage)
    
    def statement():
      self.balance -= Decimal(amount)
      return Decimal(self.balance)
    
    self.validate_account_status(statement)