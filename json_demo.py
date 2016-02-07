# Computer Programming 1
# JSON Demo
#
# by Jon Cooper
# January 28, 2014


# What is JSON?
#
# JSON, or JavaScript Object Notation, is an open standard format that
# uses  human-readable text to transmit data objects consisting of
# attribute–value pairs. It is used primarily to transmit data between
# a server and web application, as an alternative to XML.
#
# Although originally derived from the JavaScript scripting language,
# JSON is a language-independent data format, and code for parsing and
# generating JSON data is readily available in a large variety of
# programming languages.
#
# source: http://en.wikipedia.org/wiki/JSON


# Import json module (We'll use this later.)
import json


# Make some dictionaries
a = {'lang': 'spanish', 'one': 'uno', 'two': 'dos', 'three': 'tres'}
b = {'lang': 'french', 'one': 'un', 'two': 'deux', 'three': 'trios'}
c = {'lang': 'latin', 'one': 'unus', 'two': 'duo', 'three': 'tres'}


# Now the dictionaries in a list
languages = [a, b, c]


# Check the contents of the list.
print(languages)


# Check the types of our data to confirm that we do have a list of
# dictionaries.
print(type(languages))
print(type(languages[0]))


# Python's built-in json module is designed to handle exactly this
# kind of data represented as a string.

json_string = json.dumps(languages)
print(json_string)       # The data looks the same, but
print(type(json_string)) # it's not a list of dicts anymore.


# Let's write the json_string to a text file. Then open the newly-
# created file to confirm that it contains our language data.

file_name = 'data1.json' # use the .json extension

with open(file_name, 'w') as f:
    f.write(json_string)


# Even though it is fairly easy to see that our data file contains
# a list of strings, it is still not easily 'human-readable' which
# is one of the main reasons for using JSON. Fortunately, Python's
# json library supports 'pretty printing'.

pretty_json_string = json.dumps(languages, indent=4)
print(pretty_json_string) # much better


# The nicer output is much better for putting in a data file.
# (Python dicts aren't ordered, so the terms are a little jumbled.
#  At least it's neat.)

file_name = 'data2.json'

with open(file_name, 'w') as f:
    f.write(pretty_json_string)


# We can also read JSON files.

file_name = 'data3.json'

with open(file_name, 'r') as f:
    raw_data = f.read()

print(type(raw_data))


# Convert the data to a JSON format (list of dicts).
json_data = json.loads(raw_data)


# Test the types.
print(type(json_data))
print(type(json_data[1]))


# So now we have our file loaded into a program as a list of
# dict items again. What this means is that we can now write
# applications that keep the data and code separate. This
# will allow us to write much cleaner and more maintainable
# code. 


# Note:
#
# We could have accomplished everything in this program without
# ever using the json module. We already know how to read files
# as strings. We could split the strings on commas and colons
# and loop through the data to create dicts and lists. However,
# the json module already has the code that does this for us.
# Why not just use the json module and make it easy!



# Your turn...
#
# Design a JSON file that would keep track of something you like.
# (Perhaps Pokemon cards, players on your fantasy football team,
# your music library, etc.) You do not need to write any Python code.
# just create the json file using a text editor. (Notepad++ or 
# Komodo Edit will work well.) Make sure your file has at least
# 10 items and each item has at least 4 key:value pairs.
#
# Your next project will be to make a contact manager. However, I 
# will allow you to "manage" some other kind of data if you would like.
# Write a proposal for what you would like to do instead. I'll review
# the proposals and either approve or help you modify the proposal
# so that it will meet rubric requirements. We'll begin a project next
# week.
