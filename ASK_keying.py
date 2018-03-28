import numpy as np
import matplotlib.pyplot as plt

#Drawing the Graph of Carrier Wave
def draw_carrier(ac, fc):
    t = np.arange(0, 10, 0.001)
    xc = ac*np.sin(2*np.pi*fc*t)
    plt.title("Carrier Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(t, xc)
    plt.show()
    return xc

#Drawing the Graph of Message Wave
def draw_message(message):
    t = np.arange(0, 10, 0.001)
    xm = []
    for i in message:
        xm.extend([i]*1000)
    plt.title("Message Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(t, xm)
    plt.show()
    return xm

#Drawing the Graph of ASK Wave
def draw_ASK(xc, xm):
    t = np.arange(0,10,0.001)
    xt = xc*xm
    plt.title("Amplitude Shift Keying Modulated Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(t, xt, "b")
    plt.show()
    

ac, fc = map(float, raw_input("Input Amplitude and Frequency of Carrier Signal : ").split())
m = map(float, raw_input("Input message signal bits : ").split())

xc = draw_carrier(ac, fc)
xm = draw_message(m)
draw_ASK(xc, xm)
