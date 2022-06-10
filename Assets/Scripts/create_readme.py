import create_solutions_list as gen

# 生成分类题解列表
solotions_path = '../../Solutions'
categories_origin_list_path = '../Origins/Categories-List.md'
categories_list_path = '../../Contents/00.Introduction/05.Categories-List.md'

gen.gen_categories_list(solotions_path, categories_origin_list_path, categories_list_path)

# 生成面试 Top 100 题解列表
interview_100_origin_list_path = '../Origins/Interview-100-List.md'
interview_100_list_path = '../../Contents/00.Introduction/06.Interview-100-List.md'
gen.gen_interview_list(solotions_path, interview_100_origin_list_path, interview_100_list_path)

# 生成面试 Top 200 题解列表
interview_200_origin_list_path = '../Origins/Interview-200-List.md'
interview_200_list_path = '../../Contents/00.Introduction/07.Interview-200-List.md'
gen.gen_interview_list(solotions_path, interview_200_origin_list_path, interview_200_list_path)

# 生成全部题解列表
solotions_output_path = '../../Contents/00.Introduction/04.Solutions-List.md'

solutions_count = gen.gen_solutions_list(solotions_path, solotions_output_path) 


# 生成 README.md index.md 文件
readme_head_path = '../Origins/README-Head.md'
readme_catalogue_list_path = '../Origins/README-Catalogue-List.md'
content_index_path = '../../Contents/index.md'
readme_path = '../../README.md'

gen.merge_readme_file(solotions_output_path, readme_head_path, readme_catalogue_list_path, content_index_path, readme_path, solutions_count)

