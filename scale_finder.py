import PyQt5

noteList=["A","A#", "B", "C", "C#","D" ,"D#","E", "F", "F#", "G", "G#", "A",
         "A#", "B", "C", "C#","D" ,"D#","E", "F", "F#", "G", "G#"]

Minor = [2,1,2,2,1,2,2]
Major = [2,2,1,2,2,2,1]
TizitaMajor = [2,2,3,2]
TizitaMinor = [2,1,4,1]
BatiMajor  = [4,1,2,4]
BatiMinor  = [3,2,2,3]
Ambassel   = [1,4,2,1]
AnchiHoye  = [1,4,1,3]
Major7 = [4,3,4]
Minor7 = [3,4,3]






def majorscale(indexnote):
    newlist=[]
    newlist.append(noteList[indexnote])
    for i in range(len(Major)):
        indexnote += Major[i]
        newlist.append(noteList[indexnote])
    return newlist

def minorscale(indexnote):
    newlist=[]
    newlist.append(noteList[indexnote])
    for i in range(len(Minor)):
        indexnote += Minor[i]
        newlist.append(noteList[indexnote])
    return newlist           

def TizitaMajorscale(indexnote):
    newlist=[]
    newlist.append(noteList[indexnote])
    for i in range(len(TizitaMajor)):
        indexnote += TizitaMajor[i]
        newlist.append(noteList[indexnote])
    return newlist   

def TizitaMinorscale(indexnote):
    newlist=[]
    newlist.append(noteList[indexnote])
    for i in range(len(TizitaMinor)):
        indexnote += TizitaMinor[i]
        newlist.append(noteList[indexnote])
    return newlist   

def BatiMajorscale(indexnote):
    newlist=[]
    newlist.append(noteList[indexnote])
    for i in range(len(BatiMajor)):
        indexnote += BatiMajor[i]
        newlist.append(noteList[indexnote])
    return newlist   
        
def BatiMinorscale(indexnote):
    newlist=[]
    newlist.append(noteList[indexnote])
    for i in range(len(BatiMinor)):
        indexnote += BatiMinor[i]
        newlist.append(noteList[indexnote])
    return newlist   

def Ambasselscale(indexnote):
    newlist=[]
    newlist.append(noteList[indexnote])
    for i in range(len(Ambassel)):
        indexnote += Ambassel[i]
        newlist.append(noteList[indexnote])
    return newlist 

def AnchiHoyescale(indexnote):
    newlist=[]
    newlist.append(noteList[indexnote])
    for i in range(len(AnchiHoye)):
        indexnote += AnchiHoye[i]
        newlist.append(noteList[indexnote])
    return newlist 

def Major7scale(indexnote):
    newlist=[]
    newlist.append(noteList[indexnote])
    for i in range(len(Major7)):
        indexnote += Major7[i]
        newlist.append(noteList[indexnote])
    return newlist 

def Minor7scale(indexnote):
    newlist=[]
    newlist.append(noteList[indexnote])
    for i in range(len(Minor7)):
        indexnote += Minor7[i]
        newlist.append(noteList[indexnote])
    return newlist 

        
def ChooseScale(choose,indexnote): 
    
    scale=[]
    
    if choose =="1":
       scale = majorscale(indexnote)
       return(f'\nYour {samplenote} Major Scale is:\n\n{scale}')
    
    elif choose =="2":
       scale = minorscale(indexnote)
       return(f'\nYour {samplenote} Minor Scale is:\n\n{scale}')
    
    elif choose=="3":
       scale = TizitaMajorscale(indexnote)
       return(f'\nYour {samplenote} Tizita Full Scale is:\n\n{scale}')
    
    elif choose=="4":
       scale = TizitaMinorscale(indexnote)
       return(f'\nYour {samplenote} Tizita Half Scale is:\n\n{scale}')
    
    elif choose=="5":
       scale = BatiMajorscale(indexnote) 
       return(f'\nYour {samplenote} Bati Major Scale is:\n\n{scale}')
    
    elif choose=="6":
       scale = BatiMinorscale(indexnote)        
       return(f'\nYour {samplenote} Bati Minor Scale is:\n\n{scale}') 
    
    elif choose=="7":
       scale = Ambasselscale(indexnote)
       return(f'\nYour {samplenote} Ambassel Scale is:\n\n{scale}')
    
    elif choose=="8":
       scale = AnchiHoyescale(indexnote)     
       return(f'\nYour {samplenote} Anchi Hoye Scale is:\n\n{scale}')
   
    else:
       return("Choose not found! Try Again")
        
        

#find the index samplenote in noteList
def FindIndex(samplenote):
    samplenote.upper()
    indexnote=0
    for i, val in enumerate (noteList):
       if samplenote == val:
         indexnote = i
         return(indexnote)
      
          
#App Starts Here:
samplenote=0
# samplenote= input("Enter your note here:\n ")
# indexnote = FindIndex(samplenote)

# print("Choose which scale you want to play:\n\n 1.Major\n 2.Minor\n 3.Tizita Full\n 4.Tizita Half\n 5.Bati major\n 6.Bati Minor\n 7.Ambassel\n 8.Anchi Hoye\n")
# choose = input("Enter Your Choose Here:")
# print(ChooseScale(choose,indexnote))
 






# match case work for python 3.10

# match choose:
#     case "1":
#         scale = majorscale(indexnote)
#         print(f'\nYour {samplenote} Major Scale is:\n\n{scale}')
#     case "2":
#         scale = minorscale(indexnote)
#         print(f'\nYour {samplenote} Minor Scale is:\n\n{scale}')
#     case "3":
#         scale = TizitaFullscale(indexnote)
#         print(f'\nYour {samplenote} Tizita Full Scale is:\n\n{scale}')
#     case "4":
#         scale = TizitaHalfscale(indexnote)
#         print(f'\nYour {samplenote} Tizita Half Scale is:\n\n{scale}')
#     case "5":
#         scale = BatiMajorscale(indexnote) 
#         print(f'\nYour {samplenote} Bati Major Scale is:\n\n{scale}')
#     case "6":
#         scale = BatiMinorscale(indexnote)        
#         print(f'\nYour {samplenote}Bati Minor Scale is:\n\n{scale}') 
#     case "7":
#         scale = Ambasselscale(indexnote)
#         print(f'\nYour {samplenote} Ambassel Scale is:\n\n{scale}')
#     case "8":
#         scale = AnchiHoyescale(indexnote)     
#         print(f'\nYour {samplenote} Anchi Hoye Scale is:\n\n{scale}')
    
#     case _:
#         print("Code not found!")
        
        
