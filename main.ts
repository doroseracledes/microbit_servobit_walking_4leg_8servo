function FR (A: number, B: number) {
    ServoBit.setServo(FR_A, A)
    ServoBit.waitServo(FR_A)
    ServoBit.setServo(FR_B, B)
}
function FL (A: number, B: number) {
    ServoBit.setServo(FL_A, A)
    ServoBit.waitServo(FL_A)
    ServoBit.setServo(FL_B, B)
}
function walk (step: number) {
    if (step == 0) {
        FL(-45, 15)
        RR(15, -15)
        basic.pause(500)
        FL(-30, 30)
        RR(30, 10)
    } else if (step == 1) {
        FR(45, -15)
        RL(-15, 15)
        basic.pause(500)
        FR(30, 15)
        RL(-30, 30)
    }
}
function resetAll () {
    ServoBit.setServo(FL_A, -30)
    ServoBit.setServo(FL_B, 0)
    ServoBit.setServo(FR_A, 30)
    ServoBit.setServo(FR_B, 0)
    ServoBit.setServo(RL_A, -30)
    ServoBit.setServo(RL_B, 0)
    ServoBit.setServo(RR_A, 30)
    ServoBit.setServo(RR_B, 0)
}
function RR (A: number, B: number) {
    ServoBit.setServo(RR_A, A)
    ServoBit.waitServo(RR_A)
    ServoBit.setServo(RR_B, B)
}
function walk2 (step: number) {
    if (step == 0) {
        FL(-45, 10)
        RR(15, 30)
        basic.pause(200)
        FL(-30, 30)
        RR(30, -15)
    } else if (step == 1) {
        FR(45, 0)
        RL(-15, -30)
        basic.pause(200)
        FR(30, -30)
        RL(-30, 15)
    }
}
radio.onReceivedString(function (receivedString) {
    if (receivedString == "W") {
        for (let index = 0; index <= 3; index++) {
            walk2(index)
            basic.pause(200)
        }
    } else if (receivedString == "J") {
        for (let index = 0; index < 1; index++) {
            basic.showIcon(IconNames.Butterfly)
            resetAll()
        }
    }
    basic.pause(200)
})
function RL (A: number, B: number) {
    ServoBit.setServo(RL_A, A)
    ServoBit.waitServo(RL_A)
    ServoBit.setServo(RL_B, B)
}
let RR_B = 0
let RR_A = 0
let RL_B = 0
let RL_A = 0
let FR_B = 0
let FR_A = 0
let FL_B = 0
let FL_A = 0
let speed = 300
FL_A = 0
FL_B = 1
FR_A = 2
FR_B = 3
RL_A = 4
RL_B = 5
RR_A = 6
RR_B = 7
radio.setGroup(10)
resetAll()
basic.pause(100)
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        for (let index = 0; index <= 3; index++) {
            walk(index)
        }
    } else if (input.buttonIsPressed(Button.B)) {
        for (let index = 0; index < 1; index++) {
            basic.showIcon(IconNames.Butterfly)
            resetAll()
        }
    }
})
