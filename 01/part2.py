'''
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
'''

nums = []

with open('./input.txt') as f:
    for l in f.readlines():
        nums.append(int(l))

def solve():
    for num in nums:
        for num2 in nums:
            for num3 in nums:
                if num + num2 + num3 == 2020:
                    return num * num2 * num3

print(solve())
