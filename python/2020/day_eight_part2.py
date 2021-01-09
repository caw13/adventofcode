def runProgram(programLines,swapLine):
    result = [False,0]
    accumulator = 0

    executionIndex = 0
    setOfRunInstructions = []

    while (executionIndex not in setOfRunInstructions) and (executionIndex < len(programLines)):
        #print("Execution index: " + str(executionIndex)+ " accumulator: " + str(accumulator)+ " instruction: "+ programLines[executionIndex])
        setOfRunInstructions.append(executionIndex)
        instructionLine = programLines[executionIndex]
        instructionParts = instructionLine.split(" ")
        instruction = instructionParts[0]
        if executionIndex == swapLine:
            if instruction == "nop":
                instruction = "jmp"
            else:
                instruction = "nop"
        argument = instructionParts[1]
        if instruction == "nop":
            executionIndex += 1
        elif instruction == "acc":
            accumulator += int(argument)
            executionIndex += 1
        else:
            executionIndex += int(argument)
    if executionIndex in setOfRunInstructions:
        print("Loop detected on line: " + str(executionIndex) + " accumulator value: " + str(accumulator))
        return result
    else:
        print("program executed successfully")
        return [True,accumulator]

filename = "inputs\\2020\\input-day8.txt"
with open(filename) as f:
    originalProgramLines = f.readlines()

# Go through program swapping each nop/jmp and executing program to see if corrected
# If still incorrect continue to look for a different instruction to swap
curLine = 0
result = [False,0]
while not result[0]:
    instructionLine = originalProgramLines[curLine]
    if instructionLine.startswith("nop") or instructionLine.startswith("jmp"):
        result = runProgram(originalProgramLines,curLine)
    curLine += 1

print("When fixed, accumlator value is: " + str(result[1]))
