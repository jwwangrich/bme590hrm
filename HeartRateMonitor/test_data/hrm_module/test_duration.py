def test_duration():
    from hrm_module.myrhm import Myrhm
    import math
    import pytest
    duration_output_1 = duration([1, 2, 3, 4, 5])
    assert duration_output_1 == 4
    with pytest.raueses(ValueError):
        duration(-2)
    with pytest.raises(TypeError):
        duration('time')
    with pytest.raises(ImportError):
        import MyLittlePony
