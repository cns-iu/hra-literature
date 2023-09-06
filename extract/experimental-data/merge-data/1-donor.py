import pandas as pd
import re

# Function to extract age from development_stage
def extract_age_from_stage(stage):
    match = re.search(r'(\d+)-year-old', stage)
    return match.group(1) if match else stage

def extract_age_unit_from_stage(stage):
    match = re.search(r'(\d+)-year-old', stage)
    return 'years' if match else ''

# Load the datasets
gtex_donor = pd.read_csv("data/experimental/gtex_donor.csv")
hubmap_donor = pd.read_csv("data/experimental/hubmap_donor.csv")
cxg_donor = pd.read_csv("data/experimental/cxg_donor.csv")

# Map GTEx columns
gtex_mapped = gtex_donor[['SUBJID', 'SEX', 'AGE', 'DTHHRDY', 'source']].copy()
gtex_mapped.columns = ['donor_id', 'sex', 'age', 'death_event', 'source']
gtex_mapped['sex'] = gtex_mapped['sex'].map({1: 'male', 2: 'female'})
gtex_mapped['death_event'] = gtex_mapped['death_event'].map({0: 'Ventilator Case', 1: 'Violent and fast death',
                                                             2: 'Fast death of natural causes', 3: 'Intermediate death',
                                                             4: 'Slow death'})

# Map HuBMAP columns
hubmap_mapped = hubmap_donor[['HBM_ID', 'Sex_Preferred Term', 'Age_Data Value', 'Age_Units', 'Weight_Data Value',
                              'Weight_Units', 'Height_Data Value', 'Height_Units', 'Race_Preferred Term',
                              'Body Mass Index_Data Value', 'Body mass index_Units', 'Blood type_Preferred Term',
                              'Rh Blood Group_Preferred Term', 'Rh factor_Preferred Term',
                              'Kidney donor profile index_Data Value', 'Kidney donor profile index_Units',
                              'Cause of death_Preferred Term', 'Death event_Preferred Term',
                              'Medical history_Preferred Term','Mechanism of injury_Preferred Term',
                              'Social history_Preferred Term']].copy()
hubmap_mapped.columns = ['donor_id', 'sex', 'age', 'age_unit', 'weight', 'weight_unit', 'height', 'height_unit', 'race',
                         'body_mass_index', 'body_mass_index_unit', 'blood_type', 'rh_blood_group', 'rh_factor',
                         'kidney_donor_profile_index', 'kidney_donor_profile_index_unit', 'cause_of_death', 'death_event',
                         'medical_history', 'mechanism_of_injury', 'social_history']
hubmap_mapped['source'] = 'hubmap'
hubmap_mapped['kidney_donor_profile_index_unit'] = hubmap_mapped['kidney_donor_profile_index_unit'].replace(['%', 'percent'], '%')


# Map CXG columns
cxg_mapped = cxg_donor[['donor_id', 'sex', 'sex_ontology_term_id', 'self_reported_ethnicity',
                        'self_reported_ethnicity_ontology_term_id', 'development_stage']].copy()
cxg_mapped.columns = ['donor_id', 'sex', 'sex_ontotlogy', 'race', 'race_ontotlogy', 'age']
cxg_mapped['source'] = 'cxg'
cxg_mapped['age_unit'] = cxg_mapped['age'].apply(extract_age_unit_from_stage)
cxg_mapped['age'] = cxg_mapped['age'].apply(extract_age_from_stage)


# Concatenate the tables and replace NaN with ''
harmonized_donor_expanded = pd.concat([gtex_mapped, hubmap_mapped, cxg_mapped], ignore_index=True, sort=False)
harmonized_donor_expanded = harmonized_donor_expanded.fillna('')

harmonized_donor_expanded.to_csv('data/experimental/harmonized_donor.csv')
