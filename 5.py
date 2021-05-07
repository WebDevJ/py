'''

a = 'Hello!'

Here’s a simple example of a Python function:
len(a)
Result: 6

And an example for a Python method:
a.upper()
Result: 'HELLO!'

1 - Python functions and methods - len upper

So what are Python functions and methods? In essence they transform something into something else. In this case the input was 'Hello!' and the output was the length of this string (6), and then the capitalized version: 'HELLO!'. Of course, these are not the only 2 functions you can use: there are plenty of them. Combining them will help you in every part of your data project – from data cleaning to machine learning. Everything.

Built-in vs. user-defined functions and methods
The cool thing is that besides the long list of built-in functions/methods, you can create your own too! Also, you will see that when you download, installing and importing different Python libraries, they will come with extra functions and methods as well. So there are indeed infinite possibilities. I’ll get back to this topic later. For now, let’s focus on the built-in things.

The most important built-in Python functions for data projects
Python functions work very simply. You call the function and specify the required arguments, then it will return the results. The type of the argument (e.g. string, list, integer, boolean, etc…) can be restricted (e.g. in some cases it has to be an integer), but in most cases it can be multiple value types. Let’s take a look at the most important built-in Python functions:

print()
We have already used print(). It prints your stuff to the screen.
Example: print("Hello, World!")

2 - Python functions and methods - print

abs()
returns the absolute value of a numeric value (e.g. integer or float). Obviously it can’t be a string. It has to be a numeric value.
Example: abs(-4/3)

3 - Python functions and methods - abs

round()
returns the rounded value of a numeric value.
Example: round(-4/3)

4 - Python functions and methods - round

min()
returns the smallest item of a list or of the typed-in arguments. It can even be a string.
Example 1: min(3,2,5)
Example 2: min('c','a','b')

5 - Python functions and methods - min

max()
Guess, what! It’s the opposite of min(). 🙂

sorted()
It sorts a list into ascending order. The list can contain strings or numbers.
Example:
a = [3, 2, 1]
sorted(a)

6 - Python functions and methods - sorted

sum()
It sums a list. The list can have all types of numeric values, although it handles floats… well, not smartly.
Example1:
a = [3, 2, 1]
sum(a)
Example1:
b = [4/3, 2/3, 1/3, 1/3, 1/3]
sum(b)

7 - Python functions and methods - sum

len()
returns the number of elements in a list or the number of characters in a string.
Example: len('Hello!')

8 - Python functions and methods - len

type()
returns the type of the variable.
Example 1:
a = True
type(a)
Example 2:
b = 2
type(b)

9 - Python functions and methods - type

These are the built-in Python functions that you will use quite regularly. If you want to see all of them, here’s the full list: https://docs.python.org/3/library/functions.html

But I’ll also show you more in my upcoming tutorials.

The most important built-in Python methods
Most of the Python methods are applicable only for a given value type. Eg. .upper() works with strings, but doesn’t work with integers. And .append() works with lists only and doesn’t work with strings, integers or booleans. So I’ll break down the methods by value type!

Methods for Python Strings
The string methods are usually used during the data cleaning phase of the data project. E.g. imagine that you collect data about what people are searching for on your ecommerce website. And you find these strings: 'mug', 'mug ', 'Mug'. You know that this is the same, but to let Python know too, you should handle this situation! Let’s see the most important string methods in Python:

a.lower()
returns the lowercase version of a string.
Example:
a = 'MuG'
a.lower()

9 - Python functions and methods - lower

a.upper()
the opposite of lower()

a.strip()
if the string has whitespaces at the beginning or at the end, it removes them.
Example:
a = ' Mug '
a.strip()

10 - Python functions and methods strip

a.replace('old', 'new')
replaces a given string with another string. Note that it’s case sensitive.
Example:
a = 'muh'
a.replace('h','g')

11 - Python functions and methods - replace

a.split('delimiter')
splits your string into a list. Your argument specifies the delimiter.
Example:
a = 'Hello World'
a.split(' ')
Note: in this case the space is the delimiter.

12 - Python functions and methods - split

'delimiter'.join(a)
It joins elements of a list into one string. You can specify the delimiter again.
Example:
a = ['Hello', 'World']
' '.join(a)

13 - Python functions and methods - join

Okay, that’s it for the most important string methods in Python.

Methods for Python Lists
Do you remember the last article, when we went through the Python data structures? Let’s talk a little bit about them again. Last time we discussed how to create a list and how to access its elements. But I haven’t told you about how to modify a list. Any tips? Yes, you will need the Python List methods!

Let’s bring back our favorite Python Dog, Freddie:
dog = ['Freddie', 9, True, 1.1, 2001, ['bone', 'little ball']]

Let’s see how we can modify this list!
a.append(arg)
The .append() method adds an element to the end of our list. In this case, let’s say we want to add the number of legs Freddie has (which is 4).
Example:
dog.append(4)
dog

14 - Python functions and methods - append

a.remove(arg)
If we want to remove the birth year, we can do it using the .remove() method. We have to specify the element that we want to remove and Python will remove the first item with that value from the list.
dog.remove(2001)
dog

15 - Python functions and methods - remove

a.count(arg)
returns the number of the specified value in a list.
Example:
dog.count('Freddie')

16 - Python functions and methods - count

a.clear()
removes all elements of the list. It will basically delete Freddie. No worries, we will get him back.
Example:
dog.clear()
dog

17 - Python functions and methods - clear

By the way, here you can find the full list of list methods in Python: https://docs.python.org/3/tutorial/datastructures.html

Methods for Python Dictionaries
As with the lists, there are some important dictionary functions to learn about.

Here’s Freddie again (see, I told you he’d be back):

dog_dict = {'name': 'Freddie',
'age': 9,
'is_vaccinated': True,
'height': 1.1,
'birth_year': 2001,
'belongings': ['bone', 'little ball']}
dog_dict.keys()
will return all the keys from your dictionary.

18 - Python functions and methods - keys

dog_dict.values()
will return all the values from your dictionary.

19 - Python functions and methods - values

dog_dict.clear()
will delete everything from your dictionary.

20 - Python functions and methods - clear

Note:
Adding an element to a dictionary doesn’t require you to use a method; you have to do it by simply defining a key-value pair like this:
dog_dict['key'] = 'value'
Eg.
dog_dict['name'] = 'Freddie'

21 - Python functions and methods - add element to dictionary

Okay, these are all the methods you should know for now! We went through string, list and dictionary Python methods!
It’s time to test yourself!

Test yourself!
For this exercise you will have to use not only what you have learned today, but what you have learned about Python Data Structures and variable types too! Okay, let’s see:

Take this list:
test_yourself = [1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]
Calculate the mean of the list elements – by using only those things that you have read in this and the previous articles!
Calculate the median of the list elements – by using only those things that you have read in this and the previous articles!
.

.

.

And the solutions are:
2) sum(test_yourself) / len(test_yourself)
Where the sum() sums the numbers and the len() counts the elements. The division of those will return the mean. The result is: 2.909090

22 - Python functions and methods - test yourself 1

3) test_yourself[round(len(test_yourself) / 2) - 1]
We are lucky to have a list with an odd number of elements.

Note: this formula won’t work for a list with an even number of elements.

len(test_yourself) / 2 will basically tell us where in the list we should look for our middle number – which will be the median. The result is 5.5, but in fact the result of len() / 2 will always be less by 0.5 than our exact number – when the list has odd number of elements (check it out for a 3 or 5-element list too). So let’s round this 5.5 up to 6 by using round(len(test_yourself) / 2). That’s right: we can put a function into a function. Then subtract one because of the zero-based indexing: round(len(test_yourself) / 2) - 1

And eventually use this result as the index of the list: test_yourself[round(len(test_yourself) / 2) - 1] or replace it with the exact number: test_yourself[5]. The result is: 3.

'''