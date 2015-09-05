#RUNLENGTH OF THE STRING
def runlength(string):
	i = 0;
	output = [];
	while i < len(string):
		value = 1;
		while string[i] == string[i+1]:
			value += 1;
			i += 1;
        output.append(value);
        output.append(string[i]);
        i += 1;
	output = "".join(output);
	return output;

print runlength("aabbcde");

#PALINDROME OF THE CHARACTER IN THE STRING
def palindrome_two(string):
	string = string.lower();
	new_string = '';
	for i in string:
		if i in 'abcdefghijklmnopqrstuvwxyz':
			new_string += i;
	if new_string == new_string[::-1]:
		return True;
	else:
		return False;

print palindrome_two("Anne, I vote more cars race Rome-to-Vienna");

#FIND THE ARITHMETIC PROGRESSION
def arithmetic(array):
	i = 0;
	if len(array) > 2:
		num1 = array[0] - array[1];
		num2 = num1;
	while i+1 < len(array) and num1 == num2:
		num2 = array[i] - array[i+1];
		i += 1;
	if num1 == num2:
		return True;
	else:
		return False;

print arithmetic([1,2,3,4]);

#FIND THE GEOMETRIC PROGRESSION
def geometric(array):
	i = 0;
	if len(array) > 2:
		num1 = array[1]/array[0];
		num2 = num1;
	while i+1 < len(array) and num1 == num2:
		num2 = array[i+1]/array[i];
		i += 1;
	if num1 == num2:
		return True;
	else:
		return False;

print geometric([2, 6, 18, 53]);

#CHECK WHETHER THE ARRAY IS AP OR GP
def arith_geo(array):
	if arithmetic(array):
		return "Arithmetic";
	elif geometric(array):
		return "Geometric";
	else:
		return "-1";

print arith_geo([2,4,3,5]);

#ARRAY ADDITION
def greatest(list):
	for i in range(len(list)-1,0,-1):
		for j in range(i):
			if list[j] < list[j+1]:
				temp = list[j];
				list[j] = list[j+1];
				list[j+1] = temp;
	return list[0];

def array_addition(array):
	num = greatest(array);
	array.remove(num);
	array.sort();
	res = 0;
	for i in range(len(array)-1,0,-1):
		for j in range(i):
			res += j;
		if res == num:
			return True;
	return False;

print array_addition([4, 6, 23, 10, 1, 3]);

#NEAREST MAXIMUM INTEGER WITH RESPECT TO THE INDEX POSITION
def nearest_interger(array,idx):
	i = idx;
	j  = 0;
	while i < len(array)-1:
		if array[i+1] > array[idx]:
			j = i+1;
			return j;
		i += 1;
	return 'nil';


print(nearest_interger([2,4,3,1],1));


#REMOVE THE YEAR WITH REPITITIVE DIGITS
def repeat(year):
	year = str(year);
	i = 0;
	while i < len(year):
		if year.count(year[i]) > 1:
			return False;
		i += 1;
	return True;

def no_repeat(year1,year2):
	new_list = [];
	for i in range(year1,year2 + 1):
		if repeat(i):
			new_list.append(i);
	return new_list;

print(no_repeat(1984,1984));

#COUNT THE NUMBER OF OCCURENCE OF CHARACTER IN THE STRING
def letter_count(string):
	string = string.lower();
	dic = {};
	i = 0;
	while i < len(string):
		count = string.count(string[i]);
		dic[string[i]] = count;
		i += 1;
	for i in dic.keys():
		print(i + " => " + str(dic[i]));

letter_count('Hehmaa');

#MORSE CODE OF THE STRING
def morse_code(word):
	dic = {
	'c' : '-.-.',
	'a' : '.-',
	't' : '-'
	};
	i = 0;
	new_string = '';
	while i < len(word):
		letter = word[i];
		if i < len(word)-1:
			new_string += dic[letter] + ' ';
		else:
			new_string += dic[letter];
		i += 1;
	return new_string;

print morse_code('cat');


#SORT THE STRING
def sort_string(string):
	string = ' '.join(string);
	string = string.split(' ');
	string.sort();
	string = ''.join(string);
	return string;

print sort_string('hema');

#FIND THE ACRONYM OF THE STRING
def word_unscramble(inn,array):
	inn = sort_string(inn);
	i = 0;
	new_list = [];
	while i < len(array):
		elm = sort_string(array[i]);
		if inn == elm:
			new_list.append(array[i]);
		i += 1;
	return new_list;

print(word_unscramble("cat", ["tic", "toc", "tac", "toe"]));

#BUBBLE SORT
def bubble_sort(array):
	for i in range(len(array)-1,0,-1):
		for j in range(i):
			if array[i] < array[j]:
				temp = array[j];
				array[j] = array[i];
				array[i] = temp;
	return array;

print bubble_sort([5,4,3,2]);

#TOWER OF HANOI
def hanoi(n,src,dest,thro):
	if n > 0:
		hanoi(n-1,src,thro,dest);
		dest.append(src.pop());
		hanoi(n-1,thro,dest,src);
	return dest

src = [4,3,2,1];
thro = [];
dest = [];
n = len(src)
print hanoi(n,src,dest,thro);

#TRANSPOSE THE MATRIX
def my_transpose(arr):
	for i in range(0,len(arr)):
		for j in range(0,len(arr[0])):
			if i < j:
				arr[i][j],arr[j][i] = arr[j][i],arr[i][j];
	return arr

print my_transpose([[0, 1, 2],[3, 4, 5],[6, 7, 8]]);

#MULTIPLY THE ARRAY ELEMENT BY TWO
def multiply(arr):
	for i in range(0,len(arr)):
		arr[i] = arr[i]*2
	return arr

print multiply([1,3,4]);

#FIND THE MEDIAN OF THE ARRAY
def median(arr):
	arr.sort()
	length = len(arr)
	if length%2 == 0:
		value = (arr[length/2]+arr[(length/2)-1])/2;
	else:
		value = arr[length/2];
	return value;

print median([4,3,2]);

#CONCATENATE THE ARRAY ELEMENT
def concatenate(arr):
	res = '';
	for i in arr:
		res += i;
	return res;

print concatenate(["Yay ", "for ", "strings!"]);

#SET AND REMOVE THE VALUE TO THE DICTIONARY KEY
def set_add_el(dic,key):
	if dic == {}:
		dic[key] = True;
	return dic;

print set_add_el({'x' : True},'x');

def set_remove_el(dic,key):
	if dic.has_key(key):
		del dic[key];
	return dic
print set_remove_el({'x' : True,'y':False},'x');

def set_list_els(dic):
	return dic.keys();

print set_list_els({'x' : True,'y':False,'t':False});

def set_member(dic,key):
	if dic.has_key(key):
		return True;
	else:
		return False;

print set_member({'x' : True,'y':False},'c');

#UNION OF TWO DICTIONARY
def set_union(dic1,dic2):
	for key in dic2:
		dic1[key] = dic2[key];
	return dic1;

print set_union({'x' : True,'y':False},{'t':False});

#INTERSECTION OF TWO DICTIONARY
def set_intersection(dic1,dic2):
	for key in dic2:
		if not dic1.has_key(key):
			dic1[key] = dic2[key];
	return dic1;

print set_intersection({'x' : True,'y':False,'t':False},{'t':False,'j':True});

#FIZZBUZZ
def fizzbuzz():
	for i in range(0,101):
		if i%3 == 0 and i%5 == 0:
			print "FIZZBUZZ";
		elif i%3 == 0:
			print "FIZZ";
		elif i%5 == 0:
			print "BUZZ";
		else:
			print i;

print fizzbuzz();

#FIND THE UNIQUE ITEMS IN THE ARRAY
def unique_items(arr):
    i = 0;
    new_arr = [];
    while i < len(arr):
        if arr.count(arr[i]) == 1:
            new_arr.append(arr[i]);   
        i += 1;
    return new_arr;
print unique_items([1, 5, 5, 7, 'sixtyten', 'orange', 1, 'orange']);


#FIND NUMBER OF CATS WITH HAT
def cat_hat(cats):
    arr = [];
    for i in range(1,cats+1,1):
        arr.append(i);
    i = 1;
    j = 1;
    res_array = [];
    while j < len(arr): 
        while i < len(arr):
            if i in res_array:
                res_array.pop(i);
            else:
                res_array.append(i);
            i += j;
        j += 1;
    return res_array;
     
print(cat_hat(100));

