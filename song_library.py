
from song import Song
import random
class Songlibrary:#creates class
    def __init__(self,input_file):
        input_file.pop(0)# removes header
        
        self.song_list = []#creates list
        for line in input_file:
            Artist = line[:line.index(';')] #Makes Artist in string up intil the ;
            Song_Name = line[line.index(';')+1:]#fixes the song name
            self.song_list.append(Song(Artist,Song_Name))#adds to list
        self.number = len(input_file)

    def lookup(self,Artist):#creates instance method (lookup)
        Songs = ""
        for i in self.song_list:#creates loop using previous instance varible
            if  Artist.lower() == i.Artist.lower():
                Songs += i.Song_Name

        
        if Songs != "":
            print(f"Songs found by {Artist}:")
            print(f"{Songs}", end = "")#fixes whitespace
        else:
            print("No Songs avalible by that artist")

    def random_songs(self,Num_of_songs):#creates function for the random playlist
        counter = 0 
       
        song_list_copy = self.song_list[:]#copys list to new varible
        random.shuffle(song_list_copy)#uses shuffle function on copy of list
        RandomList = song_list_copy[:Num_of_songs]
        for i in RandomList:
            counter += 1
            print(f" Random song {counter}:{i}")#prints random song 
        






    

        
