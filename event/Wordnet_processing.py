from nltk.corpus import wordnet as wn


def remove_pair_same_exmple(sense_examples):
    if sense_examples[0]!= sense_examples[1]:
        return sense_examples 

def get_wordnet_dataset():
    word_info = []
    sentence1 = []
    sentence2 = []
    sentence3 = []

    #第一种生成正样本策略
    for word in wn.all_lemma_names():
        for synset in wn.synsets(word):
            if word != synset.lemma_names[0]:
                continue
            if(len(synset.examples())) > 2:
                pos_sense_examples = list(itertools.product(synset.examples(), synset.examples()))
                pos_filtered_sense_examples = list(filter(remove_pair_same_exmple, pos_sense_examples))
                print(1)

def test(word):
    syns = wn.synsets(word)
    print(syns[0].name())
    print(syns[0].lemmas()[0].name())

if __name__ == "__main__":
    #get_all_word()
    test("program")