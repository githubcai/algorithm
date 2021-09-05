
import random
import time

def gen_data(cnt, st, ed):
	data = []
	for _ in range(cnt):
		data.append(random.randint(st, ed))
	return data

def cal_time(func):
	def wrapper(*args, **kwargs):
		st = time.time()
		res = func(*args, **kwargs)
		ed = time.time()
		print("cost time: ", ed-st)
		return res
	return wrapper

# ----------------------------------------------------------

@cal_time
def func1(data):
	res = st = ed = None
	for t_st in range(len(data)):
		t_sum = 0
		for t_ed in range(t_st, len(data)):
			t_sum += data[t_ed]
			if res is None or res < t_sum:
				res = t_sum
				st = t_st
				ed = t_ed
	return st, ed, res

# ----------------------------------------------------------

def find_max_crossing_subarray(data, low, mid, high):
	left_sum = left_idx = None
	tmp_sum = 0
	for i in range(mid, low-1, -1):
		tmp_sum += data[i]
		if left_sum is None or left_sum < tmp_sum:
			left_sum = tmp_sum
			left_idx = i
	right_sum = right_idx = None
	tmp_sum = 0
	for i in range(mid+1, high+1):
		tmp_sum += data[i]
		if right_sum is None or right_sum < tmp_sum:
			right_sum = tmp_sum
			right_idx = i
	return left_idx, right_idx, left_sum+right_sum

def find_maximum_subarray(data, low, high):
	if high == low:
		return low, high, data[low]
	mid = int((low+high)/2)
	left_low, left_high, left_sum = find_maximum_subarray(data, low, mid)
	right_low, right_high, right_sum = find_maximum_subarray(data, mid+1, high)
	cross_low, cross_high, cross_sum = find_max_crossing_subarray(data, low, mid, high)
	if left_sum >= right_sum and left_sum >= cross_sum:
		return left_low, left_high, left_sum
	if right_sum >= left_sum and right_sum >= cross_sum:
		return right_low, right_high, right_sum
	return cross_low, cross_high, cross_sum

@cal_time
def func2(data):
	return find_maximum_subarray(data, 0, len(data)-1)

# ----------------------------------------------------------

@cal_time
def func3(data):
	res = st = ed = None
	right_max = right_max_st = right_max_ed = None
	for idx in range(len(data)):
		if res is None:
			res = right_max = data[idx]
			st = ed = right_max_st = right_max_ed = idx
			continue
		right_max += data[idx]
		right_max_ed = idx
		if data[idx] > right_max:
			right_max = data[idx]
			right_max_st = right_max_ed = idx
		if right_max > res:
			res = right_max
			st = right_max_st
			ed = right_max_ed
	return st, ed, res

# ----------------------------------------------------------


if __name__ == "__main__":
	cnt, st, ed = 10000, -10, 10
	data = gen_data(cnt, st, ed)
	print(data)
	st, ed, res = func1(data)
	print(st, ed, res)
	st, ed, res = func2(data)
	print(st, ed, res)
	st, ed, res = func3(data)
	print(st, ed, res)
