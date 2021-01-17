def createMask(maskInput):
    orMask = ""
    for i in range(len(maskInput)):
        if maskInput[i] == "1":
            orMask = orMask + "1"
        else:
            orMask = orMask + "0"
    return orMask

def getSubAddresses(pos,mask,address):
    if pos == len(mask):
        return []
    else:
        subAddresses = getSubAddresses(pos+1,mask,address)
        if len(subAddresses) == 0:
            if mask[pos] == "X":
                return ["0","1"]
            else:
                return [address[pos]]
        else:
            result = []
            for subAddress in subAddresses:
                if mask[pos] == "X":
                    result.append("0" + subAddress)
                    result.append("1" + subAddress)
                else:
                    result.append(address[pos] + subAddress)
            return result

filename = "inputs\\2020\\input-day14.txt"
with open(filename) as f:
    lines = f.readlines()

mem = {}
numMask = ""
mask = ""
for line in lines:
    parts = line.strip().split(" = ")
    if parts[0] == "mask":
        mask = parts[1]
        numMask = createMask(parts[1])
        #print("Mask: " + mask)
        #print("numMask: " + numMask)
    else:
        origAddress = int(parts[0][4:len(parts[0])-1])
        address = bin((origAddress | int(numMask,2)))
        address = ("0" * (2+len(mask)-len(address))) + address[2:]
        #print("origAddr: " + str(origAddress) +" addr: " + str(address))
        addresses = getSubAddresses(0,mask,address)
        for addr in addresses:
            #print(int(addr,2))
            mem[int(addr,2)] = int(parts[1])
print(str(mem))

result = 0
for value in mem.values():
    result += value

print("result: " + str(result))
