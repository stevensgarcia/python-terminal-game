from modules.owner import Owner
from modules.bank_account import Bank_Account
from decimal import Decimal

b = bank_account = None
o = owner = None

#############################################################################
# Build UI in terminal
#############################################################################

def print_intro():
  intro_message = """
-------------------------------------------------------------------------------
Welcome to Country Side Bank!

Here you can create a savings account, check your balance, deposit money, 
withdraw money, lock your account, and print your transactions log.

Follow the instructions below to use the program.
-------------------------------------------------------------------------------
"""
  print(f"{intro_message}")

# Display self service options to start user interactions
def print_instructions():

  print("\nBelow you can find what you can do here:\n")
  print("1. Create a Savings Account.")
  print("2. Check your balance.")
  print("3. Deposit money in your savings account")
  print("4. Withrow money from your account")
  print("5. Check account status")
  print("6. Lock you account")
  print("7. Unlock you account")
  print("8. Print your transactions log")
  print("9. Export your transactions log to CSV")

  print("0. Exit")

#############################################################################
# Execute user's actions
#############################################################################

def get_user_data():
  # Get user input or perform other tasks here
  user_name = input("Enter your name: ")
  user_id = int(input("Enter your id: "))
  print(f"\nHello, {user_name}!")

  print_instructions()

  return user_name, user_id

def user_action():
  return input("\nEnter the number of the action you want to perform: ")

def perform_menu_action(menu_option, user_name, user_id):

  # Print a message confirmation the action was done
  def confirmation_message(owner, message):
    print(f"Dear {owner.name}, {message}")

  match menu_option:

    case "1": # Create savings account
      global o, b 
      o = Owner(user_name, user_id)
      b = Bank_Account(owner = o)
      confirmation_message(o, "your savings account has been created successfully!")

    case "2": # Check balance
      confirmation_message(o, f"your current balance is: ${Decimal(b.check_balance())} {b.currency}")

    case "3": # Deposit money
      amount = Decimal(input("How much do you want to deposit?: "))
      b.deposit_money(amount)
      confirmation_message(o, f"your current balance is: ${Decimal(b.check_balance())} {b.currency}")

    case "4": # Withrow money
      amount = Decimal(input("How much do you want to withrow?: "))
      b.withrow_money(amount)
      confirmation_message(o, f"your current balance is: ${Decimal(b.check_balance())} {b.currency}")

    case "5": # Check account status
      confirmation_message(o, f"your account status is: {b.check_account_status().upper()}")

    case "6": # Lock account
      b.lock_account()

    case "7": # Unlock account
      b.unlock_account()

    case "8": # Print transactions logs
      print(b.get_transaction_logs())

    case "9": # Export transactions logs to CSV file
      b.export_csv()
      confirmation_message(o, "your transactions log has been exported successfully!")

    case _:
      print("We're sorry. That option is not available. Please try again or hit '9' to close this program.")


#############################################################################
# Start program
#############################################################################

def main():
  print_intro()

  # Request user to identify and print available options
  user_name, user_email = get_user_data()

  # Get user's desired action
  menu_option = user_action()

  while menu_option != "0":

    # Execute user's action
    perform_menu_action(menu_option, user_name, user_email)
    # Continue asking for an action
    menu_option = user_action()


if __name__ == "__main__":
  main()