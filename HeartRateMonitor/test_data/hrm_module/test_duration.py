def test_duration():
    from myrhm import Myrhm
    import math
    import pytest
    duration_output_1 = [1, 2, 3, 4, 5]

    output_1 = Myrhm(duration_output_1)

    assert output_1 == 4

    with pytest.raises(ValueError):
        duration(-2)
    with pytest.raises(TypeError):
        duration('time')
    with pytest.raises(ImportError):
        import MyLittlePony
