##This is a script to strip of  files and create a series of small text files.

##there are alist of function that can be used
## first is textchop trims text, filecho trims file 
## First lybraries
# encoding: utf-8
import string
import os
import urllib2

def rff(fileinput):
   #this is a read from file function since it is getting a bit obsufcated to use open file
   try:
       str_file=open(fileinput,"r")
   except ValueError:
       return "Can not open file"
   try:
       readreturn=str_file.read()
   except ValueError:
       return "can not read the file after open"
   try:
       str_file.close()
   except ValueError:
       return "can not close the fiel"
   return readreturn

def wfo(fileinput,text):
   #this is a read from file function since it is getting a bit obsufcated to use open file
   try:
       str_file=open(fileinput,"w")
   except ValueError:
       return "Can not open file"
   try:
       readreturn=str_file.write(text)
   except ValueError:
       return "can not write the file after open"
   try:
       str_file.close()
   except ValueError:
       return "can not close the fiel"
   return 0


def textchop(texts, front, endfile):

   #this function splits the text between first front and after first endfile
   #selection rules:
   #if front is not find start from begining if end is not find end with the end,
   #searching of end starts after string if it is found
   #also exception throwed is else

   print(texts.find("\n",texts.find(front)))
   print(texts.find(endfile))
   #print(texts)
    
   return texts[texts.find("\n",texts.find(front)):texts.find(endfile)]

def removetext(texts,word):
  #this is the function that removes all the line with the words in it
  while texts.find(word)>0:
    texts=texts[:texts.find(word)] + texts[texts.find("\n\n",texts.find(word)):]
  return texts

def recovertitle(texts):
  textslow=texts.lower()
  title=texts[:texts.find("\n\n",textslow.find("by"))]
  title=title.replace("\n"," ")
  title=' '.join(title.split())
  print(title)
  #wfo(title,texts)
  return

def main():

   #this is the main function

   #print(textchop(removetext(rff("36-0.txt"),"[Illustration"),"Produce","\n\nEnd of"))
   #print(textchop(rff("36-0.txt"),"***","\nEnd of"))
   #recovertitle(textchop(removetext(rff("pg6315.txt"),"[Illustration"),"Produce","\n\nEnd of"))

   os.system("ls -1v *txt > navi.text")
   string1=rff("navi.text")
   arrayavi=string1.splitlines(True)
   if len(arrayavi)>1:
     
     for i in range(len(arrayavi)):
        print(arrayavi[i][:-1])
        #chtext=removetext(rff(arrayavi[i][:-1]),"[Illustration")
        chtext=rff(arrayavi[i][:-1])

        if chtext.find("Produced by ")!=-1:
           if chtext.find("End of Project ")!=-1:
             chtext=textchop(chtext,"Produced by ","\nEnd of Project ")
             wfo("text.txt",chtext)
             os.system("mkdir "+arrayavi[i][:-4])
             os.system("mv text.txt "+arrayavi[i][:-4])
             continue
   
           if chtext.find("End of the Project ")!=-1:
             chtext=textchop(chtext,"Produced by ","\nEnd of the Project ")
             wfo("text.txt",chtext)
             os.system("mkdir "+arrayavi[i][:-4])
             os.system("mv text.txt "+arrayavi[i][:-4])
             continue
   
           if chtext.find("End of The Project ")!=-1:
             chtext=textchop(chtext,"Produced by ","\nEnd of The Project ")
             wfo("text.txt",chtext)
             os.system("mkdir "+arrayavi[i][:-4])
             os.system("mv text.txt "+arrayavi[i][:-4])
             continue
   
           if chtext.find("***E")!=-1:
             chtext=textchop(chtext,"Produced by ","***E")
             wfo("text.txt",chtext)
             os.system("mkdir "+arrayavi[i][:-4])
             os.system("mv text.txt "+arrayavi[i][:-4])
             continue
   
           else:
             chtext=textchop(chtext,"Produced by ","*** E")
             wfo("text.txt",chtext)
             os.system("mkdir "+arrayavi[i][:-4])
             os.system("mv text.txt "+arrayavi[i][:-4])
             continue

        if chtext.find("Produced by ")==-1:
           if chtext.find("End of Project ")!=-1:
              chtext=textchop(chtext,"***","\nEnd of Project ")
              wfo("text.txt",chtext)
              os.system("mkdir "+arrayavi[i][:-4])
              os.system("mv text.txt "+arrayavi[i][:-4])
              continue
    
           if chtext.find("End of the Project ")!=-1:
              chtext=textchop(chtext,"***","\nEnd of the Project ")
              wfo("text.txt",chtext)
              os.system("mkdir "+arrayavi[i][:-4])
              os.system("mv text.txt "+arrayavi[i][:-4])
              continue
    
           if chtext.find("End of The Project ")!=-1:
              chtext=textchop(chtext,"***","\nEnd of The Project ")
              wfo("text.txt",chtext)
              os.system("mkdir "+arrayavi[i][:-4])
              os.system("mv text.txt "+arrayavi[i][:-4])
              continue
    
           if chtext.find("***E")!=-1:
              chtext=textchop(chtext,"***","***E")
              wfo("text.txt",chtext)
              os.system("mkdir "+arrayavi[i][:-4])
              os.system("mv text.txt "+arrayavi[i][:-4])
              continue
    
           else:
              chtext=textchop(chtext,"***","*** E")
              wfo("text.txt",chtext)
              os.system("mkdir "+arrayavi[i][:-4])
              os.system("mv text.txt "+arrayavi[i][:-4])
              continue
    
   


        #print(chtext)

        wfo("text.txt",chtext)
        os.system("mkdir "+arrayavi[i][:-4])
        os.system("mv text.txt "+arrayavi[i][:-4])
        #continue
        
   """

   try:
       os.system("ls -1v *txt > navi.text")

       string1=rff("navi.text")
       #string1=string1.replace("\'","\\'")
       arrayavi=string1.splitlines(True)
       if len(arrayavi)>1:
          for i in range(len(arrayavi)):
             print(arrayavi[i][:-1])
             chtext=removetext(rff(arrayavi[i][:-1]),"[Illustration")
             print(chtext.find("Produced by"))
             print(chtext.find("End of project"))
             #chtext=textchop(chtext,"Produced by","End of")
             print(chtext)        
             #chtext=textchop(removetext(rff(arrayavi[i][:-1]),"[Illustration"),"Produce","\n\nEnd of")
             #print(chtext)
             title=recovertitle(chtext)
             print(title)
             #os.system("ebook-convert "+arrayavi[i][:-1]+" "+str(i)+".txt")
             #os.system("espeak -s 260 -f "+str(i)+".txt -w "+str(i)+".wav")
             #os.system("convert -density 300 "+arrayavi[i][:-1]+" "+str(i)+".jpeg")
             #os.system("ffmpeg -i "+str(i)+".jpeg -i "+str(i)+".wav -b:a 192k "+str(i)+".avi") 
             #os.system("mkdir \'"+arrayavi[i][:-6]+"\'\n")
             #os.system("echo \""+"ebook-convert "+arrayavi[i][:-1]+" book"+str(i)+"\\text.txt\"")
             #os.system("ebook-convert \'"+arrayavi[i][:-1]+"\' \'"+arrayavi[i][:-6]+"\'/text.txt")
             #os.system("echo \""+"ebook-convert \'"+arrayavi[i][:-1]+"\' \'"+arrayavi[i][:-6]+"\'/text.txt\"")
   except ValueError:
       return "can not create files"

   """
   print('Script has ended')
   return(0)

#calling the main function
if __name__ == '__main__':
   main()


