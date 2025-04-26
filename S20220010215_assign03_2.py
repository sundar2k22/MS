import cv2
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

# Function to resize frames using OpenCV
def resize_frame(frame, newsize):
    return cv2.resize(frame, newsize, interpolation=cv2.INTER_LINEAR)

# Function to resize the entire clip
def resize_clip(clip, newsize):
    return clip.fl_image(lambda frame: resize_frame(frame, newsize))

# Load and trim video clips
clip1 = VideoFileClip("sample1.mp4").subclip(0, 25)  # First 25 seconds of sample1.mp4
clip2 = VideoFileClip("sample2.mp4").subclip(36, 70)  # From 0:36 to 1:10 of sample2.mp4

# Define desired resolution (width, height)
desired_resolution = (1920, 1080)  # Adjust as needed

# Resize clips to the desired resolution
clip1 = resize_clip(clip1, desired_resolution)
clip2 = resize_clip(clip2, desired_resolution)

# Load and trim background audio
background_audio = AudioFileClip("background.mp3").subclip(73, 98)  # From 1:13 to 1:38

# Set the background audio to clip1
clip1 = clip1.set_audio(background_audio)

# Concatenate the video clips
final_video = concatenate_videoclips([clip1, clip2])

# Create a title text clip
title_text = TextClip("My First Remix, Hope you all enjoy!!!", fontsize=70, color='white', size=desired_resolution)
title_text = title_text.set_duration(5)  # Display for 5 seconds

# Overlay the title text on the final video
final_video = CompositeVideoClip([title_text.set_start(0), final_video.set_start(3)])

# Define captions and their display times
captions = [
    ("How is the Josh??", 5),      # Display at 5 seconds
    ("Enjoy the show!", 15),       # Display at 15 seconds
    ("Love the music!", 20),       # Display at 20 seconds
    ("Wow the transition!", 30),       # Display at 30 seconds
    ("Stay tuned for more!",45),  # Display at 45 seconds
    ("Enjoy the dance too!", 50),    # Display at 50 seconds
    ("Thanks for watching guys! Do support me!", 57),    # Display at 57 seconds
]

# Create a list to hold the caption clips
caption_clips = []

# Iterate through the captions and create TextClip for each
for text, start_time in captions:
    caption_text = TextClip(text, fontsize=50, color='yellow', size=desired_resolution)
    caption_text = caption_text.set_position(('center', 'bottom')).set_duration(5).set_start(start_time)
    caption_clips.append(caption_text)

# Overlay all caption text clips on the final video
final_video = CompositeVideoClip([final_video] + caption_clips)

# Write the final video to a file
final_video.write_videofile("S20220010215_final_video.mp4", codec='libx264', bitrate='2000k', fps=24)
