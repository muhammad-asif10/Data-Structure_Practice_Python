st_list = [1,2,3,4,5,6,7,8,9]
print(st_list)
st_list.append(10) # add at the end
print("After append", st_list)
st_list.insert(10,11) # insert at the specific index
print("After insert", st_list)
st_list.pop() # delete at the end
print("After pop", st_list)
# st_list.reverse() # reverse the list
# print("After reverse", st_list)
print("First Number:", st_list[0]) # return first number
st_list.extend([11,12]) # add multiple numbers
print("After extend", st_list)
length = len(st_list) #return length
print("Length:", length)
print("Maximum", max(st_list)) # give maximum number from list
print("Minimum",min(st_list)) # give minimum number from list
print("Sum fo list", sum(st_list)) # return sum of list