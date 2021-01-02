import copy

from helpers import *

def get_initial_three_bit_state():
    """Return the initial state for your 3b/4b encoder."""
    return -1

def get_initial_five_bit_state():
    """Return the initial state for your 5b/6b encoder."""
    return -1

def get_disparity_of_parts( three_bit_input, five_bit_input ):
    """Given the three bit and five bit parts of the input, determine whether the four bit output and the six bit output will have disparity"""
    six_bit_input = five_bit_lookup_table(five_bit_input)
    four_bit_input = three_bit_lookup_table(three_bit_input)

    if weight(six_bit_input) == 0.5*len(six_bit_input):
        is_five_bit_disparity = False
    else:
        is_five_bit_disparity = True
    if weight(four_bit_input) == 0.5*len(four_bit_input):
        is_three_bit_disparity = False
    else:
        is_three_bit_disparity = True

    return is_three_bit_disparity, is_five_bit_disparity

def do_five_bit_encoding( current_input, current_state, is_three_bit_disparity, is_five_bit_disparity ):
    six_bit_input = copy.deepcopy(five_bit_lookup_table(current_input))
    next_state = 0
    if current_state == 1:
        if (is_five_bit_disparity and is_three_bit_disparity) or ( not is_five_bit_disparity and not is_three_bit_disparity):
            next_state = current_state
        else:
            next_state = -1
    else:
        if(is_five_bit_disparity and is_three_bit_disparity):
            next_state = current_state
            six_bit_input = bitflip(six_bit_input)
        elif(not is_five_bit_disparity and not is_three_bit_disparity):
            next_state = current_state
        elif(is_five_bit_disparity and not is_three_bit_disparity):
            six_bit_input = bitflip(six_bit_input)
            next_state = 1
        else:
            next_state = 1
    """Given the current state and five bit part of the current input, return a tuple containing the six bit of the output, the next state and a value to feed into the 3b/4b encoder (you can put None if you don't need to send anything to the 3b/4b encoder)."""
    return six_bit_input, next_state
 
def do_three_bit_encoding( current_input, current_state, is_three_bit_disparity, is_five_bit_disparity ):
    four_bit_input = copy.deepcopy(three_bit_lookup_table(current_input))
    next_state = 0
    if current_state == 1:
        if (is_five_bit_disparity and is_three_bit_disparity):
            four_bit_input = bitflip(four_bit_input)
            next_state = current_state
        elif (not is_five_bit_disparity and not is_three_bit_disparity):
            next_state = current_state
        elif (is_five_bit_disparity and not is_three_bit_disparity):
            next_state = -1
        else:
            next_state = -1
    else:
        if(not is_five_bit_disparity and not is_three_bit_disparity) or (is_five_bit_disparity and is_three_bit_disparity):
            next_state = current_state
        elif(not is_five_bit_disparity and is_three_bit_disparity):
            four_bit_input = bitflip(four_bit_input)
            next_state = 1
        else:
            next_state = 1
    """Given the current input, the current state and a message from the 5b/6b encoder and returns its next state and a four bit output."""
    return four_bit_input, next_state

def bitflip (current_input):

    for x in range(len(current_input)):
        if current_input[x] == 1:
            current_input[x] = 0
        else:
            current_input[x] = 1

    return current_input


