import glob
import csv
import numpy as np
import math
import pandas as pd
from num_beat import num_beat
from mean_hr_bpm import mean_hr_bpm

def main():
    readcsv_tolist()
    write_data()

def write_data(type='json'):
    global files
    csvfiles = open(files, "r")
    temp = list(csv.reader(csvfiles, delimiter=","))
    json_filename = files.replace('.csv', '.json')
    json_file = open(json_filename, "w")
    json_file.write(",".join(temp[0]))

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
        voltage_extremes_result : find the min and max value of a given voltage array
        duration_result : find the time duration of the ECG strip
        beat : numpy array of times when a beat occurred
        num_beat_result : number of detected beats in the strip
        mean_hr_bpm_result :
    """

    def __init__(self, filename):
        readcsv_tolist()
        self.time = None
        self.voltage = None
        self.voltage_extremes_result = None
        self.duration_result = None
        self.num_beat_result = None
        self.mean_hr_bpm_result = None
        self.beat_result = None

    def readcsv_tolist(self):
        """ read the csv raw data file
                :param:  timearr: raw data of collecting timing
                :param:  voltagearr: raw data of voltage value
                :returns: return the two array from input *.csv, Time and Voltage, respectively
                :raises: ImportError
                :raises: TypeError
                :raises: ValueError
            """
        global logging
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
        df = pd.read_csv('*.csv', names=['Time', 'Voltage'], delimiter=',')
        self.time = df["Time"].values
        self.voltage = df["Voltage"].values
        return self.time, self.voltage

    def voltage_extremes(self):
        self.voltage_extremes_result = tuple(min(self.voltage); max(self.voltage))
        return self.voltage_extremes_result

    def duration(self):
        self.duration_result = tuple(max(self.time) - min(self.time))
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
        peak_indexes = find_peaks_cwt(cb, np.arange(1, 400))

        except TypeError:
        logging.error("There is a TypeError")
        print("peak must be a list containing variable type entries.")

        except ValueError:
        logging.error("There is a ValueError")
        print("The entries list must consist only of real numbers.")

        logging.info("All entries successfully added up.")
        self.num_beat_result = len(peak_indexes)
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

        # BPM beats per minute
        global peakindexes
        RR_list = []
        cnt = 0
        while (cnt < (len(peakindexes) - 1)):
            RR_interval = (peakindexes[cnt + 1] - peakindexes[cnt])
            ms_dist = ((RR_interval / 100) * 1000.0)
            RR_list.append(ms_dist)
            cnt += 1
        self.mean_hr_bpm_result = cnt
        return self.mean_hr_bpm_result

    def beat(self):
        self.beat_result = tuple()