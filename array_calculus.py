#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Royal Cuevas
#2285562
#cueva114@mail.chapman.edu
#PHYS220 Fall 2018
#CW 09

import numpy as np
import matplotlib.pyplot as plt

def gradient(x, o=1):
    """Requires a 1-dimensional matrix.
    Will compute the derivative of the 
    corresponding function.
    For larger order derivatives put the
    order as an int in the 2nd argument,
    defaults to 1."""
    D = np.zeros((len(x), len(x)))
    ones = np.ones(len(D)-1)
    np.fill_diagonal(D[1:], -ones)
    np.fill_diagonal(D[:, 1:], ones)
    D[0][0] = -2
    D[0][1] = 2
    D[len(D)-1][len(D)-1] = 2
    D[len(D)-1][len(D)-2] = -2
    for i in range(o-1):
        D = D@D
    return D@x*.5

def xx():
    """Plots x^2 and its derivative"""
    x = np.arange(0, 7)
    f = x**2
    fp = gradient(f)

    a = plt.axes()

    a.plot(x, f, label="f(x)")
    a.plot(x, fp, color="Red", label="f'(x)")

    a.set(xlabel="x", ylabel="y", title="$x^2$")
    a.legend()
    plt.show()

def second():
    """Plots x^2 and its 2nd derivative"""
    x = np.arange(0, 7)
    f = x**2
    fpp = gradient(f, 2)

    a = plt.axes()

    a.plot(x, f, label="f(x)")
    a.plot(x, fpp, color="Red", label="f''(x)")

    a.set(xlabel="x", ylabel="y", title="$x^2$")
    a.legend()
    plt.show()

def xxgrad():
    x = np.arange(0, 7)
    f = x**2
    fp = np.gradient(f)
    a = plt.axes()
    a.plot(x, f, label="f(x)")
    a.plot(x, fp, color="Red", label="f'(x)")
    a.set(xlabel="x", ylabel="y", title="$x^2$")
    a.legend()
    plt.show()
    
def sinx():
    """Plots sin(x) and its derivative"""
    x = np.arange(0, 8)
    s = np.sin(x)
    sp = gradient(s)

    a = plt.axes()

    a.plot(x, s, label="s(x)")
    a.plot(x, sp, color="Red", label="s'(x)")

    a.set(xlabel="x", ylabel="y", title="sin(x)")
    a.legend()
    plt.show()

def sin2():
    """Plots sin(x) and its 2nd derivative"""
    x = np.arange(0, 8)
    s = np.sin(x)
    spp = gradient(s, 2)

    a = plt.axes()

    a.plot(x, s, label="s(x)")
    a.plot(x, spp, color="Red", label="s''(x)")

    a.set(xlabel="x", ylabel="y", title="sin(x)")
    a.legend()
    plt.show()

def sinxgrad():
    x = np.arange(0, 8)
    s = np.sin(x)
    sp = np.gradient(s)
    a = plt.axes()
    a.plot(x, s, label="s(x)")
    a.plot(x, sp, color="Red", label="s'(x)")
    a.set(xlabel="x", ylabel="y", title="$sin(x)$")
    a.legend()
    plt.show()

def exp():
    """Plots e^(-x^2/2)/sqrt(2pi) and its derivative"""
    x = np.arange(0, 6)
    g = np.exp(-x**2/2)/np.sqrt(2*np.pi)
    gp = gradient(g)

    a = plt.axes()

    a.plot(x, g, label="g(x)")
    a.plot(x, gp, color="Red", label="g'(x)")

    a.set(xlabel="x", ylabel="y", title="$e^{-x^2/2}/\sqrt{2\pi}$")
    a.legend()
    plt.show()

def expgrad():
    x = np.arange(0, 6)
    g = np.exp(-x**2/2)/np.sqrt(2*np.pi)
    gp = np.gradient(g)
    a = plt.axes()
    a.plot(x, g, label="g(x)")
    a.plot(x, gp, color="Red", label="g'(x)")
    a.set(xlabel="x", ylabel="y", title="$e^{-x^2/2}/\sqrt{2\pi}$")
    a.legend()
    plt.show()