from hrm_module.myhrm import Myhrm
def test_duration():
    import math
    import pytest
    from hrm_module.read import collection
    import numpy as np
    input1 = Myhrm(time=[1, 2, 3, 4, 5],
                   voltage=[1, 2, 3, 4, 5],
                   minutes=1.0)
    input2 = Myhrm(time=[1, 2, 3, 4, 5],
                   voltage=[-2, -9, 43, 15, 10],
                   minutes=1.0)

    duration_output_1 = Myhrm.duration(input1)
    extreme_output_1 = Myhrm.voltage_extremes(input1)
    extreme_output_2 = Myhrm.voltage_extremes(input2)
    num_beat_output_1 = Myhrm.num_beat(input1)

    assert duration_output_1 == 4
    assert extreme_output_1 == (1, 5)
    assert extreme_output_2 == (-9, 43)
    assert num_beat_output_1 == 1
