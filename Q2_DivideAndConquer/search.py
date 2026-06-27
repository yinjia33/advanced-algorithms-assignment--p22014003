def binary_search(transactions, target_id):

    left = 0
    right = len(transactions) - 1

    while left <= right:

        mid = (left + right) // 2

        if transactions[mid].transaction_id == target_id:
            return transactions[mid]

        elif transactions[mid].transaction_id < target_id:
            left = mid + 1

        else:
            right = mid - 1

    return None

def linear_search(transactions, target_id):

    for transaction in transactions:

        if transaction.transaction_id == target_id:
            return transaction

    return None