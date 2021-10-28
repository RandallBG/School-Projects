#!/usr/bin/env python3

while True:
    print("\n\n1. Creating Lists and accessing members")
    print("2. Negative Indexes")
    print("3. Slicing")
    print("4. Appending and Extending lists in Python")
    print("5. Concatenating and repeating lists")
    print("6. Demonstration of list insert() method")
    print("7. Exit")
    section = int(input("Run example code: "))
    
    if section == 1:
        print("\n\nCreating Lists and accessing members")
        # list of integers
        my_list = [1, 2, 3]
        print(my_list)
        
        # empty list
        my_list = []

        # list with mixed data types
        my_list = [1, "Hello", 3.4]
        print(my_list)
        
        # nested list
        my_list = ["mouse", [8, 4, 6], ['a']]
        print(my_list)
        
        my_list = ['C', 'l', 'e', 'v', 'E', 'l', 'a', 'n', 'd']
        print(my_list)
        
        # first item
        print(my_list[0])  # C

        # third item
        print(my_list[2])  # e

        # fifth item
        print(my_list[4])  # E

        # Nested List
        n_list = ["Happy", [2, 0, 1, 5]]

        # Nested indexing
        print(n_list[0][1])

        print(n_list[1][3])

        # Error! Only integer can be used for indexing
        #  print(my_list[4.0])
        
    if section == 2:
        print("\n\nNegative Indexes")
        # Negative indexing in lists
        my_list = ['C', 'l', 'e', 'v', 'E', 'l', 'a', 'n', 'd']
        print(my_list)
        
        # last item
        print(my_list[-1])

        # fifth last item
        print(my_list[-5])
        
    if section == 3:
        print("\n\nSlicing")
        # List slicing in Python

        my_list = ['p','r','o','g','r','a','m','m','i', 'n', 'g']

        # elements from index 2 to index 4
        print(my_list[2:5])

        # elements from index 5 to end
        print(my_list[5:])

        # elements beginning to end
        print(my_list[:])

        #When we slice lists, the start index is inclusive but the end index is exclusive. 
        #For example, my_list[2: 5] returns a list 
        #with elements at index 2, 3 and 4, but not 5.

        # Correcting mistake values in a list
        odd = [2, 4, 6, 8]

        # change the 1st item    
        odd[0] = 1            

        print(odd)

        # change 2nd to 4th items
        odd[1:4] = [3, 5, 7]  

        print(odd) 

    if section == 4:
        print("\n\nAppending and Extending lists in Python")
        # Appending and Extending lists in Python
        odd = [1, 3, 5]

        odd.append(7)

        print(odd)

        odd.extend([9, 11, 13])

        print(odd)

    if section == 5:
        print("\n\nConcatenating and repeating lists")
        # Concatenating and repeating lists
        odd = [1, 3, 5]

        print(odd + [9, 7, 5])

        print(["re"] * 3)

    if section == 6:
        print("\n\nDemonstration of list insert() method")
        # Demonstration of list insert() method
        odd = [1, 9]
        odd.insert(1,3)

        print(odd)

        odd[2:2] = [5, 7]

        print(odd)
    if section == 7:
         break
print("\n\nBye")

