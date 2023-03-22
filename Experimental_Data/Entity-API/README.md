# HuBMAP Entity API

A set of standard RESTful web service that provides CRUD operations into our entity metadata store. A description of the API calls is found here: [Entities API](https://smart-api.info/ui/0065e419668f3336a40d1f5ab89c6ba3).

### [Diagram-Link](https://app.diagrams.net/#G1REdLjoMMJaP6tBk-P2wAPLvq50BI7lfw)

![image](https://github.com/Aashay7/organizing_data_HRAlit/blob/main/Experimental_Data/Entity-API/entity_api.png)

### Contents:
- `entity_api_data.ipynb` : Python notebook file to query the `Entity API`. 
- `entity_api.png` : Entity API endpoint responses visualized. 




## Entity API Specifications (March 22 2023)

[GET] Endpoints:

```
1. /entities/{id}
2. /entities-types
3. /entities/{id}/provenance
4. /entities/{id}/ancestor-organs
5. /samples/prov-info
6. /ancestors/{id}
7. /descendants/{id}
8. /parents/{id}
9. /children/{id}
10. /collections/{id}
11. /datasets/{id}/paired-dataset
12. /datasets/{id}/latest-revision
13. /datasets/{id}/revision
14. /datasets/{id}/revisions
15. /datasets/prov-info
16. /datasets/{id}/prov-info
17. /datasets/sankey_data
18. /datasets/unpublished
```


### 1. `/entities/{id}` - REQUIRES [nexus_token, uuid/hubmap_id]

> Retrieve a provenance entity by id. Entity types of Donor, Sample and Datasets. 

```
 collections :  list
           contacts :  list
                     affiliation :  str
                     first_name :  str
                     last_name :  str
                     middle_name_or_initial :  str
                     name :  str
                     orcid_id :  str

           created_by_user_displayname :  str
           created_by_user_email :  str
           created_timestamp :  int
           creators :  list
                     affiliation :  str
                     first_name :  str
                     last_name :  str
                     middle_name_or_initial :  str
                     name :  str
                     orcid_id :  str

           description :  str
           doi_url :  str
           entity_type :  str
           hubmap_id :  str
           last_modified_timestamp :  int
           registered_doi :  str
           title :  str
           uuid :  str

 contacts :  list
           affiliation :  str
           first_name :  str
           last_name :  str
           middle_name_or_initial :  str
           name :  str
           orcid_id :  str

 contains_human_genetic_sequences :  bool
 contributors :  list
           affiliation :  str
           first_name :  str
           last_name :  str
           middle_name_or_initial :  str
           name :  str
           orcid_id :  str

 created_by_user_displayname :  str
 created_by_user_email :  str
 created_by_user_sub :  str
 created_timestamp :  int
 data_access_level :  str
 data_types :  list

 dataset_info :  str
 description :  str
 direct_ancestors :  list
           created_by_user_displayname :  str
           created_by_user_email :  str
           created_by_user_sub :  str
           created_timestamp :  int
           data_access_level :  str
           description :  str
           entity_type :  str
           group_name :  str
           group_uuid :  str
           hubmap_id :  str
           last_modified_timestamp :  int
           protocol_url :  str
           sample_category :  str
           specimen_type :  str
           submission_id :  str
           tissue_type :  str
           uuid :  str

 doi_url :  str
 entity_type :  str
 group_name :  str
 group_uuid :  str
 hubmap_id :  str
 ingest_id :  str
 ingest_metadata :  dict
      dag_provenance_list :  list
                hash :  str
                origin :  str

      metadata :  dict
           _from_metadatatsv :  bool
           acquisition_instrument_model :  str
           acquisition_instrument_vendor :  str
           analyte_class :  str
           assay_category :  str
           assay_type :  str
           collectiontype :  str
           data_path :  str
           donor_id :  str
           execution_datetime :  str
           is_targeted :  str
           metadata_path :  str
           ms_source :  str
           mz_range_high_value :  str
           mz_range_low_value :  str
           operator :  str
           operator_email :  str
           overall_protocols_io_doi :  str
           pi :  str
           pi_email :  str
           polarity :  str
           preparation_instrument_model :  str
           preparation_instrument_vendor :  str
           preparation_maldi_matrix :  str
           preparation_type :  str
           protocols_io_doi :  str
           resolution_x_unit :  str
           resolution_x_value :  str
           resolution_y_unit :  str
           resolution_y_value :  str
           section_prep_protocols_io_doi :  str
           tissue_id :  str
 lab_dataset_id :  str
 last_modified_timestamp :  int
 last_modified_user_displayname :  str
 last_modified_user_email :  str
 last_modified_user_sub :  str
 local_directory_rel_path :  str
 pipeline_message :  str
 published_timestamp :  int
 published_user_displayname :  str
 published_user_email :  str
 published_user_sub :  str
 registered_doi :  str
 run_id :  str
 status :  str
 title :  str
 uuid :  str

```


### 2. `/entity-types`

> Get a list of all the available entity types defined in the schema yaml

Response:
```
 ['Collection', 'Dataset', 'Publication', 'Donor', 'Sample', 'Upload']

```





### 3. `/entities/{id}/provenance` - REQUIRES [nexus_token, uuid/hubmap_id]

> Get Provenance Data for Entity. This returns a PROV JSON compliant representation of the entity's provenance. Refer to this document for more information regarding [PROV JSON format](https://www.w3.org/Submission/2013/SUBM-prov-json-20130424/)

```
  prefix :  dict
      hubmap :  str
 agent :  dict
      hubmap:agent/ce74ea5c-86bd-44b1-bfc4-4459d4fe20b5 :  dict
           prov:type :  dict
                $ :  str
                type :  str
           hubmap:userDisplayName :  str
           hubmap:userEmail :  str
           hubmap:userUUID :  str
      hubmap:organization/73bb26e4-ed43-11e8-8f19-0a7c1eab007a :  dict
           prov:type :  dict
                $ :  str
                type :  str
           hubmap:groupUUID :  str
           hubmap:groupName :  str
      hubmap:agent/83ae233d-6d1d-40eb-baa7-b6f636ab579a :  dict
           prov:type :  dict
                $ :  str
                type :  str
           hubmap:userDisplayName :  str
           hubmap:userEmail :  str
           hubmap:userUUID :  str

 activity :  dict
      hubmap:activities/[uuid] :  dict
           prov:startTime :  str
           prov:endTime :  str
           prov:type :  str
           hubmap:created_by_user_sub :  str
           hubmap:uuid :  str
           hubmap:created_by_user_email :  str
           hubmap:created_by_user_displayname :  str
           hubmap:creation_action :  str
           hubmap:created_timestamp :  str
           hubmap:hubmap_id :  str
      
 actedOnBehalfOf :  dict
      [id] :  dict
           prov:delegate :  str
           prov:responsible :  str
           prov:activity :  str
    
      
 entity :  dict
      hubmap:entities/[uuid] :  dict
           prov:type :  str
           hubmap:data_access_level :  str
           hubmap:dataset_info :  str
           hubmap:pipeline_message :  str
           hubmap:published_user_email :  str
           hubmap:created_by_user_sub :  str
           hubmap:last_modified_user_email :  str
           hubmap:description :  str
           hubmap:uuid :  str
           hubmap:created_by_user_email :  str
           hubmap:local_directory_rel_path :  str
           hubmap:ingest_id :  str
           hubmap:published_user_sub :  str
           hubmap:last_modified_user_sub :  str
           hubmap:registered_doi :  str
           hubmap:created_by_user_displayname :  str
           hubmap:entity_type :  str
           hubmap:last_modified_user_displayname :  str
           hubmap:run_id :  str
           hubmap:published_user_displayname :  str
           hubmap:group_name :  str
           hubmap:status :  str
           hubmap:last_modified_timestamp :  str
           hubmap:doi_url :  str
           hubmap:created_timestamp :  str
           hubmap:group_uuid :  str
           hubmap:hubmap_id :  str
           hubmap:contains_human_genetic_sequences :  bool
           hubmap:published_timestamp :  str
           hubmap:lab_dataset_id :  str
           hubmap:title :  str

 wasGeneratedBy :  dict
      [id] :  dict
           prov:entity :  str
           prov:activity :  str
      
 used :  dict
      [id] :  dict
           prov:activity :  str
           prov:entity :  str
      

```

### Note: 
```
-> [id] refers to the id present in the dictionary. For example: _:id1, _:id3, _:id6, _:i9, _:id12, _:id15, 

-> [uuid] refers to the uuid of the entity. For example: 6e95d91da2870ffc0a473c23038fc5e1
 
```




### 4. `/entities/{id}/ancestor-organs` - REQUIRES [nexus_token, uuid/hubmap_id]

> Retrieves a list of ancestor organ(s) of a given uuid

```
      created_by_user_displayname :  str
      created_by_user_email :  str
      created_by_user_sub :  str
      created_timestamp :  int
      data_access_level :  str
      entity_type :  str
      group_name :  str
      group_uuid :  str
      hubmap_id :  str
      lab_tissue_sample_id :  str
      last_modified_timestamp :  int
      last_modified_user_displayname :  str
      last_modified_user_email :  str
      last_modified_user_sub :  str
      organ :  str
      portal_metadata_upload_files :  list
                description :  str
                filepath :  str

      protocol_url :  str
      sample_category :  str
      specimen_type :  str
      submission_id :  str
      tissue_type :  str
      uuid :  str
```



### 5. `/samples/prov-info` - REQUIRES [nexus_token, group_uuid] 

> Returns all provenance information for a  each sample in a json format.

```
      donor_has_metadata :  bool
      donor_hubmap_id :  str
      donor_submission_id :  str
      donor_uuid :  str
      lab_id_or_name :  str
      organ_hubmap_id :  str
      organ_submission_id :  str
      organ_type :  str
      organ_uuid :  str
      sample_ancestor_entity :  str
      sample_ancestor_id :  str
      sample_created_by_email :  str
      sample_group_name :  str
      sample_has_metadata :  bool
      sample_has_rui_info :  bool
      sample_hubmap_id :  str
      sample_submission_id :  str
      sample_type :  str
      sample_uuid :  str

```


### 6. `/ancestors/{id}` - REQUIRES [nexus_token, uuid/hubmap_id] 

> Gets the ancestor list for an Entity. The ancestors are the nodes connected "upstream" from the current node. This list traverses all the levels in the graph.

```
      created_by_user_displayname :  str
      created_by_user_email :  str
      created_by_user_sub :  str
      created_timestamp :  int
      data_access_level :  str
      description :  str
      entity_type :  str
      group_name :  str
      group_uuid :  str
      hubmap_id :  str
      lab_tissue_sample_id :  str
      last_modified_timestamp :  int
      last_modified_user_displayname :  str
      last_modified_user_email :  str
      last_modified_user_sub :  str
      metadata :  dict
           cold_ischemia_time_unit :  str
           cold_ischemia_time_value :  str
           health_status :  str
           organ_condition :  str
           pathologist_report :  str
           perfusion_solution :  str
           sample_id :  str
           specimen_preservation_temperature :  str
           specimen_quality_criteria :  str
           specimen_tumor_distance_unit :  str
           specimen_tumor_distance_value :  str
           vital_state :  str
           warm_ischemia_time_unit :  str
           warm_ischemia_time_value :  str
      protocol_url :  str
      rui_location :  dict
           @context :  str
           @id :  str
           @type :  str
           ccf_annotations :  list

           creation_date :  str
           creator :  str
           creator_first_name :  str
           creator_last_name :  str
           dimension_units :  str
           placement :  dict
                @context :  str
                @id :  str
                @type :  str
                placement_date :  str
                rotation_order :  str
                rotation_units :  str
                scaling_units :  str
                target :  str
                translation_units :  str
                x_rotation :  int
                x_scaling :  int
                x_translation :  float
                y_rotation :  int
                y_scaling :  int
                y_translation :  float
                z_rotation :  int
                z_scaling :  int
                z_translation :  float
           x_dimension :  int
           y_dimension :  int
           z_dimension :  int
      sample_category :  str
      specimen_type :  str
      submission_id :  str
      tissue_type :  str
      uuid :  str

```



### 7. `/descendants/{id}` - REQUIRES [nexus_token, uuid/hubmap_id] 

> Get the descendant for an Entity. The descendants are the nodes "downstream" from the current node. This list traverses all the levels in the graph. Returns all descendants as an array of Entities.


```
      contains_human_genetic_sequences :  bool
      created_by_user_displayname :  str
      created_by_user_email :  str
      created_by_user_sub :  str
      created_timestamp :  int
      data_access_level :  str
      data_types :  list

      dataset_info :  str
      entity_type :  str
      group_name :  str
      group_uuid :  str
      hubmap_id :  str
      ingest_metadata :  dict
           dag_provenance_list :  list
                     hash :  str
                     name :  str
                     origin :  str

           files :  list
                     description :  str
                     edam_term :  str
                     rel_path :  str
                     size :  int
                     type :  str

      lab_dataset_id :  str
      last_modified_timestamp :  int
      last_modified_user_displayname :  str
      last_modified_user_email :  str
      last_modified_user_sub :  str
      local_directory_rel_path :  str
      pipeline_message :  str
      published_timestamp :  int
      published_user_displayname :  str
      published_user_email :  str
      published_user_sub :  str
      status :  str
      uuid :  str

```



### 8. `/parents/{id}` - REQUIRES [nexus_token, uuid/hubmap_id] 

> Get the immediate parent for an Entity. The parents are the nodes connected one level "upstream" from the current node. This list only goes to the next higher level in the graph. 


```
      created_by_user_displayname :  str
      created_by_user_email :  str
      created_by_user_sub :  str
      created_timestamp :  int
      data_access_level :  str
      description :  str
      entity_type :  str
      group_name :  str
      group_uuid :  str
      hubmap_id :  str
      lab_tissue_sample_id :  str
      last_modified_timestamp :  int
      last_modified_user_displayname :  str
      last_modified_user_email :  str
      last_modified_user_sub :  str
      metadata :  dict
           cold_ischemia_time_unit :  str
           cold_ischemia_time_value :  str
           health_status :  str
           organ_condition :  str
           pathologist_report :  str
           perfusion_solution :  str
           sample_id :  str
           specimen_preservation_temperature :  str
           specimen_quality_criteria :  str
           specimen_tumor_distance_unit :  str
           specimen_tumor_distance_value :  str
           vital_state :  str
           warm_ischemia_time_unit :  str
           warm_ischemia_time_value :  str
      protocol_url :  str
      rui_location :  dict
           @context :  str
           @id :  str
           @type :  str
           ccf_annotations :  list

           creation_date :  str
           creator :  str
           creator_first_name :  str
           creator_last_name :  str
           dimension_units :  str
           placement :  dict
                @context :  str
                @id :  str
                @type :  str
                placement_date :  str
                rotation_order :  str
                rotation_units :  str
                scaling_units :  str
                target :  str
                translation_units :  str
                x_rotation :  int
                x_scaling :  int
                x_translation :  float
                y_rotation :  int
                y_scaling :  int
                y_translation :  float
                z_rotation :  int
                z_scaling :  int
                z_translation :  float
           x_dimension :  int
           y_dimension :  int
           z_dimension :  int
      sample_category :  str
      specimen_type :  str
      submission_id :  str
      tissue_type :  str
      uuid :  str

```



### 9. `/children/{id}` - REQUIRES [nexus_token, uuid/hubmap_id] 

> Get the list of children directly connected to an Entity. The children are the nodes one level below the current nodes. This list only returns the items one level below in the graph.


```
      contains_human_genetic_sequences :  bool
      created_by_user_displayname :  str
      created_by_user_email :  str
      created_by_user_sub :  str
      created_timestamp :  int
      data_access_level :  str
      data_types :  list

      dataset_info :  str
      entity_type :  str
      group_name :  str
      group_uuid :  str
      hubmap_id :  str
      ingest_metadata :  dict
           dag_provenance_list :  list
                     hash :  str
                     name :  str
                     origin :  str

           files :  list
                     description :  str
                     edam_term :  str
                     rel_path :  str
                     size :  int
                     type :  str

      lab_dataset_id :  str
      last_modified_timestamp :  int
      last_modified_user_displayname :  str
      last_modified_user_email :  str
      last_modified_user_sub :  str
      local_directory_rel_path :  str
      pipeline_message :  str
      published_timestamp :  int
      published_user_displayname :  str
      published_user_email :  str
      published_user_sub :  str
      status :  str
      uuid :  str

```



### 10. `/collections/{id}` - REQUIRES [nexus_token, uuid/hubmap_id] 

> Returns the information of the Collection specified by the uuid with all connected datasets. If a valid token is provided with group membership in the HuBMAP-Read group any collection matching the id will be returned. Otherwise if no token is provided or a valid token with no HuBMAP-Read group membership then only a public collection will be returned. Public collections are defined as being published via a DOI (collection.doi_registered == true) and at least one of the connected datasets is public (dataset.metadata.data_access_level == 'public'). For public collections only connected datasets that are public are returned with it.


```
[
  {
    "created_timestamp": 0,
    "created_by_user_displayname": "string",
    "created_by_user_email": "string",
    "created_by_user_sub": "string",
    "uuid": "string",
    "hubmap_id": "string",
    "last_modified_timestamp": 0,
    "last_modified_user_sub": "string",
    "last_modified_user_email": "string",
    "last_modified_user_displayname": "string",
    "entity_type": "string",
    "registered_doi": "string",
    "doi_url": "string",
    "creators": [
      {
        "first_name": "string",
        "last_name": "string",
        "middle_name_or_initial": "string",
        "orcid_id": "string",
        "affiliation": "string"
      }
    ],
    "contacts": [
      {
        "first_name": "string",
        "last_name": "string",
        "middle_name_or_initial": "string",
        "orcid_id": "string",
        "affiliation": "string"
      }
    ],
    "title": "string",
    "datasets": [
      {
        "created_timestamp": 0,
        "created_by_user_displayname": "string",
        "created_by_user_email": "string",
        "created_by_user_sub": "string",
        "uuid": "string",
        "hubmap_id": "string",
        "error_message": "string",
        "last_modified_timestamp": 0,
        "last_modified_user_sub": "string",
        "last_modified_user_email": "string",
        "last_modified_user_displayname": "string",
        "entity_type": "string",
        "registered_doi": "string",
        "doi_url": "string",
        "creators": [
          {
            "first_name": "string",
            "last_name": "string",
            "middle_name_or_initial": "string",
            "orcid_id": "string",
            "affiliation": "string"
          }
        ],
        "contacts": [
          {
            "first_name": "string",
            "last_name": "string",
            "middle_name_or_initial": "string",
            "orcid_id": "string",
            "affiliation": "string"
          }
        ],
        "antibodies": [
          {
            "antibody_name": "string",
            "channel_id": "string",
            "conjugated_cat_number": "string",
            "conjugated_tag": "string",
            "dilution": "string",
            "lot_number": "string",
            "rr_id": "string",
            "uniprot_accession_number": "string"
          }
        ],
        "description": "string",
        "data_access_level": "public",
        "contains_human_genetic_sequences": true,
        "status": "New",
        "title": "string",
        "data_types": [
          "AF"
        ],
        "collections": [
          "string"
        ],
        "upload": [
          {
            "created_timestamp": 0,
            "created_by_user_displayname": "string",
            "created_by_user_email": "string",
            "created_by_user_sub": "string",
            "uuid": "string",
            "hubmap_id": "string",
            "last_modified_timestamp": 0,
            "last_modified_user_sub": "string",
            "last_modified_user_email": "string",
            "last_modified_user_displayname": "string",
            "entity_type": "string",
            "description": "string",
            "title": "string",
            "status": "string",
            "validation_message": "string",
            "group_uuid": "string",
            "group_name": "string",
            "datasets": [
              "string"
            ]
          }
        ],
        "contributors": [
          {
            "first_name": "string",
            "last_name": "string",
            "middle_name_or_initial": "string",
            "orcid_id": "string",
            "affiliation": "string"
          }
        ],
        "direct_ancestors": [
          {
            "created_timestamp": 0,
            "created_by_user_displayname": "string",
            "created_by_user_email": "string",
            "created_by_user_sub": "string",
            "uuid": "string",
            "hubmap_id": "string",
            "last_modified_timestamp": 0,
            "last_modified_user_sub": "string",
            "last_modified_user_email": "string",
            "last_modified_user_displayname": "string",
            "entity_type": "string",
            "registered_doi": "string",
            "doi_url": "string",
            "creators": [
              {
                "first_name": "string",
                "last_name": "string",
                "middle_name_or_initial": "string",
                "orcid_id": "string",
                "affiliation": "string"
              }
            ],
            "contacts": [
              {
                "first_name": "string",
                "last_name": "string",
                "middle_name_or_initial": "string",
                "orcid_id": "string",
                "affiliation": "string"
              }
            ],
            "description": "string",
            "data_access_level": "consortium",
            "sample_category": "organ",
            "specimen_type": "atacseq",
            "specimen_type_other": "string",
            "protocol_url": "string",
            "group_uuid": "string",
            "group_name": "string",
            "organ": "AO",
            "organ_other": "string",
            "direct_ancestor": {},
            "submission_id": "string",
            "lab_tissue_sample_id": "string",
            "metadata": {
              "sample_id": "string",
              "vital_state": "living",
              "health_status": "cancer",
              "organ_condition": "healthy",
              "procedure_date": "string",
              "perfusion_solution": "UWS",
              "pathologist_report": "string",
              "warm_ischemia_time_value": 0,
              "warm_ischemia_time_unit": "string",
              "cold_ischemia_time_value": 0,
              "cold_ischemia_time_unit": "string",
              "specimen_preservation_temperature": "string",
              "specimen_quality_criteria": "string",
              "specimen_tumor_distance_value": "string",
              "specimen_tumor_distance_unit": "string"
            },
            "rui_location": {},
            "visit": "string",
            "image_files": [
              {
                "filename": "string",
                "description": "string",
                "file_uuid": "string"
              }
            ],
            "metadata_files": [
              {
                "filename": "string",
                "description": "string",
                "file_uuid": "string"
              }
            ],
            "metadata_files_to_add": [
              "string"
            ],
            "metadata_files_to_remove": [
              "string"
            ]
          },
          "string"
        ],
        "published_timestamp": 0,
        "published_user_displayname": "string",
        "published_user_sub": "string",
        "published_user_email": "string",
        "ingest_metadata": {},
        "local_directory_rel_path": "string",
        "group_uuid": "string",
        "group_name": "string",
        "previous_revision_uuid": "string",
        "next_revision_uuid": "string",
        "thumbnail_file": "string",
        "sub_status": "string",
        "retraction_reason": "string",
        "dbgap_sra_experiment_url": "string",
        "dbgap_study_url": "string"
      }
    ]
  }
]

```






### 11. `/datasets/{id}/paired-dataset` - REQUIRES [nexus_token, uuid/hubmap_id] 

> Retrieve uuids for associated dataset of given data_type which shares a sample ancestor of a given dataset id.

```
[failed fetch]
```

### 12. `/datasets/{id}/latest-revision` - REQUIRES [nexus_token, uuid/hubmap_id] 

> Retrieve the latest revision of a given dataset. Public/Consortium access rules apply - if no token/consortium access the must be for a public dataset and the returned Dataset must be the latest public version. If the given dataset itself is the latest revision, meaning it has no next revisions, this dataset gets returned.

```
 contacts :  list
           affiliation :  str
           first_name :  str
           last_name :  str
           name :  str
           orcid_id :  str

 contains_human_genetic_sequences :  bool
 contributors :  list
           affiliation :  str
           first_name :  str
           last_name :  str
           middle_name_or_initial :  str
           name :  str
           orcid_id :  str

 created_by_user_displayname :  str
 created_by_user_email :  str
 created_by_user_sub :  str
 created_timestamp :  int
 data_access_level :  str
 data_types :  list

 dataset_info :  str
 description :  str
 direct_ancestors :  list
           created_by_user_displayname :  str
           created_by_user_email :  str
           created_by_user_sub :  str
           created_timestamp :  int
           data_access_level :  str
           description :  str
           entity_type :  str
           group_name :  str
           group_uuid :  str
           hubmap_id :  str
           lab_tissue_sample_id :  str
           last_modified_timestamp :  int
           last_modified_user_displayname :  str
           last_modified_user_email :  str
           last_modified_user_sub :  str
           metadata :  dict
                cold_ischemia_time_unit :  str
                cold_ischemia_time_value :  str
                health_status :  str
                organ_condition :  str
                pathologist_report :  str
                perfusion_solution :  str
                sample_id :  str
                specimen_preservation_temperature :  str
                specimen_quality_criteria :  str
                specimen_tumor_distance_unit :  str
                specimen_tumor_distance_value :  str
                vital_state :  str
                warm_ischemia_time_unit :  str
                warm_ischemia_time_value :  str
           protocol_url :  str
           rui_location :  dict
                @context :  str
                @id :  str
                @type :  str
                ccf_annotations :  list

                creation_date :  str
                creator :  str
                creator_first_name :  str
                creator_last_name :  str
                dimension_units :  str
                placement :  dict
                     @context :  str
                     @id :  str
                     @type :  str
                     placement_date :  str
                     rotation_order :  str
                     rotation_units :  str
                     scaling_units :  str
                     target :  str
                     translation_units :  str
                     x_rotation :  int
                     x_scaling :  int
                     x_translation :  float
                     y_rotation :  int
                     y_scaling :  int
                     y_translation :  float
                     z_rotation :  int
                     z_scaling :  int
                     z_translation :  float
                x_dimension :  int
                y_dimension :  int
                z_dimension :  int
           sample_category :  str
           specimen_type :  str
           submission_id :  str
           tissue_type :  str
           uuid :  str

 doi_url :  str
 entity_type :  str
 group_name :  str
 group_uuid :  str
 hubmap_id :  str
 ingest_id :  str
 ingest_metadata :  dict
      dag_provenance_list :  list
                hash :  str
                origin :  str

      metadata :  dict
           _from_metadatatsv :  bool
           acquisition_instrument_model :  str
           acquisition_instrument_vendor :  str
           analyte_class :  str
           assay_category :  str
           assay_type :  str
           cell_barcode_offset :  str
           cell_barcode_read :  str
           cell_barcode_size :  str
           collectiontype :  str
           data_path :  str
           donor_id :  str
           execution_datetime :  str
           is_targeted :  str
           is_technical_replicate :  str
           library_adapter_sequence :  str
           library_average_fragment_size :  str
           library_construction_protocols_io_doi :  str
           library_final_yield_unit :  str
           library_final_yield_value :  str
           library_id :  str
           library_layout :  str
           library_pcr_cycles :  str
           library_pcr_cycles_for_sample_index :  str
           metadata_path :  str
           operator :  str
           operator_email :  str
           other_metadata :  dict
                 :  str
                10x_Genomics_Index_well_ID :  str
                Concentration_ng_ul :  str
                FRAGMENT_SIZE_report_from_core :  str
                HuBMAP Case Identifier :  str
                Name :  str
                Path :  str
                Quantification_method :  str
                Run_date_reported_from_ICBR :  str
                SI_INDEX_SEQUENCE :  str
                Seq_run :  str
                Sequencing_concentration_reported_from_ICBR :  str
                UUID Identifier :  str
                Volume_ul :  str
                fragment_analysis_method_report_from_core :  str
                qPCR_library_quantification_results :  str
                qPCR_quantification_method :  str
           pi :  str
           pi_email :  str
           protocols_io_doi :  str
           rnaseq_assay_input :  str
           rnaseq_assay_method :  str
           sc_isolation_cell_number :  str
           sc_isolation_enrichment :  str
           sc_isolation_entity :  str
           sc_isolation_protocols_io_doi :  str
           sc_isolation_quality_metric :  str
           sc_isolation_tissue_dissociation :  str
           sequencing_phix_percent :  str
           sequencing_read_format :  str
           sequencing_read_percent_q30 :  str
           sequencing_reagent_kit :  str
           tissue_id :  str
 lab_dataset_id :  str
 last_modified_timestamp :  int
 last_modified_user_displayname :  str
 last_modified_user_email :  str
 last_modified_user_sub :  str
 local_directory_rel_path :  str
 pipeline_message :  str
 published_timestamp :  int
 published_user_displayname :  str
 published_user_email :  str
 published_user_sub :  str
 registered_doi :  str
 run_id :  str
 status :  str
 title :  str
 uuid :  str

```

### 13,14. `/datasets/{id}/revisions` - REQUIRES [nexus_token, uuid/hubmap_id, include_dataset=False]

> From a given ID of a versioned dataset, retrieve a list of every dataset in the chain ordered from most recent to oldest. The revision number, as well as the dataset uuid will be included. An optional parameter ?include_dataset=true will include the full dataset for each revision as well. Public/Consortium access rules apply, if is for a non-public dataset and no token or a token without membership in HuBMAP-Read group is sent with the request then a 403 response should be returned. If the given id is published, but later revisions are not and the user is not in HuBMAP-Read group, only published revisions will be returned. The field next_revision_uuid will not be returned if the next revision is unpublished

```
      revision_number :  int
      uuid :  str

```

### 13,14. `/datasets/{id}/revisions` - REQUIRES [nexus_token, uuid/hubmap_id, include_dataset=True]

> From a given ID of a versioned dataset, retrieve a list of every dataset in the chain ordered from most recent to oldest. The revision number, as well as the dataset uuid will be included. An optional parameter ?include_dataset=true will include the full dataset for each revision as well. Public/Consortium access rules apply, if is for a non-public dataset and no token or a token without membership in HuBMAP-Read group is sent with the request then a 403 response should be returned. If the given id is published, but later revisions are not and the user is not in HuBMAP-Read group, only published revisions will be returned. The field next_revision_uuid will not be returned if the next revision is unpublished

```   
      dataset :  dict
           contacts :  list
                     affiliation :  str
                     first_name :  str
                     last_name :  str
                     name :  str
                     orcid_id :  str

           contains_human_genetic_sequences :  bool
           contributors :  list
                     affiliation :  str
                     first_name :  str
                     last_name :  str
                     middle_name_or_initial :  str
                     name :  str
                     orcid_id :  str

           created_by_user_displayname :  str
           created_by_user_email :  str
           created_by_user_sub :  str
           created_timestamp :  int
           data_access_level :  str
           data_types :  list

           dataset_info :  str
           description :  str
           doi_url :  str
           entity_type :  str
           group_name :  str
           group_uuid :  str
           hubmap_id :  str
           ingest_id :  str
           ingest_metadata :  dict
                dag_provenance_list :  list
                          hash :  str
                          origin :  str

                metadata :  dict
                     _from_metadatatsv :  bool
                     acquisition_instrument_model :  str
                     acquisition_instrument_vendor :  str
                     analyte_class :  str
                     assay_category :  str
                     assay_type :  str
                     cell_barcode_offset :  str
                     cell_barcode_read :  str
                     cell_barcode_size :  str
                     collectiontype :  str
                     data_path :  str
                     donor_id :  str
                     execution_datetime :  str
                     is_targeted :  str
                     is_technical_replicate :  str
                     library_adapter_sequence :  str
                     library_average_fragment_size :  str
                     library_construction_protocols_io_doi :  str
                     library_final_yield_unit :  str
                     library_final_yield_value :  str
                     library_id :  str
                     library_layout :  str
                     library_pcr_cycles :  str
                     library_pcr_cycles_for_sample_index :  str
                     metadata_path :  str
                     operator :  str
                     operator_email :  str
                     other_metadata :  dict
                           :  str
                          10x_Genomics_Index_well_ID :  str
                          Concentration_ng_ul :  str
                          FRAGMENT_SIZE_report_from_core :  str
                          HuBMAP Case Identifier :  str
                          Name :  str
                          Path :  str
                          Quantification_method :  str
                          Run_date_reported_from_ICBR :  str
                          SI_INDEX_SEQUENCE :  str
                          Seq_run :  str
                          Sequencing_concentration_reported_from_ICBR :  str
                          UUID Identifier :  str
                          Volume_ul :  str
                          fragment_analysis_method_report_from_core :  str
                          qPCR_library_quantification_results :  str
                          qPCR_quantification_method :  str
                     pi :  str
                     pi_email :  str
                     protocols_io_doi :  str
                     rnaseq_assay_input :  str
                     rnaseq_assay_method :  str
                     sc_isolation_cell_number :  str
                     sc_isolation_enrichment :  str
                     sc_isolation_entity :  str
                     sc_isolation_protocols_io_doi :  str
                     sc_isolation_quality_metric :  str
                     sc_isolation_tissue_dissociation :  str
                     sequencing_phix_percent :  str
                     sequencing_read_format :  str
                     sequencing_read_percent_q30 :  str
                     sequencing_reagent_kit :  str
                     tissue_id :  str
           lab_dataset_id :  str
           last_modified_timestamp :  int
           last_modified_user_displayname :  str
           last_modified_user_email :  str
           last_modified_user_sub :  str
           local_directory_rel_path :  str
           pipeline_message :  str
           published_timestamp :  int
           published_user_displayname :  str
           published_user_email :  str
           published_user_sub :  str
           registered_doi :  str
           run_id :  str
           status :  str
           uuid :  str
      revision_number :  int
      uuid :  str



```

### 15. `/datasets/prov-info` - REQUIRES [nexus_token, uuid/hubmap_id]

> Returns all the provenance information for each sample in a json format.

```
      dataset_created_by_email :  str
      dataset_data_types :  list

      dataset_date_time_created :  str
      dataset_date_time_modified :  str
      dataset_group_name :  str
      dataset_group_uuid :  str
      dataset_hubmap_id :  str
      dataset_modified_by_email :  str
      dataset_portal_url :  str
      dataset_status :  str
      dataset_uuid :  str
      donor_group_name :  list

      donor_hubmap_id :  list

      donor_submission_id :  list

      donor_uuid :  list

      first_sample_hubmap_id :  list

      first_sample_portal_url :  list

      first_sample_submission_id :  list

      first_sample_type :  list

      first_sample_uuid :  list

      lab_id_or_name :  NoneType
      organ_hubmap_id :  list

      organ_submission_id :  list

      organ_type :  list

      organ_uuid :  list

      previous_version_hubmap_ids :  list
      processed_dataset_hubmap_id :  list
      processed_dataset_portal_url :  list
      processed_dataset_status :  list
      processed_dataset_uuid :  list
      rui_location_hubmap_id :  list

      rui_location_submission_id :  list

      rui_location_uuid :  list

      sample_metadata_hubmap_id :  list
      sample_metadata_submission_id :  list
      sample_metadata_uuid :  list

```





