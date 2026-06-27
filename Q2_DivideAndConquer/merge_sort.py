recursive_calls = 0

def merge_sort(transactions):

    global recursive_calls
    recursive_calls += 1

    # Base Case
    if len(transactions) <= 1:
        return transactions

    mid = len(transactions) // 2

    left_half = merge_sort(transactions[:mid])
    right_half = merge_sort(transactions[mid:])

    return merge(left_half, right_half)

def merge(left, right):

    sorted_list = []

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index].transaction_id < right[right_index].transaction_id:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # Add remaining items from left
    while left_index < len(left):
        sorted_list.append(left[left_index])
        left_index += 1

    # Add remaining items from right
    while right_index < len(right):
        sorted_list.append(right[right_index])
        right_index += 1

    return sorted_list