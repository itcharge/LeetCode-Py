import create_solutions_list as gen

# 生成分类题解列表
solotions_path = '../Solutions'
categories_origin_list_path = './Assets/Categories-Origin-List.md'
categories_list_path = '../Contents/00.Introduction/05.Categories-List.md'

gen.gen_categories_list(solotions_path, categories_origin_list_path, categories_list_path)


# 生成全部题解列表
solotions_output_path = '../Contents/00.Introduction/04.Solutions-List.md'

solutions_count = gen.gen_solutions_list(solotions_path, solotions_output_path) 


# 生成 README.md index.md 文件
readme_head_path = './Assets/README-Head.md'
readme_catalogue_list_path = './Assets/README-Catalogue-List.md'
content_index_path = '../Contents/index.md'
readme_path = '../README.md'

gen.merge_readme_file(solotions_output_path, readme_head_path, readme_catalogue_list_path, content_index_path, readme_path, solutions_count)

