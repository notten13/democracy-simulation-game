from simulation_objects import Indicator, Policy, VoterGroup, define_influence
from propagate_change import propagate_change
from display import print_game_state

# Voter groups
capitalists = VoterGroup('Capitalists', 0.45, 0.5, 0.7)
socialists = VoterGroup('Socialists', 0.7, 0.65, 0.3)
voter_groups = [capitalists, socialists]

# Policies
nhs_funding = Policy('NHS Funding', 100)
tobacco_tax = Policy('Tobacco Tax', 100)
policies = [nhs_funding, tobacco_tax]

# Indicators
health = Indicator('Health', 100)
unemployment = Indicator('Unemployment', 100)
poverty = Indicator('Poverty', 100)
tobacco_usage = Indicator('Tobacco Usage', 100)
private_health_care = Indicator('Private Health Care', 100)
indicators = [health, private_health_care, unemployment, poverty, tobacco_usage]

define_influence(nhs_funding, health, 0.1)
define_influence(nhs_funding, private_health_care, -0.25)
define_influence(nhs_funding, unemployment, -0.05)
define_influence(nhs_funding, poverty, -0.13)
define_influence(tobacco_tax, tobacco_usage, -0.05)
define_influence(tobacco_usage, health, -0.18)
define_influence(nhs_funding, capitalists.happiness, -0.03)
define_influence(nhs_funding, socialists.happiness, 0.3)
define_influence(nhs_funding, socialists.membership, 0.03)

print_game_state(indicators, policies, voter_groups)
print()

nhs_funding.update_value(200)
tobacco_tax.update_value(200)
propagate_change(nhs_funding)
propagate_change(tobacco_tax)

print_game_state(indicators, policies, voter_groups)

print(health.valueHistory)
print(health.changeHistory)
