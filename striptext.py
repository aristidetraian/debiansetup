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

   """
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
   
    """
   #print(texts.find("\n\n",texts.find(front)))
   #print(texts)
    
   return texts[texts.find("\n\n",texts.find(front)):texts.find(endfile)]

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
  wfo(title,texts)
  return

def main():

   #this is the main function

   #print(textchop(removetext(rff("pg6315.txt"),"[Illustration"),"Produce","\n\nEnd of"))
   recovertitle(textchop(removetext(rff("pg6315.txt"),"[Illustration"),"Produce","\n\nEnd of"))

   print('Script has ended')
   return(0)

#calling the main function
if __name__ == '__main__':
   main()


