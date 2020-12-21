'''
You reach the train's last stop and the closest you can get to your vacation island without getting wet. There aren't even any boats here, but nothing can stop you now: you build a raft. You just need a few days' worth of food for your journey.

You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens are listed in a language you do understand. You should be able to use this information to determine which ingredient contains which allergen and work out which foods are safe to take with you on your trip.

You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that food's ingredients list followed by some or all of the allergens the food contains.

Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. Allergens aren't always marked; when they're listed (as in (contains nuts, shellfish) after an ingredients list), the ingredient that contains each listed allergen will be somewhere in the corresponding ingredients list. However, even if an allergen isn't listed, the ingredient that contains that allergen could still be present: maybe they forgot to label it, or maybe it was labeled in a language you don't know.

For example, consider the following list of foods:

mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
The first food in the list has four ingredients (written in a language you don't understand): mxmxvkd, kfcds, sqjhc, and nhms. While the food might contain other allergens, a few allergens the food definitely contains are listed afterward: dairy and fish.

The first step is to determine which ingredients can't possibly contain any of the allergens in any food in your list. In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. Counting the number of times any of these ingredients appear in any ingredients list produces 5: they all appear once each except sbzzf, which appears twice.

Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do any of those ingredients appear?
'''

from collections import defaultdict


def run():
    allergen_map = {}
    counts = defaultdict(int)
    with open('./input.txt') as f:
        for l in f.readlines():
            l = l.strip()
            l = l.replace(')', '')
            ingredients, allergens = l.split(' (contains ')
            ingredients = ingredients.split(' ')
            allergens = allergens.split(', ')

            for a in allergens:
                if a in allergen_map:
                    allergen_map[a] = allergen_map[a] & set(ingredients)
                else:
                    allergen_map[a] = set(ingredients)

            for i in ingredients:
                counts[i] += 1

    resolved = {}
    while allergen_map:
        found = None
        for allergen, ingredients in allergen_map.items():
            if len(ingredients) == 1:
                found = list(ingredients)[0]
                resolved[found] = allergen
                del allergen_map[allergen]
                break

        assert found is not None
        for allergen in allergen_map.keys():
            if found in allergen_map[allergen]:
                allergen_map[allergen].remove(found)

    non_allergens = []
    for i in counts.keys():
        if i not in resolved:
            non_allergens.append(i)

    return sum(counts[i] for i in non_allergens)


print(run())
