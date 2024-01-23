# Thuật toán sắp xếp nổi bọt
def bubbleSort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1 - i):
            if array[j]>array[j+1]:                             # thứ tự từ nhỏ đến lớn
                array[j], array[j+1] = array[j+1], array[j]     # swap
    return array

arr = [7, 3, 9, 2, 0, 4, 8, 1, 6, 5]
print(bubbleSort(arr))

