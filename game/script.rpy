# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define character.teacher = Character("Eileen", color="#c8ffc8")
define character.bertram = Character("Bertram", color="ffc8c8")

# Images
image bg room = "assets/bg01-hallway.jpg"

image teacher idle = Composite(
    (556, 1000),
    (0, 0), "assets/fm01/fm01-body.png",
    (0, 0), "assets/fm01/fm01-eyes-smile.png",
    (0, 0), "assets/fm01/fm01-mouth-smile00.png",
)

image bertram idle = Composite(
    (556, 1000),
    (0, 0), im.Flip("assets/m01/m01-body.png", horizontal=True),
    (0, 0), im.Flip("assets/m01/m01-eyes-smile.png", horizontal=True),
    (0, 0), im.Flip("assets/m01/m01-mouth-smile00.png", horizontal=True),
)

image teacher hover = Composite(
    (556, 1000),
    (0, 0), "assets/fm01/fm01-body.png",
    (0, 0), "assets/fm01/fm01-eyes-wow.png",
    (0, 0), "assets/fm01/fm01-mouth-wow.png",
)

image bertram hover = Composite(
    (556, 1000),
    (0, 0), im.Flip("assets/m01/m01-body.png", horizontal=True),
    (0, 0), im.Flip("assets/m01/m01-eyes-wow.png", horizontal=True),
    (0, 0), im.Flip("assets/m01/m01-mouth-wow.png", horizontal=True),
)

# The game starts here.

label start:
    scene bg room
    pause

    # "At the beginning of an exciting new day..."

    show eileen at left with dissolve
    pause

    teacher "Hi [bertram]. Did you rest well?"

    show bertram at right with dissolve
    pause

    bertram "Oh yes, thank you! And you?"
    teacher "Same, thanks for asking."
    extend "Let's continue the exercise!"

    bertram "Alright, let's get going..."

    window hide
    pause

    return
