import myhrm


def test_num_beat():
    import math
    import pytest
    numbeat_output_1 = num_beat([1, 2, 3, 4, 5])
    assert numbeat_output_1 == 5
    with pytest.raueses(ValueError):
        duration(-5)
    with pytest.raises(TypeError):
        duration('number')
    with pytest.raises(ImportError):
        import MyLittlePony
