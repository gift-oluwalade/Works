def recursive_search(numbers, target, index):
    """
    Recursively search for a target number in a list of numbers
    :param numbers: list of numbers
    :param target: target number to search for
    :param index: current index in the list
    :return: True if target is found, False otherwise
    """

    # If the list is empty, the target is not found
    if not numbers:
        return False

    # If the target is found, return True
    elif numbers[index] == target:
        return True

    # If the target is not found at the current index, recursively search the rest of the list
    else:
        return recursive_search(numbers[:index] + numbers[index + 1:], target, index)

# Example usage
numbers = [1, 2, 3, 4, 5]
target = 3
index = 2

found = recursive_search(numbers, target, index)
print(f'Target {target} found: {found}')