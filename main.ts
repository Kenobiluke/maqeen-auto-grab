let foundPos = 0
let distance = 0
let approxPos = 0
let foundLine = 0
while (foundLine == 0) {
    if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1) {
        while (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 50)
        }
        maqueen.motorStop(maqueen.Motors.M1)
    } else if (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        while (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 50)
        }
        maqueen.motorStop(maqueen.Motors.M2)
    } else {
        foundLine = 1
    }
}
while (approxPos == 0) {
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 25)
    if (distance < 60) {
        approxPos = 1
    }
    maqueen.motorStop(maqueen.Motors.All)
}
while (foundPos == 0) {
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 23)
    if (distance < 60) {
        maqueen.motorStop(maqueen.Motors.All)
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 23)
        if (distance < 60) {
            maqueen.motorStop(maqueen.Motors.All)
            foundPos = 1
            maqueen.servoRun(maqueen.Servos.S1, 39)
        }
    }
}
while (distance < 5) {
    maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 16)
}
maqueen.servoRun(maqueen.Servos.S1, 0)
maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 175)
basic.forever(function () {
    distance = maqueen.Ultrasonic(PingUnit.Centimeters)
})
