import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))  # go find 'x' attribute

# this is checking the nested structure
'''
print(" \n\n Let's look in to more in id elements")
lst1 = stuff.findall('users/user/id')
print('Id count:', len(lst1))

for elmt in lst1:
    print('ID :', elmt.text)
'''
