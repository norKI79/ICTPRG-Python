def IsPalindrome(str_x):
    str_x = str_x.lower().replace(" ", "")
    str_backward=""
    for x in range(len(str_x)-1,-1,-1):
        str_backward = str_backward+str_x[x]
    if(str_backward == str_x):
        return True
    else:
        return False


# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("frank") == False))