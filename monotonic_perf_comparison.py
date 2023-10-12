"""
import yourprogram.py
import myprogram.py

testListinAscending = generateTestNumbersInAscending()
testListinDescending = generateTestNumbersInDescending()
testListinRandomOrder = generateTestNumbersInRandomOrder()

Call yourprogram.IsMonotonic(testListinAscending)
Call myprogram.IsMonotonic(testListinAscending)
Check time difference between both programs for the same set of data

"""

from traceback import print_list
import random
import array_monotonic as gp
import array_ismonotonic as bp
import cProfile

def generateTestNumbersInAscending():
    lists = list(range(1,100000001))
    return lists

def generateTestNumbersInDescending():
    lists = list(range(1,100000001))
    lists.sort(reverse=True)
    return lists

def generateTestNumbersInRandomOrder():
    lists = list(range(1,100000001))
    random.shuffle(lists)
    return lists


testListinAscending = generateTestNumbersInAscending()
testListinDescending = generateTestNumbersInDescending()
testListinRandomOrder = generateTestNumbersInRandomOrder()

"""print ("\nTest Result of Bingiz Program")
print("Paru Program: ", bp.is_Monotonic(testListinAscending))
print("Paru Program: ", bp.is_Monotonic(testListinDescending))
print("Paru Program: ", bp.is_Monotonic(testListinRandomOrder))



print("\nTest Result of Ganesan Program")
print("Paru Program: ", gp.isMonotonic(testListinAscending))
print("Paru Program: ", gp.isMonotonic(testListinDescending))
print("Paru Program: ", gp.isMonotonic(testListinRandomOrder))"""

cProfile.run('bp.is_Monotonic(testListinAscending)')
cProfile.run('bp.is_Monotonic(testListinDescending)')
cProfile.run('bp.is_Monotonic(testListinRandomOrder)')

cProfile.run('gp.isMonotonic(testListinAscending)')
cProfile.run('gp.isMonotonic(testListinDescending)')
cProfile.run('gp.isMonotonic(testListinRandomOrder)')









