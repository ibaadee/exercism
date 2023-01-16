"""Functions for tracking poker hands and assorted card tasks.
 
Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""
def get_rounds(number):
    """Create a list containing the current and next two round numbers.
 
    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    round_number = number
    round_list = []
    while round_number <= (number + 2):
        round_list.append(round_number)
        round_number += 1
    return round_list
def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.
 
    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2
def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.
 
    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    is_played = False
    for item in rounds:
        if item == number:
            is_played = True
    return is_played
def card_average(hand):
    """Calculate and returns the average card value from the list.
 
    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    sum_result = 0
    for item in hand:
        sum_result += item
    return sum_result / len(hand)
def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.
 
    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    is_average = False
    hand_average = card_average(hand)
    if hand_average in ((hand[0] + hand[-1])/2, hand[len(hand)//2]):
        is_average = True
    return is_average
def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).
 
    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    sum_even = 0
    sum_odd = 0
    for item in hand[0::2]:
        sum_even += item
    for item in hand[1::2]:
        sum_odd += item
    return bool(sum_even/len(hand[0::2]) == sum_odd/len(hand[1::2]))
def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.
 
    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
    return hand
