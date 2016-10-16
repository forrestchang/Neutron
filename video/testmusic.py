import pyglet

music = pyglet.resource.media('./default.mp3')
music.play()

pyglet.app.run()