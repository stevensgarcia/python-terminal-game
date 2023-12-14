class Owner:

  def __init__(self, name, id) -> None:
    self.name = name
    self.id = id
  
  def get_owner(self) -> dict:
    return {
      "name": self.name, 
      "id": self.id
    }

