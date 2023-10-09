def on_gesture_screen_up():
    radio.send_string("とまる")
    basic.show_string("P")
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_gesture_tilt_right():
    radio.send_string("みぎ")
    basic.show_string("R")
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_tilt_left():
    radio.send_string("ひだり")
    basic.show_string("L")
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_logo_up():
    radio.send_string("こうしん")
    basic.show_string("B")
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_logo_down():
    radio.send_string("ぜんしん")
    basic.show_string("F")
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

radio.set_group(7)

def on_forever():
    pass
basic.forever(on_forever)
