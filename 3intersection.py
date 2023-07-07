# to find intersection of two list
def find_intersection(list1, list2):
    intersection = list(set(list1) & set(list2))
    return intersection

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection_result = find_intersection(list1, list2)
print("Intersection of the two lists:", intersection_result)
