from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os

# Input YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Input the desired output filename (without extension)
output_filename = input("Enter the desired output filename (without extension): ")

# Add the ".mp3" extension to the output filename
output_filename += ".mp3"

# Download the video
yt = YouTube(video_url)
stream = yt.streams.filter(only_audio=True).first()
stream.download(output_path='downloads')  # Download to a 'downloads' folder

# Get the downloaded video file path
video_filename = f'{yt.title}.mp4'
video_path = os.path.join('downloads', video_filename)

# Convert the downloaded video to MP3
audio = AudioFileClip(video_path)
audio.write_audiofile(output_filename)

print(f'{output_filename} has been saved.')

# Delete the original video file (optional)
os.remove(video_path)
