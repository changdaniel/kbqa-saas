


# ------------------------- Data Filter -------------------------
"""
Description: 
Parameters: 
Return: 
"""
def filter_fields(data, included_fields):

    included_fields = set(included_fields)
    field_filtered_data = {entity: {field: entity_info[field] for field in entity_info if field in included_fields} for entity, entity_info in data.items()}


    return field_filtered_data
