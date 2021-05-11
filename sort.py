import operator
def heap_sort(seq):
    s = seq
    sequence_length = len(s)


    def swap_ASC_by_index(i, j):
        if s[i] < s[j]:
            s[i], s[j] = s[j], s[i]

    def greater_value_index(a, b):
        if s[a] > s[b]:
            return a
        return b

    def shift_down(begin, end):
        while begin * 2 + 2 < end:
            gt_val_index = greater_value_index(begin * 2 + 1, begin * 2 + 2)
            swap_ASC_by_index(begin, gt_val_index)
            begin = gt_val_index


    for i in range((sequence_length // 2) - 1, -1, -1):
        shift_down(i, sequence_length)

    for i in range(sequence_length - 1, 0, -1):
        swap_ASC_by_index(i, 0)
        shift_down(0, i)
    return s


def bubble_sort(seq):
    sequence = seq
    sequence_length = len(sequence)

    for i in range(sequence_length-1):
        for j in range(sequence_length-i-1):
            if sequence[j] > sequence[j+1]:
                buff = sequence[j]
                sequence[j] = sequence[j+1]
                sequence[j+1] = buff
    return sequence


def Merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = Merge_sort(L[:middle], compare)
        right = Merge_sort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result