def solution(array_a, array_b):
    sum_MRE = 0
    len_array = len(array_a)
    for i in range(len_array):
        sum_MRE += (array_a[i] - array_b[i]) ** 2

    return sum_MRE / len_array

array_1 = [1, 2 ,3]
array_2 = [4, 5, 6]

print(solution(array_1, array_2))