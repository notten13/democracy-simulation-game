def display_game_state(indicators, policies):
  print('Indicators:')
  for indicator in indicators.values():
    print(f'  {indicator.name}: {indicator.value}')
  print('Policies:')
  for policy in policies.values():
    print(f'  {policy.name}:')
    print(f'    Level: {policy.value}')
    # print(f'    Cost: {policy.cost}')
    # print(f'    Income: {policy.income}')
  # print('Voter Groups:')
  # for voter_group in game_state['voter_groups'].values():
  #   print(f'{voter_group.name}:')
  #   print(f'  Membership: {voter_group.membership.value}')
  #   print(f'  Happiness: {voter_group.happiness.value}')
  #   print(f'  Income: {voter_group.income.value}')
  # print('Popularity:')
  # total_popularity = 0
  # total_membership = 0
  # for voter_group in game_state['voter_groups'].values():
  #   total_popularity += voter_group.membership.value * voter_group.happiness.value
  #   total_membership += voter_group.membership.value
  # print(total_popularity / total_membership)