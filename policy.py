class Policy:
  def __init__(self, key, name, description, min_value, max_value, default_value, min_cost, max_cost, cost_formula, min_income, max_income, income_formula):
    self.key = key
    self.name = name
    self.description = description
    self.min_value = min_value
    self.max_value = max_value
    self.default_value = default_value
    self.value = default_value
    self.min_cost = min_cost
    self.max_cost = max_cost
    self.cost_formula = cost_formula
    self.min_income = min_income
    self.max_income = max_income
    self.income_formula = income_formula
