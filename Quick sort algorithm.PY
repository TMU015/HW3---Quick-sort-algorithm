def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = array[start]
    left = start + 1
    right = end

    print(f"\n開始排序子陣列：{array[start:end+1]}")
    print(f"選擇基準值 pivot = {pivot}")

    while left <= right:
        while left <= right and array[left] <= pivot:
            left += 1
        while left <= right and array[right] >= pivot:
            right -= 1
        if left < right:
            print(f"交換 {array[left]} 和 {array[right]}")
            array[left], array[right] = array[right], array[left]

    print(f"交換基準值 {pivot} 和 {array[right]}")
    array[start], array[right] = array[right], array[start]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

data = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print(f"原始資料：{data}")
quick_sort(data, 0, 9)
print(f"\n排序後結果：{data}")