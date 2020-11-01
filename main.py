def FR(A: number, B: number):
    ServoBit.set_servo(FR_A, A)
    ServoBit.wait_servo(FR_A)
    ServoBit.set_servo(FR_B, B)
def FL(A: number, B: number):
    ServoBit.set_servo(FL_A, A)
    ServoBit.wait_servo(FL_A)
    ServoBit.set_servo(FL_B, B)
def walk(step: number):
    if step == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
        FL(-15, 15)
        RR(15, -15)
    elif step == 1:
        basic.show_icon(IconNames.SQUARE)
        FR(15, -15)
        RL(-15, 15)
    elif step == 2:
        basic.show_icon(IconNames.SMALL_DIAMOND)
        FL(-35, -15)
        RR(30, 15)
    elif step == 3:
        basic.show_icon(IconNames.DIAMOND)
        FR(35, 15)
        RL(-35, 15)
def resetAll():
    ServoBit.set_servo(FL_A, -30)
    ServoBit.set_servo(FL_B, 0)
    ServoBit.set_servo(FR_A, 30)
    ServoBit.set_servo(FR_B, 0)
    ServoBit.set_servo(RL_A, -30)
    ServoBit.set_servo(RL_B, 0)
    ServoBit.set_servo(RR_A, 30)
    ServoBit.set_servo(RR_B, 0)
def RR(A: number, B: number):
    ServoBit.set_servo(RR_A, A)
    ServoBit.wait_servo(RR_A)
    ServoBit.set_servo(RR_B, B)
def walk2(step: number):
    if step == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
        FL(-15, 15)
        RR(15, -15)
        FR(15, -15)
        RL(-15, 15)
    elif step == 1:
        basic.show_icon(IconNames.SQUARE)
        FL(-35, -15)
        RR(30, 15)
        FR(35, 15)
        RL(-35, 15)

def on_received_string(receivedString):
    if receivedString == "W":
        for index in range(4):
            walk(index)
    elif receivedString == "J":
        for index2 in range(1):
            basic.show_icon(IconNames.BUTTERFLY)
            resetAll()
    basic.pause(200)
radio.on_received_string(on_received_string)

def RL(A: number, B: number):
    ServoBit.set_servo(RL_A, A)
    ServoBit.wait_servo(RL_A)
    ServoBit.set_servo(RL_B, B)
RR_B = 0
RR_A = 0
RL_B = 0
RL_A = 0
FR_B = 0
FR_A = 0
FL_B = 0
FL_A = 0
speed = 300
FL_A = 0
FL_B = 1
FR_A = 2
FR_B = 3
RL_A = 4
RL_B = 5
RR_A = 6
RR_B = 7
radio.set_group(10)
resetAll()
basic.pause(100)

def on_forever():
    if input.button_is_pressed(Button.A):
        for index3 in range(4):
            walk(index3)
    elif input.button_is_pressed(Button.B):
        for index4 in range(1):
            basic.show_icon(IconNames.BUTTERFLY)
            resetAll()
    basic.pause(200)
basic.forever(on_forever)
