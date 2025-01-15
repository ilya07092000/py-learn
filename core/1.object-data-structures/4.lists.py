list1 = [];

list1.append(1);
list1.append(2);
list1.append(3);
list1.append(1);

# copy() - shallow copy
list2 = list1.copy();
list2.append(111);
print(list1, list2)

# clear() - Removes all elements from the list.

# count(el): Returns the number of times a specified element appears in the list.
print(list1.count(1))

# extend(list): Adds elements from another list to the end of the current list.
list1.extend(list2)
print(list1)

# index(el, start, end): Returns the index of the first occurrence of a specified element.
print(list1.index(2))

# insert(): Inserts an element at a specified position.
print(list1)
list1.insert(2, 'inserted to index 2')
print(list1)

# pop(): Removes and returns the element at the specified position (or the last element if no index is specified)
print(list1.pop(2))
print(list1.pop())

# remove(): Removes the first occurrence of a specified element.
list1.remove(3)

# reverse(): Reverses the order of the elements in the list.
print(list1)
list1.reverse()
print(list1)

#sort(): Sorts the list in ascending order (by default).
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

dictList = [{"age": 1}, {"age": 100}, {"age": 45}, {"age": 76}, {"age": 104}]

def sortFn(dict):
  return dict["age"];

dictList.sort(key=sortFn)
print(dictList)

dictList.sort(key=lambda dict: dict["age"], reverse=True)
print(dictList)

# sorted() returns a new sorted list, leaving the original list unaffected
print(sorted(dictList, key=lambda dict: dict["age"]))
print(dictList)