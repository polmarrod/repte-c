def on_received_number(receivedNumber):
    global dado_rival
    dado_rival = receivedNumber
    if dado < dado_rival:
        basic.show_icon(IconNames.SAD)
    elif dado == dado_rival:
        basic.show_icon(IconNames.ASLEEP)
    else:
        basic.show_icon(IconNames.HAPPY)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_string("String")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

dado = 0
dado_rival = 0
radio.set_group(1)

def on_every_interval():
    global dado
    dado = randint(0, 6)
    radio.send_number(dado)
loops.every_interval(2000, on_every_interval)
