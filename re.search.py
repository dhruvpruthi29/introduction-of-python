import re
txt ="Python is a wonderful language"
x = re.search("language",txt)
print(x)


import re
txt ="Python is a wonderful language"
x = re.search("^Python.*Words$",txt)
print(x)