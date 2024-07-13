class SimulationObject:
  def __init__(self, name, initialValue):
    self.name = name
    self.value = initialValue
    self.valueHistory = [initialValue]
    self.changeHistory = []

  def update_value(self, new_value):
    current_value = self.value
    self.value = new_value
    self.valueHistory.append(new_value)
    self.changeHistory.append((new_value - current_value) / current_value)
  
class Policy(SimulationObject):
  def __init__(self, name, initialValue):
    super().__init__(name, initialValue)
    self.effects = []

class Indicator(SimulationObject):
  def __init__(self, name, initialValue):
    super().__init__(name, initialValue)
    self.effects = []
    self.causes = []
