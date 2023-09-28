#! /bin/python3


#for line in file:
#    serch for "|"
#
#get_row()
#get_column()
#if needle found
#    count + 1

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def log_char_position(file_name, target_char):
	position_log = []
	try:
		with open(file_name, "r") as file:
			row, column = 1, 1
			for line in file:
				for char in line:
					if char == target_char:
						position = (row, column)
						position_log.append( position )
					if char == '\n':
						row += 1
						column = 1
					else:
						column += 1
		return position_log
	except FileNotFoundError:
		print(f"File '{file_name}' not found.")
		return None

def haystack_plot(in_file, out_file):
    x = []
    y = []
    position_log = log_char_position(in_file, "|")
    for p in position_log:
        # p is a tuple with x and y coordinates
        x.append(p[0])
        y.append(p[1])
    plt.scatter(x, y, label = "needles")
    plt.xlabel("column")
    plt.ylabel("row")
    plt.savefig(out_file)
    return

if __name__ == '__main__':
    #outfile should be .png file.
    out_file = "needle_plot.png"
    in_file = "haystack.txt"
    haystack_plot(in_file, out_file)
    #needle_list = log_char_position("haystack.txt", "|")
    #num_needles = len(needle_list)
    #print(needle_list)
    #print(num_needles)


