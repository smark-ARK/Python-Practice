def binary sum(S, start, stop):


”””Return the sum of the numbers in implicit slice S[start:stop].”””
if start >= stop:  # zero elements in slice
return 0
elif start == stop−1:  # one element in slice
return S[start]
else:  # two or more elements in slice
mid = (start + stop) // 2
return binary sum(S, start, mid) + binary sum(S, mid, stop)
