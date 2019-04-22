#!/usr/bin/env python2
import numpy as np
import soundfile as sf

def CreateTrame():
    """
    Crea una subtrama por defecto
    """

    Subtrame = range(32)

if __name__ == "__main__":
    SubTrame = CreateTrame()

    data, samplerate = sf.read('cartoon001.wav')
    print(data.shape) 
