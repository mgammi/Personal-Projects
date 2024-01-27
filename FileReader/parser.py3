import os 
import io 
import sys


# for line in sys.stdin:
# python script.py input_file.txt 

def get_info(file):
    file1 = open(file, "r")
    
    all_lines = file1.readlines() # each line = string element in the list
    
    vd = ""
    
    l1 = all_lines[0].trim()
    i = l1.index("Plan")
    date = l1[i+1,:]
    
    for line in all_lines:
        line = line.strip() # removes leading and trailing spaces
        if vd == "" and line[:2] == "VD":
            i = line.index("-")
            vd = line [i+1,:] 
            
        if :#checking if its song info lines__:  
            song_info[ctr] = [ 
                    ['song'],
                    [date] ,
                    ['key'] ,
                    [vd],
                    ['lead'],
                    ['seq'],
                    ['hi'] ,
                    ["mid"],
                    ["low"],
                    ["notes"]]
            ctr+=1
    
    file1.close()
    
# connect to folder
directory = '~/Library/Containers/com.apple.Notes/Data/Library/Notes/FOLDER_FO_VPs' # directory path here -> best if theres a VP files

# read through file 

# want to add songs to sheet file by file 

song_info = [] # should be list of list, where the inner list stores song info
# has to be in matrix format to be used later on
ctr = 0

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        get_info(f)
      #  main.add_songs_to_sheet(song_info)
        
        
#######


    