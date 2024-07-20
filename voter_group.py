class VoterGroupHappiness:
  def __init__(self, voter_group_name, default_value, causes):
    self.voter_group_name = voter_group_name
    self.default_value = default_value
    self.value = default_value
    self.causes = causes

  def __repr__(self):
    return '[Voter Group Happiness] ' + self.voter_group_name

  def set_value(self, value):
    if (value < 0):
      self.value = 0
    elif (value > 1):
      self.value = 1
    else:
      self.value = value

class VoterGroupMembership:
  def __init__(self, voter_group_name, default_value, causes):
    self.voter_group_name = voter_group_name
    self.default_value = default_value
    self.value = default_value
    self.causes = causes

  def __repr__(self):
    return '[Voter Group Membership] ' + self.voter_group_name

  def set_value(self, value):
    if (value < 0):
      self.value = 0
    elif (value > 1):
      self.value = 1
    else:
      self.value = value

class VoterGroup:
  def __init__(self, key, name, description, default_membership, default_happiness, happiness_causes):
    self.key = key
    self.name = name
    self.description = description
    self.membership = VoterGroupMembership(name, default_membership, [])
    self.happiness = VoterGroupHappiness(name, default_happiness, happiness_causes)

  def __repr__(self):
    return '[Voter Group] ' + self.key
