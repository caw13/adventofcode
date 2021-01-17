def createMasks(maskInput):
    orMask = ""
    andMask = ""
    for i in range(len(maskInput)):
        if maskInput[i] == "X":
            orMask = orMask + "0"
            andMask = andMask + "1"
        else:
            orMask = orMask + maskInput[i]
            andMask = andMask + maskInput[i]
    return [orMask, andMask]

filename = "inputs\\2020\\input-day14.txt"
with open(filename) as f:
    lines = f.readlines()

mem = {}
masks = []
for line in lines:
    parts = line.strip().split(" = ")
    if parts[0] == "mask":
        masks = createMasks(parts[1])
    else:
        mem[parts[0]] = (int(parts[1]) & int(masks[1],2)) | int(masks[0],2)
print(str(mem))

result = 0
for value in mem.values():
    result += value

print("result: " + str(result))
