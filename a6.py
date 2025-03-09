def test(lst):
    result  = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result
students = [[1, 'jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [3, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

print("\nOrginal list of lists:")
print(students)
print("\nCoverted lists to a Dictonary")
print(test(students))