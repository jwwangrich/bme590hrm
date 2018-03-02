import glob

files = ""


def main():

    collection()


def collection():
    import logging
    import glob
    import json
    import pandas as pd
    global files
    all_csv = glob.glob('*.csv')
    for files in all_csv:
        df = pd.read_csv(files, names=['Time', 'Voltage'], delimiter=',')
        timearr = df["Time"].values
        voltagearr = df["Voltage"].values
        str_minute = input()
        minutes = float(str_minute)
        from myhrm import Myhrm
        patient = Myhrm(timearr, voltagearr, minutes)
        logging.info("function run normally")
        json_add(patient.voltage_extremes_result,
                 patient.duration_result,
                 patient.num_beat_result,
                 patient.mean_hr_bpm_result)
        logging.info("function runs normally")


def json_add(voltage_extremes_result, duration_result, num_beat_result,
             mean_hr_bpm_result):
    import json
    import glob
    global files
    myhrm_info = {'voltage_extreme_result': voltage_extremes_result,
                  'duration_result': duration_result,
                  'num_beat_result': num_beat_result,
                  'mean_hr_bpm_result': mean_hr_bpm_result}

    file = open(files.replace('.csv', '.json'), 'w')
    filename = json.dumps(myhrm_info)
    file.write(filename)
    return file


if __name__ == '__main__':
    main()
