import os
setsPath = "../sets/"
imageSetsPath = "../img/sets/"
try:
    sets = os.listdir(setsPath)
    imageSets = os.listdir(imageSetsPath)
except:
    setsPath = "./sets/"
    imageSetsPath = "./img/sets/"
    sets = os.listdir(setsPath)
    imageSets = os.listdir(imageSetsPath)
missingSets = []
for imageSet in imageSets:
    imageSet = imageSet.split(".", 1)[0]
    if not imageSet in sets:
        missingSets.append(imageSet)
missingSets.sort()
print(f"Missing sets: {missingSets}")
print(f"# of sets missing: {len(missingSets)}")
print(f"Total # of sets with page: {len(sets)}/{len(imageSets)} ({round(len(sets)/len(imageSets)*100,2)}%)")