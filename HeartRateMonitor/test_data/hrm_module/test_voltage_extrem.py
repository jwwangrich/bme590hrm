def test_voltage_extreme():
    from hrm_module.myrhm import Myrhm
    import math
    import pytest
    extreme_output_1 = voltage_extremes([-5, 2, 6, 1, -7, 10])
    extreme_output_2 = voltage_extremes([9, 8, -7, 6, 5, -4])
    extreme_output_3 = voltage_extremes([0.5, -0.9, 0.1, -0.2])
    assert extreme_output_1 == [-7, 10]
    assert extreme_output_2 == [-7, 9]
    assert extreme_output_3 == [-0.9, 0.5]
    with pytest.raueses(ValueError):
        voltage_extreme(math.sqrt(2), math.sqrt(-5), math.sqrt(8))
    with pytest.raises(TypeError):
        voltage_extremes('sdj', 5, 9, 5, 9, 5)
    with pytest.raises(ImportError):
        import MyLittlePony
