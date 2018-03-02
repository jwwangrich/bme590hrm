import glob
import csv
import numpy as np
import math
import pandas as pd
from num_beat import num_beat
from mean_hr_bpm import mean_hr_bpm

class Myhrm(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        time : the array of the raw data Time column
        voltage : the array of the raw data Voltage column
        minutes : user specified time
        peak_indexes : the ECG data peak index
        voltage_extremes_result : find the min and max value of a given voltage array
        duration_result : find the time duration of the ECG strip
        num_beat_result : number of detected beats in the strip
        mean_hr_bpm_result : estimated average heart rate over a user-specified number of minutes
        beat : numpy array of times when a beat occurred
    """

    def __init__(self, time = None, voltage = None, minutes = 1.0):
        self.time = time
        self.voltage = voltage
        self.minutes = minutes
        self.duration_result = 0
        self.peak_indexes = []
        self.num_beat_result = 0
        self.beat_result = []

    def voltage_extremes(self):
        self.voltage_extremes_result = tuple(min(self.voltage); max(self.voltage))
        return self.voltage_extremes_result

    def duration(self):
        self.duration_result = max(self.time) - min(self.time)
        return self.duration_result

    def num_beat(self):
        """ count the value of the number of beats
                first find the max voltage of the raw data as the reference
                make an array with five point with the max vol as center index
                utilize correlate to find peaks

                :param:  maxindex : maximum value of the index in voltagearr
                :param:  maxwave : the array of specific index arrange
                :param:  maxwave_oned : transfer into 1D array
                :param:  volarr_oned : transfer into 1D array
                :returns: return the max two adjacent diff value from input num_list
                :raises: ImportError
                :raises: TypeError
                :raises: ValueError
            """
        import numpy as np
        from scipy.signal import find_peaks_cwt
        try:
            import logging
        except ImportError:
            logging.error("There is an ImportError")
            print("Requested import file does not exist.")

        logging.basicConfig(filename='divlog.txt',
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.DEBUG)

        if len(self.time) == 0:
            logging.warning("list is empty")
        try:
        max_index = np.argmax(self.voltage)
        max_wave = np.array([self.voltage[max_index - 2:max_index + 2]])
        max_wave_oned = np.ravel(max_wave)
        volarr_oned = np.ravel(self.voltage)
        peak = np.correlate(max_wave_oned, volarr_oned, mode='full')
        cb = np.array(peak)
        self.peak_indexes = find_peaks_cwt(cb, np.arange(1, 400))
        self.num_beat_result = len(self.peak_indexes)
        return self.num_beat_result

    def mean_hr_bpm(self):
        """ count the value of the number of beats
                first find the max voltage of the raw data as the reference
                make an array with five point with the max vol as center index
                utilize correlate to find peaks

                :param:  num_list: list of values
                :param:  i : the index in num_list
                :param:  j : the index i + 1 in num_list
                :returns: return the max two adjacent diff value from input num_list
                :raises: ImportError
                :raises: TypeError
                :raises: ValueError
            """
        try:
            import logging
        except ImportError:
            logging.error("There is an ImportError")
            print("Requested import file does not exist.")

        logging.basicConfig(filename='divlog.txt',
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.DEBUG)

        # beats in given minutes
        global peak_indexes
        RR_list = []
        cnt = 0
        while (cnt < (len(peak_indexes) - 1)):
            RR_interval = (peak_indexes[cnt + 1] - peak_indexes[cnt])
            ms_dist = ((RR_interval / self.duration_result) * 60 * self.minutes)
            RR_list.append(ms_dist)
            cnt += 1
        self.mean_hr_bpm_result = cnt
        return self.mean_hr_bpm_result

    def beat(self):
        self.beat_result = tuple(np.where[self.peak_indexes])
        return self.beat_result