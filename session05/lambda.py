#!/usr/bin/env python

#lambda and keyword argument magic

#using a for loop
def function_list(n):
    my_list = []
    for i in range(n):
        my_list.append(lambda x, i=i: x+i)
    return my_list

the_list = function_list(2)

print the_list[0](2)
print the_list[1](2)


#list comprehension
def function_list2(n):
    return [lambda x, i=i: x+1 for i in range(n)]

the_list = function_list2(2)

print the_list[0](2)







