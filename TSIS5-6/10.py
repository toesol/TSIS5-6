import re
def TM(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return 'Not matched!'
a = input()
print(TM(a))