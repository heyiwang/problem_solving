from Stack import Stack

def divideBy2(decNumber):
    sta = Stack()
    while decNumber > 0:
        remains = decNumber % 2
        sta.push(remains)
        decNumber = decNumber // 2

    binString = ""
    while not sta.isEmpty():
        binString = binString + str(sta.pop())

    return binString

print(divideBy2(3))