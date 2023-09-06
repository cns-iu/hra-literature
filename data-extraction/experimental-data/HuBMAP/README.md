# HuBMAP metadata

HuBMAP Metadata TSV URL: https://portal.hubmapconsortium.org/metadata/v0/datasets.tsv

### [Diagram-Link](https://app.diagrams.net/#G1REdLjoMMJaP6tBk-P2wAPLvq50BI7lfw)

![image](https://github.com/Aashay7/organizing_data_HRAlit/blob/main/Experimental_Data/HuBMAP/hubmap.png)

### Contents:
- `hubmap_data.ipynb` : Python notebook file to explore the contents of the `HuBMAP metadata file`. 
- `hubmap.png` : CCF API endpoint response schemas visualized. 

Response Schema: 
```
 ancestor_counts :  dict
      entity_type :  dict
           Donor :  int
           Sample :  int
 ancestor_ids :  list

 ancestors :  list
           created_by_user_displayname :  str
           created_by_user_email :  str
           created_timestamp :  int
           data_access_level :  str
           description :  str
           entity_type :  str
           group_uuid :  str
           hubmap_id :  str
           lab_tissue_sample_id :  str
           last_modified_timestamp :  int
           mapped_data_access_level :  str
           mapped_last_modified_timestamp :  str
           mapped_metadata :  dict
           mapped_sample_category :  str
           metadata :  dict
                cold_ischemia_time_unit :  str
                cold_ischemia_time_value :  str
                health_status :  str
                organ_condition :  str
                pathologist_report :  str
                perfusion_solution :  str
                procedure_date :  str
                specimen_preservation_temperature :  str
                specimen_quality_criteria :  str
                specimen_tumor_distance_unit :  str
                specimen_tumor_distance_value :  str
                vital_state :  str
                warm_ischemia_time_unit :  str
                warm_ischemia_time_value :  str
           protocol_url :  str
           rui_location :  str
           sample_category :  str
           specimen_type :  str
           submission_id :  str
           tissue_type :  str
           uuid :  str

 contacts :  list
           affiliation :  str
           first_name :  str
           is_contact :  str
           last_name :  str
           middle_name_or_initial :  str
           name :  str
           orcid_id :  str
           version :  str

 contains_human_genetic_sequences :  bool
 contributors :  list
           affiliation :  str
           first_name :  str
           is_contact :  str
           last_name :  str
           middle_name_or_initial :  str
           name :  str
           orcid_id :  str
           version :  str

 created_by_user_displayname :  str
 created_by_user_email :  str
 created_timestamp :  int
 data_access_level :  str
 data_types :  list

 descendant_counts :  dict
      entity_type :  dict
           Dataset :  int
 descendant_ids :  list

 descendants :  list
           contains_human_genetic_sequences :  bool
           created_by_user_displayname :  str
           created_by_user_email :  str
           created_timestamp :  int
           data_access_level :  str
           data_types :  list

           dataset_info :  str
           entity_type :  str
           files :  list
                     description :  str
                     edam_term :  str
                     is_qa_qc :  bool
                     rel_path :  str
                     size :  int
                     type :  str

           group_uuid :  str
           hubmap_id :  str
           last_modified_timestamp :  int
           metadata :  dict
                dag_provenance_list :  list
                          hash :  str
                          name :  str
                          origin :  str

                files :  list
                          description :  str
                          edam_term :  str
                          is_qa_qc :  bool
                          rel_path :  str
                          size :  int
                          type :  str

           published_timestamp :  int
           status :  str
           title :  str
           uuid :  str

 description :  str
 display_subtype :  str
 doi_url :  str
 donor :  dict
      created_by_user_displayname :  str
      created_by_user_email :  str
      created_timestamp :  int
      data_access_level :  str
      entity_type :  str
      group_uuid :  str
      hubmap_id :  str
      lab_donor_id :  str
      label :  str
      last_modified_timestamp :  int
      mapped_data_access_level :  str
      mapped_last_modified_timestamp :  str
      mapped_metadata :  dict
           age_unit :  list

           age_value :  list

           blood_type :  list

           body_mass_index_unit :  list

           body_mass_index_value :  list

           cause_of_death :  list

           death_event :  list

           height_unit :  list

           height_value :  list

           kidney_donor_profile_index_unit :  list

           kidney_donor_profile_index_value :  list

           mechanism_of_injury :  list

           race :  list

           sex :  list

           social_history :  list

           weight_unit :  list

           weight_value :  list

      metadata :  dict
           organ_donor_data :  list
                     code :  str
                     concept_id :  str
                     data_type :  str
                     data_value :  str
                     end_datetime :  str
                     graph_version :  str
                     grouping_code :  str
                     grouping_concept :  str
                     grouping_concept_preferred_term :  str
                     grouping_sab :  str
                     numeric_operator :  str
                     preferred_term :  str
                     sab :  str
                     start_datetime :  str
                     units :  str

      protocol_url :  str
      submission_id :  str
      uuid :  str
 entity_type :  str
 files :  list
 group_name :  str
 group_uuid :  str
 hubmap_id :  str
 immediate_ancestors :  list
           created_by_user_displayname :  str
           created_by_user_email :  str
           created_timestamp :  int
           data_access_level :  str
           description :  str
           entity_type :  str
           group_uuid :  str
           hubmap_id :  str
           lab_tissue_sample_id :  str
           last_modified_timestamp :  int
           metadata :  dict
                cold_ischemia_time_unit :  str
                cold_ischemia_time_value :  str
                health_status :  str
                organ_condition :  str
                pathologist_report :  str
                perfusion_solution :  str
                procedure_date :  str
                specimen_preservation_temperature :  str
                specimen_quality_criteria :  str
                specimen_tumor_distance_unit :  str
                specimen_tumor_distance_value :  str
                vital_state :  str
                warm_ischemia_time_unit :  str
                warm_ischemia_time_value :  str
           protocol_url :  str
           rui_location :  str
           sample_category :  str
           specimen_type :  str
           submission_id :  str
           tissue_type :  str
           uuid :  str

 immediate_descendants :  list
           contains_human_genetic_sequences :  bool
           created_by_user_displayname :  str
           created_by_user_email :  str
           created_timestamp :  int
           data_access_level :  str
           data_types :  list

           dataset_info :  str
           entity_type :  str
           files :  list
                     description :  str
                     edam_term :  str
                     is_qa_qc :  bool
                     rel_path :  str
                     size :  int
                     type :  str

           group_uuid :  str
           hubmap_id :  str
           last_modified_timestamp :  int
           metadata :  dict
                dag_provenance_list :  list
                          hash :  str
                          name :  str
                          origin :  str

                files :  list
                          description :  str
                          edam_term :  str
                          is_qa_qc :  bool
                          rel_path :  str
                          size :  int
                          type :  str

           published_timestamp :  int
           status :  str
           title :  str
           uuid :  str

 index_version :  str
 last_modified_timestamp :  int
 mapped_consortium :  str
 mapped_data_access_level :  str
 mapped_data_types :  list

 mapped_last_modified_timestamp :  str
 mapped_metadata :  dict
 mapped_status :  str
 mapper_metadata :  dict
      datetime :  str
      size :  int
      validation_errors :  list
      version :  str
 metadata :  dict
      dag_provenance_list :  list
                hash :  str
                origin :  str

      extra_metadata :  dict
           collectiontype :  str
      files :  list
      metadata :  dict
           acquisition_instrument_model :  str
           acquisition_instrument_vendor :  str
           analyte_class :  str
           assay_category :  str
           assay_type :  str
           cell_barcode_read :  str
           cell_barcode_size :  str
           contributors_path :  str
           description :  str
           execution_datetime :  str
           expected_cell_count :  int
           is_targeted :  str
           is_technical_replicate :  str
           library_adapter_sequence :  str
           library_average_fragment_size :  int
           library_construction_protocols_io_doi :  str
           library_final_yield_unit :  str
           library_final_yield_value :  float
           library_id :  str
           library_layout :  str
           library_pcr_cycles :  int
           library_pcr_cycles_for_sample_index :  int
           operator :  str
           operator_email :  str
           pi :  str
           pi_email :  str
           protocols_io_doi :  str
           rnaseq_assay_input :  int
           rnaseq_assay_method :  str
           sc_isolation_cell_number :  int
           sc_isolation_enrichment :  str
           sc_isolation_entity :  str
           sc_isolation_protocols_io_doi :  str
           sc_isolation_quality_metric :  str
           sc_isolation_tissue_dissociation :  str
           sequencing_phix_percent :  int
           sequencing_read_format :  str
           sequencing_read_percent_q30 :  float
           sequencing_reagent_kit :  str
 origin_sample :  dict
      created_by_user_displayname :  str
      created_by_user_email :  str
      created_timestamp :  int
      data_access_level :  str
      entity_type :  str
      group_uuid :  str
      hubmap_id :  str
      last_modified_timestamp :  int
      mapped_data_access_level :  str
      mapped_last_modified_timestamp :  str
      mapped_organ :  str
      mapped_sample_category :  str
      organ :  str
      protocol_url :  str
      sample_category :  str
      specimen_type :  str
      submission_id :  str
      tissue_type :  str
      uuid :  str
 origin_samples :  list
           created_by_user_displayname :  str
           created_by_user_email :  str
           created_timestamp :  int
           data_access_level :  str
           entity_type :  str
           group_uuid :  str
           hubmap_id :  str
           last_modified_timestamp :  int
           mapped_data_access_level :  str
           mapped_last_modified_timestamp :  str
           mapped_organ :  str
           mapped_sample_category :  str
           organ :  str
           protocol_url :  str
           sample_category :  str
           specimen_type :  str
           submission_id :  str
           tissue_type :  str
           uuid :  str

 origin_samples_unique_mapped_organs :  list

 provider_info :  str
 published_timestamp :  int
 registered_doi :  str
 source_sample :  list
           created_by_user_displayname :  str
           created_by_user_email :  str
           created_timestamp :  int
           data_access_level :  str
           description :  str
           entity_type :  str
           group_uuid :  str
           hubmap_id :  str
           lab_tissue_sample_id :  str
           last_modified_timestamp :  int
           mapped_data_access_level :  str
           mapped_last_modified_timestamp :  str
           mapped_metadata :  dict
           mapped_sample_category :  str
           metadata :  dict
                cold_ischemia_time_unit :  str
                cold_ischemia_time_value :  str
                health_status :  str
                organ_condition :  str
                pathologist_report :  str
                perfusion_solution :  str
                procedure_date :  str
                specimen_preservation_temperature :  str
                specimen_quality_criteria :  str
                specimen_tumor_distance_unit :  str
                specimen_tumor_distance_value :  str
                vital_state :  str
                warm_ischemia_time_unit :  str
                warm_ischemia_time_value :  str
           protocol_url :  str
           rui_location :  str
           sample_category :  str
           specimen_type :  str
           submission_id :  str
           tissue_type :  str
           uuid :  str

 source_samples :  list
           created_by_user_displayname :  str
           created_by_user_email :  str
           created_timestamp :  int
           data_access_level :  str
           description :  str
           entity_type :  str
           group_uuid :  str
           hubmap_id :  str
           lab_tissue_sample_id :  str
           last_modified_timestamp :  int
           mapped_data_access_level :  str
           mapped_last_modified_timestamp :  str
           mapped_metadata :  dict
           mapped_sample_category :  str
           metadata :  dict
                cold_ischemia_time_unit :  str
                cold_ischemia_time_value :  str
                health_status :  str
                organ_condition :  str
                pathologist_report :  str
                perfusion_solution :  str
                procedure_date :  str
                specimen_preservation_temperature :  str
                specimen_quality_criteria :  str
                specimen_tumor_distance_unit :  str
                specimen_tumor_distance_value :  str
                vital_state :  str
                warm_ischemia_time_unit :  str
                warm_ischemia_time_value :  str
           protocol_url :  str
           rui_location :  str
           sample_category :  str
           specimen_type :  str
           submission_id :  str
           tissue_type :  str
           uuid :  str

 status :  str
 title :  str
 uuid :  str

```




