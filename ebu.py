#!/usr/bin/env python3
import numpy as np
import soundfile as sf # MAYBE IT WONT BE USED ////// REMEMBER DELETE IF NOT
import wave as wv
import sys
import time

def CreateFrame (AudioSampleX, AudioSampleY):
    """
    Crate a frame (the first frame must have been created before use this def)
    """

    SubFrameX = [b'0xD2', AudioSampleX, 1, 0, 0, 1]
    SubFrameY = [b'0xD4', AudioSampleY, 1, 0, 0, 1]
    Frame = [SubFrameX, SubFrameY]
    return Frame

def CreateBlock(audio):
    """
    Crea una subtrama por defecto
    """

    AudioWidht = audio.getsampwidth()  # Number of bytes
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
            SamplesCursor = audio.tell()  # Update cursor

        return FrameList

def InsertInStatusList(statusList, statusByte, statusByteNum):
    index = statusByteNum * 8
    for bit in statusByte:
        statusList[index] = bit
        index += 1
    return statusList

def BuildStatusBits():
    """
    This function interact with the user for archieve the needed information
    about status bits impelementation
    """

    StatusList = np.zeros(192)  # default all 0

    print ("Select a impelementation of status bits:" + '\n'
            + '1: Minimum' + '\n'
            + '2: Stantard' + '\n'
            + '3: Enhanced')
    mode = input()

    print("If the impelementation chosen it's needed of extra information "
            + "it will be asked byte by byte like input")
    time.sleep(0.5)

    if mode == '2':
        print("Write the 0 status byte (i.e. 01110010)")
        ZeroByte = input()
        StatusList = InsertInStatusList(StatusList, ZeroByte, 0)
        print(StatusList)


if __name__ == "__main__":

    BuildStatusBits()


    try:
        AudioData = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python ebu.py AudioFile")

    with wv.open(AudioData, 'r') as audio:

        FrameList = CreateBlock(audio)

        # print(FrameList)






        # print(type(b'0x02'))
        # #
        # # print(audio.getsampwidth())
        # # print(audio.getnframes())
        # # sample = audio.readframes(1)
        # # print(sample)
        # # print(audio.tell())
