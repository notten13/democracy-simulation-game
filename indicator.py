class Indicator:
  def __init__(self, key, name, description, min_value, max_value, default_value):
    self.key = key
    self.name = name
    self.description = description
    self.min_value = min_value
    self.max_value = max_value
    self.default_value = default_value
    self.value = default_value
    self.causes = []
