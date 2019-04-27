import pandas as pan

train = pan.read_csv('TrainsetTugas1ML.csv')
test = pan.read_csv('TestsetTugas1ML.csv')
train_r = train.shape[0]
test_r = test.shape[0]
plus = 0
minus = 0

def naivebayes(col1, cat1, col2, cat2, tipe):
    n = 0
    hasil = 0
    for i in range(train_r):
        if (train[col1][i] == cat1) & (train[col2][i] == cat2):
            n = n+1
    hasil = n/tipe
    return hasil

for i in range(train_r):
    if(train['income'][i]=='>50K'):
        plus = plus + 1
    else:
        minus = minus + 1

P_plus = plus/train_r
P_minus = minus/train_r
print("loading...")
output=[]
for j in range(test_r):
    P_plus_age = naivebayes('age', test['age'][j], 'income', '>50K', plus)
    P_minus_age = naivebayes('age', test['age'][j], 'income', '<=50K', minus)
    
    P_plus_workclass = naivebayes('workclass', test['workclass'][j], 'income', '>50K', plus)
    P_minus_workclass = naivebayes('workclass', test['workclass'][j], 'income', '<=50K', minus)
    
    P_plus_edu = naivebayes('education', test['education'][j], 'income', '>50K', plus)
    P_minus_edu = naivebayes('education', test['education'][j], 'income', '<=50K', minus)
    
    P_plus_martial = naivebayes('marital-status', test['marital-status'][j], 'income', '>50K', plus)
    P_minus_martial = naivebayes('marital-status', test['marital-status'][j], 'income', '<=50K', minus)
    
    P_plus_occu = naivebayes('occupation', test['occupation'][j], 'income', '>50K', plus)
    P_minus_occu = naivebayes('occupation', test['occupation'][j], 'income', '<=50K', minus)
    
    P_plus_relation = naivebayes('relationship', test['relationship'][j], 'income', '>50K', plus)
    P_minus_relation = naivebayes('relationship', test['relationship'][j], 'income', '<=50K', minus)
    
    P_plus_hours = naivebayes('hours-per-week', test['hours-per-week'][j], 'income', '>50K', plus)
    P_minus_hours = naivebayes('hours-per-week', test['hours-per-week'][j], 'income', '<=50K', minus)
    
    Pp = P_plus_age*P_plus_workclass*P_plus_edu*P_plus_martial*P_plus_occu*P_plus_relation*P_plus_hours*P_plus
    Pm = P_minus_age*P_minus_workclass*P_minus_edu*P_minus_martial*P_minus_occu*P_minus_relation*P_minus_hours*P_minus
    
    if(Pm > Pp):
        output.append('>50K')
    else:
        output.append('<=50K')

print(output)
print("menyimpan pada file TebakanTugas1ML.csv")
hasil = pan.DataFrame({'income': output}, index=test['id'])
hasil.to_csv('TebakanTugas1ML.csv')
print("menyimpan selesai")
