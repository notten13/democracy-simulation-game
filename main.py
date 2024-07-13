from simulation_objects import Indicator, Policy

def propagate_change(start):
  queue = [start]

  while len(queue) > 0:
    current = queue.pop(0)
    for effect, weight in current.effects:
      new_value = effect.value + effect.value * current.changeHistory[-1] * weight
      if new_value < 0:
        new_value = 0
      effect.update_value(new_value)
      queue.append(effect)

def print_game_state(indicators, policies):
  print('Indicators:')
  for indicator in indicators:
    print(f'{indicator.name}: {indicator.value}')
  print('Policies:')
  for policy in policies:
    print(f'{policy.name}: {policy.value}')

nhs_funding = Policy('NHS Funding', 100)
tobacco_tax = Policy('Tobacco Tax', 100)
health = Indicator('Health', 100)
unemployment = Indicator('Unemployment', 100)
poverty = Indicator('Poverty', 100)
tobacco_usage = Indicator('Tobacco Usage', 100)
private_health_care = Indicator('Private Health Care', 100)

indicators = [health, private_health_care, unemployment, poverty, tobacco_usage]
policies = [nhs_funding, tobacco_tax]

def define_influence(cause, effect, weight):
  # If effect is a policy, throw an error
  if isinstance(effect, Policy):
    raise ValueError('Cannot define influence from an Indicator to a Policy')

  cause.effects.append((effect, weight))
  effect.causes.append((effect, weight))

define_influence(nhs_funding, health, 0.1)
define_influence(nhs_funding, private_health_care, -0.25)
define_influence(nhs_funding, unemployment, -0.05)
define_influence(nhs_funding, poverty, -0.13)
define_influence(tobacco_tax, tobacco_usage, -0.05)
define_influence(tobacco_usage, health, -0.18)

print_game_state(indicators, policies)
print()

nhs_funding.update_value(200)
tobacco_tax.update_value(200)
propagate_change(nhs_funding)
propagate_change(tobacco_tax)

print_game_state(indicators, policies)

print(health.valueHistory)
print(health.changeHistory)
