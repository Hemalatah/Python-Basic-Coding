#CRAZY NUMBERS
def crazy_sum(numbers):
	i = 0;
	sum = 0;
	while i < len(numbers):
		product = numbers[i] * i;
		sum += product;
		i += 1;
	return sum;
numbers = [2,3,5];
print crazy_sum(numbers);

#FIND THE NUMBER OF PERFECT SQUARES BELOW THIS NUMBER
def square_nums(max):
	num = 1;
	count = 0;
	while num < max:
		product = num * num;
		if product < max:
			count += 1;
		num += 1;
	return count;

print square_nums(25);

#PRINTS OUT THE ELEMENT IN THE ARRAY WHICH IS EITHER DIVISIBLE BY 3 OR 5
def crazy_nums(max):
	i = 1;
	list = [];
	new_list = [];
	while i < max:
		list.append(i);
		i += 1;
	for i in list:
		if i % 3 == 0 and i % 5 == 0:
			continue;
		elif i % 3 == 0 or i % 5 == 0:
			new_list.append(i);
		else:
			continue;
	return new_list;

print crazy_nums(3);

#PRINTS OUT THE SUM OF ANY THREE NUMBERS IN THE ARRAY WHICH IS EQUAL TO SEVEN
def lucky_sevens(numbers):
	i = 0;
	Bool = False;
	if len(numbers) <= 1:
		print("Length of numbers should be atleast 2");
	while i + 2 < len(numbers):
		sum = numbers[i] + numbers[i+1] + numbers[i+2];
		if sum == 7:
			Bool = True;
		i += 1;
	return Bool;

numbers = [1,2,3,4,5];
print(lucky_sevens(numbers));

numbers = [2,1,5,1,0];
print(lucky_sevens(numbers));

numbers = [0,-2,1,8];
print(lucky_sevens(numbers));

numbers = [7,7,7,7];
print(lucky_sevens(numbers));

numbers = [3,4,3,4];
print(lucky_sevens(numbers));

#FIND THE NUMBER OF ODD ELEMENTS IN THE ARRAY
def oddball_sum(numbers):
	i = 0;
	sum = 0;
	while i < len(numbers):
		if (numbers[i]%2) != 0:
			sum = sum + numbers[i];
		i += 1;
	return sum;

numbers = [1,2,3,4,5];
print(oddball_sum(numbers));

numbers = [0,6,4,4];
print(oddball_sum(numbers));

numbers = [1,2,1];
print(oddball_sum(numbers));

#REMOVES VOWEL FROM THE STRING
def disemvowel(string):
	vowel = 'aeiou';
	i = 0;
	while i < len(string):
		if string[i] in vowel:
			string = string.replace(string[i],"");
		else:
			i += 1;
	return string;

string = "foobar";
print(disemvowel(string));
print(disemvowel("ruby"));
print(disemvowel("aeiou"));


#DASHERIZE THE NUMBER
def odd(intput):
	if (intput%2):
		return True;
	else:
		return False;

def dasherize_number(number):
	s = str(number);
	new_list = [];
	i = 0;
	while i < len(s):
		if odd(int(s[i])):
			if i == 0:
				new_list.append(s[i]);
				new_list.append('-');
			elif i == len(s)-1:
				new_list.append('-');
				new_list.append(s[i]);	
			elif odd(int(s[i-1])): 
				new_list.append(s[i]);
				new_list.append('-');
			else:
				new_list.append('-');
				new_list.append(s[i]);
				new_list.append('-');
		else:
			new_list.append(s[i]);
		i += 1;
	new_list = "".join(new_list);
	return new_list;
	
print dasherize_number(3243);








