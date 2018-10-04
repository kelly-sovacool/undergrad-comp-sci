#!/usr/local/bin/python3
# Kelly Sovacool
# CS315 Homework 5


def main():
    '''A = [8, 3, 6, 2, 7, 1, 4, 9, 5]
    pivot = partition(A, 0, len(A)-1)
    print('pivot =', pivot)
    B = [-1, 0, 1, 2, 3, 4, 7]
    print(modified_binary_search(B, 0, len(B)))'''
    C = [8,7,6,5,4,3,2,1]
    quicksort(C, 1, len(C)-1)


def quicksort(A, p, r):
    print('A =', A)
    if p < r:
        q = partition(A, p, r)
        print('pivot =',q, end='\t')
        print('left', end='\t')
        quicksort(A, p, q - 1)
        print('right', end='\t')
        quicksort(A, q + 1, r)


def modified_binary_search(A, l, r):
    # elements must be distinct
    print(A[l:r])
    i = (r-l)//2 + l
    if r-l <= 0:
        return False
    elif A[i] == i:
        print(A[i], i)
        return True
    elif A[i] < i:  # right
        return modified_binary_search(A, i+1, r)
    elif A[i] > i:  # left
        return modified_binary_search(A, l, i)


def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r+1):
        if array[j] <= x:
            i += 1
            exchange(array, i, j)
        print('i =', i, '\tj =', j, '\tA =', array)
    exchange(array, i + 1, r)
    return i + 1


def exchange(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


main()
