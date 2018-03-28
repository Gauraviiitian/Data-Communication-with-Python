import numpy as np
import matplotlib.pyplot as plt

#Drawing the graph of Carrier Wave
def draw_carrier(ac, fc):
    t = np.arange(0, 10, 0.001)
    xt = ac*np.sin(2*np.pi*fc*t)
    plt.title("Carrier Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(t, xt)
    plt.show()

#Drawing the graph of Message Wave
def draw_message(am, fm):
    t = np.arange(0, 10, 0.001)
    xt = am*np.sin(2*np.pi*fm*t)
    plt.title("Message Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(t, xt)
    plt.show()
    return xt

#Drawing Modulated Wave
def draw_modulated(ac, fc, xm):
    t = np.arange(0,10,0.001)
    xm = am*np.sin(2*np.pi*fm*t)
    xt = (xm+ac)*np.sin(2*np.pi*fc*t)
    plt.title("Amplitude Modulated Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(t, xt)
    plt.show()
    
#taking input from user
ac, fc = map(float, raw_input("Input the amplitude(cm) and frequency(kHz) of carrier signal: ").split())
am, fm = map(float, raw_input("Input the amplitude and frequency of message signal: ").split())

draw_carrier(ac, fc)
xm = draw_message(am, fm)
draw_modulated(ac, fc, xm)
