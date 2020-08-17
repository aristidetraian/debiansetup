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
       os.system("ls -1v *.avi > navi.txt")

       string1=rff("navi.txt")
       arrayavi=string1.splitlines(True)
       if len(arrayavi)>1:
          for i in range(len(arrayavi)//5):
             concat2vid(arrayavi[i*5][:-1],arrayavi[i*5+1][:-1],arrayavi[i*5+2][:-1],arrayavi[i*5+3][:-1],arrayavi[i*5+4][:-1],"out.avi")
             os.system("rm "+arrayavi[i*5][:-1])
             os.system("rm "+arrayavi[i*5+1][:-1])
             os.system("rm "+arrayavi[i*5+2][:-1])
             os.system("rm "+arrayavi[i*5+3][:-1])
             os.system("rm "+arrayavi[i*5+4][:-1])
             os.system("mv out.avi "+arrayavi[i*5][:-1])
   except ValueError:
       return "can not create files"
   
   return 0


#calling the main function
if __name__ == '__main__':
   main()



