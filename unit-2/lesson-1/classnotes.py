##### have [] for lists!! [] is a list
# myList = ["class" , "in" , "movies" , "kirsten"]

# print(myList)
# ### .append is appending to the list, allows us to add things to a list, like adding things to a list
# #### useful for looping algorithm
# myList.append("today")

# print(myList)

# #################################

# ##### looking for things specifically in a list []!!
# ### so this is something like a true or false statement
# iskirsteninlist = "kirsten" in myList
# #### "in" is useful to check if one thing is in something else, so piece of data in something else
# print(iskirsteninlist)
# ### prints back "true" or false

# #################################

##### making a dictionary {}!!!
### it's a more complex way to structure information
### the terms "key" and "value" in place of "word" and "definition"
dictionary = {}
### making a word definition pair, a key value pair
dictionary["subject"] = "theory"
### this is another key value pair
dictionary["course"] = "coding as a liberal art"
### one more key value pair
dictionary["department"] = "eugene lang"
### possible to put lists inside of dictionaries!
dictionary["colors"] = ["blue" , "green" , "red" , "pink" , "orange"]
dictionary["home"] = "maison"
# print(dictionary)

###### seeing value of key and value pairs 
# for key in dictionary:
#     print( key, "---->", dictionary[key])
######

# #################################

dictionary["total"] = 0

### use for loops because it's to update value in dictionary, so you need access to each item, need to loop over things in the dictionary
### item is variable!! 
### .items() is something you can use on a dictionary and saying that each tuple/pair is an item 
for item in dictionary.items():
    # print(item)
    #### gives access specifically to one thing in the item pair
    for x in item:
        if (type(x) is list):
            #### think string, list, integer 
            print("this is not a string, but there are", len(x), "items in this list!")
            #### can now check what type of data x is 

# ######## i is for the items in list, and each item in the list, update the total + 1
            for i in x:
                dictionary["total"] = dictionary["total"] + 1
            ### again, for the list in the dictionary, adds +1 when the items in list increases

        
        if (type(x) is str):
            print("there are", len(x), "characters in this string:", x)
            ### useful for seeing the type of data, so "str" is for seeing if it's a string, and a string is whatever is in between ""
print(dictionary)



### .values() gives each value so useful for checking what type of data it is
# #### gives metadata attached to image

# from os import listdir, path
# from PIL import Image, ExifTags

# files = listdir("images")
# img - Image.open(path.join("images"), )))

#### so depending on the number, it prints the item in the list according to the number, if I have a list of 5 items, and input "2" it will print the last three, and not the first two
# for item in range(1, len(myList)):
#     print(myList[item])