import networkx as nx
from indicator import Indicator

def propagate_changes(G):
  try:
    topological_order = list(nx.topological_sort(G))
  except nx.NetworkXUnfeasible:
    print("Could not find a valid topological order, check there is no cycle in the graph")

  for node in topological_order:
    if isinstance(node, Indicator):
      updated_value = node.default_value
      for pred in G.predecessors(node):
        formula = G[pred][node]['formula']
        effect = eval(formula, {}, { 'x': pred.value})
        updated_value += effect
      node.set_value(updated_value)
