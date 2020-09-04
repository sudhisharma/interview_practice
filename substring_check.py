# Check the given string is a substring

"""
 intputs :-

     "abcdabcdabcd"  is True
     "abcdaabcdabcd" is False
 """
x = "abcdabcdabcd"
y = "abcdaabcdabcd"
z = "aa"


def check_substring(str1):
    temp = str1 + str1  # aaaa
    temp = temp[1:-1]  # aa
    if str1 in temp:  #
        return True
    else:
        return False


print(check_substring(x))
print(check_substring(y))