import os, re, shutil, sys, getopt
from PIL import Image







SourceDir = 'C:\\pythontest'
ThumbsDir = 'Thumbs_160x120'


try:
        opts, args = getopt.getopt(sys.argv, "src")
except getopt.GetoptError:
        print('beginningScript.py -src <SourceDirectory>')
        sys.exit(2)

for opt, arg in opts:
        print(opt)
        print(arg)

for d in os.listdir(SourceDir):
    if os.path.isdir(d) and os.path.exists(os.path.join(SourceDir, d, ThumbsDir)):
        for f in os.listdir(os.path.join(SourceDir, d, ThumbsDir)):
                        if(f.endswith('.jpg') and f.endswith('_xxx.jpg')):
                                # im = Image.open(os.path.join(SourceDir, d, 'Thumbs_160x120', f))
                                # print('width: ' + str(im.size[0]) + ' height: ' + str(im.size[1]))
                                fileToDelete = f.replace('_xxx.jpg', '.jpg')
                                fullFileToDelete = os.path.join(SourceDir, d, ThumbsDir, fileToDelete)
                                print('Deleting file: ' + fullFileToDelete)
                                os.remove(fullFileToDelete)
                                
                                fullF = os.path.join(SourceDir, d, ThumbsDir, f)
                                print('Renaming file: ' + fullF + ' ::::: TO :::: ' + fullFileToDelete)
                                os.rename(fullF, fullFileToDelete)

					

