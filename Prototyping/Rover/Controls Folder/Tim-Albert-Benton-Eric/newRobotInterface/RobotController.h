#ifndef ROBOT_CONTROLLER_H
#define ROBOT_CONTROLLER_H

#include "PidController.h"
#include <Adafruit_MotorShield.h>

// An interface for controlling the robot. Assumes that the joint is exactly in
// the middle between the front and back wheels.
// All speeds are measured in TODO units. All angles are measured in degrees.
class RobotController {
    public:
        RobotController();
        // Steers the robot. 'target_speed' is the target speed 'target_angle'
        // controlls how the robot should turn. It is the angle we want the
        // central joint to be. 0 is straight forward.  Positive is turning
        // right. Negative is turning left.  'curr_angle' is the current angle
        // of the joint.
        void setDrive(double target_speed, double target_angle, double curr_angle);
    private:
        // Sets the wheel speeds such that, if maintained at these speeds for a
        // long time, will result in the robot moving at 'speed' and has the
        // central joint at 'angle'.
        void setDriveTowards(double speed, double angle);
        // Actually make the wheel turn at the values in 'motor_speeds'.
        void setMotors();

        Adafruit_MotorShield motor_shield;
        // PID controller for the angle.
        PidController angle_controller;
        // 0 is back left, 1 is back right, 2 is front right, 3 is front left
        double motor_speeds[4];
        Adafruit_DCMotor *(motors[4]);
};

#endif
