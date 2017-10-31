print "Compare Lists"

'''
Write a program that compares two lists and prints a message depending on if the inputs are identical or not.
Your program should be able to accept and compare two lists: list_one and list_two.
If both lists are identical print "The lists are the same."
If they are not identical print "The lists are not the same."
'''

def compare(list1, list2):
    if list1 == list2:
        print "The lists are the same"
    else:
        print "The lists are not the same"

list1 = [1,2,5,6,2]
list2 = [1,2,5,6,2]
#output: The lists are the same

list3 = [1,2,5,6,5]
list4 = [1,2,5,6,5,3]
#output: The lists are not the same

list5 = [1,2,5,6,5,16]
list6 = [1,2,5,6,5]
#output: the lists are not the same

list7 = ['celery','carrots','bread','milk']
list8 = ['celery','carrots','bread','cream']
#output: the lists are not the same

compare(list1, list2)
compare(list3, list4)
compare(list5, list6)
compare(list7, list8)