### 查看每一列的null分布情况



train_ax_fea_null_tmp = train_ax1.drop(columns=['loan_dt','tag'])
valid_fea_null_tmp = valid1.drop(columns=['loan_dt'])

null_tra1 = train_ax_fea_null_tmp.isnull()
null_val1 = valid_fea_null_tmp.isnull()
col_null_sum_tra = null_tra1.sum(axis=0)
col_null_sum_val = null_val1.sum(axis=0)

import joblib
null_tuple = (null_tra1,null_val1,col_null_sum_tra,col_null_sum_val)
joblib.dump(null_tuple,'./preprocess_data_new/null_tuple')



from collections import OrderedDict

def rank_fea_n_null(value,y_pos):
    if value == y_pos[-1]:
        return len(y_pos)
    for i in range(1,len(y_pos)):
        if (y_pos[i-1]<=value) and (value<y_pos[i]):
            return i
    print('error!')
    return -1

def gen_fea_null(data,col_null_sum,y_pos):
    cols = list(data.columns)[1:] # ignore id
    fea_n_null = OrderedDict()
    fea_nd_null = OrderedDict()
    for col in cols:
        fea_n_null['%s_n_null' %col] = col_null_sum[col]
        fea_nd_null['%s_nd_null' %col] = rank_fea_n_null(col_null_sum[col],y_pos)
#         print(col)
    return fea_n_null,fea_nd_null

%%time
train_ax_fea_n_null, train_ax_fea_nd_null = gen_fea_null(train_ax_fea_null_tmp,col_null_sum_tra/100000,y_pos)
valid_fea_n_null, valid_fea_nd_null = gen_fea_null(valid_fea_null_tmp,col_null_sum_val/20000,y_pos)

# 产生新特征 fea +'_n_null'  fea+'_nd_null'
import pickle
pickle.dump((train_ax_fea_n_null,train_ax_fea_nd_null),open('./preprocess_data_new/train_ax_fea_null.pkl','wb'))
pickle.dump((valid_fea_n_null,valid_fea_nd_null),open('./preprocess_data_new/valid_fea_null.pkl','wb'))

# a,b = pickle.load(open('./preprocess_data_new/train_ax_fea_nd_null.pkl','rb'))

# for i,j in a.items():
#     print(i,j)