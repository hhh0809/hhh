#-------------------------initial setup--------------------------#
OLED12864_I2C.init(60)
sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_MM, DigitalPin.P0)
wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S7, 90)
wuKong.stop_all_motor()


def mid_detect():
#-------------------------show distance--------------------------#
    DIS = sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_MM, DigitalPin.P0)/10
    OLED12864_I2C.show_string(0, 0, "DIS: "+DIS, 1)
    basic.pause(100)
#-----------------------hit wall and stop------------------------#
    if DIS>=10 and DIS<15:
        wuKong.stop_all_motor()
        OLED12864_I2C.show_string(0, 0, "AHHH!      ", 1)
        OLED12864_I2C.show_string(0, 1, "MID: "+DIS, 1)
#-------------------------turn left------------------------------#
        wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S7, 140)
        basic.pause(3000)
        LEFT = sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_MM, DigitalPin.P0)/10
        OLED12864_I2C.show_string(0, 2, "LEFT: "+LEFT, 1)
#-------------------------turn right-----------------------------#
        wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S7, 40)
        basic.pause(3000)
        RIGHT = sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_MM, DigitalPin.P0)/10
        OLED12864_I2C.show_string(0, 3, "RIGHT: "+RIGHT, 1)
        basic.pause(3000)
#-----------------------compare and turn-------------------------#
        if RIGHT>=LEFT:
            OLED12864_I2C.show_string(0, 0, "RIGHT!      ", 1)
            wuKong.set_all_motor(20, 0)
            basic.pause(500)
            wuKong.stop_all_motor()
        else:
            OLED12864_I2C.show_string(0, 0, "LEFT!       ", 1)
            wuKong.set_all_motor(0, -20)
            basic.pause(500)
            wuKong.stop_all_motor()

        OLED12864_I2C.clear()
#-------------------------no wall and go-------------------------#
    else:
        OLED12864_I2C.show_string(0, 1, "GOOD!", 1)
        wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S7, 90)
        wuKong.set_all_motor(-12,14)
#----------------------------run main----------------------------#
basic.forever(mid_detect)