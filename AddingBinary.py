
def add_numbers(num1, num2):

    if len(num2) > len(num1):
        temp = num2
        num2 = num1
        num1 = temp

    while len(num2) < len(num1):
        num2 = '0' + num2

    carry = '0'
    ret = ""
    for i in range(0, len(num2)):
        char1 = num1[len(num1) - i - 1]
        char2 = num2[len(num2) - i - 1]
        if char1 == char2:
            ret = carry + ret
            carry = char1
        else:
            if carry == '1':
                ret = '0' + ret
            else:
                ret = '1' + ret
                carry = '0'
    if carry == '1':
        ret = '1' + ret
    return ret


assert add_numbers("1001", "11") == "1100"
assert add_numbers("101010", "11011") == "1000101"
assert add_numbers("11", "1001") == "1100"
