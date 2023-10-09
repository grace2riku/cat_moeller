def on_button_pressed_a():
    radio.send_string("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

radio.set_group(7)

def on_forever():
    pass
basic.forever(on_forever)
