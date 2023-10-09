def on_received_string(receivedString):
    if receivedString == "こうしん":
        basic.show_string("B")
        pins.digital_write_pin(DigitalPin.P13, 1)
        pins.analog_write_pin(AnalogPin.P15, 500)
        pins.digital_write_pin(DigitalPin.P14, 1)
        pins.analog_write_pin(AnalogPin.P16, 500)
    elif receivedString == "みぎ":
        basic.show_string("R")
        pins.digital_write_pin(DigitalPin.P13, 0)
        pins.analog_write_pin(AnalogPin.P15, 500)
        pins.digital_write_pin(DigitalPin.P14, 0)
        pins.analog_write_pin(AnalogPin.P16, 100)
    elif receivedString == "ひだり":
        basic.show_string("L")
        pins.digital_write_pin(DigitalPin.P13, 0)
        pins.analog_write_pin(AnalogPin.P15, 100)
        pins.digital_write_pin(DigitalPin.P14, 0)
        pins.analog_write_pin(AnalogPin.P16, 500)
    elif receivedString == "ぜんしん":
        basic.show_string("F")
        pins.digital_write_pin(DigitalPin.P13, 0)
        pins.analog_write_pin(AnalogPin.P15, 500)
        pins.digital_write_pin(DigitalPin.P14, 0)
        pins.analog_write_pin(AnalogPin.P16, 500)
    elif receivedString == "とまる":
        basic.show_string("P")
        pins.digital_write_pin(DigitalPin.P13, 1)
        pins.digital_write_pin(DigitalPin.P15, 1)
        pins.digital_write_pin(DigitalPin.P14, 1)
        pins.digital_write_pin(DigitalPin.P16, 1)
radio.on_received_string(on_received_string)

radio.set_group(7)

def on_forever():
    pass
basic.forever(on_forever)
