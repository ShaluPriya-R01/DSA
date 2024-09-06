def isSubset( a1, a2, n, m):
    for i in a2:
        if i in a1:
            a1.remove(i)
        else:
            return "No"
    return "Yes"


STEPS:
1. Loop through each element in `a2`.
2. Check if the current element exists in `a1`.
3. Remove the element from `a1` if found to avoid counting the same element multiple times.
4. Return "No" if any element is not found.
5. Return "Yes" if all elements are found.
