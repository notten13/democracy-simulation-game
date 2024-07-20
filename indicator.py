class Indicator:
  def __init__(self, key, name, description, min_value, max_value, default_value, causes):
    self.key = key
    self.name = name
    self.description = description
    self.min_value = min_value
    self.max_value = max_value
    self.default_value = default_value
    self.value = default_value
    self.causes = causes

  def __repr__(self):
    return '[Indicator] ' + self.key

  def set_value(self, value):
    if (value < self.min_value):
      self.value = self.min_value
    elif (value > self.max_value):
      self.value = self.max_value
    else:
      self.value = value
