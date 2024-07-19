
from indicator import Indicator
from policy import Policy
import yaml

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
    value['default_value']
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

print(policies)