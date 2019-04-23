#!/usr/bin/env python2
import numpy as np
import soundfile as sf # MAYBE IT WONT BE USED ////// REMEMBER DELETE IF NOT
import wave as wv

def CreateTrame():
    """
    Crea una subtrama por defecto
    """
    
    Subtrame = range(32)

if __name__ == "__main__":
    SubTrame = CreateTrame()

    audio = wv.open('cartoon001.wav', 'r')

    print(audio.getsampwidth())
    print(audio.readframes(1))
    print(audio.tell())
