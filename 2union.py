#to find union of two list 
def find_union(list1, list2):
    union_set = set(list1) | set(list2)
    union_list = list(union_set)
    return union_list

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

union_result = find_union(list1, list2)
print("Union of the two lists:", union_result)
