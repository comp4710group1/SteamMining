from efficient_apriori import apriori
transactions = [('eggs', 'bacon', 'soup'),
                ('eggs', 'bacon', 'apple'),
                ('soup', 'bacon', 'banana')]

itemsets, rules = apriori(transactions, min_support=0.5, min_confidence=1)
# print(rules)  # [{eggs} -> {bacon}, {soup} -> {bacon}]
print(itemsets)

for item in itemsets:
  for t in item:
    print(t)

# test = ('eggs', 'bacon', 'soup')
# for t in test:
#   print(t)

# itemsets, rules = apriori(transactions, min_support=0.2, min_confidence=1)

# Print out every rule with 2 items on the left hand side,
# 1 item on the right hand side, sorted by lift
# rules_rhs = filter(lambda rule: len(rule.lhs) == 2 and len(rule.rhs) == 1, rules)
# for rule in sorted(rules_rhs, key=lambda rule: rule.lift):
#   print(rule)

# transactions = [('eggs', 'bacon', 'soup'),
#                 ('eggs', 'bacon', 'apple'),
#                 ('soup', 'bacon', 'banana')]
# itemsets, rules = apriori(transactions, output_transaction_ids=True)
# print(itemsets)