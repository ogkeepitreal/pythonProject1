# Write a code to return "Hero" from given string
example_string1 = "Hello bro"
string1 = example_string1[:2] + example_string1[-2:]
print(string1)


# Write a code to return "Jack is my name"
example_string2 = "jack Is My NAME"
string2 = example_string2
print(string2.capitalize())


# Write a code to return "Get rid of stars please"
example_string3 = "*Get rid of stars please*"
print(example_string3.strip('*'))


# Write a code to return "Hello my name is Jack"
example_string4 = "hello my naMe is jack"
example_string4 = (example_string4.replace('hello', 'Hello'))
example_string4 = (example_string4.replace('naMe', 'name'))
example_string4 = (example_string4.replace('jack', 'Jack'))
print(example_string4)


# Write a code to return formatted string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"

var1 = (var1.capitalize())
var2 = (var2.capitalize())
var3 = (var3.lower())
print(var2 + ', ' + var3 , var1)


# Write a code to return byte_string text value
# 'utf-8' 'utf-16'
byte_string = b"\316\273"
byte_string_utf8 = byte_string.decode('utf-8')
byte_string_utf16 = byte_string.decode('utf-16')
print(byte_string_utf8, byte_string_utf16)
