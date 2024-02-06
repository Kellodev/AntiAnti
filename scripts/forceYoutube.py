from pytube import YouTube
import os, random, string
from os import startfile

videourl2 = input("URL To YouTube Video?: ")

def downloadYouTube(videourl, path):
    yt = YouTube(videourl)
    yt_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    # Download the video and get the filename
    filename = yt_stream.download(path)
    return filename  # Return the full path to the downloaded file

characters = string.ascii_letters + string.digits
videoid = ''.join(random.choice(characters) for _ in range(8))

newpath = r'./output/youtubeForceDownloadedVideos/'

print(f"Video ({videourl2}) saved as 'video{videoid}' in ./output/youtubeForceDownloadedVideos/")
# Capture the full path of the downloaded video
downloaded_file_path = downloadYouTube(videourl2, newpath)

# Now, use the actual downloaded file path
startfile(downloaded_file_path)
