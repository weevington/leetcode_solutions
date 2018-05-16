


def multiply(num1, num2):
    """
    :return:
    :type num1: str
    :type num2: str
    :rtype: str
    """
    retarray = [0] * (len(num1) + len(num2))


    for i, a in enumerate(num1[::-1]):
        carry = 0
        for k, b in enumerate(num2[::-1]):
            prod = (ord(b) - ord('0')) * (ord(a) - ord('0'))
            retarray[i + k] += prod
            retarray[i + k + 1] += retarray[i + k] / 10
            retarray[i + k] %= 10

    prodstring = []
    for q, val in enumerate(retarray[::-1]):
        prodstring.append(str(val))

    # find first non-zero
    p = 0
    for j, val in enumerate(prodstring):
        if (ord(val) - ord('0')) != 0:
            p = j
            break

    return ''.join(prodstring[p:])

def main():

    num1 = str("761")
    num2 = str("94")

    mystring = multiply(num1, num2)
    print "mystring = {0}".format(mystring)

if __name__ == "__main__":
    main()