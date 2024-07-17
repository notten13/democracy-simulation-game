from indicator import Indicator
from policy import Policy
from voter_group import VoterGroup

# Voter groups
capitalists = VoterGroup('Capitalists', 0.5, 0.5, 0.7)
socialists = VoterGroup('Socialists', 0.5, 0.5, 0.3)

# Indicators
health = Indicator('Health', 100)
unemployment = Indicator('Unemployment', 100)
poverty = Indicator('Poverty', 100)
tobacco_usage = Indicator('Tobacco Usage', 100)
private_health_care = Indicator('Private Health Care', 100)
population = Indicator('Population', 65_000_000)

# Policies
state_health_service = Policy('State Health Service', 0.6, population.value * 3_200, 0)

population.register_effect(state_health_service.cost, 1)
state_health_service.level.register_effect(health, 0.1)
state_health_service.level.register_effect(private_health_care, -0.25)
state_health_service.level.register_effect(unemployment, -0.05)
state_health_service.level.register_effect(poverty, -0.13)
state_health_service.level.register_effect(capitalists.happiness, -0.03)
state_health_service.level.register_effect(socialists.happiness, 0.12)

game_state = {
  'indicators': {
    'health': health,
    'unemployment': unemployment,
    'poverty': poverty,
    'tobacco_usage': tobacco_usage,
    'private_health_care': private_health_care
  },
  'policies': {
    'state_health_service': state_health_service,
  },
  'voter_groups': {
    'capitalists': capitalists,
    'socialists': socialists
  }
}
