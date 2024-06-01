import re

# 3 lowercase letters
# 3 - 5 digits
# one symbol
# up to two uppercase characters (optional)

pattern = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]([A-Z]{0,2})?$")

print(pattern.search("ahd2331#AJ"))
print(pattern.search("lll44511.K"))
print(pattern.search("lll44511."))
print(pattern.search("abc123456#JJ"))
