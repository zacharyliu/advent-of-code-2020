'''

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?
'''

target = 70639851


def data():
    nums = []
    with open('./input.txt') as f:
        for l in f.readlines():
            nums.append(int(l))
            while sum(nums) > target and len(nums) > 2:
                nums.pop(0)
            if sum(nums) == target:
                return min(nums) + max(nums)


print(data())
