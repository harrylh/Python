#!/bin/python

def QuickSort(arr, l, r): # l: left of arr[], r: right of arr[]

   if len(arr) == 0:
      return -1
   
   if l <= r:
      left = l
      right = r

      x = arr[left]  # take first number as  pivot 

      
      while left < right:     
         while left < right and arr[right] > x:
            right -= 1
         if left < right:
            arr[left] = arr[right]
            left += 1

         while left < right and arr[left] < x:
            left += 1
         if left < right:
            arr[right] = arr[left]
            right -= 1
      
      arr[left] = x   
      
      QuickSort(arr, l, left-1)
      QuickSort(arr, left+1, r)


if __name__ == '__main__':
   arr = [2, 1, 4, 3, 7, 9, 10, 5, 12, 6, 30, 15]
   QuickSort(arr, 0, len(arr)-1)
   print(arr)
