array = list(map(int, input("Последовательно введите числа через пробел:  ").split()))

def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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

array = merge_sort(array)
print(array)

while True:
    try:
        element = int(input("Введите число из списка: "))
        if element < min(array) or element > max(array):
            print("УПС! Это число не входит в список")
        if element <= 0:
            raise Exception
        break
    except ValueError:
        print("Ошибка: Введите целое число.")
    except Exception:
        print("Ошибка: Введите положительное число!")

def search_num(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return search_num(array, element, left, middle - 1)
    else:
        return search_num(array, element, middle + 1, right)

print(search_num(array, element, 0, len(array) - 1))