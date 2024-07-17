from simulation_objects import SimulationObject

class PolicyCost(SimulationObject):
  pass

class PolicyIncome(SimulationObject):
  pass

class PolicyLevel(SimulationObject):
  pass

class Policy:
  def __init__(self, name, initial_level, initial_cost, initial_income):
    self.name = name
    self.level = PolicyLevel(name + ' Level', initial_level)
    self.cost = PolicyCost(name + ' Cost', initial_cost)
    self.income = PolicyIncome(name + ' Income', initial_income)
    
    self.level.register_effect(self.cost, 1)
