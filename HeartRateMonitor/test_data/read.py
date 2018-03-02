import glob

def main():
    if __name__ == '__main__':
        main()
    collection(x)

def collection(x):

    df = pd.read_csv(x, names=['Time', 'Voltage'], delimiter=',')
    timearr = df["Time"].values
    voltagearr = df["Voltage"].values
    str_minute = input()
    minutes = float(str_minute)
    patient = Myhrm(timearr, voltagearr, minutes)
    from json import json
    json_add(patient.voltage_extremes_result, patient.duration_result, patient.num_beat_result,
             patient.mean_hr_bpm_result, patient.beat_result)
    return json_add
