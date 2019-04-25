#!/usr/bin/env python3
import numpy as np
import soundfile as sf # MAYBE IT WONT BE USED ////// REMEMBER DELETE IF NOT
import wave as wv
import sys

def CreateFrame (AudioSampleX, AudioSampleY):
    SubFrameX = [b'0xD2', AudioSampleX, 1, 0, 0, 1]
    SubFrameY = [b'0xD4', AudioSampleY, 1, 0, 0, 1]
    Frame = [SubFrameX, SubFrameY]
    return Frame

def CreateBlock(audio):
    """
    Crea una subtrama por defecto
    """

    AudioWidht = audio.getsampwidth()  # In bytes
    FrameList = []
    BlockList = []
    SamplesCursor = audio.tell()  # Cursor inside audio file
    NumSamples = audio.getnframes()  # Num Samples inside audio file

    if AudioWidht == 2: #CAMBIAIAUSDJDHJASDHBASJDHBAJSHB
        # Take 2 samples and create the frist Frame
        AudioSamples = audio.readframes(2)
        SubFrameZ = [b'0xD8', AudioSamples[0:2], 1, 0, 0, 1]
        SubFrameY = [b'0xD4', AudioSamples[2:5], 1, 0, 0, 1]
        Frame = [SubFrameZ, SubFrameY]
        FrameList.append(Frame)  # First Frame with Z preamble

        SamplesCursor = audio.tell()
        while SamplesCursor != NumSamples:
            AudioSamples = audio.readframes(2)
            Frame = CreateFrame(AudioSamples[0:2], AudioSamples[2:5])
            FrameList.append(Frame)
            SamplesCursor = audio.tell()
            print(SamplesCursor)

        return FrameList


if __name__ == "__main__":

    try:
        AudioData = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python ebu.py AudioFile")

    with wv.open(AudioData, 'r') as audio:

        FrameList = CreateBlock(audio)

        print(FrameList)






        # print(type(b'0x02'))
        # #
        # # print(audio.getsampwidth())
        # # print(audio.getnframes())
        # # sample = audio.readframes(1)
        # # print(sample)
        # # print(audio.tell())
