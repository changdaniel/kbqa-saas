import questions_generator
import kb_generator
import vocab2id_augmentor
import entity2id_generator
import relation2id_generator
import entityType2id_generator
import data_filter
import json
from sys import argv
import os

### TODO: Write function signatures for data output and formatting.

# ------------------------- Data Input -------------------------


def load_data(infile_dir="./", infile_path='result_spy.json'):
    """
    Description: Loads data from specified format into dictionary
    Parameters: (str) Filepath of data file
    Return: (Dict) Dictionary containing raw_data
    """
    path = os.path.join(infile_dir, infile_path)
    with open(path, 'r') as infile:
        data = json.load(infile)

    return data


def load_vocab(infile_dir="./", infile_path='vocab2id.json'):
    """
    Description: Loads data from specified format into dictionary
    Parameters: (str) Filepath of data file
    Return: (Dict) Dictionary containing raw_data
    """
    path = os.path.join(infile_dir, infile_path)
    with open(path, 'r') as infile:
        old_vocab = json.load(infile)

    return old_vocab


# ------------------------- Data Formatting -------------------------
def format_kb(knowledge_base):
    """
    Description: 
    Parameters: 
    Return: 
    """
    output = ""
    for entity, entity_info in knowledge_base.items():

        entity_node = {entity: entity_info}
        output += json.dumps(entity_node) + "\n"

    return output


def format_questions(questions):
    """
    Description: 
    Parameters: 
    Return: 
    """
    output = ""
    for decorated_question in questions:
        output += json.dumps(decorated_question) + "\n"

    return output


# ------------------------- Data Output -------------------------
def write_kb_data(knowledge_base, dir_name):
    """
    Description: 
    Parameters: 
    Return: 
    """
    kb_path = os.path.join(dir_name, 'freebase_full.json')
    with open(kb_path, 'w') as kb_outfile:

        formmatted_kb = format_kb(knowledge_base)
        kb_outfile.write(formmatted_kb)


def write_questions_data(train_questions, valid_questions, dir_name):
    """
    Description: 
    Parameters: 
    Return: 
    """
    valid_path = os.path.join(dir_name, 'raw_valid.json')
    with open(valid_path, 'w') as valid_outfile:
        formatted_valid = format_questions(valid_questions)
        valid_outfile.write(formatted_valid)

    train_path = os.path.join(dir_name, 'raw_train.json')
    with open(train_path, 'w') as train_outfile:
        formatted_train = format_questions(train_questions)
        train_outfile.write(formatted_train)


def write_vocab2id(new_vocab, dir_name):
    """
    Description: 
    Parameters: 
    Return: 
    """
    vocab_path = os.path.join(dir_name, 'vocab2id.json')
    with open(vocab_path, 'w') as vocab_outfile:
        json.dump(new_vocab, vocab_outfile)


def write_entity2id(new_entity, dir_name):
    """
    Description: 
    Parameters: 
    Return: 
    """
    entity_path = os.path.join(dir_name, 'entity2id.json')
    with open(entity_path, 'w') as entity_outfile:
        json.dump(new_entity, entity_outfile)


def write_relation2id(new_relation, dir_name):
    """
    Description: 
    Parameters: 
    Return: 
    """
    relation_path = os.path.join(dir_name, 'relation2id.json')
    with open(relation_path, 'w') as relation_outfile:
        json.dump(new_relation, relation_outfile)


def write_entityType2id(new_entityType, dir_name):
    """
    Description: 
    Parameters: 
    Return: 
    """
    relation_path = os.path.join(dir_name, 'entityType2id.json')
    with open(relation_path, 'w') as entityType_outfile:
        json.dump(new_relation, entityType_outfile)

# ------------------------- Main -------------------------


if __name__ == "__main__":

    infile_dir = "./" if len(argv) <= 1 else argv[1]
    data = load_data(infile_dir=infile_dir)
    old_vocab = load_vocab(infile_dir=infile_dir)

    test = ['url', 'investor relations url', 'sector', 'industry', 'equity style', 'next earnings release', 'last earnings release', 'next ex-dividend date', 'last ex-dividend date', 'description', 'existing metric alerts', '1 month price returns (daily)', '3 month price returns (daily)', '6 month price returns (daily)', 'year to date price returns (daily)', '1 year price returns (daily)', '3 year price returns (daily)', '52 week high (daily)', '52 week low (daily)', '52-week high date', '52-week low date', 'shares outstanding', 'dividend', 'dividend yield (forward)', 'dividend yield', 'cash dividend payout ratio', 'payout ratio', 'latest dividend pay date', 'last split factor', 'last split date', 'beta (5y)', 'max drawdown (all)', 'daily value at risk (var) 1% (all)', 'daily value at risk (var) 5% (all)', 'monthly value at risk (var) 5% (all)', 'monthly value at risk (var) 1% (all)', 'revenue estimates for current quarter', 'revenue estimates for current fiscal year', 'eps estimates for current quarter', 'eps estimates for current fiscal year', 'pe ratio (forward)', 'pe ratio (forward 1y)', 'ps ratio (forward)', 'ps ratio (forward 1y)', 'price target upside (daily)', 'revenue (ttm)', 'revenue (per share quarterly)', 'revenue (quarterly yoy growth)', 'eps diluted (ttm)', 'eps diluted (quarterly yoy growth)', 'net income (ttm)', 'ebitda (ttm)', 'total assets (quarterly)', 'cash and short term investments (quarterly)', 'book value (per share)', 'tangible book value (per share)', 'total liabilities (quarterly)', 'non-current portion of long term debt (quarterly)', 'total long term debt (quarterly)', 'shareholders equity (quarterly)', 'cash from financing (ttm)', 'cash from investing (ttm)', 'cash from operations (ttm)', 'capital expenditures (ttm)', 'net income (% of quarterly revenues)', 'net income (% of annual revenues)', 'accruals (quarterly)', 'beneish m-score (annual)', 'gross profit margin (quarterly)', 'profit margin (quarterly)', 'ebitda margin (ttm)', 'operating margin (ttm)', 'asset utilization (ttm)', 'days sales outstanding (quarterly)', 'days inventory outstanding (quarterly)', 'days payable outstanding (quarterly)', 'receivables turnover (quarterly)', 'return on assets', 'return on equity', 'return on invested capital', 'market cap', 'enterprise value', 'pe ratio', 'pe 10', 'peg ratio', 'earnings yield', 'ps ratio', 'price to book value', 'ev to revenues', 'ev to ebitda', 'ev to ebit', 'operating pe ratio', 'operating earnings yield', 'altman z-score (ttm)', 'current ratio', 'debt to equity ratio', 'free cash flow (quarterly)', 'kz index (annual)', 'tangible common equity ratio (quarterly)', 'times interest earned (ttm)', 'total employees (annual)', 'revenue per employee (annual)', 'net income per employee (annual)', 'ca score (ttm)', 'piotroski f score (ttm)', 'fulmer h factor (ttm)', "graham's number (ttm)", 'net current asset value per share (ncavps) (quarterly)', 'ohlson score (ttm)', 'quality ratio (ttm)', 'springate score (ttm)', 'sustainable growth rate (ttm)', "tobin's q (approximate) (quarterly)", 'zmijewski score (ttm)', 'momentum score', 'market cap score', 'quality ratio score']

    knowledge_base = kb_generator.create_knowledge_base(data)
    print('Knowledge base generated')
    train_questions, valid_questions = questions_generator.generate_question_sets(data)
    print('Questions generated')
    new_vocab = vocab2id_augmentor.augment_vocab(data, old_vocab)
    print('Vocab2id augmented')
    new_entity = entity2id_generator.generate_entity2id(data)
    print('Entity2id generated')
    new_relation = relation2id_generator.generate_relation2id(data)
    print('Relation2id generated')
    new_entityType = entityType2id_generator.generate_entityType2id(data)
    print('EntityType2id generated')

    dir_name = 'data'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    write_kb_data(knowledge_base, dir_name)
    print('Knowledge base written')
    write_questions_data(train_questions, valid_questions, dir_name)
    print('Questions written')
    write_vocab2id(new_vocab, dir_name)
    print('Vocab2id written')
    write_entity2id(new_entity, dir_name)
    print('Entity2id written')
    write_relation2id(new_relation, dir_name)
    print('Relation2id written')
    write_entityType2id(new_entityType, dir_name)
    print('EntityType2id written')
