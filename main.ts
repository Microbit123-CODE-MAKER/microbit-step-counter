input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    steps += 1
    basic.showNumber(steps)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
})
let steps = 0
steps = 0
basic.forever(function on_forever() {
    
})
