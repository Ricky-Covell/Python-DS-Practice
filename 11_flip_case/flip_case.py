def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped_phrase = ''
    
    for letter in phrase:
        if letter.lower() == to_swamp.lower():
            letter = letter.swampcase()
        swapped_phrase += letter
    
    return swapped_phrase