## NAME: HASSAN ADNAN
## UCID: 30217418

## QUESTION 1
threshold = 100
product = 1
currentNumber = 1

while product <= threshold:
    product = product * currentNumber
    currentNumber = currentNumber + 1

numberThatExceeded = currentNumber - 1
print("Final product:", product)
print("Integer that caused product to exceed threshold:", numberThatExceeded)
