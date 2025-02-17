
 
I've created a complete Music Playlist Manager using Flask. Here's a breakdown of the key components:


-------------------------------------------Homepage------------------------------------------
 ![Image Alt](https://github.com/priyanshu731/Music_Playlist_Manager/blob/0da3235f03fecd725e908fc01aaec022f7e824cd/templates/screenshot/CreateNewPlaylist.png)
----------------------------------------Create New Page--------------------------------------
 
-------------------------------------------Playlist------------------------------------------
 
----------------------------------------Upload New Song--------------------------------------
 

Project Structure:
Organized files into logical directories
Separate files for models, forms, routes, and configuration
Static folder for CSS, JavaScript, and uploaded files
Templates folder for HTML files


Features:
Create and manage playlists
Upload and play music files
Responsive Bootstrap UI
Form validation
Flash messages for user feedback
Audio player controls


Database Models:
Playlist model with name, description, and creation date
Song model with title, artist, file path, and relationship to playlist


Forms:
PlaylistForm for creating playlists
SongForm for uploading songs with validation
