#importing necessary packages
import re
import shutil
from gtts import gTTS

#opening the text file
fh = open('text.txt','r')

#reading each line from the text file
mytext = fh.readlines()

#creating mp3 files from text and saving each line in mp3 format 
for i in range(len(mytext)):
    tts = gTTS(text=mytext[i], lang='en', tld='com')
    # title rename as the line name
    title = re.sub('[^A-Za-z]+', '', mytext[i])
    # save file
    tts.save(title+".mp3")
    # moving all files to mp3 folder - create "mp3" folder in the same directory
    shutil.move(title+".mp3", "mp3")
    
#closing the text file
fh.close()