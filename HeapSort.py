#!/bin/python

#i is the bottom of arr whose value is the new added member 
# this func adjust arr[i] to a propoer place in the heap
def HeapAdjust(arr, i):
   temp = arr[i]
   j = (i-1)//2

   while j>=0 and i !=0:
      
      if arr[j] <= temp:
         break

      arr[i] = arr[j]
      i    = j
      j    = (i-1)//2
   
   #find the right place for a[i] 
   arr[i] = temp

#delete i in arr[n]
def HeapDelete(arr, i, n):
   temp = arr[i]
   j = 2*i + 1
   while j < n:

      if j+1 < n and arr[j+1] < arr[j]:
         j += 1

      if arr[j] > temp:
         break
      
      arr[i] = arr[j]
      i = j
      j = 2*i + 1
      
   arr[i] = temp

def minHeapAdjust(arr, n):

   if n > 0:

      arr[0], arr[n] = arr[n], arr[0]
      HeapDelete(arr, 0, n)
      print(arr)
      minHeapAdjust(arr, n-1)

if __name__ == '__main__':
   
   arr = [2, 1, 4, 3, 7, 9, 10, 5, 12, 6, 30, 15]
   minHeapAdjust(arr, len(arr)-1)
   print(arr)
