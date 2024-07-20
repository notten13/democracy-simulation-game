
from indicator import Indicator
from policy import Policy
from voter_group import VoterGroup
from display import display_game_state
from propagate_changes import propagate_changes
import yaml
import networkx as nx

def read_yaml_file(file_path):
  with open(file_path, 'r') as file:
    data = yaml.safe_load(file)
  return data

indicators_config = read_yaml_file('config/indicators.yml')
policies_config = read_yaml_file('config/policies.yml')
voter_groups_config = read_yaml_file('config/voter_groups.yml')

indicators = {}
for key, value in indicators_config['indicators'].items():
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
for key, value in policies_config['policies'].items():
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

voter_groups = {}
for key, value in voter_groups_config['voter_groups'].items():
  voter_groups[key] = VoterGroup(
    key,
    value['name'],
    value['description'],
    value['default_membership'],
    value['default_happiness'],
    value['happiness_causes']
)

G = nx.DiGraph()

for key, value in indicators.items():
  G.add_node(value)

for key, value in policies.items():
  G.add_node(value)

for key, value in voter_groups.items():
  G.add_node(value.membership)
  G.add_node(value.happiness)

for key, value in indicators.items():
  for cause in value.causes:
    # Find node by key in graph
    cause_node = indicators[cause['key']] if cause['key'] in indicators else policies[cause['key']]
    G.add_edge(cause_node, value, formula=cause['formula'], inertia=cause['inertia'])

for key, value in voter_groups.items():
  for cause in value.happiness.causes:
    cause_node = indicators[cause['key']] if cause['key'] in indicators else policies[cause['key']]
    G.add_edge(cause_node, value.happiness, formula=cause['formula'], inertia=cause['inertia'])
  for cause in value.membership.causes:
    cause_node = indicators[cause['key']] if cause['key'] in indicators else policies[cause['key']]
    G.add_edge(cause_node, value.membership, formula=cause['formula'], inertia=cause['inertia'])

propagate_changes(G)

print('====================================')
print('======== Initial game state ========')
print('====================================\n')
display_game_state(indicators, policies, voter_groups)
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
  display_game_state(indicators, policies, voter_groups)
  print()
  
print('Game over!')
