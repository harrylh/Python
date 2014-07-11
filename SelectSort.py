#!/bin/python

def SelectSort(arr):

   if len(arr) == 0:
      return -1
   
   for i in range(0, len(arr)):
      min = i
      for j in range(i+1, len(arr)):
         if arr[min] > arr[j]:
            min = j    

      if min != i :
         arr[min], arr[i] = arr[i], arr[min]
      #print(arr)

if __name__ == '__main__':
   arr = [2, 1, 4, 3, 7, 9, 10, 5, 12, 6, 30, 15]

   SelectSort(arr)
   print(arr)

   #[1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 15, 30]
