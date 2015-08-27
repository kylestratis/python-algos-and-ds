def convert_to_binary(integer):
    if integer >= 0:
        remainder = integer % 2
        divided = integer / 2
        if divided != 0:
            return str(convert_to_binary(divided)) + str(remainder)
        else:
            return str(remainder)
    else:
        return convert_to_binary(2 ** 32 - (integer * -1))

print convert_to_binary(4)
print convert_to_binary(2)
print convert_to_binary(16)
print convert_to_binary(5)
print convert_to_binary(-4)