import numpy as np
import matplotlib.pyplot as plt

#Drawing the Graph of Message Signal
def draw_message(am, fm):
    t = np.arange(0, 10, 0.001)
    xm = am*np.sin(2*np.pi*fm*t)
    plt.title("Message Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(t, xm)
    plt.show()
    return xm

#Drawing the Graph of Sampling Signal
def draw_sampling_signal():
    t = np.arange(0, 10, 0.001)
    xss = [0]*95 + [1]*10 + [0]*95
    xss = xss*50
    plt.title("Sampling Signal Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(t, xss)
    plt.show()
    return xss

#Drawing the Graph of PAM signal
def draw_PAM(xm, xss):
    t = np.arange(0,10,0.001)
    xm = np.array(xm)
    xss = np.array(xss)
    xt = xm*xss
    plt.title("Phase Amplitude Modulated Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(t, xt, "r", t, xm, "b")
    plt.show()


am, fm = map(float, raw_input("Input the amplitude and frequency of message signal: ").split())

xm = draw_message(am, fm)
xss = draw_sampling_signal()
draw_PAM(xm, xss)
