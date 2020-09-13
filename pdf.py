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

def concat2vid(vid1,vid2,vid3,vid4,vid5,out):
   
   try:
       os.system("ffmpeg -i "+vid1+ " -i "+vid2+ " -i "+vid3+ " -i "+vid4+ " -i "+vid5+ " -filter_complex \"[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a][4:v][4:a] concat=n=5:v=1:a=1 [v] [a]\" -map \"[v]\" -map \"[a]\" " + out)
      
   except ValueError:
       return "can not concate"
   return 0

def main():
   #concat2vid("0process.txt.avi","1process.txt.avi", "out.avi")
   
   #we are going to create a while loop until only one video will remain
   
   string2=rff("text.txt")
   

   # replace bad characters
   string2=string2.replace('’', "'")
   string2=string2.replace("“","\"")
   string2=string2.replace("”","\"")
 
   string2=string2.replace("\\"," ") 
 
   string2=string2.replace("%"," ")
   string2=string2.replace("$"," ")
   string2=string2.replace("&"," ")
   string2=string2.replace("%"," ")
   string2=string2.replace("$"," ")
   string2=string2.replace("#"," ")
   string2=string2.replace("["," ")
   string2=string2.replace("]"," ")
   string2=string2.replace("("," ")
   string2=string2.replace(")"," ")
   string2=string2.replace("{"," ")
   string2=string2.replace("}"," ")
   string2=string2.replace("^"," ")
   string2=string2.replace("_"," ")
   #string2=unicode(string2,errors= "ignore")
   #string2=string2.decode()
   #string2=string2.replace("","")
   #string2=string2.encode('ascii',errors='ignore').decode()
  
   printable = set(string.printable)
   string2="".join(filter(lambda x: x in printable, string2))

   stringout=rff("text1.tex")+str(string2)+"\end{document}"
   wfo("latex.tex",stringout)
   os.system("pdflatex latex.tex")
   os.system("pdftk latex.pdf burst")
   
   #os.system("rm latex.pdf")
   
   try:
       os.system("ls -1v pg* > navi.txt")

       string1=rff("navi.txt")
       #string1=string1.replace("\'","\\'")
       arrayavi=string1.splitlines(True)
       if len(arrayavi)>1:
          for i in range(len(arrayavi)):
             os.system("ebook-convert "+arrayavi[i][:-1]+" "+str(i)+".txt")
             os.system("espeak -s 260 -f "+str(i)+".txt -w "+str(i)+".wav")
             os.system("convert -density 300 "+arrayavi[i][:-1]+" "+str(i)+".jpeg")
             os.system("ffmpeg -i "+str(i)+".jpeg -i "+str(i)+".wav -b:a 192k "+str(i)+".avi") 
             #os.system("mkdir \'"+arrayavi[i][:-6]+"\'\n")
             #os.system("echo \""+"ebook-convert "+arrayavi[i][:-1]+" book"+str(i)+"\\text.txt\"")
             #os.system("ebook-convert \'"+arrayavi[i][:-1]+"\' \'"+arrayavi[i][:-6]+"\'/text.txt")
             #os.system("echo \""+"ebook-convert \'"+arrayavi[i][:-1]+"\' \'"+arrayavi[i][:-6]+"\'/text.txt\"")
   except ValueError:
       return "can not create files"
   
   return 0


#calling the main function
if __name__ == '__main__':
   main()



