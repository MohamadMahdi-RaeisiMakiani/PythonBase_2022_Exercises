from xml.dom import minidom

#Open xml file
My_xml = minidom.parse("First_session-3.xml")

#uses phone tag
Phone_numbers = My_xml.getElementsByTagName("phone")

All_subTags = My_xml.getElementsByTagName("BusinessCard")
#second attribute value of phone tag
#where phone tag attribute is type
print(Phone_numbers[1].attributes["type"].value)
#work

print("----------------------")

#all attribute values of phone tag
#where phone tag attribute is type
for Each_PhoneNumber in Phone_numbers:
    print(Each_PhoneNumber.attributes["type"].value)

print("----------------------")

#second phone tag value that attribute is type
print(Phone_numbers[1].firstChild.data)
#It sames last line
print(Phone_numbers[1].childNodes[0].data)

print("----------------------")

#all phone tags value
for all_numbers in Phone_numbers:
    print(all_numbers.firstChild.data)

print("----------------------\n\n")

print("All phones in xml file : \n")
for all_phones in Phone_numbers:
    print(all_phones.attributes["type"].value+" : "+all_phones.firstChild.data)
