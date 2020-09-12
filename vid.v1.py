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

def concat5vid(vid1,vid2,vid3,vid4,vid5,out):
   
   try:
       os.system("ffmpeg -i "+vid1+ " -i "+vid2+ " -i "+vid3+ " -i "+vid4+ " -i "+vid5+ " -filter_complex \"[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a][4:v][4:a] concat=n=5:v=1:a=1 [v] [a]\" -map \"[v]\" -map \"[a]\" -b:a 192k " + out)
      
   except ValueError:
       return "can not concate"
   
   os.system("rm "+vid1)
   os.system("rm "+vid2)
   os.system("rm "+vid3)
   os.system("rm "+vid4)
   os.system("rm "+vid5)
   os.system("mv "+out+" "+vid1)
   return 0

def concat4vid(vid1,vid2,vid3,vid4,out):
   
   try:
       os.system("ffmpeg -i "+vid1+ " -i "+vid2+ " -i "+vid3+ " -i "+vid4+ " -filter_complex \"[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a] concat=n=4:v=1:a=1 [v] [a]\" -map \"[v]\" -map \"[a]\" -b:a 192k " + out)
      
   except ValueError:
       return "can not concate"
   os.system("rm "+vid1)
   os.system("rm "+vid2)
   os.system("rm "+vid3)
   os.system("rm "+vid4)
   os.system("mv "+out+" "+vid1)
   return 0

def concat3vid(vid1,vid2,vid3,out):
   
   try:
       os.system("ffmpeg -i "+vid1+ " -i "+vid2+ " -i "+vid3+" -filter_complex \"[0:v][0:a][1:v][1:a][2:v][2:a] concat=n=3:v=1:a=1 [v] [a]\" -map \"[v]\" -map \"[a]\" -b:a 192k " + out)
      
   except ValueError:
       return "can not concate"
   os.system("rm "+vid1)
   os.system("rm "+vid2)
   os.system("rm "+vid3)
   os.system("mv "+out+" "+vid1)
   return 0

def concat2vid(vid1,vid2,out):
   
   try:
       os.system("ffmpeg -i "+vid1+ " -i "+vid2+ " -filter_complex \"[0:v][0:a][1:v][1:a] concat=n=2:v=1:a=1 [v] [a]\" -map \"[v]\" -map \"[a]\" -b:a 192k " + out)
      
   except ValueError:
       return "can not concate"
   os.system("rm "+vid1)
   os.system("rm "+vid2)
   os.system("mv "+out+" "+vid1)
   return 0

def interlat(vid1,out):
   os.system("ffmpeg -y -i "+vid1+" -filter_complex loop=loop=1 -max_muxing_queue_size 9999 "+ out)
   os.system("mv "+out+" "+vid1)
   return 0

def vidcheck():
   #concat2vid("0process.txt.avi","1process.txt.avi", "out.avi")
   
   #we are going to create a while loop until only one video will remain
   try:
       os.system("ls -1v *.avi > navi.txt")

       string1=rff("navi.txt")
       arrayavi=string1.splitlines(True)
       if len(arrayavi)==2:
          concat2vid(arrayavi[0][:-1],arrayavi[1][:-1],"out.avi")
       if len(arrayavi)==3:
          concat3vid(arrayavi[0][:-1],arrayavi[1][:-1],arrayavi[2][:-1],"out.avi")
       if len(arrayavi)==4:
          concat4vid(arrayavi[0][:-1],arrayavi[1][:-1],arrayavi[2][:-1],arrayavi[3][:-1],"out.avi")
       if len(arrayavi)==1:
          interlat(arrayavi[0][:-1],"out.avi")
          return 0
       if len(arrayavi)==0:
          return 0
       if len(arrayavi)>4:
          for i in range(len(arrayavi)//5):
             concat5vid(arrayavi[i*5][:-1],arrayavi[i*5+1][:-1],arrayavi[i*5+2][:-1],arrayavi[i*5+3][:-1],arrayavi[i*5+4][:-1],"out.avi")
   except ValueError:
       return "can not create files"
   vidcheck()
   return 0

def main():
   vidcheck()
   return 0


#calling the main function
if __name__ == '__main__':
   main()



