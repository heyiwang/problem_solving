from Stack import Stack
# Judge if balanced parentheses
def parCheck(parString):
    st = Stack()
    balanced = True
    index = 0
    while index < len(parString) and balanced:
        s = parString[index]
        if s in "([{":
            st.push(s)
        else:
            if st.isEmpty():
                balanced = False
            else:
                top = st.pop()
                if not matches(top, s):
                    balanced = False
        index = index + 1

    if balanced and st.isEmpty():
        return True
    else:
        return False

def matches(op, cl):
    opens = "([{"
    closers = ")]}"
    return opens.index(op) == closers.index(cl)

print(parCheck('{[]}]'))
