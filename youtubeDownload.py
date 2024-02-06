from pytube import YouTube
import os, random, string

videourl2 = input("URL To YouTube Video?: ")

def downloadYouTube(videourl, path):
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

characters = string.ascii_letters + string.digits
videoid = ''.join(random.choice(characters) for _ in range(8))

newpath = r'./youtubeDownloadedVideos/' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

print("Video (" + videourl2 + ') saved as "video' + videoid + '" in ./youtubeDownloadedVideos/')
downloadYouTube(videourl2, './youtubeDownloadedVideos/video' + videoid)