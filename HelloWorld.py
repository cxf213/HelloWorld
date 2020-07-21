print("HelloWorld")
def isPalindrome(x: int) -> bool: #回文数判断
        original_num=x
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        if (reversed_num==original_num):
            return True
        else:
            return False

print(isPalindrome(121))