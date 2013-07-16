# BUBBLE SORT
# The bubble sort makes multiple passes through a list. It compares adjacent items and exhcanges those that are out of 
# order. Each pass through the list places teh next largest value in its proper place. Each item "bubbles" up to the
# location where it belongs.

# SPEED
# worst case O(n^2) for n items
# not practical when n is large due to so many runs! Good for small number of items

# Example
#          *    *
#   1.   | 54 | 26 | 93 | 17 | 77 | 31 | 44 | 55 | 20 |  EXCHANGE 

#               *    *
#   2.   | 26 | 54 | 93 | 17 | 77 | 31 | 44 | 55 | 20 |  NO EXCHANGE

#                    *    * 
#   3.   | 26 | 54 | 93 | 17 | 77 | 31 | 44 | 55 | 20 |  EXCHANGE

#                         *    *
#   4.   | 26 | 54 | 17 | 93 | 77 | 31 | 44 | 55 | 20 |  EXCHANGE
# 
#                              *    *
#   5.   | 26 | 54 | 17 | 77 | 93 | 31 | 44 | 55 | 20 |  EXCHANGE
# 
#                                   *    *
#   6.   | 26 | 54 | 17 | 77 | 31 | 93 | 44 | 55 | 20 |  EXCHANGE

#                                        *    * 
#   7.   | 26 | 54 | 17 | 77 | 31 | 44 | 93 | 55 | 20 |  EXCHANGE

#                                             *    *
#   8.   | 26 | 54 | 17 | 77 | 31 | 44 | 55 | 93 | 20 |  EXCHANGE


#   9.   | 26 | 54 | 17 | 77 | 31 | 44 | 55 | 20 | 93 |  93 in place after first pass

# At the start of the 2nd pass, the largest value is now in place. There are n - 1 items left to sort, meaning there will be n-2 pairs. 
# Because each pass placees the next largest value in place, the total number of passes necessary will be n - 1. After n - 1 passes, the smallest item must be in the correct
# position with no further processing required. 


# How to swap
# swapping two elements in a list

# temp = alist[i]
# alist[i] = alist[j]
# alist[j] = temp

# the code above will exchange the ith and jth items in the list 

# However in Python you can use a,b = b,a to swap simultaneously. But the method using temp is common is most programming languages


#               2nd
#            __________
#           |          |
#           i          j
#   |  |  |93|  |  |  |44|  |  | 
#           |          |
#          1st        3rd     
#           ----|  |----
#               temp        



#             a,b = b,a          
#
#           |-----------|
#           *           |  
#   |  |  |93|  |  |  |44|  |  |
#           |___________*



def bubbleSort(alist):
  for passnum in range(len(alist)-1,0,-1):          # range(start,end(not including),increment). Also, passnum starts at the first number in range. 
    for i in range(passnum):                       
      if alist[i]>alist[i + 1]:                     # comparison test to see if next element is larger or smaller
        temp = alist[i]                             # swap if current element is larger than next element
        alist[i] = alist[i+1]
        alist[i + 1] = temp


