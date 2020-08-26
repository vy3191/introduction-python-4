# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
  
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.items = []

  def get_item(self, item_name: str):    
    for item in self.items:
      if item.name.lower() == item_name.lower():
        return item
    return None    
  
  def remove_item(self, item:Item):
    self.items.remove(item)