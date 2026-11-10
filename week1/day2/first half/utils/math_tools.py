def add(a,b):
    return a+b

result = add(10,20)

print(result)


def average(numbers):
    if not numbers:
        return 0

    return sum(numbers)/len(numbers)



if __name__ == "__main.py__":
    print("Testing math_tools module")
    print("Add:", add(10, 20))
    print("Average:", average([10, 20, 30]))