from typing import List

def generate_substrings(s: str, k: int) -> List[str]:
    """
    Generate all substrings of a string s with length k.

    Args:
        s: The string.
        k: The length of the substrings.

    Returns:
        A list of all substrings.
    """
    if k == 0:
        return [""]
    else:
        subsequences = []
        for i in range(len(s) - k + 1):
            subsequences.append(s[i:i + k])
        return subsequences


def generate_subsequences(s: str, k: int) -> List[str]:
    """
    Generate all subsequences of a string s with length k.

    Args:
        s: The string.
        k: The length of the subsequences.

    Returns:
        A list of all subsequences.
    """
    if k == 0:
        return [""]
    else:
        subsequences = []
        for i in range(len(s)):
            for subsequence in generate_subsequences(s[i + 1:], k - 1):
                subsequences.append(s[i] + subsequence)
        return subsequences
    
if __name__ == '__main__':
    s = "abc"
    k = 2
    print(generate_subsequences(s, k))