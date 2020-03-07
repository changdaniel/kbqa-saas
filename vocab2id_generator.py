# ------------------------- Vocab2id Augmentation -------------------------
def augment_vocab(data, old_vocab):


    start_index = max(old_vocab.values())
    vocab = old_vocab

    for entity in data.keys():
        
        entity_lower = entity.lower()
        
        if entity_lower not in old_vocab:
            vocab[entity_lower] = start_index = start_index + 1
            

    return old_vocab