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
  
class Policy(SimulationObject):
  pass

class Indicator(SimulationObject):
  pass

class VoterGroupMembership(SimulationObject):
  pass

class VoterGroupHappiness(SimulationObject):
  pass

class VoterGroupIncome(SimulationObject):
  pass

class VoterGroup:
  def __init__(self, name, initial_membership, initial_happiness, initial_income):
    self.name = name
    self.membership = VoterGroupMembership(name + ' Membership', initial_membership)
    self.happiness = VoterGroupHappiness(name + ' Happiness', initial_happiness)
    self.income = VoterGroupIncome(name + ' Income', initial_income)

def define_influence(cause, effect, weight):
  # If effect is a policy, throw an error
  if isinstance(effect, Policy):
    raise ValueError('Cannot define influence from an Indicator to a Policy')

  cause.effects.append((effect, weight))
  effect.causes.append((effect, weight))