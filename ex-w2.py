import re
hand = open('regex_sum_738834.txt')

# create a list of numbers
nums = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    if len(x) > 0:  # only code runs x is not empty
        for num in x:  # x is a list of strings, which are actually numbers
            # string to int, and added to the list 'nums'
            nums.append(int(num))

print(sum(nums))  # print the sum of elemetns in 'nums'
