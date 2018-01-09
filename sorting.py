import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-sorter', help="which sorting algorithm to use (quick, bubble, heap)", required=True)
args = parser.parse_args()

from skimage import color
from scipy.misc import imsave

import numpy as np
import os

# Most of these sorting algorithms are modified from
# geekviewpoint.com's sorting implementations

def partition(array, begin, end):
    pivot = begin
    swaps = []
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
            swaps.append([i, pivot])
    array[pivot], array[begin] = array[begin], array[pivot]
    swaps.append([pivot, begin])
    return pivot, swaps


def quicksort(array, begin=0, end=None):
    # modified from http://www.geekviewpoint.com/python/sorting/quicksort
    global swaps
    swaps = []
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        global swaps
        if begin >= end:
            return
        pivot, newSwaps = partition(array, begin, end)
        swaps += newSwaps
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)
    return _quicksort(array, begin, end), swaps


def bubblesort(A):
    # modified from http://www.geekviewpoint.com/python/sorting/bubblesort
    swaps = []
    for i in range(len(A)):
        for k in range(len(A) - 1, i, -1):
            if (A[k] < A[k - 1]):
                swaps.append([k, k - 1])
                tmp = A[k]
                A[k] = A[k - 1]
                A[k - 1] = tmp
    return A, swaps

def heapsort( aList ):
    # modified from http://www.geekviewpoint.com/python/sorting/heapsort
    global swaps
    swaps = []
    # convert aList to heap
    length = len( aList ) - 1
    leastParent = length // 2
    for i in range ( leastParent, -1, -1 ):
        moveDown( aList, i, length )

    # flatten heap into sorted array
    for i in range ( length, 0, -1 ):
        if aList[0] > aList[i]:
            swaps.append([0, i])
            swap( aList, 0, i )
            moveDown( aList, 0, i - 1 )
    return aList, swaps

def moveDown( aList, first, last ):
    global swaps
    largest = 2 * first + 1
    while largest <= last:
        # right child exists and is larger than left child
        if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
            largest += 1

        # right child is larger than parent
        if aList[largest] > aList[first]:
            swaps.append([largest, first])
            swap( aList, largest, first )
            # move down to largest child
            first = largest;
            largest = 2 * first + 1
        else:
            return # force exit

def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

img = np.zeros((200, 200, 3), dtype='float32') # hsv works in range from 0 - 1

for i in range(img.shape[1]):
    img[:,i,:] = i / img.shape[0], .9, .9

in_rgb = color.convert_colorspace(img, 'HSV', 'RGB')

# Uncomment bellow to see starting image
imsave('initial.png', in_rgb)

for i in range(img.shape[0]):
    np.random.shuffle(img[i,:,:])

in_rgb = color.convert_colorspace(img, 'HSV', 'RGB')
imsave('initial_shuffled.png', in_rgb)

# we've now got our shuffled, perfect image. let's jump through hoops now

maxMoves = 0
moves = []

for i in range(img.shape[0]):
    newMoves = []
    if args.sorter == 'bubble':
        _, newMoves = bubblesort(list(img[i,:,0]))
    elif args.sorter == 'quick':
        _, newMoves = quicksort(list(img[i,:,0]))
    elif args.sorter == 'heap':
        # need to convert to integers for heap
        integer_version = img[i,:,0] * 10000
        integer_version = integer_version.astype(int)
        _, newMoves = heapsort(list(integer_version))

    if len(newMoves) > maxMoves:
        maxMoves = len(newMoves)
    moves.append(newMoves)

currentMove = 0

def swap_pixels(row, places):
    tmp = img[row,places[0],:].copy()
    img[row,places[0],:] = img[row,places[1],:]
    img[row,places[1],:] = tmp

# 24 fps, and we want a 5 second gif 24 * 5 = 120 total frames (* 24 5)
movie_image_step = maxMoves // 120
movie_image_frame = 0

os.makedirs(args.sorter, exist_ok=True)

while currentMove < maxMoves:
    for i in range(img.shape[0]):
        if currentMove < len(moves[i]) - 1:
            swap_pixels(i, moves[i][currentMove])

    if currentMove % movie_image_step == 0:
        imsave('%s/%05d.png' % (args.sorter, movie_image_frame), color.convert_colorspace(img, 'HSV', 'RGB'))
        movie_image_frame += 1
    currentMove += 1

