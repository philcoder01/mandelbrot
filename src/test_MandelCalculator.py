from MandelCalculator import MandelCalculator
import pytest

def test_if_max_iteration_reached_for_origin ():
    # GIVEN the MandelCalculator
    max_iter = 100
    calculator = MandelCalculator(-2, 3, -1, 2, max_iter, 4)
    
    # WHEN calculating the mandelValue for the origin of the complex plane
    iter = calculator.getMandelValue(0, 0)
    
    # THEN the result should be the number of max_iterations
    assert iter == max_iter

########################################################################################################
##########################################Test##########################################################

def test_if__05_i05__as_expected ():
    assert help_chk_if_condition_for_complex_number_correct(complex(0.5, 0.5), 5, 4) 

def test_if__03_i1__as_expected ():
    assert help_chk_if_condition_for_complex_number_correct(complex(0.3, 1), 3, 4) 

########################################################################################################

def test_if__05_i05__as_expected_for_limit_200 ():
    assert help_chk_if_condition_for_complex_number_correct(complex(0.5, 0.5), 7, 200) 

def test_if__03_i1__as_expected_for_limit_100 ():
    assert help_chk_if_condition_for_complex_number_correct(complex(0.3, 1), 5, 100) 

#############################################TEST#######################################################
########################################################################################################


        
#########################################################################################################
#########################################################################################################
# Helper Function
#

def help_chk_if_condition_for_complex_number_correct (complex_numb: complex, expected_iter_count: int, set_infinity_limit: int):
    #Function to check mandelbrot correctness
    #-----------------------------------------
    #complex number
    #End condition
        #infinity or max iterations
    #-----------------------------------------
    calculator = MandelCalculator(-2, 3, -1, 2, 100, set_infinity_limit)

    if(expected_iter_count == calculator.getMandelValue(complex_numb.real, complex_numb.imag)):
        return True
    else:
        return False
    
#########################################################################################################
#########################################################################################################

