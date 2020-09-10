### Use this site for https methods
# https://httpbin.org/

import requests

r = requests.get("https://xkcd.com/353/")

#print(dir(r))

print(r.status_code)

print(r.ok)

# To download the image form the portal
r = requests.get("https://imgs.xkcd.com/comics/python.png")

with open("image_file.png","wb")as f :
    f.write(r.content)

#response = requests.get("https://httpbin.org/get?page=2&count=25")
# rather than doinng that

payload = {'page':2 , "count":25}

response_new = requests.get("https://httpbin.org/get",params=payload)

#print(response_new.text)

print(response_new.url)

########################## Post methosd ################################
payload = {"name":"sudhe","password":"testing"}
r = requests.post("https://httpbin.org/post" , data=payload)

#print(r.text)

# Other than printing the normal teaxt we can convert the json response into python dictnary uisng json() method
r_dict = r.json()
print(r_dict['form'])

####################### Authentication ######################################

r_auth = requests.get("https://httpbin.org/basic-auth/sudhi/test", auth = ("sudhi","test") , timeout = 3)
print(r_auth.text)