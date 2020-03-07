from functools import reduce

# ------------------------- Entity2id Generation -------------------------
def count_fields(data):
    """
    Description: 
    Parameters: 
    Return: 
    """
    num_fields = reduce(lambda field_count, field_list: field_count + len(field_list), data.values(), 0)

    return num_fields

def generate_entity2id(data):
    """
    Description: 
    Parameters: 
    Return: 
    """

    num_fields = count_fields(data)
    default_entity2id = {"PAD": 0, "UNK": 1}
    additional_entity2id = {"/m/{}".format(i): i for i in range(2, num_fields + 2)}
    default_entity2id.update(additional_entity2id)
    return default_entity2id