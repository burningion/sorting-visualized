# Sorting Algorithms Visualized in Python

This code accompanies a post at [makeartwithpython.com](https://www.makeartwithpython.com/blog/visualizing-sort-algorithms-in-python/). It generates animations of Heap, Bubble, and Quicksort. 

They all end up looking like this:

![Everyone](https://github.com/burningion/sorting-visualized/raw/master/images/sorting.gif)

## Usage

Just run it from the command line:

```bash
$ python sorting.py -sorter heap
```
This will create an image sequence of the heap sort, in the heap folder.

[Read the post](https://www.makeartwithpython.com/blog/visualizing-sort-algorithms-in-python/) to see how to turn the image sequence into a video / gif.

To see which parameters to use for the other sort algorithms, use:

```bash
$ python sorting.py --help
```

## Prerequisites

You must have `scikit-image` installed.  You can follow the instructions at http://scikit-image.org/docs/stable/install.html#standard-installation to install it.
