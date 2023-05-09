# import module for regular expression
import re

# create pattern 666-666-6666
phone_number_regex = re.compile(pattern=r'(\d{3})-\d{3}-\d{4}')

# 1 number
# 1 hyphen
# 3 numbers
# 1 hyphen
# 4 numbers