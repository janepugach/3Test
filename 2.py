def isPalindrome(s):
    # Используем встроенную функцию
    rev = ''.join(reversed(s))

    # Проверяем строки на равенство
    if (s == rev):
        return True
    return False

s = "malayalam"
ans = isPalindrome(s)
print(s)