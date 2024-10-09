import os
import pygame
from moviepy.editor import ImageSequenceClip
import time

# Set up directories for storing frames
FRAME_DIR = "frames"
os.makedirs(FRAME_DIR, exist_ok=True)

def clear_frames():
    """
    Remove all frames from previous animation runs.
    """
    for file in os.listdir(FRAME_DIR):
        file_path = os.path.join(FRAME_DIR, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print("Frames have been cleared from the directory.")

def generate_frames(storyboard):
    """
    Generates animation frames based on the storyboard data without opening a window.
    """
    pygame.init()

    # Create a lower-resolution headless surface (640x480 instead of 800x600)
    screen = pygame.Surface((640, 480))  
    clock = pygame.time.Clock()

    # Initialize positions for objects/characters (just basic shapes for now)
    char_x, char_y = 100, 300
    dog_x, dog_y = 400, 300
    frame_count = 0

    MAX_ACTIONS = 5  # Limit the number of actions to avoid overloading the system
    actions = storyboard["actions"][:MAX_ACTIONS]  # Limit to the first 5 actions

    # Loop through the storyboard actions (e.g., 'walk', 'run', 'jump')
    for action in actions:
        for i in range(30):  # Reduced number of frames per action
            screen.fill((255, 255, 255))  # Clear screen (white background)

            # Draw the "character" (a red rectangle for now)
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(char_x, char_y, 50, 100))

            # Draw the "dog" (a blue rectangle for now)
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(dog_x, dog_y, 50, 50))

            # Simulate action (simple movement for 'walk')
            if action == 'walk':
                char_x += 2  # Move character to the right
            elif action == 'run':
                char_x += 4  # Move character faster
            elif action == 'jump':
                char_y -= 10 if i < 15 else 10  # Jump up, then down

            # Save the frame as an image
            frame_filename = f"{FRAME_DIR}/frame_{frame_count:04d}.png"
            pygame.image.save(screen, frame_filename)
            frame_count += 1

            # Add a small delay to reduce CPU load
            time.sleep(0.05)

            # Tick at 30 FPS instead of 60 FPS to reduce system strain
            clock.tick(30)  

    pygame.quit()

def generate_video_from_frames(output_filename="animation_video.mp4", fps=15):
    """
    Converts the generated frames into a video using moviepy with reduced frame rate.
    After the video is created, delete the frames to free up memory.
    The video is saved to the user's desktop.
    """
    # Get the user's desktop path
    desktop_path = os.path.expanduser("~/Desktop")
    output_path = os.path.join(desktop_path, output_filename)

    # Get all frames in order
    frame_files = sorted([os.path.join(FRAME_DIR, f) for f in os.listdir(FRAME_DIR) if f.endswith('.png')])

    # Create a video clip from the frames with a lower frame rate (15 FPS)
    clip = ImageSequenceClip(frame_files, fps=fps)
    clip.write_videofile(output_path, codec="libx264")

    # After generating the video, delete the frames
    clear_frames()

    print(f"Video has been saved to {output_path}")
