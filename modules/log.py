from datetime import datetime

class Log:

  def __init__(self, action, account_id, log_storage) -> None:
    self.account_id = account_id
    self.action = action
    self.timestamp = datetime.now()
    self.save_transaction_log(log_storage)

  def save_transaction_log(self, log_storage) -> dict:

    transaction_log = {
      "action": self.action,
      "account_id": self.account_id,
      "timestamp": self.timestamp,
    }

    log_storage.append(transaction_log)

    return transaction_log



