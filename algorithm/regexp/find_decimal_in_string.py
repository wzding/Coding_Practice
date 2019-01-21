"""
字符串转为数字，第一个小数点保留（@#￥￥.89.321）→0.89321
https://stackoverflow.com/questions/4703390/how-to-extract-a-floating-number-from-a-string

>>> import re
>>> re.findall("\d+\.\d+", "Current Level: 13.4 db.")
['13.4']
may suffice.

A more robust version would be:

>>> re.findall(r"[-+]?\d*\.\d+|\d+", "Current Level: -13.2 db or 14.2 or 3")
['-13.2', '14.2', '3']
If you want to validate user input, you could alternatively also check for a float by stepping to it directly:

user_input = "Current Level: 1e100 db"
for token in user_input.split():
    try:
        # if this succeeds, you have your (first) float
        print float(token), "is a float"
    except ValueError:
        print token, "is something else"

# => Would print ...
#
# Current is something else
# Level: is something else
# 1e+100 is a float
# db is something else
"""
import re
def convert_to_decimal(string):
    """
    该function 没有考虑1e100的这种情况
    """
    res = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", string)
    if len(res) == 1:
        return float(res[0])
    for i in range(1, len(res)):
        res[i] = res[i].replace(".", "")
    return float("".join(res))

print(convert_to_decimal('@#￥￥.89.321'))
