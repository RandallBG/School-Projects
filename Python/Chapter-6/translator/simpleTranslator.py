import xml.etree.ElementTree as ET

my_tree = ET.parse("./dictionary/englishToSpanish.xml")
root_node = my_tree.getroot()

# wordDict = {}
# def createDict():
#     for x in root_node[0]:
#         wordDict[x[0].text] = x[1].text

def translator(englishString):
    words = englishString.lower().split(' ')
    translatedSentence = ''
    
    for word in words:
        found = False
        for x in root_node[0]:
            if word == x[0].text:
                translation = []
                translation = x[1].text.split(',')
                translatedSentence +=" " +  translation[0]
                found = True
                break
        if found == False:
            translatedSentence += " " + word
    print(translatedSentence)


# createDict()

sentence = input("enter a sentance: ")

translator(sentence)

# print(root_node.tag)
# print(root_node[1].attrib)
# print(root_node[0][0])






    
    
