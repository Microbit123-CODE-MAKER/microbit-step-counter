def on_gesture_shake():
    global steps
    steps += 1
    basic.show_number(steps)
    music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

steps = 0
steps = 0

def on_forever():
    pass
basic.forever(on_forever)
