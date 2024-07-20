
from indicator import Indicator
from policy import Policy
from display import display_game_state
from propagate_changes import propagate_changes
import yaml
import networkx as nx

def read_yaml_file(file_path):
  with open(file_path, 'r') as file:
    data = yaml.safe_load(file)
  return data

indicatorsConfig = read_yaml_file('config/indicators.yml')
policiesConfig = read_yaml_file('config/policies.yml')

indicators = {}
for key, value in indicatorsConfig['indicators'].items():
  indicators[key] = Indicator(
    key,
    value['name'],
    value['description'],
    value['min_value'],
    value['max_value'],
    value['default_value'],
    value['causes']
)

policies = {}
for key, value in policiesConfig['policies'].items():
  policies[key] = Policy(
    key,
    value['name'],
    value['description'],
    value['min_value'],
    value['max_value'],
    value['default_value'],
    value['cost']['min'],
    value['cost']['max'],
    value['cost']['formula'],
    value['income']['min'],
    value['income']['max'],
    value['income']['formula']
)

G = nx.DiGraph()

for key, value in indicators.items():
  G.add_node(value)

for key, value in policies.items():
  G.add_node(value)

for key, value in indicators.items():
  for cause in value.causes:
    # Find node by key in graph
    cause_node = indicators[cause['key']] if cause['key'] in indicators else policies[cause['key']]
    G.add_edge(cause_node, value, formula=cause['formula'], inertia=cause['inertia'])

propagate_changes(G)

print('====================================')
print('======== Initial game state ========')
print('====================================\n')
display_game_state(indicators, policies)
print()

max_turns = 5
current_turn = 0

while current_turn < max_turns:
  current_turn += 1
  print(f'========================')
  print(f'======== Turn {current_turn} ========')
  print(f'========================\n')

  user_action = None
  while user_action != 0:
    print('What would you like to do?')
    print('0. End turn')
    print('1. Change a policy')
    user_action = int(input('Enter your choice: '))
    if user_action == 1:
      print('\nWhat policy would you like to change?')
      for i, policy in enumerate(policies.values()):
        print(f'{i + 1}. {policy.name}')
      policy_choice = int(input('Enter your choice: '))
      policy = list(policies.values())[policy_choice - 1]
      print(f'\nWhat level would you like to set {policy.name} to (between 0 and 1)?')
      level = float(input('Enter your choice: '))
      policy.set_value(level)
      print('Done!\n')

  propagate_changes(G)
  display_game_state(indicators, policies)
  print()
  
print('Game over!')
