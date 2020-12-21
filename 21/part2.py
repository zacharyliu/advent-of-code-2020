'''
Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient contains which allergen.

In the above example:

mxmxvkd contains dairy.
sqjhc contains fish.
fvjkl contains soy.
Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical dangerous ingredient list. (There should not be any spaces in your canonical dangerous ingredient list.) In the above example, this would be mxmxvkd,sqjhc,fvjkl.

Time to stock your raft with supplies. What is your canonical dangerous ingredient list?
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

    resolved = []
    while allergen_map:
        found = None
        for allergen, ingredients in allergen_map.items():
            if len(ingredients) == 1:
                found = list(ingredients)[0]
                resolved.append((allergen, found))
                del allergen_map[allergen]
                break

        assert found is not None
        for allergen in allergen_map.keys():
            if found in allergen_map[allergen]:
                allergen_map[allergen].remove(found)

    resolved.sort()

    return ','.join(x[1] for x in resolved)


print(run())
