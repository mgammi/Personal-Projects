import pandas as pd
import numpy  as np
import requests as re
from bs4 import BeautifulSoup
import os
import pygsheets 


# https://pygsheets.readthedocs.io/en/stable/worksheet.html  -> pygsheets documentation

# 2 parts --> parsing data from notes then adding it to the google sheet

# to be able to easily acces the files, the files would need to be stored in a different format, whether as a
# pdf, word, or text file.
# could probably also access the files if they were saved on google doc via an API call?

# Information needed:
# SONG, DATE,CAMPUS,KEY ,VPC, LEAD, SEQUENCE, PART - HIGH/SOPRANO, PART - MID/ALTO	, PART - LOW/TENOR, NOTES
# A,    B,   C,     D,   E,   F,    G,        H,                   I,                 J,                K


# best course of action ->  add new songs to the very end, and then let sheets 
# resort it by song name first, then data second!


# Organization of sheets

# 3 tabs -> Song 1, Song 2, and Song 3
# Within each tab, sorted first by song name then by date of vocal plan
# The rows are group by song where the first row of the group is the name of the
# song with the rest of the columns empty, and then the song details in the next
# row

def add_songs_to_sheet(song_info):
    
    ## connect to table 
    client = pygsheets.authorize(service_account_file="cor-project-f9213989855b.json")
    print(client.spreadsheet_titles())   # should print name of vocal plan sheet


    # read through table
    spreadsht = client.open("Copy of VOCAL PLANS MASTER 2023 - MANA")

    # master = spreadsht.worksheet("title", "Sheet1")
 
    ws1 = spreadsht.worksheet("title", "Song1") # second param is name of specific tab
    row_num = (ws1.rows()) + 1
    # first, see if the song already exists in the sheet, if not, add a row with ONLY the song name
    if len(ws1.find( )) == 0: 
        #song doesnt exist
        ws1.update_values(crange = "A" + str(row_num), values = song_info[[0][0]])
        row_num += 1
   
    ws1.update_values(crange =  "A" + str(row_num) + ":K" + str(row_num), values = song_info[0]) # inserts new row after row
    # add new values into their associating column
    # re-sort  --> how would groups be maintained tho?
    ws1.sort_range(start = "A1", end = "A" + str(row_num), basecolumnindex= 0,sortorder = 'ASCENDING')

    # create groups by looking at ranges in the Song colmn with the same name

    # write into tables
    ws2 = spreadsht.worksheet("title", "Song2")
    # get number of active rows so we can add to the end
   

    ws3 = spreadsht.worksheet("title", "Song3")
    #row_num = (ws3.rows()) + 1
    
    # if len(song_info) > 3:
    #     ws4 = spreadsht.worksheet("title", "Special")
    #     row_num = (ws4.rows()) + 1
    


                 
        

