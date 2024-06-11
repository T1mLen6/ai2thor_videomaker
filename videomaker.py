import os
import re
from moviepy.editor import ImageSequenceClip

def create_video_from_images(folder_path, output_video_path, fps=1):
    # Get all image files and sort them
    image_files = sorted(
        [f for f in os.listdir(folder_path) if f.lower().startswith('modified') and f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))],
        key=lambda x: int(re.search(r'\d+', x).group())
    )


    # Create full paths for the images
    image_paths = [os.path.join(folder_path, f"{filename}") for filename in image_files]

    # Create a video clip from the images
    clip = ImageSequenceClip(image_paths, fps=fps)

    # Write the video file
    clip.write_videofile(output_video_path, codec='libx264')

if __name__ == "__main__":
    # Folder containing the modified images
    folder_path = "/home/tim/SMART-LLM/logs/Chill_a_pan_and_take_it_out_of_the_fridge.__plans_0_06-04-2024-16-59-55/top_view"

    # Output video file path
    output_video_path = "output_video.mp4"

    # Frames per second for the video
    fps = 2  # Change this to the desired frames per second

    create_video_from_images(folder_path, output_video_path, fps)