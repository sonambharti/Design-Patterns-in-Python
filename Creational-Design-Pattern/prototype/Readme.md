# Prototype Design Pattern

The Prototype design pattern is good for when creating new objects requires more resources than you want to use or have available. You can save resources by just creating a copy of any existing object that is already in memory.
E.g., A file you've downloaded from a server may be large, but since it is already in memory, you could just clone it, and work on the new copy independently of the original.

Terminology:
i.    Prototype Interface: The interface that describes the clone() method. 
ii.   Prototype: The Object/Product that implements the Prototype interface.
iii.  Client: The client application that uses and creates the ProtoType.

## Prototype UML Diagram 
                ![Prototype Design Pattern](<Prototype Design Pattern.png>)
                
# Example to show Concept of Prototype Design Pattern

## Output:
```
python3 ./protoype/prototype_concept.py
OBJECT1 4303700192      field=[1, 2, 3, 4]      type=<class 'list'>
OBJECT2 4303700096      field=[1, 101, 3, 4]    type=<class 'list'>
OBJECT1 4303700192      field=[1, 101, 3, 4]    type=<class 'list'>
```


# Overview to run the code to design a program to handle the cloning function of a document...
## Output:
```
python3 ./prototype/client.py 

4369759840      name=Original   list=[[1, 2, 3, 4], [5, 6, 7, 8]]

4369759888      name=Copy 1     list=[[1, 2, 3, 4], [5, 6, 200, 8]]
4369759840      name=Original   list=[[1, 2, 3, 4], [5, 6, 200, 8]]

4370006288      name=Copy 2     list=[[1, 2, 3, 4], [9, 10, 11, 12]]
4369759840      name=Original   list=[[1, 2, 3, 4], [5, 6, 200, 8]]

4370006240      name=Copy 3     list=[[1, 2, 3, 4], ['1234', 6, 200, 8]]
4369759840      name=Original   list=[[1, 2, 3, 4], ['1234', 6, 200, 8]]

4370121552      name=Copy 4     list=[[1, 2, 3, 4], ['5678', 6, 200, 8]]
4369759840      name=Original   list=[[1, 2, 3, 4], ['1234', 6, 200, 8]]

```


# Read from a file and implement Prototype Design Pattern
## Output: 
```
python3 ./prototype/client1.py
The original Document: 
 4307572480     name=Orignal_txt_document       list=['Sonam: Hello, I am Sonam. How are you? \n', 'Kartikay: Hi Guys, I am good. What were you guys doing?\n', 'Faizan: Yo! Are bhot badhiya.\n']
<class 'document.Document'>


Clone 1.....
Shallow copy

file 2: 
 4307944896     name=Copy_Demo 1        list=['Sonam: Hello, I am Sonam. How are you? \n', 'Hello', 'Faizan: Yo! Are bhot badhiya.\n']

file 1: 
 4307572480     name=Orignal_txt_document       list=['Sonam: Hello, I am Sonam. How are you? \n', 'Hello', 'Faizan: Yo! Are bhot badhiya.\n']



Clone 2.....
level 2 - Shallow copy

file 3: 
 4307944944     name=Copy_Demo 2        list=['Sonam: Hello, I am Sonam. How are you? \n', 'Hello', 'Faizan: Yo! Are bhot badhiya.\n', '"Aditi:" Hey I\'m here.']

file 2: 
 4307944896     name=Copy_Demo 1        list=['Sonam: Hello, I am Sonam. How are you? \n', 'Hello', 'Faizan: Yo! Are bhot badhiya.\n']

file 1: 
 4307572480     name=Orignal_txt_document       list=['Sonam: Hello, I am Sonam. How are you? \n', 'Hello', 'Faizan: Yo! Are bhot badhiya.\n']



Clone 3.....
Recursive Clone

file 4: 
 4307944992     name=Copy_Demo 3        list=['Sonam: Hello, I am Sonam. How are you? \n', 'Hello', 'Hey Idiots']

file 3: 
 4307944944     name=Copy_Demo 2        list=['Sonam: Hello, I am Sonam. How are you? \n', 'Hello', 'Faizan: Yo! Are bhot badhiya.\n', '"Aditi:" Hey I\'m here.']

file 2: 
 4307944896     name=Copy_Demo 1        list=['Sonam: Hello, I am Sonam. How are you? \n', 'Hello', 'Faizan: Yo! Are bhot badhiya.\n']

file 1: 
 4307572480     name=Orignal_txt_document       list=['Sonam: Hello, I am Sonam. How are you? \n', 'Hello', 'Faizan: Yo! Are bhot badhiya.\n']
 ```
