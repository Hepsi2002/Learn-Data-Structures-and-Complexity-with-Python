def binary_search_iteration(A,key):
    left_index=0
    right_index=len(A)-1
    while left_index<=right_index:
        middle=(left_index+right_index)//2
        if key == A[middle]:
            return middle
        elif key<A[middle]:
            right_index=middle-1
        elif key>A[middle]:
            left_index=middle+1
    return "Not Found"

A=[45,56,67,78,89,90,95,99]
print(binary_search_iteration(A,89))