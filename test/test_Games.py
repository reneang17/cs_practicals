import numpy as np
import numpy.testing as npt

import python_data_science_practicals

def test_Games_smoke():
    #Smoke_test
    obt = python_data_science_practicals.Games_object()

def test_Games_object_fizz():
    #test the fizz_function
    obj = python_data_science_practicals.Games_object()
    output = obj.fizz()

    npt.assert_equal(output, "buzz")
