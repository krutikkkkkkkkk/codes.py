from pytube import YouTube
link = input("Enter video url: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()