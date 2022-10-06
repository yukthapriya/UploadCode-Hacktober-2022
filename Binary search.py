def binary_search(list1):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:  
           
        mid = (high + low) // 2  
  
           
        if list1[mid] < n:  
            low = mid + 1  
  
          
        elif list1[mid] > n:  
            high = mid - 1  
  
       
        else:  
            return mid  
  
            
    return -1  
  
  
print("Elements in array(space seperated)")
list1 = input()
Arr=list1.split(" ")  
Index = binary_search(Arr)  
  
if Index != -1:  
    print("Element is present at index", str(result))  
else:  
    print("Element is not present in list1") 
