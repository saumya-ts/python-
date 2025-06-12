class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1  

        large = float('-inf')
        slarge = float('-inf')

        for i in arr:
            if i > large:
                slarge = large
                large = i
            elif i > slarge and i != large:
                slarge = i

        if slarge == float('-inf'):
            return -1  
        else:
            return slarge



arr = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    element = int(input("Enter array element: "))
    arr.append(element)

solution = Solution()
slarge = solution.getSecondLargest(arr)
print("Second largest element:", slarge)
