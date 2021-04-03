"""
Made by Snehashish Laskar
Made on 03-04-2021
Developer contact: snehashish.laskar@gmail.com
This is a song suggesting CLI that will suggest songs based on what you want.
"""

# Importing json to read and write data
import json

# Opening files to read song data
with open("data.json", "r") as file:
	data = json.load(file)

# Defining a function to suggest a song
def suggest(typ):
	# Running a for loop that checks through each song
	for i in data:
		# Checking if the genre is what the user wants
		# And appending the song to the songs list if it matches
		if i["genre"] == typ:
			songs.append(i["name"])
		# checking if the singer is what the user want
		# And appending to the song to the songs list if it matches
		elif i["singer"] == typ:
			songs.append(i["name"])
			# checking if the time of release is what the user wants
			# And appending the song to the songs list if it matches
		elif i["time"] == typ:
			songs.append(i["name"])
	
	# Finally printing the songs so that the user can stream them
	print("Here is a list of songs you can stream rn!") 
	for i in songs:
		print(i)

# Main bot loop
def main():
	# Running a forever loop 
	while True:
		# Taking the user command
		com = input(">>>")
		# Checking if the user typed something or not
		if com != "":
			suggest(com)		
		else:
			pass

# Defining a list containing all the related songs
songs = []

main()





























