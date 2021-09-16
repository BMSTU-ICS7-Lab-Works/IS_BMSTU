from installator import check_keys
import pyglet
import sys

if __name__ == '__main__':
    if not check_keys("license.key"):
        # pick an animated gif file you have in the working directory
        ag_file = "fail.gif"
        animation = pyglet.resource.animation(ag_file)
        sprite = pyglet.sprite.Sprite(animation)

        # create a window and set it to the image size
        win = pyglet.window.Window(width=sprite.width, height=sprite.height)


        @win.event
        def on_draw():
            win.clear()
            sprite.draw()


        pyglet.app.run()
    else:
        # pick an animated gif file you have in the working directory
        ag_file = "cool.gif"
        animation = pyglet.resource.animation(ag_file)
        sprite = pyglet.sprite.Sprite(animation)

        # create a window and set it to the image size
        win = pyglet.window.Window(width=sprite.width, height=sprite.height)


        @win.event
        def on_draw():
            win.clear()
            sprite.draw()

        pyglet.app.run()