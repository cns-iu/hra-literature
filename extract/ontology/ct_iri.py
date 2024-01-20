    # def mutate_cell_type(self, obj):
    #     cell_types = self._get_named_cell_types(obj)
    #     for cell_type in cell_types:
    #         ct_id, is_provisional = self._get_ct_id(cell_type)
    #         ct_iri = URIRef(self._expand_cell_type_id(ct_id))

    # def _get_named_cell_types(self, obj):
    #     cell_types = obj['cell_types']
    #     return [cell_type for cell_type in cell_types
    #             if cell_type['name'] or cell_type['rdfs_label']]
    # def _get_ct_id(self, cell_type):
    #     ct_id = cell_type['id']
    #     is_provisional = False
    #     if not ct_id or ":" not in ct_id:
    #         ct_pref_label = cell_type['name']
    #         if not ct_pref_label:
    #             ct_pref_label = cell_type['rdfs_label']
    #         ct_id = self._generate_provisional_id(ct_pref_label)
    #         is_provisional = True
    #     if "PCL:" in ct_id:
    #         is_provisional = True
    #     return ct_id, is_provisional
    # def _generate_provisional_id(self, str):
    #     str = str.strip()
    #     str = lowercase(str)
    #     str = re.sub('\\W+', '-', str)
    #     str = re.sub('[^a-z0-9-]+', '', str)
    #     return f'ASCTB-TEMP:{str}'
    # def _expand_cell_type_id(self, str):
    #     if "ASCTB-TEMP:" in str:
    #         return self._expand_asctb_temp_id(str)
    #     elif "PCL:" in str:
    #         return self._expand_pcl_id(str)
    #     elif "CL:" in str:
    #         return self._expand_cl_id(str)
    #     elif "LMHA:" in str:
    #         return self._expand_lmha_id(str)
    #     elif "FMA:" in str:
    #         return self._expand_fma_id(str)
    #     else:
    #         raise ValueError("Invalid cell type ID: " + str)

    # def _expand_cl_id(self, str):
    #     cl_pattern = re.compile("CL:", re.IGNORECASE)
    #     return cl_pattern.sub(
    #         "http://purl.obolibrary.org/obo/CL_", str)

    # def _expand_lmha_id(self, str):
    #     lmha_pattern = re.compile("LMHA:", re.IGNORECASE)
    #     return lmha_pattern.sub(
    #         "http://purl.obolibrary.org/obo/LMHA_", str)

    # def _expand_pcl_id(self, str):
    #     pcl_pattern = re.compile("PCL:", re.IGNORECASE)
    #     return pcl_pattern.sub(
    #         "http://purl.obolibrary.org/obo/PCL_", str)

    # def _expand_fma_id(self, str):
    #     fma_pattern = re.compile("FMA:", re.IGNORECASE)
    #     return fma_pattern.sub(
    #         "http://purl.org/sig/ont/fma/fma", str)
    # def _expand_asctb_temp_id(self, str):
    #     asctb_temp_pattern = re.compile("ASCTB-TEMP:", re.IGNORECASE)
    #     return asctb_temp_pattern.sub(
    #         "https://purl.org/ccf/ASCTB-TEMP_", str)

import pandas as pd
import re

# 定义辅助函数
def _generate_provisional_id(input_str):
    input_str = input_str.strip().lower()
    input_str = re.sub('\\W+', '-', input_str)
    input_str = re.sub('[^a-z0-9-]+', '', input_str)
    return f'ASCTB-TEMP:{input_str}'

def _expand_cell_type_id(cell_id):
    try:
        if "ASCTB-TEMP:" in cell_id:
            return _expand_asctb_temp_id(cell_id)
        elif "PCL:" in cell_id:
            return _expand_pcl_id(cell_id)
        elif "CL:" in cell_id:
            return _expand_cl_id(cell_id)
        elif "LMHA:" in cell_id:
            return _expand_lmha_id(cell_id)
        elif "FMA:" in cell_id:
            return _expand_fma_id(cell_id)
        # else:
        #     return "Invalid ID: " + cell_id
    except Exception as e:
        return "Error processing ID: " + cell_id

def _expand_cl_id(cell_id):
    cl_pattern = re.compile("CL:", re.IGNORECASE)
    return cl_pattern.sub("http://purl.obolibrary.org/obo/CL_", cell_id)

def _expand_lmha_id(cell_id):
    lmha_pattern = re.compile("LMHA:", re.IGNORECASE)
    return lmha_pattern.sub("http://purl.obolibrary.org/obo/LMHA_", cell_id)

def _expand_pcl_id(cell_id):
    pcl_pattern = re.compile("PCL:", re.IGNORECASE)
    return pcl_pattern.sub("http://purl.obolibrary.org/obo/PCL_", cell_id)

def _expand_fma_id(cell_id):
    fma_pattern = re.compile("FMA:", re.IGNORECASE)
    return fma_pattern.sub("http://purl.org/sig/ont/fma/fma", cell_id)

def _expand_asctb_temp_id(cell_id):
    asctb_temp_pattern = re.compile("ASCTB-TEMP:", re.IGNORECASE)
    return asctb_temp_pattern.sub("https://purl.org/ccf/ASCTB-TEMP_", cell_id)

# 处理函数
def process_cell_type_row(row):
    ct_id = row['id'] if pd.notnull(row['id']) else _generate_provisional_id(row['name'] if pd.notnull(row['name']) else row['rdfs_label'])
    return _expand_cell_type_id(ct_id)

# 读取CSV文件
file_path_cell_types = 'data/ontology/asct_cell_types.csv'  # 替换为实际文件路径
df_cell_types = pd.read_csv(file_path_cell_types)

# 应用处理函数并添加新列
df_cell_types['ct_iri'] = df_cell_types.apply(process_cell_type_row, axis=1)

# 保存新的CSV文件
output_file_path_cell_types = 'data/ontology/asct_cell_types_modified.csv'  # 替换为所需的输出文件路径
df_cell_types.to_csv(output_file_path_cell_types, index=False)

print("File saved to:", output_file_path_cell_types)
