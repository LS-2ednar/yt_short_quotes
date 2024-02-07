from moviepy.editor import *

# Define the dimensions of the video
width, height = 1080, 1920

# Duration of the video
video_duration = 30  # seconds

# Create a clip with a cyan background
cyan_clip = ColorClip((width, height), color=(0, 255, 255)).set_duration(video_duration)

# Add text for the quote
quote_text = "Your quote goes here"
quote_clip = TextClip(quote_text, fontsize=70, color='white', bg_color='cyan')
quote_clip = quote_clip.set_position(('center', height // 3)).set_duration(video_duration)  

# Add text for the author
author_text = "Author's name"
author_clip = TextClip(author_text, fontsize=50, color='white', bg_color='cyan')
author_clip = author_clip.set_position(('center', 2 * height // 3)).set_duration(video_duration)

# Composite the text clips on the cyan background
final_clip = CompositeVideoClip([cyan_clip, quote_clip, author_clip])

# Write the final video to a file
final_clip.write_videofile("output_video.mp4", codec='libx264', fps=24)  # Adjust codec and fps as needed

# Close the clips
cyan_clip.close()
quote_clip.close()
author_clip.close()
final_clip.close()