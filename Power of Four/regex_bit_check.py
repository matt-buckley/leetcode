import re
from types import NoneType


def regex_bit_check(n: int) -> bool:
    """Validate if int is power of four via regex search of string representation of bits

    Args:
        n (int): input integer

    Returns:
        bool: True if n is power of four, else False
    """
    import re
    from types import NoneType

    bits_n = bin(n)[2:]
    if (
        n > 0
        and not isinstance(re.search("^10*$", bits_n), NoneType)
        and (len(bits_n) % 2) == 1
    ):
        return True
    else:
        return False


def regex_tests() -> list[bool]:
    """Regex should only pass strings of the form 1000... for all n

    Returns:
        dict: dictionary with test string, search results, and a pass/fail result
    """
    tests = ["100", "10", "11", "1", "1010", "1011", "1000", "10000"]
    solutions = [True, True, False, True, False, False, True, True]
    test_results = []

    regex = "^10*$"

    for test, solution in zip(tests, solutions):
        search_result_match = re.search(regex, test)
        if isinstance(search_result_match, NoneType):
            search_success = False
            search_result = ""
        else:
            search_success = True
            search_result = search_result_match.group()
        test_results.append(
            {
                "Test String": test,
                "Search Result": search_result,
                "Solution": str(solution),
                "Pass": str(search_success == solution),
            }
        )

    return test_results


# Call regex tests
if __name__ == "__main__":
    regex_test_results = regex_tests()
    for result in regex_test_results:
        for k, v in result.items():
            print(k + ": " + v)
        print("")
