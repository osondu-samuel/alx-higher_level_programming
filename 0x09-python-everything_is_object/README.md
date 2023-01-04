# Python - Everything is object
This document stores a simple description of each file in the  `0x09-python-everything_is_object` repository.

## Files
`0-answer.txt:` What function would you use to print the type of an object?.

`1-answer.txt:` How do you get the variable identifier (which is the memory address in the CPython implementation)?.

`2-answer.txt:` Do a and b point to the same object? >>> a = 89.

`3-answer.txt` Do a and b point to the same object? >>> a = 89 >>> b = 89.

`4-answer.txt` Do a and b point to the same object? >>> a = 89 >>> b = a".

`5-answer.txt:` Do a and b point to the same object? >>> a = 89 >>> b = a + 1.

`6-answer.txt:` What do these 3 lines print? >>> s1 = "Holberton" >>> s2 = s1 >>> print(s1 == s2).

`7-answer.txt:` What do these 3 lines print? >>> s1 = "Holberton" >>> s2 = s1 >>> print(s1 is s2).

`8-answer.txt:` What do these 3 lines print? >>> s1 = "Holberton" >>> s2 = "Holberton" >>> print(s1 is s2).

`9-answer.txt:` What do these 3 lines print? >>> s1 = "Holberton" >>> s2 = "Holberton" >>> print(s1 is s2).

`10-answer.txt:` What do these 3 lines print >>> l1 = [1, 2, 3] >>> l2 = [1, 2, 3]  >>> print(l1 == l2).

`11-answer.txt:` What do these 3 lines print >>> l1 = [1, 2, 3] >>> l2 = [1, 2, 3]  >>> print(l1 is l2).

`12-answer.txt:` What do these 3 lines print >>> l1 = [1, 2, 3] >>> l2 = l1  >>> print(l1 == l2).

`13-answer.txt:` What do these 3 lines print >>> l1 = [1, 2, 3] >>> l2 = l1  >>> print(l1 is l2).

`14-answer.txt:` What does this script print? l1 = [1, 2, 3], l2 = l1, l1.append(4), print(l2).

`15-answer.txt:` What does this script print? l1 = [1, 2, 3], l2 = l1, l1 = l1 + [4], print(l2).

`16-answer.txt:` What does this script print?; def increment(n):, n += 1; a = 1, increment(a), print(a).

`17-answer.txt:` What does this script print?; def increment(n):, n.append(4); l = [1, 2, 3], increment(l), print(l).

`18-answer.txt:` What does this script print?; def assign_value(n, v):, n = v; l1 = [1, 2, 3], l2 = [4, 5, 6], assign_value(l1, l2), assign_value(l1, l2).

`19-copy_list.py:` Function def copy_list(l): that returns a copy of a list.

`20-answer.txt:` Is a a tuple? a = ().

`21-answer.txt:` Is a a tuple? a = (1, 2).

`22-answer.txt:` Is a a tuple? a = (1).

`23-answer.txt:` Is a a tuple? a = (1,).

`24-answer.txt:` What does this script print?; a = (1), b = (1), a is b.

`25-answer.txt:` What does this script print?; a = (1, 2), b = (1, 2), a is b.

`26-answer.txt:` What does this script print?; a = (), b = (), a is b.

`27-answer.txt:` Will the last line of this script print 139926795932424? >>> a = [1, 2, 3, 4] >>> id(a), 139926795932424 >>> a = a + [5] >>> id(a).

`28-answer.txt:` Will the last line of this script print 139926795932424? >>> a = [1, 2, 3] >>> id(a), 139926795932424 >>> a += [4] >>> id(a).

`100-magic_string.py:` Function magic_string() that returns a string “Holberton” n times the number of the iteration.

`101-locked_class.py:` Class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

`103-line1.txt:` How many int objects are created by the execution of the first line of the script?, a = 1, b = 1.

`103-line2.txt:` How many int objects are created by the execution of the second line of the script?, a = 1, b = 1.

`104-line1.txt:` How many int objects are created by the execution of the first line of the script?, a = 1024, b = 1024, del a, del b, c = 1024.

`104-line2.txt:` How many int objects are created by the execution of the second line of the script?, a = 1024, b = 1024, del a, del b, c = 1024.

`104-line3.txt:` After the execution of line 3, is the int object pointed by a deleted?, a = 1024, b = 1024, del a, del b, c = 1024.

`104-line4.txt:` After the execution of line 4, is the int object pointed by b deleted?, a = 1024, b = 1024, del a, del b, c = 1024.

`104-line5.txt:` How many int objects are created by the execution of the last line of the script, a = 1024, b = 1024, del a, del b, c = 1024".

`106-line1.txt:` How many string objects are created by the execution of the first line of the script? a = "HBTN", b = "HBTN", del a, del b, c = "HBTN".

`106-line2.txt:` How many string objects are created by the execution of the second line of the script a = "HBTN", b = "HBTN", del a, del b, c = "HBTN"

`106-line3.txt:` After the execution of line 3, is the string object pointed by a deleted? a = "HBTN", b = "HBTN", del a, del b, c = "HBTN".

`106-line4.txt:` After the execution of line 4, is the string object pointed by b deleted? a = "HBTN", b = "HBTN", del a, del b, c = "HBTN".

`106-line5.txt:` How many string objects are created by the execution of the last line of the script a = "HBTN", b = "HBTN", del a, del b, c = "HBTN".

## Reference 

- [9.10. Objects and values](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values "9.10. Objects and values")
- [9.11. Aliasing](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing "9.11. Aliasing")
- [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types "Immutable vs mutable types")
- [Mutation (Only this Chapter)](http://composingprograms.com/pages/24-mutable-data.html#sequence-objects "Mutation")
- [9.12. Cloning lists](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists "9.12. Cloning lists")
- [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html "Python tuples: immutable but potentially changing")

## Authors
Raymond Lukwago A.R
