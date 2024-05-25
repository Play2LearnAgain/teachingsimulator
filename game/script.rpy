# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#c8ffc8")
define b = Character("Bertram", color="ffc8c8")

# Images
image bg room = "assets/bg01-hallway.jpg"

image eileen idle = Composite(
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


# The game starts here.

label start:
    scene bg room

    "At the beginning of an exciting new day..."

    show eileen at left with dissolve

    e "Hello there! How are you today?"

    show bertram at right with dissolve

    b "I'm good, thank you! And you?"
    e "I'm doing well, thanks for asking."
    b "Alright, let's get back to the main menu."

    return
