
from propagate_change import propagate_change
from display import print_game_state
from game_state import game_state

print_game_state(game_state)
print()

nhs_funding = game_state['policies']['nhs_funding']
nhs_funding.update_value(200)

tobacco_tax = game_state['policies']['tobacco_tax']
tobacco_tax.update_value(200)

propagate_change(nhs_funding)
propagate_change(tobacco_tax)

print_game_state(game_state)