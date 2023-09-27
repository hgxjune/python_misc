#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import clr
# clr module: pip install pythonnet
# OpenHardwareMonitor: https://openhardwaremonitor.org/

clr.AddReference(os.path.dirname(os.path.abspath(__file__)) + r"/../_3rd/OpenHardwareMonitor/OpenHardwareMonitorLib.dll") 
from OpenHardwareMonitor.Hardware import Computer


def cpu():
    c = Computer()
    c.CPUEnabled = True
    c.Open()
    print("-- CPU")
    for a in range(0, len(c.Hardware[0].Sensors)):
        if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
            print("  -- Hardware Sensors: %s, Identifier: %s, Value: %s" % (a, c.Hardware[0].Sensors[a].Identifier, c.Hardware[0].Sensors[a].get_Value()))
    c.Close()
    pass


def gpu():
    c = Computer()
    c.GPUEnabled = True
    c.Open()
    print("-- GPU")
    for a in range(0, len(c.Hardware[0].Sensors)):
        if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
            print("  -- Hardware Sensors: %s, Identifier: %s, Value: %s" % (a, c.Hardware[0].Sensors[a].Identifier, c.Hardware[0].Sensors[a].get_Value()))
    c.Close()
    pass


def main():
    cpu()
    gpu()
    pass



if __name__ == '__main__':
    print(u"测试输出")
    print(u"------------------------------------------------")
    main()



