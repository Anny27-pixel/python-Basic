# print(10+5)
# print((6+3) -(6+3))
# print(100 + 5*3)

# #list
# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# list1 = ["abc", 34, True, 40, "male"]  #list with different data types
# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# thislist = list(("apple", "banana", "cherry"))  #note the double round brackets, constructor
# thislist = ["apple", "banana", "cherry"]  #Access items, first index is 0
# print(thislist[1])

# thislist = ["apple", "banana", "cherry"]  #-1 refers to the last item, -2 refers the second items
# print(thislist[-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] #range of indexes
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] #range of indexes
# print(thislist[:4])  # this example returns the items from the beginning to, but not including "kiwi"


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] #range of indexes
# print(thislist[2:])  # this example returns the items from "cherry" to the end


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] #range of indexes
# print(thislist[-4:-1])  # this example returns the items from "orange" (-4) to, but not including "mango"

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#     print("Yes, apple is in the fruits list") 

# #change item value
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackCurrent"
# print(thislist)

# #change a range of item value
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist[1:3] = ["blackCurrent", "waterMelon"]
# print(thislist)

# #if you insert less item than you replace, the new items will be inserted where you specified,
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["waterMelon"]
# print(thislist)

# #insert new items
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "waterMelon")
# print(thislist)

# #to add an item to the end of the list, use the append() method:
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# #add the elements of tropical to thislist:
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineApple", "papaya"]
# thislist.extend(tropical)

# #remove specified item
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# #if there are more than one item with the specified value, the remove() method removes the first 
# thislist = ["apple", "banana", "cherry","banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# #remove specified index
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# #if you do not specify the index, the pop() method removes the last item
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# #the del keyword also removes the specified index 
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# #del keyword can also delete the list completely
# thislist = ["apple", "banana", "cherry"]
# del thislist

# #clear the list
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# #loop through a list
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)

# #loop through the index numbers
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[1])

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i > len(thislist):
#     print(thislist[1])
#     i = i+1

#this comprehensive offers the shortest syntax for looping through list:
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# loop for 
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1
#usual
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)



