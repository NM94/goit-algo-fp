items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for name, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            chosen_items.append(name)
            total_cost += data['cost']
            total_calories += data['calories']
    return {
        "chosen_items": chosen_items,
        "total_cost": total_cost,
        "total_calories": total_calories
    }


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        for b in range(1, budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]
    
    chosen_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = names[i - 1]
            chosen_items.append(name)
            b -= items[name]["cost"]
    chosen_items.reverse()
    total_calories = dp[n][budget]
    total_cost = sum(items[i]["cost"] for i in chosen_items)
    return {
        "chosen_items": chosen_items,
        "total_cost": total_cost,
        "total_calories": total_calories
    }


budget = 100

greedy_result = greedy_algorithm(items, budget)
print("Жадібний")
print("Страви:", greedy_result["chosen_items"])
print("Сумарна вартість:", greedy_result["total_cost"])
print("Сумарна калорійність:", greedy_result["total_calories"])

print("\nДінамічний")
dp_result = dynamic_programming(items, budget)
print("Страви:", dp_result["chosen_items"])
print("Сумарна вартість:", dp_result["total_cost"])
print("Сумарна калорійність:", dp_result["total_calories"])
