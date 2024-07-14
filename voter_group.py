from simulation_objects import SimulationObject

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