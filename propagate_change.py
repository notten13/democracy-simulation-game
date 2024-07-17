from policy import PolicyCost, PolicyIncome

def propagate_change(start):
  queue = [start]

  while len(queue) > 0:
    current = queue.pop(0)
    for effect, weight in current.effects:
      new_value = effect.value + effect.value * current.changeHistory[-1] * weight
      if new_value < 0:
        new_value = 0
      effect.update_value(new_value)
      queue.append(effect)
