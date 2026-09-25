"""
W03 Project: Water Pressure
Author: Gabriel Rengifo
Course CSS111

I add a new function that converts the kpa into psi, the function is called water_pressure_kpa_into_psi

"""

from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction, water_pressure_kpa_into_psi
from pytest import approx
import pytest


def test_water_column_height():
    assert water_column_height(48.3, 12.8 ) == approx(57.9)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)

def test_reynolds_number():
    assert reynolds_number(0.286870, 1.75 ) == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

def test_water_pressure_kpa_into_psi():
    assert water_pressure_kpa_into_psi(20) == approx(2.90075, abs=0.001)
    

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])