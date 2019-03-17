**1.explore_int**
通过统计unique_num的数量，然后设置阈值，进一步来挑选出变量中最有可能是“类型变量”的那一部分。在**3.search_cat_con_thre**中，我们寻找一个较为合理的阈值。  

**2.explore_null.ipynb**
查看样本缺失值的分布，并提取缺失值相关的特征  

**3.search_cat_con_thre**
寻找合适阈值    

**4.explore_time.ipynb**
探索时间与逾期率的关系，在构造与时间相关的特征的时候，要注意：特征的稳定性，即是否在较长一段时间内与假设相符。有些时间特征受节日等因素的影响，表现出来的只是暂时假象。  

**5.explore_maj.ipynb**
探索maj特征  

**6.explore_tag**
给6w条没有tag的数据打标签
