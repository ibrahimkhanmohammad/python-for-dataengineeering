details = ['Asta', 15, 5.3, True, 'Black Bulls']

#   adding values -> .append() , .insert()

#   .append()   add elements at the vert=y end of the list
details.append('Wizard King')
print(details)

#   .insert()   insert element at particular index
details.insert(4, 'Magic Knight')
print(details)

#   removing elements -> .remove() , .pop()

#   .remove()   remove the value to be precise the first occurrence in a list
details.remove(5.3)
print(details)

#   .pop()  pop the element by default last element if mention then that particular index element, it return the pop element so better store in a variable
last_popped_element = details.pop()
print(details)

popped_element = details.pop(2)
print(details)