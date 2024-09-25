left = 0
right = 0
difference = 0

def on_forever():
    global left, right, difference
    left = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT)
    right = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.RIGHT)
    difference = left - right
    if difference > 10:
        if left > right:
            Kitronik_Move_Motor.motor_off(Kitronik_Move_Motor.Motors.MOTOR_RIGHT)
            Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_LEFT,
                Kitronik_Move_Motor.MotorDirection.FORWARD,
                30)
        else:
            Kitronik_Move_Motor.motor_off(Kitronik_Move_Motor.Motors.MOTOR_LEFT)
            Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_RIGHT,
                Kitronik_Move_Motor.MotorDirection.FORWARD,
                30)
    else:
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 30)
basic.forever(on_forever)
