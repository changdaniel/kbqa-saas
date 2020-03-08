

# ------------------------- Data Filter -------------------------
def filter_fields(data, included_fields):
    """
    Description: Filters original data to only include specified fields.
    Parameters: (Dict) Dictionary representation of raw data from load function, (List) List of fields to include in knowledge base.
    Return: (Dict) Field filtered version of raw data. 
    """
    included_fields = set(included_fields)
    field_filtered_data = {entity: {field: entity_info[field] for field in entity_info if field.lower() in included_fields} for entity, entity_info in data.items()}


    return field_filtered_data
