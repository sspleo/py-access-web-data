import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)  # make a tree from string
print('Name:', tree.find('name').text)  # attribute : text
print('Attr:', tree.find('email').get('hide'))  # attribute : get('hide')
# eml = tree.find('email')
# print('email:', eml.get('hide'))
