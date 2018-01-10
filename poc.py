import lxml.etree as ET

tree = ET.parse('poc.xml')

root = tree.getroot()

payload=ET.fromstring("""
    <country name="LOLXD">
        <rank>68</rank>  
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
""")
payload.tail='\n'

last_item=None
for pos, one_element in enumerate(root.iter('country')):
	last_item=one_element
else:
	last_item.getparent().insert(pos+1, payload)
	last_item.tail='\n{}'.format(' '*4) # multiply by amount that you need

tree.write('poc_res.xml', xml_declaration=True)

