class SimulationObject:
  def __init__(self, name, initialValue):
    self.name = name
    self.value = initialValue
    self.valueHistory = [initialValue]
    self.changeHistory = []
    self.effects = []
    self.causes = []

  def update_value(self, new_value):
    current_value = self.value
    self.value = new_value
    self.valueHistory.append(new_value)
    self.changeHistory.append((new_value - current_value) / current_value)

  def register_effect(self, effect, weight):
    self.effects.append((effect, weight))
    effect.causes.append((self, weight))