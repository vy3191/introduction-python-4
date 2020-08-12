# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name="Player A", location):
    self.name = name
    self.location = location
  def __str__(self):
    return f"{self.name} you are in {self.location}"