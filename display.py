def print_game_state(indicators, policies):
  print('Indicators:')
  for indicator in indicators:
    print(f'{indicator.name}: {indicator.value}')
  print('Policies:')
  for policy in policies:
    print(f'{policy.name}: {policy.value}')