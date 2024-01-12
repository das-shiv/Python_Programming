def divisor(x):
    def divident(y):
        return y/x
    return divident

div = divisor(2)

result = div(10)
print(result)