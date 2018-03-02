def json_add(voltage_extremes_result, duration_result, num_beat_result,
             mean_hr_bpm_result, beat_result):

    myhrm_info = {'voltage_extrems_result': voltage_extremes_result, 'duration_result': duration_result,
                 'num_beat_result': num_beat_result, 'mean_hr_bpm_result': mean_hr_bpm_result,
                  'beat_result': beat_result}

    file = open(info.replace('.csv', '.json'), 'w')
    filename = json.dumps(myhrm_info)
    file.write(filename)
    return file