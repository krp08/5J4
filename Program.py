1)Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
Code :=
 import re
print(bool(re.match("^[A-Za-z0-9_-]*$", 'aValidString123--__')))
print(bool(re.match("^[A-Za-z0-9_-]*$", 'inv@lid')))

Output :=
True                             
False  




2)Write a Python program to find the occurrence and position of the substrings within a string.
Code :=
import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))
Output :=
Found "exercises" at 7:16        
Found "exercises" at 22:31       
Found "exercises" at 36:45   
