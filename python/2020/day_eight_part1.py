filename = "inputs\\2020\\input-day8.txt"
with open(filename) as f:
    lines = f.readlines()

accumulator = 0

executionIndex = 0
setOfRunInstructions = []

while executionIndex not in setOfRunInstructions:
    print("Execution index: " + str(executionIndex)+ " accumulator: " + str(accumulator)+ " instruction: "+ lines[executionIndex])
    setOfRunInstructions.append(executionIndex)
    instructionLine = lines[executionIndex]
    instructionParts = instructionLine.split(" ")
    instruction = instructionParts[0]
    argument = instructionParts[1]
    if instruction == "nop":
        executionIndex += 1
    elif instruction == "acc":
        accumulator += int(argument)
        executionIndex += 1
    else:
        executionIndex += int(argument)

print("Loop detected on line: " + str(executionIndex) + " accumulator value: " + str(accumulator))