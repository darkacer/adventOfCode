Take arr = [3, 5, 7] as an example

lets have our increment by init to 1
and num init to 0


for 0th element i.e 3 we increment num by 1 until it reaches the element value (3 in this case, then we break)

for 1st element we now increment num by 1x3=3 where 3 being previous number 
we do it until (num + index is divisible by 5 (our ith element)
so until num becomes 24 because 24+index is divisible by 5 (24+1 is divisible by 5)


for 1st element we now increment num by 1x3x5=15 where 5 being previous number 
we do it until (num + index is divisible by 7 (our ith element)
so until num becomes 54 because 54+index is divisible by 7 (54+2 is divisible by 7)