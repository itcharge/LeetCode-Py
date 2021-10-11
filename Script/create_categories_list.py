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
#	frame = frame.sort_values(by='题号')
	frame = frame.reset_index(drop=True)
	for i in range(H):
		lines += ["| {} | {} | {} | {} | {} |".format(frame.at[i, '题号'], frame.at[i, '标题'], frame.at[i, '题解'], frame.at[i, '标签'], frame.at[i, '难度'])]
	table = '\n'.join(lines)
	return table


def create_categories_list(solotions_path, input_path, output_path):
	f = open(input_path)
	lines = f.readlines()
	category_h2 = None
	category_h3 = None
	category_h4 = None
	category_h6 = None
	category_h3_file_path = None
	category_h3_file_content = ""
	
	for i in range(len(lines)):
		pattern = re.compile(r'(#{2,6}) (.*)')
		match = pattern.match(lines[i])
		if match:
			title_size, title_content =  match.group(1,2)
			if title_size == "##":
				category_h2 = title_content
			elif title_size == "###":
				if category_h3 and category_h3_file_path and category_h3_file_content:
#					print(category_h3_file_content)
					with open(category_h3_file_path, 'w') as fi:
						fi.write(category_h3_file_content)
					fi.close()
					category_h3 = None
					category_h3_file_path = None
					category_h3_file_content = ""
				pattern1 = re.compile(r'\[(.*)\]\((.*)\)')
				match1 = pattern1.match(title_content)
				if match1:
					category_h3, category_h3_file_path = match1.group(1,2)
					category_h3_file_content += "### " + category_h3 + "\n\n"
			elif title_size == "####":
				category_h4 = title_content
				category_h3_file_content += "#### " + category_h4 + "\n\n"
			elif title_size == "######":
				category_h6 = title_content
				problem_ids = title_content.split('、')
				if not problem_ids:
					continue
				
				frame = pd.DataFrame(columns=['题号', '标题', '题解', '标签', '难度'])
				frame_cout = 0
				for problem_id in problem_ids:
					problem_id_path = solotions_path + "/" + problem_id + ".md"
					res = get_problem_id_row(problem_id_path, problem_id)
					if res:
						frame.loc[frame_cout] = res
						frame_cout += 1
				table = gen_markdown_table(frame)
				category_h3_file_content += table + "\n\n"
	
	if category_h3 and category_h3_file_path and category_h3_file_content:
		with open(category_h3_file_path, 'w') as fi:
			fi.write(category_h3_file_content)
		fi.close()
				
				
					
def get_problem_id_row(problem_id_path, problem_id):
	title_id = None
	title_offer_id = None
	title_offer_id1 = None
	title_offer_id2 = None
	title_name = None
	title_solution_url = None
	title_url = None
	title_label = None
	title_diff = None
	res = None
	
	if not os.path.exists(problem_id_path):
		title_offer_id = ""
		pattern_1 = re.compile(r'剑指 Offer ([0-9]\d*|0)+( - [I]*)*\. (.*)')
		pattern_2 = re.compile(r'剑指 Offer II ([0-9]\d*|0)+\. (.*)')
		pattern_3 = re.compile(r'面试题 ([0-9]\d*|0)+\.+([0-9]\d*|0)+\. (.*)')
		pattern_4 = re.compile(r'([0-9]\d*|0)+\. (.*)')
		
		if re.search(pattern_1, problem_id):
			match_1 = pattern_1.finditer(problem_id)
			for a in match_1:
				title_offer_id1, title_offer_id2, title_name = a.group(1,2,3)
				if title_offer_id2:
					title_offer_id = "剑指 Offer " + title_offer_id1 + title_offer_id2
				else:
					title_offer_id = "剑指 Offer " + title_offer_id1
		elif re.search(pattern_2, problem_id):
			match_2 = pattern_2.finditer(problem_id)
			for a in match_2: 
				title_offer_id1, title_name = a.group(1,2)
				title_offer_id = "剑指 Offer II " + title_offer_id1
		elif re.search(pattern_3, problem_id):
			match_3 = pattern_3.finditer(problem_id)
			for a in match_3:
				title_offer_id1, title_offer_id2, title_name = a.group(1,2,3)
				title_offer_id = "面试题 " + title_offer_id1 + "." + title_offer_id2
		elif re.search(pattern_4, problem_id):
			match_4 = pattern_4.finditer(problem_id)
			for a in match_4:
				title_offer_id, title_name = a.group(1,2)
		
		title_chinese = " "
		title_solution_url = " "
		title_name_url = title_name
		title_label = " "
		title_diff = " "
		res = [title_offer_id, title_name_url, title_solution_url, title_label, title_diff]
		return res
	
	f = open(problem_id_path)
	lines = f.readlines()
	for i in range(len(lines)):
		if i == 0:
			pattern_1 = re.compile(r'\[剑指 Offer ([0-9]\d*|0)+( - [I]*)*\. (.*)\]\((.*)\)')
			pattern_2 = re.compile(r'\[剑指 Offer II ([0-9]\d*|0)+\. (.*)\]\((.*)\)')
			pattern_3 = re.compile(r'\[面试题 ([0-9]\d*|0)+\.+([0-9]\d*|0)+\. (.*)\]\((.*)\)')
			pattern_4 = re.compile(r'\[([0-9]\d*|0)+\. (.*)\]\((.*)\)')
			if re.search(pattern_1, lines[i]):
				match_1 = pattern_1.finditer(lines[i])
				for a in match_1:
					title_offer_id1, title_offer_id2, title_name, title_url = a.group(1,2,3,4)
					if title_offer_id2:
						title_offer_id = "剑指 Offer " + title_offer_id1 + title_offer_id2
					else:
						title_offer_id = "剑指 Offer " + title_offer_id1
			elif re.search(pattern_2, lines[i]):
				match_2 = pattern_2.finditer(lines[i])
				for a in match_2: 
					title_offer_id1, title_name, title_url = a.group(1,2,3)
					title_offer_id = "剑指 Offer II " + title_offer_id1
			elif re.search(pattern_3, lines[i]):
				match_3 = pattern_3.finditer(lines[i])
				for a in match_3:
					title_offer_id1, title_offer_id2, title_name, title_url = a.group(1,2,3,4)
					title_offer_id = "面试题 " + title_offer_id1 + "." + title_offer_id2
			else:
				match_4 = pattern_4.finditer(lines[i])
				for a in match_4:
					title_id, title_name, title_url = a.group(1,2,3)
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
		
	if title_offer_id and title_name and title_url and title_label and title_diff:					
		title_chinese = quote(title_offer_id + ". " + title_name + ".md")
		title_solution_url = "[Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/" + title_chinese + ")"
		title_name_url = "[" + title_name + "](" + title_url + ")"
		
		res = [title_offer_id, title_name_url, title_solution_url, title_label, title_diff]
	elif title_id and title_name and title_url and title_label and title_diff:
		title_id = "{:0>4d}".format(int(title_id))
		title_chinese = quote(title_id + ". " + title_name + ".md")
		title_solution_url = "[Python](https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/" + title_chinese + ")"
		title_name_url = "[" + title_name + "](" + title_url + ")"

		res = [title_id, title_name_url, title_solution_url, title_label, title_diff]
	else:
		title_id = problem_id
		title_chinese = " "
		title_solution_url = " "
		title_name_url = " "
		title_label = " "
		title_diff = " "
		res = [title_id, title_name_url, title_solution_url, title_label, title_diff]
	f.close()
	return res
	
def merge_file(list_path, readme_head_path, readme_path, solutions_count):
	readme_head_file = open(readme_head_path)
	list_file = open(list_path)
	readme_file = open(readme_path,'w')
	
	for line in readme_head_file:
		readme_file.writelines(line)
#	readme_file.writelines("# LeetCode 题解（已完成 {} 道）\n ".format(solutions_count))
	
	for line in list_file:
		readme_file.writelines(line)
	
	readme_head_file.close()
	list_file.close()
	readme_file.close()

solotions_path = '../Solutions'
input_path = '../Contents/Assets/Categories-Origin-List.md'
output_path = '../Contents/Chapter-01/05-Categories-List.md'
readme_head_path = '../Contents/index.md'
readme_path = '../README.md'

#frame_cout = create_list(solotions_path, output_path) 
#merge_file(list_path, readme_head_path, readme_path, frame_cout)

create_categories_list(solotions_path, input_path, output_path)