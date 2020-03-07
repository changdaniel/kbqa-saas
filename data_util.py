import questions_generator
import kb_generator
import vocab2id_generator
import json
from sys import argv


# ------------------------- Data Input -------------------------
def load_data(infile_path):
    """
    Description: Loads data from specified format into dictionary
    Parameters: (str) Filepath of data file
    Return: (Dict) Dictionary containing raw_data
    """
    with open(infile_path, 'r') as infile:
        data = json.load(infile)

    return data


def load_vocab(infile_path = 'vocab2id.json'):
    """
    Description: Loads data from specified format into dictionary
    Parameters: (str) Filepath of data file
    Return: (Dict) Dictionary containing raw_data
    """
    with open(infile_path, 'r') as infile:
        old_vocab = json.load(infile)

    return old_vocab


# ------------------------- Data Output -------------------------
def write_kb_data(knowledge_base):

    def format_kb(knowledge_base):

        output = ""
        for entity, entity_info in knowledge_base.items():

            entity_node = {entity: entity_info}
            output += str(entity_node) + "\n"

        return output
        
    with open('freebase_full.json','w') as kb_outfile:

        formmatted_kb = format_kb(knowledge_base)
        kb_outfile.write(formmatted_kb)



def write_questions_data(train_questions, valid_questions):

    def format_questions(questions):
        output = ""
        for decorated_question in questions:
            output += str(decorated_question) + "\n"

        return output

    with open('raw_valid.json', 'w') as valid_outfile:
        formatted_valid = format_questions(valid_questions)
        valid_outfile.write(formatted_valid)
    
    with open('raw_train.json', 'w') as train_outfile:
        formatted_train = format_questions(valid_questions)
        train_outfile.write(formatted_train)


def write_vocab2id(new_vocab):

    with open('new_vocab2id.json', 'w') as vocab_outfile:
        json.dump(new_vocab, vocab_outfile)


# ------------------------- Main -------------------------
if __name__ == "__main__":

    data_infile_path = argv[1]
    data = load_data(data_infile_path)
    old_vocab = load_vocab()

    knowledge_base = kb_generator.create_knowledge_base(data)
    print('Knowledge base generated')
    train_questions, valid_questions = questions_generator.generate_question_sets(data)
    print('Questions generated')
    new_vocab = vocab2id_generator.augment_vocab(data, old_vocab)
    print('Vocab2id augmented')

    write_kb_data(knowledge_base)
    print('Knowledge base written')
    write_questions_data(train_questions, valid_questions)
    print('Questions written')
    write_vocab2id(new_vocab)
    print('Vocab written')


