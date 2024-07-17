
from propagate_change import propagate_change
from display import print_game_state
from game_state import game_state

print_game_state(game_state)
print()

state_health_service = game_state['policies']['state_health_service']
state_health_service.level.update_value(0.7)

propagate_change(state_health_service.level)

print_game_state(game_state)
print()
