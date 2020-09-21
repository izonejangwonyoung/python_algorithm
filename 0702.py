import re

# p= re.compile('[a-z]+')
# m=p.match('3154')
# print(m)




# p= re.compile('[a-z]+')
# m=p.search('3 pythonm')
# print(m)

# p= re.compile('[a-c]+')
# m=p.findall('black desert mobile')
# print(m)


# import re
# p = re.compile('[a-z]+')
# m= p.finditer('black desert mobile')
# for r in m:
#     print(r)



p= re.compile('[a-z]+')
m=p.match('black desert mobile')
print(m.group)
print(m.start())
print(m.end())
print(m.span())
