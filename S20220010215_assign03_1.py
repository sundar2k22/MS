import os
import pyglet
from pyglet import image
from moviepy.editor import ImageSequenceClip

# Create a window with specified dimensions and title
window = pyglet.window.Window(width=1000, height=800, caption="Bouncing Ball Animation")

# Ball properties
ball_radius = 30
ball_x = window.width // 2
ball_y = window.height // 2
ball_dx = 200  # Speed in the x-direction (pixels per second)
ball_dy = 150  # Speed in the y-direction (pixels per second)

# Create a circle shape for the ball
ball = pyglet.shapes.Circle(ball_x, ball_y, ball_radius, color=(0, 100, 150))

# Frame counter
frame_counter = 0

# Output directory for frames and video
output_directory = './output_video'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Update function to move the ball and handle bouncing
def update(dt):
    global ball_x, ball_y, ball_dx, ball_dy, frame_counter

    # Update ball position based on its speed and the elapsed time
    ball_x += ball_dx * dt
    ball_y += ball_dy * dt

    # Reverse horizontal direction if the ball hits the left or right window boundaries
    if ball_x - ball_radius < 0 or ball_x + ball_radius > window.width:
        ball_dx = -ball_dx

    # Reverse vertical direction if the ball hits the top or bottom window boundaries
    if ball_y - ball_radius < 0 or ball_y + ball_radius > window.height:
        ball_dy = -ball_dy

    # Update the ball shape's position
    ball.x = ball_x
    ball.y = ball_y

    # Save frame as an image
    pyglet.image.get_buffer_manager().get_color_buffer().save(os.path.join(output_directory, f'frame_{frame_counter}.png'))
    frame_counter += 1

# Set the background color
pyglet.gl.glClearColor(173/255, 216/255, 230/255, 1)  # Light blue color

# Draw the ball in the window
@window.event
def on_draw():
    pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)  # Clear the window with the background color
    ball.draw()

# Key press event to exit the application
@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ESC:  # Use ESC key to exit
        pyglet.app.exit()

# Schedule the update function to run at 60 frames per second
pyglet.clock.schedule_interval(update, 1/60.0)

# Run the pyglet application
pyglet.app.run()

# After the application is closed, compile the images into a video
try:
    if frame_counter > 0:  # Check if any frames were saved
        clip = ImageSequenceClip(output_directory, fps=60)  # Use the output directory for frames
        clip.write_videofile(os.path.join(output_directory, 'animation.mp4'), codec='libx264')
    else:
        print("No frames were captured to create a video.")
except Exception as e:
    print(f"An error occurred while creating the video: {e}")