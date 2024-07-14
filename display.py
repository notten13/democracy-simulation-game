def print_game_state(game_state):
  print('Indicators:')
  for indicator in game_state['indicators'].values():
    print(f'  {indicator.name}: {indicator.value}')
  print('Policies:')
  for policy in game_state['policies'].values():
    print(f'  {policy.name}: {policy.value}')
  print('Voter Groups:')
  for voter_group in game_state['voter_groups'].values():
    print(f'{voter_group.name}:')
    print(f'  Membership: {voter_group.membership.value}')
    print(f'  Happiness: {voter_group.happiness.value}')
    print(f'  Income: {voter_group.income.value}')
    print()
  print('Popularity:')
  total_popularity = 0
  total_membership = 0
  for voter_group in game_state['voter_groups'].values():
    total_popularity += voter_group.membership.value * voter_group.happiness.value
    total_membership += voter_group.membership.value
  print(total_popularity / total_membership)