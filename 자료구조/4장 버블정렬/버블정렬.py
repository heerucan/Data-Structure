#버블 정렬 함수 구현
def bubble_sort1(list):
    #어떤 인덱스까지 아직 정렬되지 않았는지 기록
    unsorted_until_index = len(list) - 1

    #배열의 정렬 여부를 기록
    sorted = False

    #배열이 완전히 정렬됐음을 알 때까지 while 루프 실행

    while not sorted:
        #for루프는 배열의 첫 인덱스부터 아직 정렬되지 않은 인덱스까지 수행
        for i in range(unsorted_until_index):
            #모든 인접 값 쌍을 비교하고 순서가 뒤바뀌어 있으면 교환
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]

        #unsorted_until_index값을 1 감소
        unsorted_until_index = unsorted_until_index -1
        if unsorted_until_index == 0:
            sorted = True

#버블 정렬 실행
list1 = [65, 55, 45, 35, 25, 15, 10]
list2 = [1, 3, 65, 55, 45, 35, 25, 15, 10]

bubble_sort1(list1)
# print (list1)

bubble_sort1(list2)
# print (list2)



# 배열에 중복 값이 있는지 확인하는 프로그램
## 중첩 루프 사용
def hasDuplicateValue(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if (i != j) and array[i] == array[j]:
                return True
    return False


# 중첩 루프 사용하지 않음
def hasDuplicateValue2(array):
    existingNumbers = []
    for i in range(max(array)+1):
        existingNumbers.append("undefined")
        
    # print(len(existingNumbers), existingNumbers,"이거")
    for i in range(len(array)):
        if existingNumbers[array[i]] == "undefined":
            existingNumbers[array[i]] = 1
            print(len(existingNumbers), existingNumbers,"이거")

        else:
            print("중복있다.")
            return True
        # print(len(existingNumbers), existingNumbers,"이거")
    print("중복없어.")
    return False

myArray = [2, 3, 5, 3]
hasDuplicateValue2(myArray)
# print(len(myArray))