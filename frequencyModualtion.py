import numpy as np
import matplotlib.pyplot as plt

#Drawing the Graph of Carrier Wave
def draw_carrier(ac, fc):
    t = np.arange(0, 10, 0.001)
    xt = ac*np.sin(2*np.pi*fc*t)
    plt.title("Carrier Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(t, xt)
    plt.show()

#Drawing the Graph of Carrier Wave
def draw_message(am, fm):
    t = np.arange(0, 10, 0.001)
    xt = am*np.sin(2*np.pi*fm*t)
    plt.title("Message Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(t, xt)
    plt.show()
    return xt

#Drawing the Graph of Modulated Signal
def draw_modulated(ac, am, fc, fm):
    t = np.arange(0,10,0.001)
    xm = am*np.cos(2*np.pi*fm*t + np.pi)
    xt = ac*np.sin(2*np.pi*t*fc+xm)#assuming proportionality constant to be 1 i.e. kf = 1
    plt.title("Frequency Modulated Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(t, xt, "r", t, xm, "b")
    plt.show()
    

ac, fc = map(float, raw_input("Input the amplitude(cm) and frequency(kHz) of carrier signal: ").split())
am, fm = map(float, raw_input("Input the amplitude and frequency of message signal: ").split())

draw_carrier(ac, fc)
xm = draw_message(am, fm)
draw_modulated(ac, am, fc, fm)
