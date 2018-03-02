def test_beat():
    from MyHRM import Myhrm
    import math
    import pytest
    beat_output_1 = beat([-5, 2, 6, 1, -7, 10])
    beat_output_2 = beat([9, 8, -7, 6, 5, -4])
    beat_output_3 = beat([0.5, -0.9, 0.1, -0.2])
    assert beat_output_1 == [-7, 10]
    assert beat_output_2 == [-7, 9]
    assert beat_output_3 == [-0.9, 0.5]
    with pytest.raueses(ValueError):
        voltage_extreme(math.sqrt(2), math.sqrt(-5), math.sqrt(8))
    with pytest.raises(TypeError):
        voltage_extremes('sdj', 5, 9, 5, 9, 5)
    with pytest.raises(ImportError):
        import MyLittlePony