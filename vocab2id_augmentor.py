# ------------------------- Vocab2id Augmentation -------------------------
def augment_vocab(data, old_vocab):
    """
    Description: Adds new topic entities to vocab2id. Starts off from last index.
    Parameters: (Dict) Raw data from load functions, (Dict) Original vocab2id.
    Return: (Dict) Vocab2id augmented with new topic entities.
    """
    start_index = max(old_vocab.values())
    vocab = old_vocab

    for entity in data.keys():
        
        entity_lower = entity.lower()
        
        if entity_lower not in old_vocab:
            vocab[entity_lower] = start_index = start_index + 1
            

    return vocab