def isPalindrome(s: str) -> bool:
    str_alnu = ""
    for str in s:
        if str.isalnum():
            str_alnu += str
    str_alnu = str_alnu.lower()
    str_alnu_reversed = "".join(reversed(str_alnu))
    return str_alnu == str_alnu_reversed

stra = "1A man, a plan, a canal: Panama1"
print(isPalindrome(s=stra))


