import os, re
from pathlib import Path
import pandas as pd
from urllib.parse import quote

# 根据 frame 生成 Markdown 表格
def gen_markdown_table(frame, need_sort):
    
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
    if need_sort:
        frame = frame.sort_values(by='题号')
    frame = frame.reset_index(drop=True)
    for i in range(H):
        lines += ["| {} | {} | {} | {} | {} |".format(frame.at[i, '题号'], frame.at[i, '标题'], frame.at[i, '题解'], frame.at[i, '标签'], frame.at[i, '难度'])]
    table = '\n'.join(lines)
    return table

# 根据题解目录 solutions_path 自动生成题解列表，并保存到 output_path 中
def gen_solutions_list(solutions_path, solotions_output_path):
    files = os.listdir(solutions_path)
    frame = pd.DataFrame(columns=['题号', '标题', '题解', '标签', '难度'])
    frame_cout = 0
    
    df = pd.read_csv("leetcode-problems.csv")
    
    for file in files:
        # 判断是否是文件夹
        if ".md" not in file:
            continue
        
        # 获取题目所在行
        df_indexs = df[df['标题'] == Path(file).stem].index.tolist()
        
        if not df_indexs:
            print('%s 没有出现在 leetcode-problems.csv 中' % (Path(file).stem))
            continue
        row = df_indexs[0]
        
        problem_id = df.loc[row, "序号"]
        problem_catalog = df.loc[row, "所在目录"]
        problem_title = df.loc[row, "标题"]
        problem_title_slug = df.loc[row, "标题末尾"]
        problem_link = "[" + problem_title_slug + "](" + df.loc[row, "标题链接"] + ")"
        problem_link_slug = df.loc[row, "标题链接末尾路径"]
        problem_solution_path = os.path.join(solutions_path, problem_title + ".md")
        if os.path.exists(problem_solution_path):
            problem_solution_link = "[Python](" + df.loc[row, "github 题解链接"] + ")"
        else:
            problem_solution_link = ""
        problem_label = df.loc[row, "标签"]
        problem_difficulty = df.loc[row, "难度"]
        res = [problem_id, problem_link, problem_solution_link, problem_label, problem_difficulty]
        frame.loc[frame_cout] = res
        frame_cout += 1
        
    table = gen_markdown_table(frame, True)
    with open(solotions_output_path, 'w') as f:
        f.writelines("# LeetCode 题解（已完成 {} 道）\n\n".format(frame_cout))
        f.write(table)
    f.close()
    print("Create Solutions List Success")
    return frame_cout


# 将 readme_head、list 合并到，自动生成 README.md 并保存到 readme_path 中
def merge_readme_file(solotions_output_path, readme_head_path, readme_catalogue_list_path, content_index_path, readme_path, solutions_count):
    
    # 生成项目 README.md 文件
    readme_file = open(readme_path,'w')
    
    # 将 README 开头部分写入 README.md 中
    readme_head_file = open(readme_head_path)
    readme_file.writelines(readme_head_file.readlines())
    readme_head_file.close()
    
    # 将章节目录写入 README.md 中
    readme_catelogue_list_file = open(readme_catalogue_list_path)
    readme_catelogue_list_lines = readme_catelogue_list_file.readlines()
    for readme_catelogue_list_line in readme_catelogue_list_lines:
        readme_catelogue_list_line = readme_catelogue_list_line.replace('https://github.com/itcharge/LeetCode-Py/blob/main', '.')
        readme_file.write(readme_catelogue_list_line)
    readme_catelogue_list_file.close()
    
    # 将题解标题写入 readme 文件
    catalogue_list_file = open(solotions_output_path)
    catalogue_list_lines = catalogue_list_file.readlines()
    if len(catalogue_list_lines) > 0:
        catalogue_list_title = catalogue_list_lines[0].strip('\n')
        catalogue_list_title = '## [' + catalogue_list_title + '](./Contents/00.Introduction/04.Solutions-List.md)'
        catalogue_list_title = catalogue_list_title.replace('# LeetCode 题解', '12. LeetCode 题解')
        readme_file.writelines(catalogue_list_title)
    catalogue_list_file.close()
    
    readme_file.close()
    
    
    # 生成 Contents/index.md 文件
    content_index_file = open(content_index_path, 'w')
    content_index_file.writelines("# 算法通关手册（LeetCode）\n\n")
    
    # 将章节目录写入 Contents/index.md 文件中
    readme_catelogue_list_file = open(readme_catalogue_list_path)
    catalogue_list_lines = readme_catelogue_list_file.readlines()
    for catalogue_list_line in catalogue_list_lines:
        catalogue_list_line = catalogue_list_line.replace('https://github.com/itcharge/LeetCode-Py/blob/main/Contents', '.')
        content_index_file.write(catalogue_list_line)
    readme_catelogue_list_file.close()
    content_index_file.close()

# 根据题解目录, 题目分类原始列表目录，生成分类题解，并将整体保存到 categories_list_path
def gen_categories_list(solutions_path, categories_origin_list_path, categories_list_path):
    
    f = open(categories_origin_list_path)
    lines = f.readlines()
    category_h2 = None
    category_h3 = None
    category_h4 = None
    category_h6 = None
    category_h3_file_path = None
    category_h3_file_content = ""
    category_file_content = ""
    
    df = pd.read_csv("leetcode-problems.csv")
    
    for i in range(len(lines)):
        pattern = re.compile(r'(#{2,6}) (.*)')
        match = pattern.match(lines[i])
        if match:
            title_size, title_content =  match.group(1,2)
            if title_size == "##":
                category_h2 = title_content
                category_file_content += "## " + category_h2 + "\n\n"
            elif title_size == "###":
                if category_h3 and category_h3_file_path and category_h3_file_content:
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
                    category_file_content += "### " + category_h3 + "\n\n"
                else:
                    category_h3 = title_content
                    category_file_content += "### " + category_h3 + "\n\n"
            elif title_size == "####":
                category_h4 = title_content
                category_h3_file_content += "#### " + category_h4 + "\n\n"
                category_file_content += "#### " + category_h4 + "\n\n"
            elif title_size == "######":
                category_h6 = title_content
                problem_titles = title_content.split('、')
                if not problem_titles:
                    continue
                
                frame = pd.DataFrame(columns=['题号', '标题', '题解', '标签', '难度'])
                frame_cout = 0
                for problem_title in problem_titles:
                    # 获取题目所在行
                    df_indexs = df[df['标题'] == problem_title].index.tolist()
                    
                    if not df_indexs:
                        print('%s 没有出现在 leetcode-problems.csv 中' % (problem_title))
                        continue
                    row = df_indexs[0]
                    
                    problem_id = df.loc[row, "序号"]
                    problem_catalog = df.loc[row, "所在目录"]
                    problem_title = df.loc[row, "标题"]
                    problem_title_slug = df.loc[row, "标题末尾"]
                    problem_link = "[" + problem_title_slug + "](" + df.loc[row, "标题链接"] + ")"
                    problem_link_slug = df.loc[row, "标题链接末尾路径"]
                    problem_solution_path = os.path.join(solutions_path, problem_title + ".md")
                    if os.path.exists(problem_solution_path):
                        problem_solution_link = "[Python](" + df.loc[row, "github 题解链接"] + ")"
                    else:
                        problem_solution_link = ""
                    problem_label = df.loc[row, "标签"]
                    problem_difficulty = df.loc[row, "难度"]
                    res = [problem_id, problem_link, problem_solution_link, problem_label, problem_difficulty]
                    frame.loc[frame_cout] = res
                    frame_cout += 1
                
                table = gen_markdown_table(frame, False)
                category_h3_file_content += table + "\n\n"
                category_file_content += table + "\n\n"
                
    if category_h3 and category_h3_file_path and category_h3_file_content:
        with open(category_h3_file_path, 'w') as fi:
            fi.write(category_h3_file_content)
        fi.close()
        
    if category_file_content:
        with open(categories_list_path, 'w') as fi:
            fi.write("# LeetCode 题解（按分类排序，推荐刷题列表 ★★★）\n\n")
            fi.write(category_file_content)
        fi.close()
    
    print("Create Categories List Success")
        

# 根据题解目录, 面试题目分类原始列表目录，生成面试题解，并将整体保存到 interview_list_path
def gen_interview_list(solutions_path, interview_origin_list_path, interview_list_path):
    
    f = open(interview_origin_list_path)
    lines = f.readlines()
    interview_h2 = None
    interview_h3 = None
    interview_h4 = None
    interview_h6 = None
    interview_h3_file_path = None
    interview_h3_file_content = ""
    interview_file_content = ""
    
    df = pd.read_csv("leetcode-problems.csv")
    
    problems_set = set()
    for i in range(len(lines)):
        pattern = re.compile(r'(#{2,6}) (.*)')
        match = pattern.match(lines[i])
        if match:
            title_size, title_content =  match.group(1,2)
            if title_size == "##":
                interview_h2 = title_content
                interview_file_content += "## " + interview_h2 + "\n\n"
            elif title_size == "###":
                if interview_h3 and interview_h3_file_path and interview_h3_file_content:
                    interview_h3 = None
                    interview_h3_file_path = None
                    interview_h3_file_content = ""
                pattern1 = re.compile(r'\[(.*)\]\((.*)\)')
                match1 = pattern1.match(title_content)
                if match1:
                    interview_h3, interview_h3_file_path = match1.group(1,2)
                    interview_h3_file_content += "### " + interview_h3 + "\n\n"
                    interview_file_content += "### " + interview_h3 + "\n\n"
                else:
                    interview_h3 = title_content
                    interview_file_content += "### " + interview_h3 + "\n\n"
            elif title_size == "####":
                interview_h4 = title_content
                interview_h3_file_content += "#### " + interview_h4 + "\n\n"
                interview_file_content += "#### " + interview_h4 + "\n\n"
            elif title_size == "######":
                interview_h6 = title_content
                problem_titles = title_content.split('、')
                if not problem_titles:
                    continue
                
                frame = pd.DataFrame(columns=['题号', '标题', '题解', '标签', '难度'])
                frame_cout = 0
                for problem_title in problem_titles:
                    # 获取题目所在行
                    df_indexs = df[df['标题'] == problem_title].index.tolist()
                    
                    if not df_indexs:
                        print('%s 没有出现在 leetcode-problems.csv 中' % (problem_title))
                        continue
                    
                    problems_set.add(problem_title)
                    row = df_indexs[0]
                    
                    problem_id = df.loc[row, "序号"]
                    problem_catalog = df.loc[row, "所在目录"]
                    problem_title = df.loc[row, "标题"]
                    problem_title_slug = df.loc[row, "标题末尾"]
                    problem_link = "[" + problem_title_slug + "](" + df.loc[row, "标题链接"] + ")"
                    problem_link_slug = df.loc[row, "标题链接末尾路径"]
                    problem_solution_path = os.path.join(solutions_path, problem_title + ".md")
                    if os.path.exists(problem_solution_path):
                        problem_solution_link = "[Python](" + df.loc[row, "github 题解链接"] + ")"
                    else:
                        problem_solution_link = ""
                    problem_label = df.loc[row, "标签"]
                    problem_difficulty = df.loc[row, "难度"]
                    res = [problem_id, problem_link, problem_solution_link, problem_label, problem_difficulty]
                    frame.loc[frame_cout] = res
                    frame_cout += 1
                        
                table = gen_markdown_table(frame, False)
                interview_h3_file_content += table + "\n\n"
                interview_file_content += table + "\n\n"
            
    if interview_file_content:
        with open(interview_list_path, 'w') as fi:
            if "Interview-100-List.md" in interview_origin_list_path:
                fi.write("# LeetCode 面试最常考 100 题（按分类排序）\n\n")
            elif "Interview-200-List.md" in interview_origin_list_path:
                fi.write("# LeetCode 面试最常考 200 题（按分类排序）\n\n")
            fi.write(interview_file_content)
            fi.write("\n## 参考资料\n")
            fi.write("\n- 【清单】[CodeTop 企业题库](https://codetop.cc/home)\n")
        fi.close()
    
    print("Total Problems Count: " + str(len(problems_set)))
    print(sorted(list(problems_set)))
    print("Create Interview List Success")