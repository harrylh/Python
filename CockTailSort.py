#!/bin/python


def CockTailSort(arr):
   
   if len(arr) == 0:
      return -1
   
   i = 0
   tail = len(arr) - 1

   while  i < len(arr)//2 :
   
      min_ = i

      for j in range(tail, i, -1):
         if arr[j] < arr[min_]:
            min_ = j
      arr[i], arr[min_] = arr[min_], arr[i]

      i += 1
      max_ = tail 

      for j in range(i, tail):
         if arr[j] > arr[max_]:
            max_ = j
      arr[max_], arr[tail] = arr[tail], arr[max_]

      tail -= 1


       
if __name__ == '__main__':
   arr = [2, 1, 4, 3, 7, 9, 10, 5, 12, 6]
   CockTailSort(arr)
   print(arr)
      
      

