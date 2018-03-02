def num_beats():
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

    if len() == 0:
        logging.warning("list is empty")
    try:
    global voltagearr
    maxindex = np.argmax(voltagearr)
    maxwave = np.array([voltagearr[maxindex - 2:maxindex + 2]])
    maxwave_oned = np.ravel(maxwave)
    volarr_oned = np.ravel(voltagearr)
    peak = np.correlate(maxwave_oned, volarr_oned, mode='full')
    cb = np.array(peak)
    peakindexes = find_peaks_cwt(cb, np.arange(1, 400))
    return len(peakindexes)

    except TypeError:
        logging.error("There is a TypeError")
        print("num_list must be a list containing variable type entries.")
    except ValueError:
        logging.error("There is a ValueError")
        print("The entries list must consist only of real numbers.")

    logging.info("All entries successfully added up.")