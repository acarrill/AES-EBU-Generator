#!/usr/bin/env python2
import numpy as np
import soundfile as sf # MAYBE IT WONT BE USED ////// REMEMBER DELETE IF NOT
import wave as wv

def CreateFrame(audio):
    """
    Crea una subtrama por defecto
    """

    AudioWidht = audio.getsampwidth()  # In bytes
    Frame = []
    FrameList = []
    BlockList = []

    if AudioWidht == 2: #CAMBIAIAUSDJDHJASDHBASJDHBAJSHB
        SubFrameZ = [0x02, 'MuestrasAudio', 1, 0, 0, 1]  # Trama 20 bits audio
        SubFrameY = [0x04, 'MuestrasAudio', 1, 0, 0, 1]  # Trama 20 bits audio
        Frame = [SubFrameZ, SubFrameY]

        return FramesBlock


if __name__ == "__main__":


    audio = wv.open('cartoon001.wav', 'r')

    FramesBlock = CreateFrame(audio)
    print(FramesBlock)

    print(audio.getsampwidth())
    print(audio.readframes(1))
    print(audio.tell())
