
def bubble_sort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
    return alist


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum = passnum - 1


def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

    while position > 0 and alist[position - 1] > currentvalue:
        alist[position] = alist[position - 1]
        position = position - 1

    alist[position] = currentvalue


def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


def mergeSort(alist):
    # print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        # print(f"mid = {mid}")
        lefthalf = alist[:mid]
        # print(f"lefthalf = {lefthalf}")
        righthalf = alist[mid:]
        # print(f"righthalf = {righthalf}")

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        # print("Merging ", lefthalf, righthalf)
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                # print(f"alist = {alist}")
                i = i + 1
                # print(f"i = {i}")

            else:
                alist[k] = righthalf[j]
                # print(f"alist = {alist}")
                j = j + 1
                # print(f"j = {j}")
            k = k + 1
            # print(f"k = {k}")

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            # print(f"alist = {alist}")
            i = i + 1
            k = k + 1
            # print(f"i = {i} k = {k}")

        while j < len(righthalf):
            alist[k] = righthalf[j]
            # print(f"alist = {alist}")
            j = j + 1
            k = k + 1
            # print(f"j = {j} k = {k}")
        print("Merged ", alist)
