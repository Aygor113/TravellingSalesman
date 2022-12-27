class City:
  def __init__(self, name, xPos, yPos):
    self.name = name
    self.xPos = xPos
    self.yPos = yPos

  def listCity(self):
    print(self.name, "Position: " + str(self.xPos) + ", " + str(self.yPos))

