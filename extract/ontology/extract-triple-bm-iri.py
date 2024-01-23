
import pandas as pd
import re


# 函数：根据给定的biomarker ID生成IRI
def expand_biomarker_id(bm_id):
    if "ASCTB-TEMP:" in bm_id:
        return re.sub("ASCTB-TEMP:", "https://purl.org/ccf/ASCTB-TEMP_", bm_id, flags=re.IGNORECASE)
    elif "HGNC:" in bm_id:
        return re.sub("HGNC:", "http://identifiers.org/hgnc/", bm_id, flags=re.IGNORECASE)
    else:
        raise ValueError("Invalid biomarker ID: " + bm_id)


# 函数：生成临时ID
def generate_provisional_id(name):
    name = name.strip()
    name = name.lower()
    name = re.sub(r'\W+', '-', name)
    name = re.sub(r'[^a-z0-9-]+', '', name)
    return f'ASCTB-TEMP:{name}'

# 读取CSV文件
df = pd.read_csv('data/ontology/hralit_ontology_triple.csv', sep=',')
df = df[df['ontology_type'] == 'B']

# 新列初始化
df['bm_iri'] = ''
df['pref_label'] = ''

# 处理每一行
for index, row in df.iterrows():
    if re.match(r"HGNC:[0-9]+", str(row['id'])):
        bm_id = row['id']
    elif str(row['id']) == "GNC:7569":
        bm_id = "HGNC:7569"
    else:
        bm_id=''
    name = row['name'] if pd.notna(row['name']) else row['rdfs_label']

    # 检查ID是否存在
    if pd.isna(bm_id) or bm_id == '':
        # bm_id = is_valid_marker(bm_id)
        bm_id = generate_provisional_id( str(name).lower())
    try:
        bm_iri = expand_biomarker_id(bm_id)
    except ValueError as e:
        print(f"Error processing row {index}: {e}")
        continue

    df.at[index, 'bm_iri'] = bm_iri

    # 检查 'name' 是否存在 NaN 值
    if not pd.isna(name):
        df.at[index, 'pref_label'] = name
    else:
        df.at[index, 'pref_label'] = ''

# df = df[['bm_iri', 'pref_label','b_type']].drop_duplicates().dropna(subset=['bm_iri'])
# 将结果保存为新的CSV文件
df.to_csv('C:\\Users\\Administrator\\Desktop\\hralit_triple4.csv', sep='|', index=False)