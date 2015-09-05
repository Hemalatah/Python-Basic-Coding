#REVERSE A STRING
def reverse(string):
	return string[::-1];


#FACTORIAL
def factorial(number):
	result = 1;
	while number > 0:
		result *= number;
		number -= 1;
	return result;

#FIND THE LONGEST WORD IN THE SENTENCE
def longest_word(string):
	my_array = string.split(" ");
	longest_word = "";
	for i in my_array:
		if len(i) > len(longest_word):
			longest_word = i;
	return longest_word;

#FIND THE SUM OF ALL NUMBERS FROM ZERO TO THE NUMBER
def sum_num(num):
	sum = 0;
	while num > 0:
		sum += num;
		num -= 1;
	return sum;
	
#TIME CONVERSION
def time_conversion(number):
	hours = "%02d" %(number/60);
	minutes = "%02d" %(number%60);
	result = hours + ':' + minutes;
	return result;

print(time_conversion(360));

#COUNT VOWELS IN THE STRING
def count_vowels(string):
	vowels = 'aeiou';
	count = 0;
	for i in string:
		if i in vowels:
			count += 1;
	return count;

print(count_vowels('cecilia'));

#CHECK PALINDROME
def palindrome(string):
	if string == string[::-1]:
		return True;
	else:
		return False;

print(palindrome("abcba"));

#CHECK SUM OF ANY TWO ELEMENTS OF AN ARRAY IS ZERO
def two_sum(my_array):
	for i in range(0,len(my_array)):
		for j in range(i+1,len(my_array)):
			add = my_array[i] + my_array[j];
			if add == 0:
				return i,j;
	return 'nil';

my_array = [-1,2,3,4];
print(two_sum(my_array));

#CHECK THE NUMBER IF POWER OF 2
def power_of_two(number):
	while number > 2 and number%2 == 0:
		number = number/2;
	if number == 1 or number == 2:
		return True;
	return False;

print(power_of_two(1));

#FIND THE CHARACTER OCCURS MAXIMUM NUMBER OF TIMES IN THE STRING
def common_letters(string):
	my_dict = {};
	count = 0;
	key = '';
	for i in string:
		values = string.count(i);
		my_dict[i] = values;
	for i in my_dict.keys():
		if my_dict[i] > count:
			key = i;
			count = my_dict[i];
	return key,count;

print common_letters("abbab");

#TITALIZE THE STRING
def capitalize_word(string):
	my_array = string.split(" ");
	i = 0;
	while i < len(my_array):
		my_array[i] = my_array[i].capitalize();
		i += 1;
	new_string = " ".join(my_array);
	return new_string;

print capitalize_word("hi good morning have a nice");

#SCRAMBLE THE STRING
def scramble_string(string,array):
	new_string = "";
	for i in array:
		new_string += string[i];
	new_string = "".join(new_string);
	return new_string;

print scramble_string("markov", [5, 3, 1, 4, 2, 0]);

#CHECK IF THE NUMBER IS PRIME
def is_prime(number):
	if number == 2:
		return True;
	div = 2;
	while div < number:
		if(number%div) == 0:
			return False;
		div += 1;
	return True;

print is_prime(21);

# FIND GCF
def greatest_common_factor(num1, num2):
	div = 2;
	gcf = 1;
	while div <= num1 and div <= num2:
		if num1%div == 0 and num2%div == 0:
			gcf = div;
		div += 1;
	return gcf;

print greatest_common_factor(12,30);

#CEASER-CIPHER ENCRYPTION OF THE STRING
def caesar_cipher(offset,string):
	new_string = '';
	for i in string:
		value = ord(i);
		num = value + offset
		new_string += chr(num);
	return new_string;

print caesar_cipher(3,'abc');

#FIND THE CAHRACTER APPEARS MAXIMUM NUMBER OF TIMES
def num_repeats(string):
	my_dict = {};
	for i in string:
		num = string.count(i);
		my_dict[i] = num;
	repeat = 0;
	for value in my_dict.values():
		if value > repeat:
			repeat = value;
	return repeat;

print(num_repeats('aabbc'));

#FIND THE Nth PRIME NUMBER
def nth_prime(nth):
	n = 2;
	res = 0;
	while res < nth:
		if is_prime(n):
			res += 1;
			number = n;
		n += 1;
	return number;

print nth_prime(5);

#FIND THE THIRD GREATEST ELEMENT IN THE ARRAY
def third_greatest(list):
	for i in range(len(list)-1,0,-1):
		for j in range(i):
			if list[j] < list[j+1]:
				temp = list[j];
				list[j] = list[j+1];
				list[j+1] = temp;
	return list[2];

list = [5,4,3,2,1];
print third_greatest(list);


#FIND THE LONGEST PALINDROME IN THE STRING
def longest_palindrome_in_string(string):
	if string == string[::-1]:
		return True;
s = "abbcdmadambeffe";
longest = "";
for i, item in enumerate(s):
    for j, item in enumerate(s):
        palin = s[j:i+1];
        if longest_palindrome_in_string(palin) and (len(palin) > len(longest)):
            longest = palin;

print longest;

#FIBONACCI SERIES
def fib(n):
 a,b = 1,1;
 for i in range(n-1):
  	a,b = b,a+b;
 return a;

print fib(7);

