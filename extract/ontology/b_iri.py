# # def mutate_biomarker(self, obj):
# #     markers = self._get_named_biomarkers(obj)
# #     for marker in markers:
# #         bm_id, is_provisional = self._get_bm_id(marker)
# #         bm_iri = URIRef(self._expand_biomarker_id(bm_id))
# # def _get_named_biomarkers(self, obj):
# #     markers = obj['biomarkers']
# #     return [marker for marker in markers
# #             if marker['name'] or marker['rdfs_label']]

# # def _get_bm_id(self, marker):
# #     bm_id = marker['id']
# #     is_provisional = False
# #     if not self._is_valid_marker(marker):
# #         bm_pref_label = marker['name']
# #         if not bm_pref_label:
# #             bm_pref_label = marker['rdfs_label']
# #         bm_id = self._generate_provisional_id(bm_pref_label)
# #         is_provisional = True
# #     return bm_id, is_provisional
# # def _generate_provisional_id(self, str):
# #     str = str.strip()
# #     str = lowercase(str)
# #     str = re.sub('\\W+', '-', str)
# #     str = re.sub('[^a-z0-9-]+', '', str)
# #     return f'ASCTB-TEMP:{str}'
# # def _expand_biomarker_id(self, str):
# #     if "ASCTB-TEMP:" in str:
# #         return self._expand_asctb_temp_id(str)
# #     elif "HGNC:" in str:
# #         return self._expand_hgnc_id(str)
# #     else:
# #         raise ValueError("Invalid biomarker ID: " + str)

# # def _expand_hgnc_id(self, str):
# #     hgnc_pattern = re.compile("HGNC:", re.IGNORECASE)
# #     return hgnc_pattern.sub(
# #         "http://identifiers.org/hgnc/", str)

# # def _expand_asctb_temp_id(self, str):
# #     asctb_temp_pattern = re.compile("ASCTB-TEMP:", re.IGNORECASE)
# #     return asctb_temp_pattern.sub(
# #         "https://purl.org/ccf/ASCTB-TEMP_", str)

# import pandas as pd
# import re

# # 定义辅助函数
# def _generate_provisional_id(input_str):
#     input_str = input_str.strip().lower()
#     input_str = re.sub('\\W+', '-', input_str)
#     input_str = re.sub('[^a-z0-9-]+', '', input_str)
#     return f'ASCTB-TEMP:{input_str}'

# def _expand_biomarker_id(bm_id):
#     try:
#         if "ASCTB-TEMP:" in bm_id:
#             return _expand_asctb_temp_id(bm_id)
#         elif "HGNC:" in bm_id:
#             return _expand_hgnc_id(bm_id)
#         else:
#             return "Invalid ID: " + bm_id
#     except Exception as e:
#         return "Error processing ID: " + bm_id

# def _expand_hgnc_id(bm_id):
#     hgnc_pattern = re.compile("HGNC:", re.IGNORECASE)
#     return hgnc_pattern.sub("http://identifiers.org/hgnc/", bm_id)

# def _expand_asctb_temp_id(bm_id):
#     asctb_temp_pattern = re.compile("ASCTB-TEMP:", re.IGNORECASE)
#     return asctb_temp_pattern.sub("https://purl.org/ccf/ASCTB-TEMP_", bm_id)

# def _is_valid_marker(marker):
#     return marker['id'] and re.match(r"HGNC:[0-9]+", marker['id'])

# # 处理函数
# def process_biomarker_row(row):
#     bm_id = row['id'] if not _is_valid_marker(row['id']) else _generate_provisional_id(row['name'] if pd.notnull(row['name']) else row['rdfs_label'])
#     return _expand_biomarker_id(bm_id)

# # 读取CSV文件
# file_path_biomarkers = 'data/ontology/asct_biomarkers.csv'  # 替换为实际文件路径
# df_biomarkers = pd.read_csv(file_path_biomarkers)

# # 应用处理函数并添加新列
# df_biomarkers['b_iri'] = df_biomarkers.apply(process_biomarker_row, axis=1)

# # 保存新的CSV文件
# output_file_path_biomarkers = 'data/ontology/asct_biomarkers_modified.csv'  # 替换为所需的输出文件路径
# df_biomarkers.to_csv(output_file_path_biomarkers, index=False)

# print("File saved to:", output_file_path_biomarkers)


import pandas as pd
import re

# 定义辅助函数
def _generate_provisional_id(input_str):
    input_str = input_str.strip().lower()
    input_str = re.sub('\\W+', '-', input_str)
    input_str = re.sub('[^a-z0-9-]+', '', input_str)
    return f'ASCTB-TEMP:{input_str}'

def _expand_biomarker_id(bm_id):
    try:
        if "ASCTB-TEMP:" in bm_id:
            return _expand_asctb_temp_id(bm_id)
        elif "HGNC:" in bm_id:
            return _expand_hgnc_id(bm_id)
        else:
            return "Invalid ID: " + bm_id
    except Exception as e:
        return "Error processing ID: " + bm_id

def _expand_hgnc_id(bm_id):
    hgnc_pattern = re.compile("HGNC:", re.IGNORECASE)
    return hgnc_pattern.sub("http://identifiers.org/hgnc/", bm_id)

def _expand_asctb_temp_id(bm_id):
    asctb_temp_pattern = re.compile("ASCTB-TEMP:", re.IGNORECASE)
    return asctb_temp_pattern.sub("https://purl.org/ccf/ASCTB-TEMP_", bm_id)

def _is_valid_marker(marker):
    if 'id' in marker and isinstance(marker['id'], str):
        return re.match(r"HGNC:[0-9]+", marker['id']) is not None
    return False

# 处理函数
def process_biomarker_row(row):
    bm_id = row['id'] if _is_valid_marker(row) else _generate_provisional_id(row['name'] if pd.notnull(row['name']) else row['rdfs_label'])
    return _expand_biomarker_id(bm_id)

# 读取CSV文件
file_path_biomarkers = 'data/ontology/asct_biomarkers.csv'  # 替换为实际文件路径
df_biomarkers = pd.read_csv(file_path_biomarkers)

# 应用处理函数并添加新列
df_biomarkers['b_iri'] = df_biomarkers.apply(process_biomarker_row, axis=1)

# 保存新的CSV文件
output_file_path_biomarkers = 'data/ontology/asct_biomarkers_modified.csv'  # 替换为所需的输出文件路径
df_biomarkers.to_csv(output_file_path_biomarkers, index=False)

print("File saved to:", output_file_path_biomarkers)
