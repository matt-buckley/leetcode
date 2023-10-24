class Solution:
    def isPowerOfFour(self, n: int) -> bool:
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
