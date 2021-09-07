import os
import re
import numpy as np
import pandas as pd
from urllib.parse import quote

def gen_markdown_table(frame):
	
	ELEMENT = " {} |"
	
	H = frame.shape[0]
	W = frame.shape[1]
	
	LINE = "|" + ELEMENT * W
	
	head_name = ["题号", "标题", "题解", "标签", "难度"]
	
	lines = []
	
	## 表头部分
	lines += ["| {} | {} | {} | {} | {} |".format(head_name[0], head_name[1], head_name[2], head_name[3], head_name[4])]

	## 分割线
	SPLIT = ":{}"
	line = "|"
	for i in range(W):
		line = "{} {} |".format(line, SPLIT.format('-'*6))
	lines += [line]
	
	## 数据部分
	frame = frame.sort_values(by='题号')
	frame = frame.reset_index(drop=True)
	for i in range(H):
		lines += ["| {} | {} | {} | {} | {} |".format(frame.at[i, '题号'], frame.at[i, '标题'], frame.at[i, '题解'], frame.at[i, '标签'], frame.at[i, '难度'])]
	table = '\n'.join(lines)
	return table

def create_list(solotions_path, output_path):
	files =  os.listdir(solotions_path)
	frame = pd.DataFrame(columns=['题号', '标题', '题解', '标签', '难度'])
	frame_cout = 0
	for file in files:
		if not os.path.isdir(file) and ".md" in file: #判断是否是文件夹   
			f = open(solotions_path + "/" + file)
			
			lines = f.readlines()
			title_id = None
			title_offer_id = None
			title_offer_id1 = None
			title_offer_id2 = None
			title_name = None
			title_solution_url = None
			title_url = None
			title_label = None
			title_diff = None
			
			for i in range(len(lines)):
				if i == 0:
					pattern = re.compile(r'\[([0-9]\d*|0)+\. (.*)\]\((.*)\)')
					match = pattern.finditer(lines[i])
					pattern_1 = re.compile(r'\[(剑指 Offer [0-9]\d*|0)+(- [I]*)*\. (.*)\]\((.*)\)')
					match_1 = pattern_1.finditer(lines[i])
					if match:
						for a in match:
							title_id, title_name, title_url = a.group(1,2,3)
					if match_1:
						for a in match_1:
							title_offer_id1, title_offer_id2, title_name, title_url = a.group(1,2,3,4)
				elif "标签" in lines[i]:
					pattern = re.compile(r'- 标签：(.*)')
					match = pattern.finditer(lines[i])
					for a in match:
						title_label = a.group(1)
				elif "难度" in lines[i]:
					pattern = re.compile(r'- 难度：(.*)')
					match = pattern.finditer(lines[i])
					for a in match:
						title_diff = a.group(1)
			if not title_diff:
				title_diff = "简单"
			if not title_label:
				title_label = " "
			if title_id and title_name and title_url and title_label and title_diff:
				title_id = "{:0>4d}".format(int(title_id))
				title_chinese = quote(title_id + ". " + title_name + ".md")
				title_solution_url = "[Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/" + title_chinese + ")"
				title_name_url = "[" + title_name + "](" + title_url + ")"
				
				frame.loc[frame_cout] = [title_id, title_name_url, title_solution_url, title_label, title_diff]
				frame_cout += 1
#				print(title_id, title_name_url, title_url, title_label, title_diff, title_solution_url)	
			if title_offer_id1 and title_offer_id2 and title_name and title_url and title_label and title_diff:
				title_offer_id = title_offer_id1 + title_offer_id2
				title_chinese = quote(title_offer_id + ". " + title_name + ".md")
				title_solution_url = "[Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/" + title_chinese + ")"
				title_name_url = "[" + title_name + "](" + title_url + ")"
				
				frame.loc[frame_cout] = [title_offer_id, title_name_url, title_solution_url, title_label, title_diff]
				frame_cout += 1
				print(title_offer_id, title_name_url, title_url, title_label, title_diff, title_solution_url)	
				
			f.close()
		
	table = gen_markdown_table(frame)
	with open(output_path, 'w') as f:
		f.write(table)
	f.close()
	print("Create success")
	return frame_cout

def merge_file(list_path, readme_head_path, readme_path, solutions_count):
	readme_head_file = open(readme_head_path)
	list_file = open(list_path)
	readme_file = open(readme_path,'w')
	
	for line in readme_head_file:
		readme_file.writelines(line)
	readme_file.writelines("# 3. LeetCode 题解（已完成 {} 道）\n ".format(solutions_count))
	
	for line in list_file:
		readme_file.writelines(line)
	
	readme_head_file.close()
	list_file.close()
	readme_file.close()

solotions_path = '../Solutions'
list_path = './README_LIST.md'
readme_head_path = './README_HEAD.md'
readme_path = '../README.md'

frame_cout = create_list(solotions_path, list_path) 
merge_file(list_path, readme_head_path, readme_path, frame_cout)

