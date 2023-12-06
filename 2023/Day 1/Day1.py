# --- Day 1: Trebuchet?! ---
# 
# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.
# 
# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.
# 
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
# 
# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").
# 
# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.
# 
# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
# 
# For example:
# 
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# 
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
# 
# Consider your entire calibration document. What is the sum of all of the calibration values?
# 
# To play, please identify yourself via one of these services:
import re

digit_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", 'nine', 'reserved', '1', '2', '3', '4', '5', '6','7','8','9','0']

def string_to_number(string_to_convert : str ) -> int:
    digits_in_the_string = []

    for char in string_to_convert:
        if char.isdigit():
            digits_in_the_string.append(char)
    
    return int(digits_in_the_string[0] + digits_in_the_string[-1])

def sort_digit_strings(string_to_convert: str) -> list:
    sorted_digits = []
    for d in digit_strings:
        # index_of_digit = string_to_convert.find(d)
        indexes_of_digits = [i.start() for i in re.finditer(d, string_to_convert)]
        for i in indexes_of_digits:
            sorted_digits.append((i, d))
    sorted_digits.sort() 
    return sorted_digits

def convert_string_to_digit_(string_to_convert : str) -> str:
    original_string = string_to_convert
    sorted_digit_strings = sort_digit_strings(string_to_convert)
    for sd in sorted_digit_strings:
        print(sd)
    # for i, s in enumerate(sorted_digit_strings):
    #     string_to_convert = string_to_convert.replace(s[1], str(digit_strings.index(s[1])+1))
    print("Converted {} to {} and it then becomes {}".format(original_string, string_to_convert, string_to_number(string_to_convert)))
    return string_to_convert

def tuple_to_int(int_tuple) -> int:
    ret_int = ''
    for i in int_tuple:
        if digit_strings.index(i) < 9:
            ret_int = ret_int + str(digit_strings.index(i) + 1)
        else:
            ret_int = ret_int +  str(digit_strings.index(i) - 9)
    return int (ret_int)

def main():
    calibration_values = []
    # with open("/home/scarzer/Projects/AdventOfCode/2023/test_input.txt", "r") as f:
    with open("/home/scarzer/Projects/AdventOfCode/2023/day1_input.txt", "r") as f:
        calibration_strings = f.readlines()
        # calibration_strings = map(convert_string_to_digit_, calibration_strings)
        # calibration_digits = map(string_to_number, calibration_strings)
        for c in calibration_strings:
            digits = sort_digit_strings(c)
            val = (digits[0][1], digits[-1][1])
            print(c[0:-1])
            print(digits)
            print(val)
            print(tuple_to_int(val))
            print("====")
            calibration_values.append( tuple_to_int( (val) ) )
        
        print(calibration_values)
             
        print(sum(calibration_values))

if __name__ == "__main__":
    main()