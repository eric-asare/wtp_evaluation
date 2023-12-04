import scoring
import Punkt_implementation
import os
from collections import defaultdict

mount = "/Users/mashrafi/Desktop/NLP/Final Project"
directory = mount + "/MASC-3.0.0/data/written/"

folders = os.listdir(directory)

for folder in folders:
  if os.listdir(directory+folder):
    foundOne = False
    for item in os.listdir(directory+folder):
      if "." not in item:
        foundOne = True
        folders.append(f"{folder}/{item}")
    if foundOne:
      folders.remove(folder)

files = defaultdict(dict)

for folder in folders:
  if folder.startswith('.'):
    continue
  files[folder][".xml"] = []
  files[folder][".txt"] = []
  for file in os.listdir(directory+folder):
    if "-s.xml" in file:
      files[folder][".xml"].append(file)
    elif ".txt" in file:
      files[folder][".txt"].append(file)

score = {}

for genre in files:
  text_files = files[genre][".xml"]
  correct = 0
  system = 0
  answer = 0
  for text_file in text_files: 
    print(text_file) 
    mount1 = "MASC-3.0.0/data/written/"
    mount2 = "WtP_System/data/written/"
    correct_t, system_t, answer_t = scoring.score(mount1 + genre + "/" + text_file, mount2 + genre + "/" + text_file.rstrip(".xml") + "ystem.txt")
    correct += correct_t
    system += system_t
    answer += answer_t
  score[genre] = {}
  score[genre]["precision"] = correct/system
  score[genre]["recall"] = correct/answer
  score[genre]["f-score"] = 2*correct/(answer+system)



score_punkt = {}
for genre in files:
  text_files = files[genre][".txt"]
  mount1 = "MASC-3.0.0/data/written/"
  correct = 0
  system = 0
  answer = 0
  for text_file in text_files:
    system_list = Punkt_implementation.implementation(mount1 + genre + "/" + text_file)
    temp_text = text_file.replace(".txt", "-s.xml")
    correct_t, system_t, answer_t = scoring.score(mount1 + genre + "/" + temp_text, system_list, list = True)
    correct += correct_t
    system += system_t
    answer += answer_t
  score_punkt[genre] = {}
  score_punkt[genre]["precision"] = correct/system
  score_punkt[genre]["recall"] = correct/answer
  score_punkt[genre]["f-score"] = 2*correct/(answer+system)

sc = open("Scores.txt", 'w')
for genre in score:
  print(f'''{genre}:
                                "WtP"                           "Punkt"
                    Precision:  {score[genre]["precision"]}     {score_punkt[genre]["precision"]}
                    Recall :    {score[genre]["recall"]}        {score_punkt[genre]["recall"]}
                    F-score:    {score[genre]["f-score"]}       {score_punkt[genre]["f-score"]}
        ''', file = sc)