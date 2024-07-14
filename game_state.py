from indicator import Indicator
from policy import Policy
from voter_group import VoterGroup

# Voter groups
capitalists = VoterGroup('Capitalists', 0.5, 0.5, 0.7)
socialists = VoterGroup('Socialists', 0.5, 0.5, 0.3)
voter_groups = [capitalists, socialists]

# Policies
nhs_funding = Policy('NHS Funding', 100)
tobacco_tax = Policy('Tobacco Tax', 100)

# Indicators
health = Indicator('Health', 100)
unemployment = Indicator('Unemployment', 100)
poverty = Indicator('Poverty', 100)
tobacco_usage = Indicator('Tobacco Usage', 100)
private_health_care = Indicator('Private Health Care', 100)

nhs_funding.register_effect(health, 0.1)
nhs_funding.register_effect(private_health_care, -0.25)
nhs_funding.register_effect(unemployment, -0.05)
nhs_funding.register_effect(poverty, -0.13)
tobacco_tax.register_effect(tobacco_usage, -0.05)
tobacco_usage.register_effect(health, -0.18)
nhs_funding.register_effect(capitalists.happiness, -0.03)
nhs_funding.register_effect(socialists.happiness, 0.12)
nhs_funding.register_effect(socialists.membership, 0.01)

game_state = {
  'indicators': {
    'health': health,
    'unemployment': unemployment,
    'poverty': poverty,
    'tobacco_usage': tobacco_usage,
    'private_health_care': private_health_care
  },
  'policies': {
    'nhs_funding': nhs_funding,
    'tobacco_tax': tobacco_tax
  },
  'voter_groups': {
    'capitalists': capitalists,
    'socialists': socialists
  }
}