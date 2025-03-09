def test(lst):
    result  = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result
students = [[1, 'David', 'V'], [2, 'Daniel', 'V'], [3, 'jude', 'VI'], [3, 'Lynne', 'VI'], [5, 'Simon', 'VII']]

print("\nOrginal list of lists:")
print(students)
print("\nCoverted lists to a Dictonary")
print(test(students))