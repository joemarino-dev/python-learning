income = 250_000
lowtaxland_rate = 0.05 #5% rate in Lowtaxland
ripoffland_rate = 0.43 #43% rate in Ripoffland
lowtaxland_amount = income * lowtaxland_rate
ripoffland_amount = income * ripoffland_rate

print(f'Your income is {income} and you would pay {lowtaxland_amount} income tax in Lowtaxland or {ripoffland_amount} income tax in Ripoffland. You would save {ripoffland_amount - lowtaxland_amount} by paying taxes in Lowtaxland!')
