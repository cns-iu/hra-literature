# def mutate_anatomical_structure(self, obj):
#     anatomical_structures = self._get_named_anatomical_structures(obj)
#     for anatomical_structure in anatomical_structures:
#         as_id, is_provisional = self._get_as_id(anatomical_structure)
#         as_iri = URIRef(self._expand_anatomical_entity_id(as_id))

# def _get_named_anatomical_structures(self, obj):
#     anatomical_structures = obj['anatomical_structures']
#     return [anatomical_structure for anatomical_structure
#             in anatomical_structures
#             if anatomical_structure['name']
#             or anatomical_structure['rdfs_label']]

# def _get_as_id(self, anatomical_structure):
#     as_id = anatomical_structure['id']
#     is_provisional = False
#     if not as_id or ":" not in as_id:
#         as_pref_label = anatomical_structure['name']
#         if not as_pref_label:
#             as_pref_label = anatomical_structure['rdfs_label']
#         as_id = self._generate_provisional_id(as_pref_label)
#         is_provisional = True
#     return as_id, is_provisional

# def _generate_provisional_id(self, str):
#     str = str.strip()
#     str = lowercase(str)
#     str = re.sub('\\W+', '-', str)
#     str = re.sub('[^a-z0-9-]+', '', str)
#     return f'ASCTB-TEMP:{str}'

# def _expand_anatomical_entity_id(self, str):
#     if "ASCTB-TEMP:" in str:
#         return self._expand_asctb_temp_id(str)
#     elif "FMA:" in str:
#         return self._expand_fma_id(str)
#     elif "UBERON:" in str:
#         return self._expand_uberon_id(str)
#     else:
#         raise ValueError("Invalid anatomical structure ID: " + str)

# def _expand_fma_id(self, str):
#     fma_pattern = re.compile("FMA:", re.IGNORECASE)
#     return fma_pattern.sub(
#         "http://purl.org/sig/ont/fma/fma", str)

# def _expand_uberon_id(self, str):
#     uberon_pattern = re.compile("UBERON:", re.IGNORECASE)
#     return uberon_pattern.sub(
#         "http://purl.obolibrary.org/obo/UBERON_", str)

# def _expand_asctb_temp_id(self, str):
#     asctb_temp_pattern = re.compile("ASCTB-TEMP:", re.IGNORECASE)
#     return asctb_temp_pattern.sub(
#         "https://purl.org/ccf/ASCTB-TEMP_", str)

import pandas as pd
import re

def _generate_provisional_id(input_str):
    input_str = input_str.strip().lower()
    input_str = re.sub('\\W+', '-', input_str)
    input_str = re.sub('[^a-z0-9-]+', '', input_str)
    return f'ASCTB-TEMP:{input_str}'

# # def _expand_anatomical_entity_id(anatomical_id):
#     if "ASCTB-TEMP:" in anatomical_id:
#         return _expand_asctb_temp_id(anatomical_id)
#     elif "FMA:" in anatomical_id:
#         return _expand_fma_id(anatomical_id)
#     elif "UBERON:" in anatomical_id:
#         return _expand_uberon_id(anatomical_id)
#     else:
#         raise ValueError("Invalid anatomical structure ID: " + anatomical_id)

def _expand_anatomical_entity_id(anatomical_id):
    try:
        if "ASCTB-TEMP:" in anatomical_id:
            return _expand_asctb_temp_id(anatomical_id)
        elif "FMA:" in anatomical_id:
            return _expand_fma_id(anatomical_id)
        elif "UBERON:" in anatomical_id:
            return _expand_uberon_id(anatomical_id)
        # else:
        #     # 如果ID不符合预期格式，返回一个明确的错误信息或原始ID
        #     return "Invalid ID: " + anatomical_id
    except Exception as e:
        # 处理任何其他异常
        return "Error processing ID: " + anatomical_id


def _expand_fma_id(anatomical_id):
    fma_pattern = re.compile("FMA:", re.IGNORECASE)
    return fma_pattern.sub("http://purl.org/sig/ont/fma/fma", anatomical_id)

def _expand_uberon_id(anatomical_id):
    uberon_pattern = re.compile("UBERON:", re.IGNORECASE)
    return uberon_pattern.sub("http://purl.obolibrary.org/obo/UBERON_", anatomical_id)

def _expand_asctb_temp_id(anatomical_id):
    asctb_temp_pattern = re.compile("ASCTB-TEMP:", re.IGNORECASE)
    return asctb_temp_pattern.sub("https://purl.org/ccf/ASCTB-TEMP_", anatomical_id)

def process_row(row):
    as_id = row['id']
    if pd.isna(as_id) or ":" not in str(as_id):
        as_pref_label = row['name'] if pd.notnull(row['name']) else row['rdfs_label']
        as_id = _generate_provisional_id(as_pref_label)
    return _expand_anatomical_entity_id(as_id)


# 读取CSV文件
file_path = 'data/ontology/asct_anatomical_structures.csv'  # 替换为实际文件路径
df = pd.read_csv(file_path)

# 应用处理函数
df['as_iri'] = df.apply(process_row, axis=1)

# 保存新的CSV文件
output_file_path = 'data/ontology/asct_anatomical_structures_modified.csv'  # 替换为所需的输出文件路径
df.to_csv(output_file_path, index=False)

print("File saved to:", output_file_path)
