#!/bin/python
##
# Project Euler, Problem 1: Multiples of 3 and 5.
# This solution by yannic, 2017-01-05

#int[] ary = new int[10];  // < java array

print "an array"
ary = range(1, 10)
print(ary)

#for x (ary) {
#  System.ou.println(x);
#}

#**** TEST
print "our loop"
sm = 0
for x in range(1, 10):
  #print "rest von {} ist {}".format(x, x%3)
  if x % 3 == 0:
    #print str(x) + " ist 3-teilbar"
    sm = sm + x
  if x % 5 == 0:
    #print str(x) + " ist 5-teilbar"
    sm += x
  #print "summe ist {}".format(sm)

print "fnale test-summe ist {}".format(sm)

#**** PROBLEM
print "our loop"
sm = 0
for x in range(1, 1000):
  #print "rest von {} ist {}".format(x, x%3)
  if (x % 3 == 0) or (x % 5 == 0):
    #print str(x) + " ist 3-teilbar"
    sm = sm + x

print "fnale end-summe ist {}".format(sm)
