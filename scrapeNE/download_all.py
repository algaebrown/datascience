# download all old questions
import sys

root_url = 'https://wwwc.moex.gov.tw/ExamQuesFiles/'
type = ['Question', 'StandardAnswer', 'ModifyAnswer']
type2 = ['', '_ANS', '_MOD']
times = ['020', '100']
year = ['103', '104', '105', '106', '107']
subject_first = ['1302', '2302', '3302', '4302', '6301', '6032']
subject_second = subject_first[:-2] + ['2301', '1301']

for t, t2, ti, y, sf, ss in type, type2, times, year, subject_first, subject_second:
    try:
        sys.

