from moviepy.editor import VideoFileClip
clip = VideoFileClip("Video.mp4")
clip1 = clip.subclip(56,66)
clip2 = clip.subclip(70,76)
clip3 = clip.subclip(50, 52)
clip4 = clip.subclip(30, 35)
final_clip = concatenate_videoclips([clip1,clip2,clip3,clip4])
final_clip.write_videofile("output_1.mp4")
#clip.preview()