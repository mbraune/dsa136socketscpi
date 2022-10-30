"""
dsa_meas1.py

example to control SpectrumAnalyzer DSA136
use class DSA136Socket
---
functions 
    status
    set span
    set cf 
    meas f, amp
"""
from dsa136socket import DSA136Socket
import time

def status(dsa):
    """ print settings"""
    print(dsa.instId)

def setfreq(dsa, cf):
    dsa.write(f':FREQ:CENT {cf}')
    print("freq", dsa.query(':FREQ:CENT?'))

def setspan(dsa, span):
    dsa.write(f':FREQ:SPAN {span}')
    print("span", dsa.query(':FREQ:SPAN?'))

def meas(dsa):
    """ get max marker position, return position """
    time.sleep(0.2)
    dsa.write(f':CALC:MARK1:MAX')
    time.sleep(0.1)
    return dsa.query(':CALC:MARK1:X?'), dsa.query(':CALC:MARK1:Y?')



def main():
    """init dsa136 """
    dsa = DSA136Socket('192.168.2.40')
    dsa.write(':DISP:MENU:STAT 1')
    status(dsa)

    setspan(dsa,40e6)
    setfreq(dsa,1.70e9)
    print(meas(dsa))
    time.sleep(2)
    setfreq(dsa,1.71e9)
    print(meas(dsa))
    setfreq(dsa,1.72e9)
    print(meas(dsa))

    dsa.disconnect()

if __name__ == '__main__':
    main()