test_str = "12345";

# print(test_str);
# print(test_str[1]);
# print(test_str[-1]); #negative index also possible
# print(test_str[10]); #string index out of range
# print(type(test_str)); #<class 'str'>

# slicing test_str[start:stop:step]

# print(test_str[:2]) #12
# print(test_str[2:]) #345
# print(test_str[:]) #12345
# print(test_str[::2]) #135
# print(test_str[::-1]) # Reverse a string
# print("10///" + test_str[1:]) #concatenation
# print(test_str.replace('2', 'two'), " -> ", test_str)


# print("stRiNg".upper())
# print("stRiNg".lower())
str_with_spaces = "  dfs sfdsf sd ";
# print(str_with_spaces.strip()) #deletes spaces at the and and at the start
# print(str_with_spaces.lstrip()) #deletes spaces at the left
# print(str_with_spaces.rstrip()) #deletes spaces at the right
# print("*" * 5) #repeating
# print("1" in test_str) #check if in string
# print(test_str.find("3")) #check if in string

multi_line_str_1 = """
  123
  123
  123fasd
  ads
""";

multi_line_str_2 = '''
  123 12
  12123
  123
  21
  3
''';

# print(multi_line_str_2.count("2")) #returns number of occurrences in a string
# print(multi_line_str_1)
# print(multi_line_str_2)


# f string

# print(f"my numbers are {test_str}")

