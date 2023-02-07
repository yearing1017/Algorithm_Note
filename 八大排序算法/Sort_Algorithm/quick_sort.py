def quick_sort(arr, left, right):
    if left > right:
        return
    l = left
    r = right
    pivot = arr[l]

    while l < r:
        while l < r and arr[r] >= pivot:
            r -= 1
        arr[l] = arr[r]

        while l < r and arr[l] <= pivot:
            l += 1
        arr[r] = arr[l]
    arr[l] = pivot
    quick_sort(arr, left, l-1)
    quick_sort(arr, l+1, right)

    return arr


if __name__ == "__main__":
    arr = [9,4,1,6,8,3]
    arr_sort = quick_sort(arr, 0, len(arr)-1)
    print(arr_sort)
