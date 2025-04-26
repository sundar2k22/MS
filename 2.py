import pyglet
width = 1500
height = 1500
title = "My First Animation"
window = pyglet.window.Window(width, height, title)
pyglet.gl.glClearColor(0.5, 0.5, 0.5, 1)
text  = "Welcome to the world of Animation"
label = pyglet.text.Label(text, font_name='Cooper', font_size=16, x=250, y=150, anchor_x='center', anchor_y='center')

# image = pyglet.resource.image('Red.jpeg')
# carsprite = pyglet.sprite.Sprite(image, x=200, y=200)
s0 = pyglet.resource.image('Red.jpeg')
s1 = pyglet.resource.image('Blue.jpeg')
images = [s0,s1]
anim = pyglet.image.Animation.from_image_sequence(images, 0.5, True)
sprite = pyglet.sprite.Sprite(anim)
@window.event
def on_draw():
    window.clear()
    label.draw()
    sprite.draw()
pyglet.app.run()