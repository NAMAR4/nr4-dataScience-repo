def test_libraries_installed():
    import numpy
    import pandas
    import matplotlib
    import seaborn

    # wenn keine fehler geworfen wurden wird der test gepased
    assert True