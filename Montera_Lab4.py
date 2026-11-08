training_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

weight1 = 0
weight2 = 0
bias = 0
learning_rate = 0.1

def step_function(total):
    if total >= 0:
        return 1
    else:
        return 0

print("PERCEPTRON FOR OR GATE")
print("Initial values: weight 1 =", weight1, " weight 2 =", weight2, " bias =", bias)
print("Learning rate:", learning_rate)
print()

epoch = 1
while epoch <= 100:
    print("Epoch", epoch)
    errors = 0

    for row in training_data:
        a = row[0]
        b = row[1]
        target = row[2]

        total = (weight1 * a) + (weight2 * b) + bias
        output = step_function(total)
        error = target - output

        weight1 = weight1 + (learning_rate * error * a)
        weight2 = weight2 + (learning_rate * error * b)
        bias = bias + (learning_rate * error)

        if error != 0:
            errors = errors + 1

        print("  A =", a, " B =", b, " target =", target, " output =", output,
              " error =", error, " -> weight 1 =", round(weight1, 2), " weight 2 =", round(weight2, 2),
              " bias =", round(bias, 2))

    print()
    if errors == 0:
        print("No errors in this epoch, training stops here.")
        print("Total epochs:", epoch)
        print()
        break

    epoch = epoch + 1

print("Final weights: weight 1 =", round(weight1, 2), " weight 2 =", round(weight2, 2), " bias =", round(bias, 2))
print()

print("Testing the perceptron:")
print("A  B  | A OR B")
for row in training_data:
    a = row[0]
    b = row[1]
    result = step_function((weight1 * a) + (weight2 * b) + bias)
    print(a, " ", b, " |   ", result)