def solution(sequence, k):
    if k in sequence:
        return [sequence.index(k), sequence.index(k)]

    start, end = 0, 1
    current_sum = sequence[start] + sequence[end]
    result = [start, len(sequence) - 1]

    while end < len(sequence) and start < len(sequence):
        if current_sum == k:
            if (result[1] - result[0]) > (end - start):
                result = [start, end]
            
            # After updating the result, move the start pointer to adjust the sum
            current_sum -= sequence[start]
            start += 1

        elif current_sum < k:
            end += 1
            if end < len(sequence):  # Avoid IndexError
                current_sum += sequence[end]
        else:  # current_sum > k
            current_sum -= sequence[start]
            start += 1

            if start == end and end < len(sequence) - 1: 
                end += 1
                current_sum += sequence[end]

    return result