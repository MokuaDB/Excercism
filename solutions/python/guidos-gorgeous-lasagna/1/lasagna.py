"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
elapsed_time_in_minutes = 10

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_time_in_minutes):
    """Calcula el tiempo que le queda, teniendo en cuenta la diferencia del tiempo que debe estar horneando con el tiempo transcurrido"""
    return(EXPECTED_BAKE_TIME - elapsed_time_in_minutes)
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

def preparation_time_in_minutes(number_of_layers):
    """Calcula el tiempo de preparación teniendo en cuenta el numero de capas.
    """
    time = number_of_layers * PREPARATION_TIME
    return(time)

def elapsed_time_in_minutes(number_of_layers, elapsed_baked_time):
    """ Calcula el tiempo total preparación mas horneado"""
    return(preparation_time_in_minutes(number_of_layers) + elapsed_baked_time)

#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.



#TODO (student): define the 'elapsed_time_in_minutes()' function below.



# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
