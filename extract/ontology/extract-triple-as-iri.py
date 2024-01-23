import pandas as pd
import re

def _expand_anatomical_entity_id(id_str):
    if "ASCTB-TEMP:" in id_str:
        return _expand_asctb_temp_id(id_str)
    elif "FMA:" in id_str:
        return _expand_fma_id(id_str)
    elif "UBERON:" in id_str:
        return _expand_uberon_id(id_str)
    # else:
        # raise ValueError("Invalid anatomical structure ID: " + id_str)

def _expand_fma_id(str):
    fma_pattern = re.compile("FMA:", re.IGNORECASE)
    return fma_pattern.sub("http://purl.org/sig/ont/fma/fma", str)

def _expand_uberon_id(str):
    uberon_pattern = re.compile("UBERON:", re.IGNORECASE)
    return uberon_pattern.sub("http://purl.obolibrary.org/obo/UBERON_", str)

def _expand_asctb_temp_id(str):
    asctb_temp_pattern = re.compile("ASCTB-TEMP:", re.IGNORECASE)
    return asctb_temp_pattern.sub("https://purl.org/ccf/ASCTB-TEMP_", str)

def _generate_provisional_id(str):
    str = str.strip().lower()
    str = re.sub('\\W+', '-', str)
    str = re.sub('[^a-z0-9-]+', '', str)
    return f'ASCTB-TEMP:{str}'

def original_data():
    data = {
        'as_iri': [
            'http://purl.obolibrary.org/obo/UBERON_0013702',
            'http://purl.obolibrary.org/obo/UBERON_0004548',
            'http://purl.obolibrary.org/obo/UBERON_0004549',
            'http://purl.obolibrary.org/obo/UBERON_0001303',
            'http://purl.obolibrary.org/obo/UBERON_0001302',
            'http://purl.obolibrary.org/obo/UBERON_0004538',
            'http://purl.obolibrary.org/obo/UBERON_0004539',
            'http://purl.org/sig/ont/fma/fma24978',
            'http://purl.org/sig/ont/fma/fma24977',
            'http://purl.org/sig/ont/fma/fma7214',
            'http://purl.org/sig/ont/fma/fma7213',
            'http://purl.obolibrary.org/obo/UBERON_0001223',
            'http://purl.obolibrary.org/obo/UBERON_0001222',
            'http://purl.obolibrary.org/obo/UBERON_0001911',
            'http://purl.org/sig/ont/fma/fma57991',
            'http://purl.org/sig/ont/fma/fma57987',
            'http://purl.obolibrary.org/obo/UBERON_0000310',
            'http://purl.obolibrary.org/obo/UBERON_0001270',
            'http://purl.obolibrary.org/obo/UBERON_0002373',
            'http://purl.org/sig/ont/fma/fma54974',
            'http://purl.org/sig/ont/fma/fma54973',
            'http://purl.obolibrary.org/obo/UBERON_0001737'
        ],
        'pref_label': [
            'body',
            'left eye',
            'right eye',
            'left fallopian tube',
            'right fallopian tube',
            'left kidney',
            'right kidney',
            'left knee',
            'right knee',
            'left ovary',
            'right ovary',
            'left ureter',
            'right ureter',
            'mammary gland',
            'left mammary gland',
            'right mammary gland',
            'breast',
            'pelvis',
            'palatine tonsil',
            'left palatine tonsil',
            'right palatine tonsil',
            'larynx'
        ]
    }
    return (pd.DataFrame(data))

def process_data(input_file, output_file):
    # 读取CSV文件
    df = pd.read_csv(input_file, sep=',')
    df = df[df['ontology_type'] == 'AS']

    # 处理每一行数据
    df['as_id'] = df.apply(lambda row: row['id'] if pd.notnull(row['id']) and ':' in row['id'] else _generate_provisional_id(row['name'] if pd.notnull(row['name']) else row['rdfs_label']), axis=1)
    df['as_iri'] = df['as_id'].apply(_expand_anatomical_entity_id)
    df['pref_label'] = df.apply(lambda row: row['name'].lower() if pd.notnull(row['name']) else (row['rdfs_label'].lower() if pd.notnull(row['rdfs_label']) else row['as_id'].lower()), axis=1)

    # 删除临时列as_id
    df.drop('as_id', axis=1, inplace=True)

    # data=original_data()

    # df = df[['as_iri', 'pref_label']].drop_duplicates()
    # df = pd.concat([df, data], ignore_index=True)
    # 写入CSV文件
    df.to_csv(output_file, sep='|', index=False)


# 请指定您的输入和输出文件路径
input_file = 'data/ontology/hralit_ontology_triple.csv'  # 更改为您的输入文件路径
output_file = 'C:\\Users\\Administrator\\Desktop\\hralit_triple2.csv'  # 更改为您希望保存输出的文件路径

# 运行数据处理函数
process_data(input_file, output_file)