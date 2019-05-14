###coding challege examples
import math

"""If we listed all the natural numbers below 10 that are multiples of 3 || 5, we get 
3,4,6,9. the sum of these is 23. find sum of all multiples of 3 or 5 below 1000"""

def Multiples3And5(val1,val2,size):
    counter = val1;
    sum = 0
    while True:
        if counter % val1 == 0 or counter % val2 == 0:
            if counter >= size:
                break
            print('%d,'%(counter))
            sum += counter
            print(sum)
        counter += 1

"""Sum of Even valued Fibonacci #
create fib array then"""

def Fibonacci(size):
    array = [1,2]
    i = 0
    j = 1
    fib = 0
    sum = 0
    while True:
        fib = array[i] + array[j]
        if fib >= size:
            break
        array.append(fib)
        i += 1
        j += 1
    return array
"""check and sum even values in fib array"""
def checkEven(array):
    sum = 0
    for item in array:
        if item % 2 == 0:
            sum += item
    return sum


"""Prime Factors are prime # that can be multipled to give original number
It is also a prime number itself"""
def FindPrimeFactor(num):
    lpf = 2;
    while (num > lpf):
        if (num % lpf == 0):
            num = num / lpf
            lpf = 2
        else:
            lpf += 1;
    print("Largest Prime Factor: %d" % (lpf))

def NoDupPermuatons(list):
    """"""
    # If lst is empty then there are no permutations
    if len(list) == 0:
        return

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(list) == 1:
        return list
    levels = 0
    result =[]
    factcount, letters = findFactorialCount(list)
    print "# of permutations: " + repr(factcount)
    permute_remainder(letters,"",len(list),result)


    return result

def permute_remainder(char_counts, prefix, remainder, results):
    if remainder == 0:
        results.append(prefix)

    for ch in char_counts:
        if char_counts[ch] > 0:
            char_counts[ch] -= 1
            permute_remainder(char_counts, prefix + ch, remainder - 1, results)
            char_counts[ch] += 1

"""gets factorial count of # of chars from list
returns # of permutations that will occur and a dict without dups
and with count for each different char"""
def findFactorialCount(list):
    #first find factorial count # of each letter
    # divided by duplicates
    words = {}

    for l in list:
        #add to dict listing if it exists
        if words.get(l) != None:
            value = words[l]
            words[l] = value + 1
        else:
            words[l] = 1

    count = len(list) # number of input
    duplicates = []
    for word in words:
        if words[word] > 1:
            val = words[word]
            duplicates.append(val)
    countfact = math.factorial(count)
    if duplicates is not None:
        dupfact = duplicates.pop()
        dupTotal = math.factorial(dupfact)
        for dup in duplicates:
            dupTotal = dupTotal * math.factorial(dup)
    #lexorder
    #newWords = sorted(words)
    return countfact/dupTotal, words

"""merge sort"""

def mergeSort(sortedArray):
   # print("Splitting ", sortedArray)
    if 1 < len(sortedArray):
        q = len(sortedArray)//2
        left = sortedArray[:q]
        right = sortedArray[q:]
        mergeSort(left)
        mergeSort(right)
        merge(left,right,sortedArray)
    print("Merged ", sortedArray)

def merge(L,R, finalArray):
    i = 0 # left half index
    j = 0 # right half index
    index = 0 #for merged array
    while i < len(L) and j < len(R):
        if L[i] >= R[j]:
            finalArray[index]=L[i]
            i += 1
        else:
            finalArray[index]=R[j]
            j += 1
        index += 1
    while i < len(L):
        finalArray[index] = L[i]
        i += 1
        index += 1
    while j < len(R):
        finalArray[index] = R[j]
        j += 1
        index += 1

"""Merge 2 arrays/lists
cite: https://www.geeksforgeeks.org/merge-two-sorted-arrays-python-using-heapq/"""
# Function to merge two sorted arrays
def mergeArray(arr1, arr2):
    return list(merge(arr1, arr2))

"""Binary Search
uses bag type data, sorted will split up
search depending on if next value is > or <
 if does not contain returns -1
 Runtime O(logn) this one works with sorted array"""
def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

"""k largest(or smallest) elements in an array | added Min Heap method
Input Array unsorted and num of elements requested either the largest
 or smallest """

def KLargest(array,num):
    mergeSort(array)
    i = 0
    while i < num:
        print array[i]
        i += 1




if __name__ == "__main__":
    #Multiples3And5(3,5,1000)
    #array = Fibonacci(4000000)
    #print array
    #print(checkEven(array))
    #FindPrimeFactor(600851475143)
    # Driver program to test above function
    str = 'notalisit'
    test = 'AABC'
    data = list(str)
   # data = list('this ais not numbers')
    #for p in permutation(data):
    #    print p
    #words = LexNoneDupPermuatons(str)
    #print findFactorialCount(test)
    print NoDupPermuatons(test)
    #result = [0 for x in range(len(test))]
    #print test
    #array = [1,23,12,9,30,2,50]
    #KLargest(array, 3)







