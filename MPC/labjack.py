from psychopy.hardware.labjacks import U3
import u3
lj = U3()

# Get calibration info and turn FIO 0 to off (usually starts as ON)
cal_data = lj.getCalibrationData()
if lj.getFIOState(0) == 1:
    lj.setFIOState(0,0) #Make sure we start with the trigger off

# At onset of event toggle FIO 0 to ON
lj.setFIOState(0,t)

# At offset of event toggle FIO 0 to OFF
lj.setFIOState(0,0)
