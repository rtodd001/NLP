import re

#"^": This expression matches the start of a string
#"w+": This expression matches the alphanumeric character in the string
#only check the very first word of the sentence
xx = "guru99, education11 is fun"
r1 = re.findall(r"^\w+",xx)
print(r1)

abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com, thisIsnotanEmail, sothing@, @@'

emails = re.findall(r'[\w\.-]+.@[\w-]+\.[a-z]{3}', abc)
for i in emails:
    print(i)