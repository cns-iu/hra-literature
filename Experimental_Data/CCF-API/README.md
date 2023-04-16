# CCF API

This API provides programmatic access to data registered to the CCF. More details at https://hubmapconsortium.github.io/ccf/

### [Diagram-Link](https://app.diagrams.net/#G1REdLjoMMJaP6tBk-P2wAPLvq50BI7lfw)

![image](https://github.com/Aashay7/organizing_data_HRAlit/blob/main/Experimental_Data/CCF-API/ccf_api.png)

### Contents:
- `ccf_api_data.ipynb` : Python notebook file to query the `CCF API`. 
- `ccf_api.png` : CCF API endpoint response schemas visualized. 

## CCF API (April 04 2023)

API Details: https://ccf-api.hubmapconsortium.org/#/

[GET] Endpoints:

```
1. /db-status
2. /sparql
3. /aggregate-results
4. /hubmap/rui-locations.jsonld
5. /ontology-term-occurences
6. /cell-type-term-occurences
7. /ontology-tree-model
8. /cell-type-tree-model
9. /provider-names
10. /reference-organs  [Requires {'organ-uri'}]
11. /reference-organ-scene   [Requires {'organ-uri'}]
12. /scene
13. /technology-names
14. /tissue-blocks
15. /gtex/rui_locations.jsonld
```

[POST] Endpoints:

```
1. /sparql
2. /get-spatial-placement
```

### `[GET] Endpoint Response Schema`


### 1. `/db-status` 

> Retrieves the status of the database.


Schema
```
 status :  str
 message :  str
 checkback :  int
 loadTime :  int
```

API Response Example
```
{
    'status': 'Ready',
    'message': 'Database successfully loaded',
    'checkback': 3600000,
    'loadTime': 12121
}
```

### 2. `/sparql` 

> Run a SPARQL query to get the requested content.

Schema - Varies as per the input SPARQL query.

### 3. `/aggregate-results`

> Generates aggregated results based on `age` range, `bmi` range filtered by `cell-type-terms`, `ontology-terms`, `sex`, `providers`, `technologies` and `spatial-searches`

Schema
```
list of -
    label :  str
    count :  int
```

### 4. /hubmap/rui-locations.jsonld 

> Get HuBMAP registered rui-locations.

Schema
```
 @context :  dict
      @base :  str
      @vocab :  str
      ccf :  str
      rdfs :  str
      label :  str
      description :  str
      link :  dict
           @id :  str
           @type :  str
      samples :  dict
           @reverse :  str
      sections :  dict
           @id :  str
           @type :  str
      datasets :  dict
           @id :  str
           @type :  str
      rui_location :  dict
           @id :  str
           @type :  str
      ontologyTerms :  dict
           @id :  str
           @type :  str
      cellTypeTerms :  dict
           @id :  str
           @type :  str
      thumbnail :  dict
           @id :  str
 @graph :  list
           @id :  str
           @type :  str
           label :  str
           description :  str
           link :  str
           age :  int
           sex :  str
           bmi :  float
           consortium_name :  str
           provider_name :  str
           provider_uuid :  str
           samples :  list
                     @type :  str
                     sample_type :  str
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
                          slice_count :  int
                          slice_thickness :  int
                          x_dimension :  int
                          y_dimension :  int
                          z_dimension :  int
                     @id :  str
                     label :  str
                     link :  str
                     sections :  list
                               @id :  str
                               @type :  str
                               label :  str
                               description :  str
                               link :  str
                               sample_type :  str
                               section_number :  int
                               samples :  list
                               datasets :  list

                     datasets :  list
                     section_count :  int
                     section_size :  int
                     section_units :  str
                     description :  str

```


### 5. /ontology-term-occurences

> Get the ontology term occurence statistics - CCF data

Schema
```
dictionary of-
    [UBERON_ID] : int

```

Example [Note: Incomplete response - shown for reference]
```
{
    'http://purl.obolibrary.org/obo/UBERON_0002113': 94,
    'http://purl.obolibrary.org/obo/UBERON_0013702': 451,
}
```


### 6. /cell-type-term-occurences

> Get the cell type term occurence statistics - CCF data

Schema
```
dictionary of -
    [Cell_Ontology_ID] : int
```

Example [Note: Incomplete response - shown for reference]
```
{
    'http://purl.obolibrary.org/obo/CL_0000084': 173,
    'http://purl.obolibrary.org/obo/CL_0000775': 247,
}
```


### 7. /ontology-tree-model

> Returns UBERON ontology tree model based on `age` range, `bmi` range filtered by `cell-type-terms`, `ontology-terms`, `sex`, `providers`, `technologies` and `spatial-searches` entered. [Not required to specify these parameters and filters]

Schema
```
root :  str
nodes :  dict
      [UBERON_ID] :  dict
           @id :  str
           @type :  str
           id :  str
           parent :  str
           children :  list
           synonymLabels :  list
           label :  str
```

Example [Note: Incomplete response - shown for reference]
```
{
    'root': 'http://purl.obolibrary.org/obo/UBERON_0013702',
    'nodes': {
        'http://purl.obolibrary.org/obo/UBERON_0000059': {
            '@id': 'http://purl.obolibrary.org/obo/UBERON_0000059',
            '@type': 'OntologyTreeNode',
            'id': 'http://purl.obolibrary.org/obo/UBERON_0000059',
            'parent': 'http://purl.obolibrary.org/obo/UBERON_0013702',
            'children': ['http://purl.obolibrary.org/obo/UBERON_0001245',
                'http://purl.obolibrary.org/obo/UBERON_0000159',
                'http://purl.obolibrary.org/obo/UBERON_0000569',
                'http://purl.obolibrary.org/obo/UBERON_0001052',
                'http://purl.obolibrary.org/obo/UBERON_0001153',
                'http://purl.obolibrary.org/obo/UBERON_0001154',
                'http://purl.obolibrary.org/obo/UBERON_0001156',
                'http://purl.obolibrary.org/obo/UBERON_0001157',
                'http://purl.obolibrary.org/obo/UBERON_0001158',
                'http://purl.obolibrary.org/obo/UBERON_0001159',
                'http://purl.obolibrary.org/obo/UBERON_0022276',
                'http://purl.obolibrary.org/obo/UBERON_0022277'],
            'synonymLabels': [],
            'label': 'large intestine'},
        ...
    }
}
```

### 8. /cell-type-tree-model

> Returns Cell type ontology tree model based on `age` range, `bmi` range filtered by `cell-type-terms`, `ontology-terms`, `sex`, `providers`, `technologies` and `spatial-searches` entered. [Not required to specify these parameters and filters]

Schema
```
root :  str
nodes :  dict
      [Cell_Ontology_ID] :  dict
           @id :  str
           @type :  str
           id :  str
           parent :  str
           children :  list

           synonymLabels :  list

           label :  str
```

Example [Note: Incomplete response - shown for reference]
```
{
    'root': 'http://purl.obolibrary.org/obo/CL_0000000',
    'nodes': {
        'http://purl.obolibrary.org/obo/CL_0000151': {
            '@id': 'http://purl.obolibrary.org/obo/CL_0000151',
            '@type': 'OntologyTreeNode',
            'id': 'http://purl.obolibrary.org/obo/CL_0000151',
            'parent': 'http://purl.obolibrary.org/obo/CL_0000000',
            'children': [],
            'synonymLabels': [],
            'label': 'germinative (epithelial) cell, sebocyte'
        },
        'http://purl.obolibrary.org/obo/CL_0000034': {
            '@id': 'http://purl.obolibrary.org/obo/CL_0000034',
            '@type': 'OntologyTreeNode',
            'id': 'http://purl.obolibrary.org/obo/CL_0000034',
            'parent': 'http://purl.obolibrary.org/obo/CL_0000000',
            'children': [],
            'synonymLabels': ['animal stem cell'],
            'label': 'stem cell'
        },
        ...
    }
}
```




### 9. /provider-names

> Returns the names of the providers of these datapoints

Sample Response
```
['GTEx Project',
 'KPMP-IU/OSU',
 'RTI-General Electric',
 'SPARC-UCLA',
 'TMC-CalTech',
 'TMC-Florida',
 'TMC-Stanford',
 'TMC-UCSD',
 'TMC-UConn',
 'TMC-Vanderbilt']
```

### 10. /reference-organs

Returns all reference organs.

```
      @id :  str
      @type :  str
      label :  str
      creator :  str
      creator_first_name :  str
      creator_last_name :  str
      creation_date :  str
      representation_of :  str
      reference_organ :  str
      sex :  str
      side :  str
      rui_rank :  int
      x_dimension :  float
      y_dimension :  float
      z_dimension :  float
      dimension_units :  str
      object :  dict
           @id :  str
           @type :  str
           file :  str
           file_format :  str
           file_subpath :  str

```

### 11.  /reference-organ-scene

Returns all nodes to form the 3D scenes for an organ

```
list of -
    root :  str
    nodes :  dict
      http://purl.obolibrary.org/obo/CL_0000033 :  dict
           @id :  str
           @type :  str
           id :  str
           parent :  str
           children :  list
           synonymLabels :  list
           label :  str
```

### 12. /scene

Returns all nodes to form the 3D scene of reference body, organs, and tissues

```
list of -
      @id :  str
      @type :  str
      representation_of :  str
      reference_organ :  str
      scenegraph :  str
      scenegraphNode :  str
      transformMatrix :  list
      tooltip :  str
      color :  list
      opacity :  float
      unpickable :  bool
      _lighting :  str
      zoomBasedOpacity :  bool
```

### 13.  /technology-names

Response 
```
['10x', 'AF', 'CODEX', 'IMC', 'LC', 'MALDI', 'OTHER', 'PAS']
```

### 14.  /tissue-blocks

> Get the tissue blocks results 
>   filters: ['age', 'bmi', 'cell-type-terms', 'ontology-terms', 'providers', 'sex', 'spatial', 'technologies']

Response Schema
```
      @id :  str
      @type :  str
      sections :  list
      datasets :  list
                @id :  str
                @type :  str
                label :  str
                description :  str
                link :  str
                technology :  str
                thumbnail :  str

      label :  str
      description :  str
      link :  str
      sampleType :  str
      sectionCount :  int
      sectionSize :  float
      sectionUnits :  str
      donor :  dict
           @id :  str
           @type :  str
           label :  str
           description :  str
           link :  str
           providerName :  str
      spatialEntityId :  str
```

### 15.  /gtex/rui_locations.jsonld

Schema
```
list of - 
    @context :  dict
        @base :  str
        @vocab :  str
        ccf :  str
        rdfs :  str
        label :  str
        description :  str
        link :  dict
            @id :  str
            @type :  str
        samples :  dict
            @reverse :  str
        sections :  dict
            @id :  str
            @type :  str
        datasets :  dict
            @id :  str
            @type :  str
        rui_location :  dict
            @id :  str
            @type :  str
        ontologyTerms :  dict
            @id :  str
            @type :  str
        cellTypeTerms :  dict
            @id :  str
            @type :  str
        thumbnail :  dict
            @id :  str
    @graph :  list
            @id :  str
            @type :  str
            label :  str
            description :  str
            link :  str
            sex :  str
            consortium_name :  str
            provider_name :  str
            provider_uuid :  str
            samples :  list
                        @id :  str
                        @type :  str
                        label :  str
                        description :  str
                        link :  str
                        sample_type :  str
                        section_count :  int
                        section_size :  float
                        section_units :  str
                        rui_location :  dict
                            @context :  str
                            @id :  str
                            @type :  str
                            creator :  str
                            creator_first_name :  str
                            creator_last_name :  str
                            creation_date :  str
                            ccf_annotations :  list

                            x_dimension :  int
                            y_dimension :  int
                            z_dimension :  int
                            dimension_units :  str
                            placement :  dict
                                @context :  str
                                @id :  str
                                @type :  str
                                target :  str
                                placement_date :  str
                                x_scaling :  int
                                y_scaling :  int
                                z_scaling :  int
                                scaling_units :  str
                                x_rotation :  int
                                y_rotation :  int
                                z_rotation :  int
                                rotation_order :  str
                                rotation_units :  str
                                x_translation :  float
                                y_translation :  float
                                z_translation :  float
                                translation_units :  str
                        datasets :  list
                                @id :  str
                                @type :  str
                                label :  str
                                description :  str
                                link :  str
                                technology :  str
                                thumbnail :  str
```


## `[POST] Endpoints`

```
1. /sparql
2. /get-spatial-placement
```

###  1. /sparql

Returns the result of the executed SPARQL query

Schema varies based on the SPARQL query. 


### 2. /get-spatial-placement

Schema
```
 @context :  str
 @id :  str
 @type :  str
 source :  str
 target :  str
 placement_date :  str
 x_scaling :  int
 y_scaling :  int
 z_scaling :  int
 scaling_units :  str
 x_rotation :  int
 y_rotation :  int
 z_rotation :  int
 rotation_order :  str
 rotation_units :  str
 x_translation :  float
 y_translation :  float
 z_translation :  float
 translation_units :  str
 ```
