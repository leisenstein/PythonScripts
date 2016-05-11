import os, re, shutil, sys, getopt
from PIL import Image



SourceDir = 'C:\\Working\\SourceThumbnails\\GrantImageUpdate'
ThumbsDir = 'Thumbs_160x120'

print(SourceDir)

try:
    opts, args = getopt.getopt(sys.argv, "src")
except getopt.GetoptError:
    print('beginningScript.py -src <SourceDirectory>')
    sys.exit(2)

print('Options: ' + ', '.join(opts))
print('Arguments: ' + ', '.join(args))



for d in os.listdir(SourceDir):
    ImageDir = os.path.join(SourceDir, d)
    if os.path.isdir(ImageDir) and os.path.exists(os.path.join(ImageDir, ThumbsDir)):
        for f in os.listdir(os.path.join(ImageDir, ThumbsDir)):
            if(f.endswith('.jpg') and f.endswith('_xxx.jpg')):
                # im = Image.open(os.path.join(ImageDir, ThumbsDir, f))
                fileToDelete = f.replace('_xxx.jpg', '.jpg')
                fullFileToDelete = os.path.join(ImageDir, ThumbsDir, fileToDelete)
                print('Deleting file: ' + fullFileToDelete)
                # os.remove(fullFileToDelete)
                
                fullF = os.path.join(ImageDir, ThumbsDir, f)
                print('Renaming file: ' + fullF + ' ::::: TO :::: ' + fullFileToDelete)
                #os.rename(fullF, fullFileToDelete)