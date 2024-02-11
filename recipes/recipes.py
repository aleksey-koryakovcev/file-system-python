with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
                })
        file.readline()
        cook_book[dish] = ingredients
    print(cook_book)
print()
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity']
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += int(quantity)*person_count
            else:
                shop_list[ingredient_name] = {
                    'measure': measure,
                    'quantity': int(quantity)*person_count
                    }
    return shop_list
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))