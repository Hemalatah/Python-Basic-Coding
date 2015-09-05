print "Hello World!"

#COMBINE TWO SORTED ARRAY IN THE SORTED FORM
def combine_arrays(arr1,arr2):
	new_arr = [];
	i = 0;
	j = 0;
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			new_arr.append(arr1[i]);
			i += 1;
		else:
			new_arr.append(arr2[j]);
			j += 1;
	while i < len(arr1):
		new_arr.append(arr1[i]);
		i += 1;
	while j < len(arr2):
		new_arr.append(arr2[j]);
		j += 1;
	return new_arr;

print combine_arrays([1, 3, 5], [2, 4, 6]);


#FIND THE HIGHEST CUMULATIVE DIFFERENCE IN THE ARRAY
def retrieve(arr,i,j):
	new_arr = [];
	while i <= j:
		new_arr.append(arr[i]);
		i += 1;
	return new_arr;


def sum(arr):
	i = 0;
	res = 0;
	while i < len(arr):
		res += arr[i];
		i += 1;
	return res;

def res_arr(arr1,arr2):
	res = [];
	length = len(arr2)-1;
	i = arr1.index(arr2[0]);
	res.append(i);
	j = arr1.index(arr2[length]);
	res.append(j);
	return res;
print res_arr([100, -101, 200, -3, 1000],[200,-3,1000]);

def puppy_golden_age(arr):
	largest = 0;
	
	i = 0;
	j = 0;
	while i < len(arr):
		j = 0;
		while j < len(arr):
			if i != j:				
				value_arr = retrieve(arr,i,j);
				value = sum(value_arr);
				if value > largest:
					largest = value;
					new_arr = value_arr;

					
			j += 1;
		i += 1;
	return res_arr(arr,new_arr);
	

print puppy_golden_age([100, -101, 200, -3, 1000]);

#FIND THE SUBSETS OF THE GIVEN SET
def subset(arr):
	i = 0;
	j = 0;
	new_arr = [[]];
	for ele in arr:
		new_arr.append([ele]);

	while i < len(arr):
		while j < len(arr):
			if i < j:
				res = retrieve(arr,i,j);
				new_arr.append(res);
			j += 1;
		i += 1;
	return new_arr;

print subset(["a", "b", "c"]);

