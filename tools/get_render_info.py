import os
rendersPath = "../renders/"
imageRendersPath = "../img/renders/"
try:
    renders = os.listdir(rendersPath)
    imageRenders = os.listdir(imageRendersPath)
except:
    rendersPath = "./renders/"
    imageRendersPath = "./img/renders/"
    renders = os.listdir(rendersPath)
    imageRenders = os.listdir(imageRendersPath)
missingRenders = []
for imageRender in imageRenders:
    imageRender = imageRender.split(".", 1)[0]
    if not imageRender in renders:
        missingRenders.append(imageRender)
print(f"Missing renders: {missingRenders}")
print(f"# of renders missing: {len(missingRenders)}")
print(f"Total # of renders with page: {len(renders)}/{len(imageRenders)} ({round(len(renders)/len(imageRenders)*100,2)}%)")