
from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound



# A ball! This is already in the ggame-tutorials repository
ball_asset = ImageAsset("images/orb-150545_640.png")
ball = Sprite(ball_asset, (0, 0))
ball.fxcenter = 0.7
ball.fycenter = 0.6
# Original image is too big. Scale it to 1/10 its original size
ball.scale = 0.05
    
#Handle the mouse movement
def mouseMove(event):
    ball.x = event.x
    ball.y = event.y

myapp = App()
myapp.listenMouseEvent('mousemove', mouseMove)
myapp.run()