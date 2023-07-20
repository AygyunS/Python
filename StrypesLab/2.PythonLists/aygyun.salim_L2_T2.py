import sys

#Валидиране на входа, когато е със символ "=" между двата стринга
if sys.argv[2] == "=":
    input_str = sys.argv[1] + sys.argv[2] + sys.argv[3]
    s1, s2 = input_str.strip().split("=")
else:
    #Против случай имаме само два стринга
    s1 = sys.argv[1]
    s2 = sys.argv[2]


s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()


if len(s1) != len(s2):
    print("False")
else:
    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            print("False")
            break
    else:
        print("True")
