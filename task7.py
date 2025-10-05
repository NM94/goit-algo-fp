import random
import matplotlib.pyplot as plt
import pandas as pd


num_rolls = 1_000_0  

results = [0] * 13  

for _ in range(num_rolls):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    s = dice1 + dice2
    results[s] += 1

monte_carlo_probs = {s: results[s] / num_rolls * 100 for s in range(2, 13)}

analytic_probs = {
    2: 1/36*100,
    3: 2/36*100,
    4: 3/36*100,
    5: 4/36*100,
    6: 5/36*100,
    7: 6/36*100,
    8: 5/36*100,
    9: 4/36*100,
    10: 3/36*100,
    11: 2/36*100,
    12: 1/36*100
}

data = {
    "Сума": list(range(2, 13)),
    "Монте-Карло, %": [round(monte_carlo_probs[s], 2) for s in range(2, 13)],
    "Аналітична, %": [round(analytic_probs[s], 2) for s in range(2, 13)],
    "Відхилення, %": [round(monte_carlo_probs[s] - analytic_probs[s], 2) for s in range(2, 13)]
}

df = pd.DataFrame(data)
print(df)

plt.figure(figsize=(10,6))
plt.plot(df["Сума"], df["Аналітична, %"], marker='o', label='Аналітична ймовірність')
plt.bar(df["Сума"], df["Монте-Карло, %"], alpha=0.6, label='Монте-Карло')
plt.title(f"Порівняння ймовірностей при кидках 2 кубиків ({num_rolls:,} симуляцій)")
plt.xlabel("Сума на кубиках")
plt.ylabel("Ймовірність (%)")
plt.legend()
plt.grid(True)
plt.show()
