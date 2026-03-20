import numpy as np
import numpy.testing as npt

import Games

def test_Games_smoke():
    #Smoke_test
    obt = Games.Games_object()

def test_Games_object_fizz():
    #test the fizz_function
    obj = Games.Games_object()
    output = obj.fizz()

    npt.assert_equal(output, "buzz")
