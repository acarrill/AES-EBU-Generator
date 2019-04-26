#!/usr/bin/env python3
import numpy as np
import soundfile as sf # MAYBE IT WONT BE USED ////// REMEMBER DELETE IF NOT
import wave as wv
import sys
import time

def CreateFrame (audioSampleX, audioSampleY, statusList, statusCursor):
    """
    Crate a frame (the first frame must have been created before use this def)
    """

    if statusCursor == 0:
        FirstSubFrame = [b'0xD8', audioSampleX, 1, 0, statusList[statusCursor], 1]
    else:
        FirstSubFrame = [b'0xD2', audioSampleX, 1, 0, statusList[statusCursor], 1]
    SubFrameY = [b'0xD4', audioSampleY, 1, 0, statusList[statusCursor+1], 1]
    Frame = [FirstSubFrame, SubFrameY]
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
    StatusList = BuildStatusBits()  # List with all status bits
    StatusCursor = 0

    if AudioWidht == 2: #CAMBIAIAUSDJDHJASDHBASJDHBAJSHB
        # Take 2 samples and create the frist Frame
        AudioSamples = audio.readframes(2)
        Frame = CreateFrame(AudioSamples[0:2], AudioSamples[2:5],
                            StatusList, SamplesCursor)
        print(Frame)
        FrameList.append(Frame)  # First Frame with Z preamble

        SamplesCursor = audio.tell()
        while SamplesCursor != NumSamples:
            if len(FrameList) == 192:  # Each 192 frames
                BlockList.append(FrameList)
                FrameList = []
                SamplesCursor = 0  # We reset SampleCursor and FrameList
                AudioSamples = audio.readframes(2)
                Frame = CreateFrame(AudioSamples[0:2], AudioSamples[2:5],
                                    StatusList, SamplesCursor)
                FrameList.append(Frame)  # First Frame with Z preamble

            AudioSamples = audio.readframes(2)
            Frame = CreateFrame(AudioSamples[0:2], AudioSamples[2:5],
                                StatusList, StatusCursor)
            FrameList.append(Frame)
            SamplesCursor = audio.tell()  # Update cursor

        return BlockList

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
    mode = int(input())
    print("If the impelementation chosen it's needed of extra information "
            + "it will be asked byte by byte like input")

    if mode >= 2:
        for bit in range(3):
            print("Write the " + str(bit) + " status byte (i.e. 01110010)")
            ZeroByte = input()
            StatusList = InsertInStatusList(StatusList, ZeroByte, bit)
        if mode == 3:
            for bit in range(3,23):
                if bit != 5:  # Byte 5 must be set to logic 0
                    print("Write the " + str(bit) + " status byte (i.e. 01110010)")
                    ZeroByte = input()
                    StatusList = InsertInStatusList(StatusList, ZeroByte, bit)

    return StatusList

if __name__ == "__main__":

    try:
        AudioData = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python ebu.py AudioFile")

    with wv.open(AudioData, 'r') as audio:

        BlockList = CreateBlock(audio)

        # print(FrameList)






        # print(type(b'0x02'))
        # #
        # # print(audio.getsampwidth())
        # # print(audio.getnframes())
        # # sample = audio.readframes(1)
        # # print(sample)
        # # print(audio.tell())
