#this is a file where we create tex file from all txt file in the folder
#a spceific template is used
#this is a file to concate videos


import os

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
   try:
       os.system("ls -1v *.epub > navi.txt")

       string1=rff("navi.txt")
       string1=string1.replace("\'","\\'")
       string1=string1.replace("&","\\&")
       string1=string1.replace(" ","\\ ")
       string1=string1.replace(",","\\,")
       string1=string1.replace("%","\\%")
       string1=string1.replace("$","\\$")
       string1=string1.replace("#","\\#")
       string1=string1.replace("[","\\[")
       string1=string1.replace("]","\\]")
       string1=string1.replace("(","\\(")
       string1=string1.replace(")","\\)")
       string1=string1.replace("{","\\{")
       string1=string1.replace("}","\\}")
       arrayavi=string1.splitlines(True)
       if len(arrayavi)>1:
          for i in range(len(arrayavi)):
             stringd=arrayavi[i][:-6]
             stringd=stringd.replace("\\","")
             stringd=stringd.replace(" ","")
             stringd=stringd.replace("\'","")
             stringd=stringd.replace("&",".")
             stringd=stringd.replace(",","")
             stringd=stringd.replace(":","")
             stringd=stringd.replace("\"","")
             stringd=stringd.replace(";","")
             stringd=stringd.replace(">","")
             stringd=stringd.replace("<","")             
             stringd=stringd.replace("[","")
             stringd=stringd.replace("]","")
             stringd=stringd.replace("(","")
             stringd=stringd.replace(")","")
             stringd=stringd.replace("{","")
             stringd=stringd.replace("}","")             
             print(stringd)
             os.system("mkdir "+stringd)
             print(arrayavi[i][:-1])
             #os.system("echo \""+"ebook-convert "+arrayavi[i][:-1]+" book"+str(i)+"\\text.txt\"")
             os.system("ebook-convert "+arrayavi[i][:-1]+" "+stringd+"/text.txt")
             
             #os.system("cd \'"+arrayavi[i][:-6]+"\'")
             #os.system("cp ../pdf.py . ")
             #os.system("cp ../text1.tex . ")
             #os.system("cat text1.tex text.txt \"\\end{document}\" > latex.tex")
             #os.system("pdflatex latex.tex")
             #os.system("python pdf.py")
             #os.system("cd ..")
             #os.system("echo \""+"ebook-convert \'"+arrayavi[i][:-1]+"\' \'"+arrayavi[i][:-6]+"\'/text.txt\"")
   except ValueError:
       return "can not create files"
   
   return 0


#calling the main function
if __name__ == '__main__':
   main()



