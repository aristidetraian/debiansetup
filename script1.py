##This is a script to strip of  files and create a series of small text files.

##there are alist of function that can be used
## first is textchop trims text, filecho trims file 
## First lybraries

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


def textchop(texts, front, endfile):

   #this function splits the text between first front and after first endfile
   #selection rules:
   #if front is not find start from begining if end is not find end with the end,
   #searching of end starts after string if it is found
   #also exception throwed is else

   
   try:
       if texts.find(front) != (0-1):
          start = texts.find( front ) + len( front )
          end = texts.find( endfile, start )
          #somethin strange happen to [:-1] the last key is left out so to prevent we have if check

          if end>-1:
             return texts[start:end]
          else:
             return texts[start:]
       else:
          end = texts.find(endfile,0)
          # print(end) debugging
  	  #if check
          if end>-1:
             return texts[:end]
          else:
             return texts
   except ValueError:
         #it actually trigers from time to time so keep it like this at this stage than
         return "Something strange just happened in textchop call textchop"   
   
    
   return()


#debugging 
#print(textchop('testcffefe','s','2'))


def filechop(filename,textbegin,textend,outputfile):
   #this function takes the file and chop it out between textbegin,textend not inclusive and output
   #the remine into the textfile outputfile if value exist, and the text as a string
   #this function uses textchop
   
   #First we open the file read from it
   try:
       string_text=rff(filename)
   except ValueError:
       return "can not read file with function"


   #now we try to chop it

   try:
       temp_return=textchop(string_text, textbegin, textend)
   except ValueError:
       return "Exception triger in filechop by calling textchop first part"
   
   #we check if there is an output file or just left blank and then we output   
   try:
       if outputfile == '':
          return temp_return
   except ValueError:
       return "something strange happen when we try to compare file filechop"
   
   #we now write the content since there is a file that is not null
   
   try:
       wfo(outputfile,temp_return)
   except ValueError:
       return "can not write in filewith wfo"
   
   #cleanup plese check all open is closed
   
   return temp_return


#debugging

#print(filechop("testcut.txt","cufssss","cu2","return.txt"))

def textlinesplitter(thefile,linesnr):
   #this is a simple text splitter takes a text and splitts it on the nomber of lines in simple files
   #we read a file and we output files with a prefix of the file name and numbers. 
   
   try:
       temstring=rff(thefile)
   except ValueError:
       return "we can not read the file"
   
   #we than split the file
   
   try:
       spl=temstring.splitlines(True)
   except ValueError:
       return "split line did not work"
   #now is the time to try to use the method with the range to navigate the array

   try: 
       for i in range(len(spl)//linesnr+1):
           try:
               sot=""
               sotl=""
           except ValueError:
               return "we can nt create strin" 
          
           try:   
               for j in range(linesnr):
                    if (i*linesnr+j)<len(spl):
                      sot+=(spl[i*linesnr+j])
                      sotl+=(spl[i*linesnr+j]+"\n")
           except ValueError:
               return "we can not split and add strin"

           #procesing the string sot
           try:
               sotl=sotl.replace("_","\_")
               sotl=sotl.replace("%","\%")
               sotl=sotl.replace("$","\$")
               
           except ValueError:
               return "cannot replace"   

           try:
               namef=str(i)+"--"+thefile
           except ValueError:
               return "We can not assign name to file"

           try:
               wfo(namef+".tex",rff("text1.tex")+sotl+"\\end{document}")
               wfo(namef+".txt", sot)
           except ValueError:
               return "We cannot find a way to write file"

           #we create the latex and the wave
           try:
               os.system("pdflatex "+namef+".tex")
               os.system("rm "+namef+".log")
               os.system("rm "+namef+".aux")
               os.system("convert -density 300 "+namef+".pdf " +namef+".jpeg")
               os.system("espeak -f "+namef+".txt -w "+namef+".wav")
               os.system("ffmpeg -framerate 25 -loop 1 -y -i "+namef+".jpeg -i "+namef+".wav  -c:a  copy -shortest "+namef+".avi")
  
        
               ######                  Cleaning up the files except video  
               os.system("rm "+namef+".tex "+namef+".txt "+namef+".pdf "+namef+".jpeg "+namef+".wav ")

           except ValueError:
               return "we can not create pdf and wav"


   except ValueError:
       return "we can not do the for loop in renge ln " 

   return 0 

#debugging
#textlinesplitter("test.txt",7)


def main():

   #this is the main function 
   '''
   try:
       print('Hello script started\n')

       print("Input the workbanch file:")
       fileinput=input()
   
       print("Input start text file location")
       filecutstart=input()

       print("end file text location:")
       filecutend=input()

   except ValueError:
       return "Can not perform the file name reading"
   '''
   """
   try:
       filechop("11.txt",rff("start.txt"),rff("endof.txt")[:-2],"process.txt")
   except ValueError:
       return "can not filechop"
   """
   try:
       textlinesplitter("process.txt",17)
   except ValueError:
       return "can not splitfile"








   
   print('Script has ended')
   return(0)

#calling the main function
if __name__ == '__main__':
   main()


