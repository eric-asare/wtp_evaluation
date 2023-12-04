import xml.etree.ElementTree as ET
import os

def parse(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Define the namespace used in the XML file
    namespace = {'graf': 'http://www.xces.org/ns/GrAF/1.0/'}

    # Find the region tags with anchors attribute
    regions = root.findall(".//graf:region[@anchors]", namespaces=namespace)

    region_list = []
    for region in regions:
        anchor_value = region.get("anchors")
        anchor_values = anchor_value.split()
        region_list += [int(anchor_values[1])]
    return region_list

# def parse_sentence(file_path, region):
#     f = open(file_path, 'r')
#     content = f.read()
#     sentences = []
#     for tuple in region:
#         sentences += [content[tuple[0]:tuple[1]]]
#     return sentences


# file_path = 'MASC-3.0.0/data/written/ficlets/1399-s.xml'
## region = parse(file_path)
# text_file_path = 'MASC-3.0.0/data/written/ficlets/1399.txt'
# sentences = parse_sentence(text_file_path, region)
# i = 0
# ground_truths = {}
# for sentence in sentences:
#     ground_truths[i] = sentence
    # i += 1
# temp_ground_truth = open("temp_ground_truth.txt", 'w')
# for sentence in sentences:
#     sentence = sentence.replace("\n", " ")
#     print(sentence)
#     print(sentence, file = temp_ground_truth)
