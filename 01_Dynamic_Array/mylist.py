# Implemented from scratch for learning internal working of Python list
# Not using built-in list methods intentionally
import ctypes
# to create C type array
"""WHY ctypes is used:
Python list internally is dynamic array (C array concept)
But Python does not allow direct C-array creation
ctypes allows us to create low-level C type array manually
So we can build our own dynamic list like Python list internally
"""
class MyList :
    def __init__(self):
        self.size=1
        self.n=0
        # create a C type array with size -> self.size
        self.A=self.__make_array(self.size)
        
    def __make_array(self,capacity):
        #referential array(C type)
        return(capacity*ctypes.py_object)()
    
    def __resize(self,new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity)
        # the reason we write "B" instead of "self.B" becoz it is temp storage(isnt really the object   
        # attribute and we will reassign it to self.A at the end of this method
        self.size = new_capacity
        # copy the content of old array to new one
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B
    
    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n==self.size :
            self.__resize(self.size*2)
        #indexing start at n=0 , so the next free position is always at index     
        self.A[self.n]=item
        #updating the no of elements count
        self.n=self.n+1
        
    def __str__(self):
        #Magic method ,defines how object is printed using print()
        result = '' 
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        
        return '[' + result[:-1] + ']'
    
    def pop(self):
        # checking if array is empty 
        if self.n==0:
            return "Empty list"
        # pops the last element and update the size of array
        item = self.A[self.n-1]
        self.n -= 1
        return item
    
    def clear(self):
        self.n=0
        self.size=1
        self.A = self.__make_array(self.size)
        
    def find(self,item):
        for i in range(self.n):
            if self.A[i]==item:
                return i
        return "ValueError - not in List"
        
    def insert(self,pos,item):
        # if array is full , resizing
        if self.n == self.size:
            self.__resize(self.size*2)
            
        # while inserting -> move right to left -> For prevention of data lost    
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
            
        self.A[pos]=item
        self.n=self.n+1
        
    def __delitem__(self,pos):
        if 0<=pos< self.n :
            # while deleting -> move left to right -> For prevention of data lost
            for i in range(pos,self.n-1):
                self.A[i]=self.A[i+1]
            self.n=self.n-1
            
    def remove(self,item):
        pos = self.find(item)
        if type(pos)==int:
            self.__delitem__(pos)
        else :
            return pos 
        
      #slicing is also done in this , getitem inital for just for index call , now slicing too  
      
    def __getitem__(self,index):
        
        if isinstance(index,slice):
            start = index.start
            stop = index.stop

            if start is None:
                start = 0
            if stop is None:
                stop = self.n

            if start < 0:
                start = self.n + start
            if stop < 0:
                stop = self.n + stop

            if start < 0:
                start = 0
            if stop > self.n:
                stop = self.n

            result = MyList()
            for i in range(start, stop):
                result.append(self.A[i])

            return result

    # ---- single index ----
        else:
                if index < 0:
                    index = self.n + index

                if 0 <= index < self.n:
                    return self.A[index]
                else:
                    return "IndexError"
    
    def min(self):
        # check if empty
        if self.n==0 :
            return "Empty List"
        
        # assume first element is min
        min_val = self.A[0]
        
        # compare with rest of elements
        for i in range(1,self.n):
            if self.A[i]< min_val:
                min_val = self.A[i]
        return min_val
        
    def max(self):
        # check if empty
        if self.n == 0:
            return "Empty list" 
        
        # assume first element is max
        max_val=self.A[0]
        
        # compare with rest of elements
        for i in range(1,self.n):
            if self.A[i]>max_val:
                max_val = self.A[i]
        return max_val
            
    def sum(self):
        # check if empty
        if self.n == 0:
            return "Empty list" 
        sum_val=0
        for i in range(0,self.n):
            sum_val = self.A[i]+sum_val
        return sum_val
    
    def extend(self,items):
        for i in range(items.n):
            self.append(items[i])
    
    def neg_indx(self,index):
        if index < 0 :
            # convert negative index to positive equivalent
           index = self.n + index 
        return index
  
    def sort(self):
        for pass_no in range(self.n-1):
            # As pass number increases, the number of iterations reduces because after every pass, 
            # the largest element gets fixed at the end of the list.
            for i in range(self.n- pass_no -1):
                if self.A[i]> self.A[i+1]:
                    temp = self.A[i]
                    self.A[i] = self.A[i+1]
                    self.A[i+1] = temp 
                    
    def merge(self, other):
    # Merge takes two already sorted MyList objects
    # and returns a new sorted MyList
        result = MyList()
        i = 0   # pointer for self
        j = 0   # pointer for other
        # compare elements of both lists
        while i < self.n and j < other.n:
            if self.A[i] < other.A[j]:
                result.append(self.A[i])
                i += 1
            else:
                result.append(other.A[j])
                j += 1
        # remaining elements of self
        while i < self.n:
            result.append(self.A[i])
            i += 1
        # remaining elements of other
        while j < other.n:
            result.append(other.A[j])
            j += 1

        return result

print("---- BASIC OPERATIONS TEST ----")

L = MyList()
L.append(10)
L.append(5)
L.append(30)
L.append(2)

print("Initial list:", L)

print("Length:", len(L))

print("Min:", L.min())
print("Max:", L.max())
print("Sum:", L.sum())

print("\n---- SORT TEST ----")

L2 = MyList()
L2.append(8)
L2.append(1)
L2.append(6)
L2.append(3)

print("Before sorting:", L2)
L2.sort()
print("After sorting:", L2)

print("\n---- INDEXING & SLICING TEST ----")

print("Element at index 1:", L2[1])
print("Negative index [-1]:", L2[-1])

print("Slice [1:3]:", L2[1:3])
print("Slice [:2]:", L2[:2])
print("Slice [1:]:", L2[1:])

print("\n---- EXTEND TEST ----")
A = MyList()
A.append(1)
A.append(2)

B = MyList()
B.append(3)
B.append(4)

A.extend(B)
print("After extending A with B:", A)

print("\n---- MERGE TWO SORTED LISTS ----")

L1 = MyList()
L1.append(1)
L1.append(3)
L1.append(5)

L2 = MyList()
L2.append(2)
L2.append(4)
L2.append(6)

merged = L1.merge(L2)
print("Merged sorted list:", merged)

"""""
Stuffs i learnt 
1] Python list internally behave as dynamic array 
2] There are 2 types of Category 
    a) User-defined methods 
        resize()	Public                          -> user keliye 
        _resize()	Internal (convention)           -> Internal hint
        __resize()	Name-mangled (strongly private) -> Class only    -> To prevent accidental access from outside class , Ex : user khud se array resize nhi kar sakta
    b) Python special (magic) methods
        __init__     -> Constructor for initialization of object
        __len__      
        __getitem__
        __str__      -> For printing
        __delitem__

# APPEND COMPLEXITY:
# Average case = O(1)
# When resize happens = O(n)

# INSERT COMPLEXITY:
# Worst case O(n) because elements must shift right
# If inserting at end → behaves like append (O(1))

Python never excludes the last element by default
It excludes the element at the stop index
agar last ka stop index diya ho toh it excludes nd agar 
L[2:] asa none way mei diya ho exclude nhi karta
python excludes the last index not last element


Bubble sort used here
Time complexity:
Worst & Avg = O(n^2)
Best case = O(n) (if already sorted with optimization)
Not efficient for very large data
Used here for learning purpose


MERGE LOGIC (used in merge sort)
Both lists must already be sorted
We compare elements one by one using two pointers (i & j)
Smaller element goes into result list
Time complexity = O(n + m)
Much faster than sorting again after combining
Real use:
This logic is core part of MERGE SORT algorithm


"""""
