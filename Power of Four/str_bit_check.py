def str_bit_check(n: int) -> bool:
    """Validate if int is power of four by using three checks of string representation of bits

    Args:
        n (int): input integer

    Returns:
        bool: True if n is power of four, else False
    """
    bits_n = bin(n)[2:]
    if (
        # first bit is 1
        bits_n[0] == "1"
        # every other bit is 0
        and all(bit == "0" for bit in bits_n[1:])
        # odd number of bits
        and (len(bits_n) % 2) == 1
    ):
        return True
    else:
        return False
