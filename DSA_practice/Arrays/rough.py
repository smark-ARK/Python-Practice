class Solution:
    def __init__(self):
        self.eve = []
        self.od = []

    def segregateEvenOdd(self, arr, n):
        for i in range(0, n):
            if len(arr) == 0:
                break
            if arr[i] % 2 != 0:
                self.od.append(arr[i])
            else:
                self.eve.append(arr[i])
        self.quickSort(self.od)
        self.quickSort(self.eve)
        for j in range(0, len(self.eve)):
            arr[j] = self.eve[j]
        k = 0
        for i in range(len(self.eve), len(self.eve) + len(self.od)):
            if k < len(self.od):
                arr[i] = self.od[k]
                k += 1
            else:
                break

    def quickSort(self, alist):
        self.quickSortHelper(alist, 0, len(alist) - 1)

    def quickSortHelper(self, alist, first, last):
        if first < last:

            splitpoint = self.partition(alist, first, last)

            self.quickSortHelper(alist, first, splitpoint - 1)
            self.quickSortHelper(alist, splitpoint + 1, last)

    def partition(self, alist, first, last):
        pivotvalue = alist[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark


s = Solution()
arr = [12, 34, 45, 9, 8, 90, 3]
s.segregateEvenOdd(arr, len(arr))
for x in arr:
    print(x, end=" ")

print()
