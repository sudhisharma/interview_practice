#Script to check the work count in a given string

"""
input : "This is a text contains text, this is a word of word"
output : {'this':2 ,'is':2,'a':2, 'text':2 ,......}

"""

str1  = "This is a text contains text, this is a word of word."

def word_count(string1):
    new_list = [(i.strip(",.")).lower() for i in string1.split()]
    new_dict ={}
    for i in new_list:
        new_dict[i] = new_list.count(i)
    return new_dict

print(word_count(str1))