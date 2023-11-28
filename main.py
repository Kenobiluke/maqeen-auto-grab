def on_received_number(receivedNumber):
    if receivedNumber == 1:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 100)
    elif receivedNumber == 2:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 100)
    elif receivedNumber == 3:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 100)
    elif receivedNumber == 4:
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 100)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global button1
    button1 = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global button1
    button1 = 3
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global button1
    button1 = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    global button1
    button1 = 10
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

button1 = 0
Infval = 0
button1 = 10
radio.set_group(1)

def on_forever():
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) < 30:
        basic.show_leds("""
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    else:
        basic.clear_screen()
basic.forever(on_forever)

def on_forever2():
    if button1 == 1:
        if maqueen.ultrasonic(PingUnit.CENTIMETERS) < 30:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 100)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
        else:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 150)
        basic.pause(100)
    elif button1 == 3:
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
            while maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
                maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
            maqueen.motor_stop(maqueen.Motors.M1)
        elif maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
            while maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
                maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
            maqueen.motor_stop(maqueen.Motors.M2)
        else:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 6)
    else:
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 or maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 255)
            basic.pause(200)
        else:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 20)
basic.forever(on_forever2)

def on_forever3():
    pass
basic.forever(on_forever3)
