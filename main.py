
from indicator import Indicator
from policy import Policy
from display import display_game_state
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

try:
  topological_order = list(nx.topological_sort(G))
except nx.NetworkXUnfeasible:
  print("Could not find a valid topological order, check there is no cycle in the graph")

for node in topological_order:
  if isinstance(node, Indicator):
    updated_value = node.default_value
    for pred in G.predecessors(node):
      formula = G[pred][node]['formula']
      effect = eval(formula, {}, { 'x': pred.value})
      updated_value += effect
    node.set_value(updated_value)

display_game_state(indicators, policies)
