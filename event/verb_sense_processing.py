import json
import itertools
import copy
def remove_pair_same_exmple(sense_examples):
    if sense_examples[0]!= sense_examples[1]:
        return sense_examples 

def positive_dataset_prepare(verb_sense_dict):
    pos_sentence_pair_dataset = {}
    for index, sense in enumerate(verb_sense_dict['senses']):
        if len(sense['examples']) > 1: #刨除只有一个example的sense    #############有多少个只有一个example的sense？？
            sense_examples = list(itertools.product(sense['examples'], sense['examples']))      
            filtered_sense_examples = list(filter(remove_pair_same_exmple, sense_examples)) #每个sense的exmaple两两组合
            pos_sentence_pair_dataset[verb_sense_dict['lemma'] + str(index) + '-pos'] = filtered_sense_examples #后续可以在此基础上作lemmatization, 只有成对sentence
        
    return pos_sentence_pair_dataset


def remove_empty_neg(neg_sentence_pair_dataset):
    if neg_sentence_pair_dataset != {}:
        return neg_sentence_pair_dataset 

def negative_dataset_prepare(verb_sense_dict):
    neg_sentence_pair_dataset = {}
    for index in list(itertools.product(list(range(len(verb_sense_dict['senses']))), list(range(len(verb_sense_dict['senses']))))):
        if index[0]!= index[1] and index[0] < index[1] :
            sense_examples = list(itertools.product(verb_sense_dict['senses'][index[0]]['examples'], verb_sense_dict['senses'][index[1]]['examples']))   
            neg_sentence_pair_dataset[verb_sense_dict['lemma'] + str(index[0]) + str(index[1])  + '-neg'] = sense_examples #每个sense的exmaple两两组合
    return neg_sentence_pair_dataset

with open('./resource/verb_sense_dict.json','r',encoding='utf8')as fp:
    verb_sense_dict = json.load(fp)
pos_sentence_pair_dataset = list(map(positive_dataset_prepare, verb_sense_dict))

neg_sentence_pair_dataset = list(map(negative_dataset_prepare, verb_sense_dict))
neg_sentence_pair_dataset = list(filter(remove_empty_neg, neg_sentence_pair_dataset)) ##刨除只有一个sense的verb    #############有多少个只有一个sense的verb？？


def positive_negative_dataset_prepare(verb_sense_dict):
    positive_negative_dataset = []
    for index, sense in enumerate(verb_sense_dict['senses']):
        ##一个verb的一个sense，多个句子两两组合
        temp_positive_negative_dataset = []
        if len(sense['examples']) > 1: #刨除只有一个example的sense    #############有多少个只有一个example的sense？？
            pos_sense_examples = list(itertools.product(sense['examples'], sense['examples'])) 
            pos_filtered_sense_examples = list(filter(remove_pair_same_exmple, pos_sense_examples))
            for pos_filtered_sense_example in pos_filtered_sense_examples:
                temp_positive_negative_dataset.append({pos_filtered_sense_example[0]:verb_sense_dict['lemma'] + str(index), pos_filtered_sense_example[1]:verb_sense_dict['lemma'] + str(index)})

            ##negative sentence ready, 非当前sense的其他sense的所有句子
            neg_sentence = []
            for index2, sense2 in enumerate(verb_sense_dict['senses']):
                if index != index2:
                    for sentence_example in sense2['examples']:
                        neg_sentence.append({sentence_example:verb_sense_dict['lemma'] + str(index2)})

            ##加上negative sentence
            for temp in temp_positive_negative_dataset:
                temp_list = [] 
                for j in range(len(neg_sentence)):
                    temp_list.append(copy.deepcopy(temp))
                for i, temp2 in enumerate(temp_list):
                    for k, v in neg_sentence[i].items():
                        temp2[k] = v
                positive_negative_dataset.extend(temp_list)   
    return positive_negative_dataset
                    

            
sentence_triple_dataset = list(map(positive_negative_dataset_prepare, verb_sense_dict))

print(1)