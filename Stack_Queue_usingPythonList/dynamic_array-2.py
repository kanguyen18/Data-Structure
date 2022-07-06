# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import ctypes                                      # provides low-level arrays

class DynamicArray:
  #"""A dynamic array class akin to a simplified Python list."""

    def __init__(self):
    #"""Create an empty array."""
        self._n = 0                                    # count actual elements
        self._capacity = 1                             # default array capacity
        self._A = self._make_array(self._capacity)     # low-level array
    
    def __len__(self):
    #"""Return number of elements stored in the array."""
        return self._n
    
    def __getitem__(self, k):
    #"""Return element at index k."""
        if not abs(k) < self._n:
            raise IndexError('invalid index')
        else:
            if 0 <= k < self._n:
                return self._A[k]                              # retrieve from array
            else:
                k = self._n + k
                return self._A[k]                              # retrieve from array
  
    def append(self, obj):
    #"""Add object to end of the array."""
        if self._n == self._capacity:                  # not enough room
            self._resize(2 * self._capacity)             # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                            # nonpublic utitity
    #"""Resize internal array to capacity c."""
        B = self._make_array(c)                        # new (bigger) array
        for k in range(self._n):                       # for each existing value
            B[k] = self._A[k]
        self._A = B                                    # use the bigger array
        self._capacity = c

    def _make_array(self, c):                        # nonpublic utitity
     #"""Return new array with capacity c."""   
         return (c * ctypes.py_object)()               # see ctypes documentation

    def insert(self, k, value):
    #"""Insert value at index k, shifting subsequent values rightward."""
    # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:                  # not enough room
            self._resize(2 * self._capacity)             # so double capacity
        for j in range(self._n, k, -1):                # shift rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value                             # store newest element
        self._n += 1

    def insertEfficient(self, k, value):
        if self._n == self._capacity:
            c = 2*self._capacity
            B = self._make_array(c)
            for i in range(0,k):
                B[i] = self._A[i]
            B[k] = value
            for i in range(self._n, k, -1):
                B[i] = self._A[i-1]
            self._A = B
            self._capacity = c
            self._n += 1
        else:
            for j in range(self._n, k, -1):                
                self._A[j] = self._A[j-1]
            self._A[k] = value                             
            self._n += 1
            
    def remove(self, value):
    #"""Remove first occurrence of value (or raise ValueError)."""
    # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:              # found a match!
                for j in range(k, self._n - 1):    # shift others to fill gap
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None        # help garbage collection
                self._n -= 1                       # we have one less item
                return                             # exit immediately
        raise ValueError('value not found')   # only reached if no match

    def removeAll(self, value):
        rep_count = 0
        for k in range(self._n):
            if self._A[k] == value:
                rep_count = rep_count + 1
            else:
                self._A[k - rep_count] = self._A[k]
        if rep_count == 0:
            raise ValueError('value not found')
        else:
            for j in range(self._n - 1, self._n - rep_count - 1, -1):
                self._A[j] = None
            self._n = self._n - rep_count
            
