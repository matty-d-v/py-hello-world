
msg = "Hello world!"
print(msg)

# And now for something more interesting..

def find_first_odd_total_values(inputVals):
    for val in inputVals:
        if (inputVals.count(val) % 2) != 0:
            return (val)

inputVals = [1,2,2,3,3,3,4,3,3,3,2,2,1]
print(find_first_odd_total_values(inputVals))
