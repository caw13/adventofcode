filename = "inputs\\2020\\input-day1.txt"
with open(filename) as f:
    lines = f.readlines()
numbers = []
# Read the numbers
for line in lines:
    numbers.append(int(line))
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if (numbers[i] + numbers[j]) == 2020:
            print(numbers[i] * numbers[j])
            exit()

