from xml.dom import minidom
import xml.etree.ElementTree as ET

xmlTree = ET.parse("My_Second_xml_workFile.xml")
tags = list({elem.tag for elem in xmlTree.iter()})
print(tags)

# ['exit_button', 'start', 'EnglishLanguage', 'buy_button', 'info_button']

List_of_tags_from_xmlFile_2 = []
My_xmlFile_2 = ET.parse("My_Second_xml_workFile.xml")

for i in My_xmlFile_2.iter():
    List_of_tags_from_xmlFile_2.append(i)

print(List_of_tags_from_xmlFile_2[0])

# """[<Element 'EnglishLanguage' at 0x0000021EB6FF6270>,
#  <Element 'start' at 0x0000021EB7005C20>,
#   <Element 'buy_button' at 0x0000021EB7005C70>,
#    <Element 'buy_button' at 0x0000021EB7005CC0>,
#     <Element 'buy_button' at 0x0000021EB7005D10>,
#      <Element 'info_button' at 0x0000021EB7005D60>,
#       <Element 'exit_button' at 0x0000021EB7005E00>]"""

def data_of_a_tag(TagName):
    My_xmlFile = minidom.parse("My_Second_xml_workFile.xml")
    Tags = My_xmlFile.getElementsByTagName(TagName)
    tag_datas_list = []
    for All_datas in Tags:
        Tag_data = All_datas.firstChild.data
        # Tag_data = "\n"+All_datas.firstChild.data
        tag_datas_list.append(Tag_data)
    return(tag_datas_list)


def name_sender():
    name = "Reza"
    return name

user_enteringTag = input("Enter tag name = ")

if len(data_of_a_tag(user_enteringTag)) != 0:
    print(data_of_a_tag(user_enteringTag))

else:
    print("There is no {} tag".format(user_enteringTag))

if name_sender() == "Reza":
    print("OK name .")
