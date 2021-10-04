# 선택 정렬 함수
def selectionSort(array):
    for i in range(len(array)):
        lowestNumberIndex = i # 가장 작은 값의 인덱스를 저장하는 변수
        for j in range(i+1, len(array)): # j는 i+1 인덱스부터 시작하면 됨

            # array[i+1] < array[i]
            ## 그러니까 뒤에 있는 애가 앞에 있는 애보다 작은지 판별해서 더 작으면 j를 lowestNumberIndex로 대입
            if array[j] < array[lowestNumberIndex]:
                lowestNumberIndex = j


        if lowestNumberIndex != j:
            temp = array[i]
            array[i] = array[lowestNumberIndex]
            array[lowestNumberIndex] = temp
    return array
