class Owner:

  def __init__(self, name, email) -> None:
    self.name = name
    self.email = email
  
  def get_owner(self) -> dict:
    return {
      "name": self.name, 
      "email": self.email
    }

