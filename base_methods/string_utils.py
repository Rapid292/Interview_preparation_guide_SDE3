def is_palindrome(s):
    """
    Check if a string is a palindrome.

    Examples:
        >>> is_palindrome("madam")
        True
        >>> is_palindrome("hello")
        False
    """
    return s == s[::-1]

def reverse_string(s):
    """
    Reverse a given string.

    Examples:
        >>> reverse_string("hello")
        "olleh"
        >>> reverse_string("")
        ""
    """
    return s[::-1]
