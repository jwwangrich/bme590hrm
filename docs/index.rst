bme590hrm
=========
The summary line for a class docstring should fit on one line.

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
        voltage_extremes_result : find the min and max value of a given voltage
        array
        duration_result : find the time duration of the ECG strip
        num_beat_result : number of detected beats in the strip
        mean_hr_bpm_result : estimated average heart rate over a user-specified
        number of minutes
        beat : numpy array of times when a beat occurred


count the value of the number of beats
                first find the max voltage of the raw data as the reference
                make an array with five point with the max vol as center index
                utilize correlate to find peaks

                :param:  maxindex : maximum value of the index in voltagearr
                :param:  maxwave : the array of specific index arrange
                :param:  maxwave_oned : transfer into 1D array
                :param:  volarr_oned : transfer into 1D array
                :returns: return the number of ECG strip
                :raises: ImportError

count the value of the number of beats
                first find the max voltage of the raw data as the reference
                make an array with five point with the max vol as center index
                utilize correlate to find peaks

                :param:  RR_list: heart rate list
                :param:  cnt: numbers of counts of the heart beats
                :param:  RR_interval: heart beat interval
                :param:  ms_dist: minutes rate
                :returns: return the total numbers of heart beats in a given
                time(minutes), called BPM
                :raises: ImportError


.. toctree::
   :maxdepth: 4
 
