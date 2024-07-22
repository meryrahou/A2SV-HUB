# Problem: Heap Sort - https://practice.geeksforgeeks.org/problems/heap-sort/1

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        left = 2*i+1
        right = min(2*i+2,n-1)
        
        if left >= n : 
            return
        
        largest_child = left if arr[left]>= arr[right] else right

        if arr[i] > arr[largest_child]:
            return
        
        arr[i],arr[largest_child] = arr[largest_child],arr[i]
        self.heapify(arr,n,largest_child)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        
        for i in range(n//2-1,-1,-1):
            self.heapify(arr,n,i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        
        for i in range(n-1,0,-1):
            arr[0],arr[i] = arr[i],arr[0]
            self.heapify(arr,i,0)