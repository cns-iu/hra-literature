import cellxgene_census

with cellxgene_census.open_soma() as census:
    #-------------
    #cxg_datasets_information
    print(census["census_info"]["datasets"].schema)
  
    # Reads SOMADataFrame as a slice
    cell_metadata = census["census_info"]["datasets"].read()

    # Concatenates results to pyarrow.Table
    cell_metadata = cell_metadata.concat()
    
    # Converts to pandas.DataFrame
    cell_metadata = cell_metadata.to_pandas()
    
    cell_metadata.to_csv('data/experimental/cxg_datasets.csv')

    #-------------
    #cxg_summary_information
    print(census["census_info"]["summary"].schema)
  
    # Reads SOMADataFrame as a slice
    cell_metadata = census["census_info"]["summary"].read()

    # Concatenates results to pyarrow.Table
    cell_metadata = cell_metadata.concat()
    
    # Converts to pandas.DataFrame
    cell_metadata = cell_metadata.to_pandas()
    
    cell_metadata.to_csv('data/experimental/cxg_summary.csv')

    #-------------
    #cxg_cell_metadata
    print(census["census_data"]["homo_sapiens"].obs.schema)
  
    # Reads SOMADataFrame as a slice
    cell_metadata = census["census_data"]["homo_sapiens"].obs.read()

    # Concatenates results to pyarrow.Table
    cell_metadata = cell_metadata.concat()
    
    # Converts to pandas.DataFrame
    cell_metadata = cell_metadata.to_pandas()
    
    cell_metadata.to_csv('data/experimental/cxg_cell_metadata.csv')

    #-------------
    #cxg_gene_metadata
    print(census["census_data"]["homo_sapiens"].ms["RNA"].var.schema)
  
    # Reads SOMADataFrame as a slice
    cell_metadata = census["census_data"]["homo_sapiens"].ms["RNA"].var.read()

    # Concatenates results to pyarrow.Table
    cell_metadata = cell_metadata.concat()
    
    # Converts to pandas.DataFrame
    cell_metadata = cell_metadata.to_pandas()
    
    cell_metadata.to_csv('data/experimental/cxg_gene_metadata.csv')
