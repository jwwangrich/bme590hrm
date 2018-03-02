from num_beat import num_beats

def mean_hr_bpm():
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
    print(cnt)