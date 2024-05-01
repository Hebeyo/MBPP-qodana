def second_smallest(numbers):
    if len(numbers)<2:
        return
    if len(numbers)==2 and numbers[0] == numbers[1]:
        return
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[1]
