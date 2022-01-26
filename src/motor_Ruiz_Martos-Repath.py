"""
    @file           TP_motor.py
    @brief          Driver class that sets up and controls motors.
    @author         Dylan Ruiz
                    Lucas Martos-Repath
        
"""

import pyb
import time

class TP_Motor:
    ''' @brief      A motor class for one channel of the DRV8847
        @details    Objects of this class can be used to apply PWM to a
                    given DC motor
    '''
    
    def __init__(self, en_pin, in1pin, in2pin, timer):
        ''' @brief      Initializes and returns a motor object associatted with the DRV8847
               
        '''
        ## Initializes timer 3
        self.timer = pyb.Timer(timer, freq = 20000)
        ## Initializes pin B4
        self.pinIN1 = in1pin
        ## Initializes pin B5
        self.pinIN2 = in2pin
        
        self.pinENABLE = en_pin
        

        
#         ## Initializes pin B0
#         self.pinIN3 = pyb.Pin(pyb.Pin.cpu.B0)
#         ## Initializes pin B1
#         self.pinIN4 = pyb.Pin(pyb.Pin.cpu.B1)
        ## Configures channel 1 for timer 3
        self.timer_ch1 = self.timer.channel(1, pyb.Timer.PWM, pin=self.pinIN1)
        ## Configures channel 2 for timer 3
        self.timer_ch2 = self.timer.channel(2, pyb.Timer.PWM, pin=self.pinIN2)
        ## Configures channel 3 for timer 3
#         self.t3ch3 = self.tim3.channel(3, pyb.Timer.PWM, pin=self.pinIN3)
#         ## Configures channel 4 for timer 3
#         self.t3ch4 = self.tim3.channel(4, pyb.Timer.PWM, pin=self.pinIN4)
# 
       
    def enable(self):
        ''' @brief      Brings the DRV8847 out of sleep mode
        '''
        ## Sets the sleep pin to high
        self.pinENABLE.high()
        ## Sets a delay of 25 us
        time.sleep_us(25)
   
    
    
    def disable(self):
        ''' @brief          Disables selected motor.
            @param motor    Indicates which motor is selected.
            
        '''
        # self.motor = motor
        self.pinENABLE.low()
    
        pass
        
    def set_duty(self, duty):
        ''' @brief      Sets the PWm duty cylce for the motor channel
            @details    This method sets the duty cycle to be sent to the 
                        motor to the given level. posotive values cause effort
                        in one dierction, negative values in the opposite
                        direction
            @param      duty    A signed number holding the duty cycle
                                of the PWM signal sent to the motor
        '''
        # self.motor = motor
        if duty > 0:
            self.timer_ch1.pulse_width_percent(0)
            self.timer_ch2.pulse_width_percent(abs(duty))
        elif duty < 0:
            self.timer_ch1.pulse_width_percent(abs(duty))
            self.timer_ch2.pulse_width_percent(0)
            

if __name__ == '__main__':
    
    enableA = pyb.Pin(pyb.Pin.cpu.A10, pyb.Pin.OUT_PP)
    in1 = pyb.Pin(pyb.Pin.cpu.B4)
    in2 = pyb.Pin(pyb.Pin.cpu.B5)
    
    enableB = pyb.Pin(pyb.Pin.cpu.C1, pyb.Pin.OUT_PP)
    in3 = pyb.Pin(pyb.Pin.cpu.A0)
    in4 = pyb.Pin(pyb.Pin.cpu.A1)
    
    motor1 = TP_Motor(enableA,in1,in2,3) # motor in A
    motor2 = TP_Motor(enableB,in3,in4,5) #motor in B
    motor1.enable()
    motor2.enable()
    motor1.set_duty(-50)
    motor2.set_duty(50)
    
    time.sleep_ms(10000)
    motor1.disable()
    motor2.disable()
    
    

        
    
    
    
    
    
    
    
    

