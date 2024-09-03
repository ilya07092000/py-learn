myFile = open('test.txt')
print(myFile.read())
print('DIVIDER')
print(myFile.read()) # empty

myFile.seek(0) # move cursor to the beginning
print(myFile.read()) # data is here again

myFile.seek(0) # move cursor to the beginning
print(myFile.readlines()) # lines of file stored in the list

myFile.close() # need to close the file to not get an error when you try to delete it in another place 


# in this case we do not need to care about closing the file
with open('test.txt') as myNewFile:
  print('myNewFile: ', myNewFile.read())

  