def load_hard_similarity_dataset(path = '../event/resource/hard.txt'):
    x_A = []
    x_B = []
    y = []
    for line in open(path): 
        pos_event1 = line.strip('\n').split('|')[0].strip(' ') + ' ' + line.strip('\n').split('|')[1].strip(' ') + ' ' + line.strip('\n').split('|')[2].strip(' ')
        pos_event2 = line.strip('\n').split('|')[3].strip(' ') + ' ' + line.strip('\n').split('|')[4].strip(' ') + ' ' + line.strip('\n').split('|')[5].strip(' ')
        x_A.append(pos_event1)
        x_B.append(pos_event2)
        y.append(1)
        neg_event1 = line.strip('\n').split('|')[6].strip(' ') + ' ' + line.strip('\n').split('|')[7].strip(' ') + ' ' + line.strip('\n').split('|')[9].strip(' ')
        neg_event2 = line.strip('\n').split('|')[9].strip(' ') + ' ' + line.strip('\n').split('|')[10].strip(' ') + ' ' + line.strip('\n').split('|')[11].strip(' ')
        x_A.append(neg_event1)
        x_B.append(neg_event2)
        y.append(0)
    return (x_A, x_B, y)



load_hard_similarity_dataset()

        
