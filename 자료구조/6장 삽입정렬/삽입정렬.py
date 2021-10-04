def insertion_sort(array):
    for index in range(1, len(array)):
        position = index # 삽입정렬은 처음에 인덱스를 다른 변수에 저장
        temp_value = array[index]

        while position > 0 and array[position-1] > temp_value:
            array[position] = array[position-1]
            position = position -1

        array[position] = temp_value
    return array


## 두 배열의 교집합을 구하는 프로그램
def intersection(first_array, second_array):
    result = []
    for i in range(len(first_array)):
        for j in range(len(second_array)):
            if first_array[i] == second_array[j]:
                result.append(first_array[i])
    return result