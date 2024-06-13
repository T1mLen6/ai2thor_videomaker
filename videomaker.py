import os
import re
from moviepy.editor import ImageSequenceClip

def create_video_from_images(folder_path, output_video_path, fps=1):
    # Get all image files and sort them
    image_files = sorted(
        [f for f in os.listdir(folder_path) if f.lower().startswith('modified') and f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))],
        key=lambda x: int(re.search(r'\d+', x).group())
    )

    image_paths = [os.path.join(folder_path, f"{filename}") for filename in image_files]

    clip = ImageSequenceClip(image_paths, fps=fps)

    clip.write_videofile(output_video_path, codec='libx264')

if __name__ == "__main__":
    # Folder containing the modified images
    folder_path = "/home/tim/SMART-LLM/logs/Place_a_AlarmClock_on_a_desk._plans_2_06-13-2024-14-41-49/top_view"

    # Output video file path
    output_video_path = "FloorPlan310.tasks_1.compose_1.fintune_1_robot_1.mp4"


    fps = 2  # Change this to the desired frames per second

    create_video_from_images(folder_path, output_video_path, fps)