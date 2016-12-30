from sas7bdat import SAS7BDAT

def return_rest():
    with SAS7BDAT('idmp_ui_sample_table.sas7bdat') as f:
        df = f.to_data_frame()
    return df.to_json(orient='records')
