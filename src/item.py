

class Item:

  def __init__(self, name, description):
    self.name = name
    self.description = description

  def get_item(self):
    return f"You have picked up {self.name} item."

  def __str__(self):
    return f"Item name:{self.name} and description:{self.description}"