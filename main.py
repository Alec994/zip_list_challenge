"""
For this challenge, we are going to recreate an existing built-in python function called zip().

The purpose of the zip() function in python is to merge two given lists into a single list of tuples. 
Each tuple will contain two values: one value from each list being merged.

You can see how the zip() function works using the trinket embed below.

Your task is to create a new function called zipLists() that will behave exactly the same way as the built-in zip() function, using your own algorithm. 
Your function will need to take two lists as parameters and return a “zipped list of tuples”. 
To start with, you may assume that both lists provided will be of the same length (contain the same numbers of values).
You will then be able to adapt your code to consider the case where one list has less values than the other. 
In this case you will ignore surplus values.

"""

ls1 = [1, 2, 3]
ls2 = ['a', 'b', 'c', 'd']




def zipList(first_list, second_list):
    em_list = []

    f_ls_len = len(ls1)
    s_ls_len = len(ls2)

    if f_ls_len < s_ls_len or f_ls_len == s_ls_len:
        f_ls_len
    else:
        f_ls_len = s_ls_len

    for i in range(f_ls_len):
        zipped_items = (first_list[i], second_list[i])
        em_list.append(zipped_items)
    return em_list



print(zipList(ls1, ls2))

            
    
            

