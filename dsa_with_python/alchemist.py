def get_cost(potion, recipes, memo):
    if potion not in recipes:
        return 0
    if potion in memo:
        return memo[potion]

    min_cost = float("inf")
    for recipe in recipes[potion]:
        cost = len(recipe) - 1
        for ing in recipe:
            cost += get_cost(ing, recipes, memo)
        min_cost = min(min_cost, cost)

    memo[potion] = min_cost
    return min_cost

n = int(input().strip())
recipes = {}

for _ in range(n):
    line = input().strip()
    potion, ingredients = line.split("=")
    potion = potion.strip()
    ingredients = [x.strip() for x in ingredients.split("+")]
    if potion not in recipes:
        recipes[potion] = []
    recipes[potion].append(ingredients)

desired_potion = input().strip()
print(get_cost(desired_potion, recipes, {}))
