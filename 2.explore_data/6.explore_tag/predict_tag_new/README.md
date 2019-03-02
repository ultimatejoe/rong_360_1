1.通过对全量训练数据（以tag为标签）进行学习，得到一个预测规则与“历史系统”相似的AR模型，并用它来预测valid和unlabel的tag
2.使用的特征为date、raw(fillna)、null、maj
3.main.ipynb for valid
4.main1.ipynb for unlabel
