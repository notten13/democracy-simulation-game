def print_game_state(indicators, policies, voter_groups):
  print('Indicators:')
  for indicator in indicators:
    print(f'  {indicator.name}: {indicator.value}')
  print('Policies:')
  for policy in policies:
    print(f'  {policy.name}: {policy.value}')
  print('Voter Groups:')
  for voter_group in voter_groups:
    print(f'{voter_group.name}:')
    print(f'  Membership: {voter_group.membership.value}')
    print(f'  Happiness: {voter_group.happiness.value}')
    print(f'  Income: {voter_group.income.value}')
    print()
  print('Popularity:')
  total_popularity = 0
  total_membership = 0
  for voter_group in voter_groups:
    total_popularity += voter_group.membership.value * voter_group.happiness.value
    total_membership += voter_group.membership.value
  print(total_popularity / total_membership)