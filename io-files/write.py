# modes
# r - read only
# w - write only. Will overwrite file or create a new one if it does not exist
# a - append only
# r+ - read and write
# w+ - writing and reading The file is created if it does not exist, otherwise it is truncated.

with open('test.txt', mode='w') as myFile:
  myFile.write('new data bla bla bla')

with open('test.txt', mode='a') as myFile:
  myFile.write('\nanother new data bla bla bla')