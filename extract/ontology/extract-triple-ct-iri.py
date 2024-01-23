import pandas as pd
import re

# 函数：根据给定的cell_type ID生成IRI
def expand_cell_type_id(ct_id):
    if "ASCTB-TEMP:" in ct_id:
        return re.sub("ASCTB-TEMP:", "https://purl.org/ccf/ASCTB-TEMP_", ct_id, flags=re.IGNORECASE)
    elif "PCL:" in ct_id:
        return re.sub("PCL:", "http://purl.obolibrary.org/obo/PCL_", ct_id, flags=re.IGNORECASE)
    elif "CL:" in ct_id:
        return re.sub("CL:", "http://purl.obolibrary.org/obo/CL_", ct_id, flags=re.IGNORECASE)
    elif "LMHA:" in ct_id:
        return re.sub("LMHA:", "http://purl.obolibrary.org/obo/LMHA_", ct_id, flags=re.IGNORECASE)
    elif "FMA:" in ct_id:
        return re.sub("FMA:", "http://purl.obolibrary.org/obo/FMA_", ct_id, flags=re.IGNORECASE)
    else:
        return None


# 函数：生成临时ID
def generate_provisional_id(name):
    return f'ASCTB-TEMP:{re.sub(r"[^a-z0-9-]+", "", name.lower().replace(" ", "-"))}'

# 读取CSV文件
df = pd.read_csv('data/ontology/hralit_ontology_triple.csv', sep=',')
df = df[df['ontology_type'] == 'CT']

# 新列初始化
df['ct_iri'] = ''
df['pref_label'] = ''

# 处理每一行
for index, row in df.iterrows():

    ct_id = row['id']
    name = row['name'] if pd.notna(row['name']) else row['rdfs_label']
    if name =='T cell':
        df.at[index, 'ct_iri'] = 'http://purl.obolibrary.org/obo/CL_0000084'
    else:
    # 检查ID是否存在
        if pd.isna(ct_id) or ct_id == '':
            ct_id = generate_provisional_id(name)
            df.at[index, 'ct_iri'] = expand_cell_type_id(ct_id)
        else:
            df.at[index, 'ct_iri'] = expand_cell_type_id(ct_id)

    # 设置pref_label
    # df.at[index, 'pref_label'] = name.lower()
    df.at[index, 'pref_label'] = str(name).lower()

# df = df[['ct_iri', 'pref_label']].drop_duplicates().dropna(subset=['ct_iri'])
# 将结果保存为新的CSV文件
df.to_csv('C:\\Users\\Administrator\\Desktop\\hralit_triple3.csv', sep='|', index=False)