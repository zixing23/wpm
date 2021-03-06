import sys
"""这是"trans_list.py"模块，提供了一个名为print_lol()的函数，这个函数的功能是打印列表，其中包含（可能不包含）嵌套列表。"""
def print_lol(the_list,indent=False,level=0,fh=sys.stdout):
	"""这个函数取一个位置参数，名为"the_list"，indent默认为False，表示不缩进，如果需要缩进请加参数True.level是可选变量，默认是0，根据嵌套列表向内缩进；这可以是任何python列表（也可能是包含嵌套列表的列表）。所指定的列表中的每个数据项会（递归地）输出到屏幕上，各数据项各占一行。"""
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item,indent,level+1,fh)
		else:
			if indent:
				for tab_stop in range(level):
					print('\t',end='',file=fh)
			print(each_item,file=fh)