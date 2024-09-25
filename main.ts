let left = 0
let right = 0
let difference = 0
basic.forever(function () {
    left = Kitronik_Move_Motor.readSensor(Kitronik_Move_Motor.LfSensor.Left)
    right = Kitronik_Move_Motor.readSensor(Kitronik_Move_Motor.LfSensor.Right)
    difference = left - right
    if (difference > 10) {
        if (left > right) {
            Kitronik_Move_Motor.motorOff(Kitronik_Move_Motor.Motors.MotorRight)
            Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorLeft, Kitronik_Move_Motor.MotorDirection.Forward, 30)
        } else {
            Kitronik_Move_Motor.motorOff(Kitronik_Move_Motor.Motors.MotorLeft)
            Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorRight, Kitronik_Move_Motor.MotorDirection.Forward, 30)
        }
    } else {
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, 30)
    }
})
