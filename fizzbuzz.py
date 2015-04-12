#!/usr/bin/env python
# -*- coding: utf-8 -*-

count = raw_input("Vpiši cifro do katere želiš prešteti: ")
count = int(count)

for num in xrange(1, count):
	if num % 3 == 0 and num % 5 == 0:
		print "FizzBuzz"
	elif num % 3 == 0:
		print "Fizz"
	elif  num % 5 == 0:
		print "Buzz"
	else:
		print num


