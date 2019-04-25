

path = '/home/hermuba/Documents/old_q/107/1071-3.pdf'


# PyPDF2 has problems with Chinese characters
import tika
tika.initVM()
from tika import parser


def pdf_to_string(path):
    parsed = parser.from_file(path)
    #print(parsed["metadata"])
    return(parsed["content"])
import re
import pandas as pd
def parse_string_to(s):
    clean_by_row = [elem for elem in s.split('\n') if elem != '' or ' ']
    Q_index = []
    A_index = []
    for index, row in enumerate(clean_by_row):
        # identify Q-no
        if len(row.split('.')[0]) <= 2:
            if re.match(r'([1-9]|[1-8][0-9])', row.split('.')[0]):
                Q_index.append(index) # all the index with starting Q
            elif re.match(r'([A-D])', row.split('.')[0]):
                A_index.append(index)

    # make each Q and A into pandas dataframe
    df = pd.DataFrame(columns = ['Question', 'A', 'B', 'C', 'D'])

    # start with Q:
    all_Q = []
    for q in Q_index:
        next_row = q+1
        Q_string = clean_by_row[q]
        while next_row not in A_index+Q_index: # join str
            Q_string = Q_string + clean_by_row[next_row]
            next_row += 1
        all_Q.append(Q_string)

    # testing
    if len(all_Q) != 80:
        print('Error with Question number')

    # write to dataframe
    df['Question'] = all_Q # save question to dataframe
    
    all_A = []
    for a in A_index:
        q_no = 0 # index of dataframe starts from 0
        next_row = a+1
        A_string = clean_by_row[a]
        while next_row not in A_index+Q_index and next_row < len(clean_by_row): # last row
            A_string = A_string + clean_by_row[next_row]
            next_row += 1
        all_A.append(A_string)

    # testing
    if len(all_A) != len(all_Q)*4:
        print("missing choice")

    a_s = [all_A[i] for i in list(range(0,320,4))]
    b_s = [all_A[i] for i in list(range(1,320,4))]
    c_s = [all_A[i] for i in list(range(2,320,4))]
    d_s = [all_A[i] for i in list(range(3,320,4))]
    
    df['A'] = a_s
    df['B'] = b_s
    df['C'] = c_s
    df['D'] = d_s

    return(df)
    


