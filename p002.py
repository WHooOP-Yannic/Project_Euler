#!/bin/python
##
# Project Euler, Problem 2: Even Fibonacci numbers.
# This solution by yannic, 2017-01-14


def fib(n):
  global fiblist
  if n == 1:
    fiblist.append(1)
    return 1
  elif n == 2:
    fiblist.append(2)
    return 2
  else:
    tmp = fiblist[n-1] + fiblist[n-2]
    fiblist.append(tmp)
    return tmp

#**** TEST
print "fibs upto 10"

fiblist = []
print fiblist
fiblist.append(1)
print "fiblist initial={}".format(fiblist)

evsum = 0
for n in range(1, 101):
  fb = fib(n)
  if fb > 4000000:
    break
  if fb % 2 == 0:
    evsum = evsum + fb
  print "fib({})={}".format(n, fb)


#print "fnale test-summe ist {}".format(sm)
print "fiblist @ end={}".format(fiblist)
print "Total sum of n % 2 ={}".format(evsum)

#**** PROBLEM
