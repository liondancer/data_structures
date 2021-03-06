# INSERTION SORT
# runtime of O(n^2)
# Each new item is inserted back into the previous sublist such that the sorted list is one item larger


# 
#
#
#     * 
#   | 54 | 26 | 93 | 17 | 77 | 31 | 44 | 55 | 20 |     Assume 54 is sorted list of 1 item


#     *    *
#   | 26 | 54 | 93 | 17 | 77 | 31 | 44 | 55 | 20 |     insert 26


#     *    *    * 
#   | 26 | 54 | 93 | 17 | 77 | 31 | 44 | 55 | 20 |     insert 93


#     *    *    *    *
#   | 17 | 26 | 54 | 93 | 77 | 31 | 44 | 55 | 20 |     insert 17


#     *    *    *    *    *              
#   | 17 | 26 | 54 | 77 | 93 | 31 | 44 | 55 | 20 |     insert 77


#     *    *    *    *    *    *             
#   | 17 | 26 | 31 | 54 | 77 | 93 | 44 | 55 | 20 |     insert 31


#     *    *    *    *    *    *    *          
#   | 17 | 26 | 31 | 44 | 54 | 77 | 93 | 55 | 20 |     insert 44


#     *    *    *    *    *    *    *    *        
#   | 17 | 26 | 31 | 44 | 54 | 55 | 77 | 93 | 20 |     insert 55


#     *    *    *    *    *    *    *    *    *       
#   | 17 | 20 | 26 | 31 | 44 | 31 | 54 | 77 | 93 |     insert 20


# First assume that a list with one item (at position 0) is a sorted list of one element
# On each pass, one for each item 1 through n-1 (last item is in correct position), the current item is checked against those in the already sorted sublist
# We shift the greater items to the right and the smaller items to the left to allow the current item to be inserted

# Maximum number of comparisons for an insertion sort is the sum of the first n-1 integers
# O(n^2)
# Best case is when only one comparison needs to be done on each pass. This occurs in an already sorted list.


def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]                              #saves current value
     position = index

     while position>0 and alist[position-1]>currentvalue:    
         alist[position]=alist[position-1]
         position = position-1                                  

     alist[position]=currentvalue                               








