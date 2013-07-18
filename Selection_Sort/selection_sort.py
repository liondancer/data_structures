# SELECTION SORT

# Selection sort improves on bubble sort by making on exchange for every pass through the list.
# In order to do this, selection sort locates the largest value and puts it in the proper location(the end).
# This is done by swapping 
# During the second pass, the next largest is put in it's place as well. This requires n-1 passes because the last item must be in place after the n-1 pass

# runtime of O(n^2) but is typically faster than bubble sort due to less number of exchanges.


def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):                #number of passes (n-1)
       positionOfMax=0  
       for location in range(1,fillslot+1):                 # runs through all number of items to compare(location of each element)
           if alist[location]>alist[positionOfMax]:         # if the element in the current location is higher
               positionOfMax = location                     # set positionOfMax to be the location (location of current max)

       temp = alist[fillslot]                               # swap process
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp


