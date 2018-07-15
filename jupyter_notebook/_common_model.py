'''
this file contains all the commonly used models
'''
import pandas as pd
import numpy as np
from sklearn import preprocessing as skpp
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
import xgboost as xgb


def get_encoder(df, column):
    Encoder = skpp.LabelEncoder()
    df[column] = df[column].apply(lambda x: str(x))
    Encoder.fit(df[column].unique())
    df[column] = Encoder.transform(df[column])
    return df


def encode_columns(df, char_feature):
    for f in char_feature:
        df = get_encoder(df, f)
    return df


def process_data(df, char_feature, num_feature, target_variable):
    '''
    prepare data for modeling
    '''
    if char_feature:
        df = encode_columns(df, char_feature)
    features_list = char_feature + num_feature
    df = df.dropna(subset=features_list + [target_variable], how="any")
    X = df[features_list].values
    y = df[target_variable].values
    Xtr, Xv, ytr, yv = train_test_split(X, y, test_size=0.2, random_state=1989)
    return Xtr, Xv, ytr, yv


def decison_tree(df, char_feature, num_feature, target_variable):
    Xtr, Xv, ytr, yv = process_data(df, char_feature, num_feature,
                                    target_variable)
    param_grid = {'max_depth': np.arange(3, 10)}
    tree = GridSearchCV(DecisionTreeRegressor(), param_grid)
    tree.fit(Xtr, ytr)
    print(tree.best_params_)
    best_tree = DecisionTreeRegressor(max_depth=tree.best_params_["max_depth"])
    best_tree.fit(Xtr, ytr)
    # calculate rmse of validation set
    y_pred = best_tree.predict(Xv)
    rmse = np.sqrt(sum(np.square(y_pred - yv)) / len(y_pred))
    print("rmse of best decision tree is: %.3f" % rmse)
    return best_tree


# xgb_pars = {'min_child_weight': 50, 'eta': 0.3, 'colsample_bytree': 0.3,
#             'max_depth': 9, 'subsample': 0.8, 'lambda': 1., 'nthread': -1,
#             'booster' : 'gbtree', 'silent': 1, 'eval_metric': 'rmse',
#             'objective': 'reg:linear'}
def get_xgb(df, char_feature, num_feature, target_variable, xgb_pars):
    Xtr, Xv, ytr, yv = process_data(df, char_feature, num_feature,
                                    target_variable)
    dtrain = xgb.DMatrix(Xtr, label=ytr)
    dvalid = xgb.DMatrix(Xv, label=yv)
    watchlist = [(dtrain, 'train'), (dvalid, 'valid')]
    model = xgb.train(xgb_pars, dtrain, 60, watchlist,
                      early_stopping_rounds=50, maximize=False,
                      verbose_eval=10)
    return model


def pred_test(model, test, feature_list):
    Xtst = test[feature_list].values
    dtest = xgb.DMatrix(Xtst)
    y_pred = model.predict(dtest)
    return y_pred


def get_feature_imp_dt(tree, features_list, plot="no"):
    feature_imp = pd.DataFrame({'feature': features_list,
                                'importance': list(tree.feature_importances_)})
    feature_imp = feature_imp.sort_values("importance")
    if plot == "yes":
        ppt = feature_imp.set_index("feature").plot(kind='barh',
                                                    figsize=(8, 8),
                                                    fontsize=12)
        ppt.set_title("Feature Importance", fontsize=14)
        ppt.set_xlabel("Feature Importance Score", fontsize=14)
        ppt.set_xlabel("Feature Name", fontsize=14)
    return feature_imp


def get_feature_imp_xgb(model, features_list, plot="no"):
    fs = ['f%i' % i for i in range(len(features_list))]
    name = dict(zip(fs, features_list))
    feature_imp_dict = model.get_fscore()
    feature_imp = pd.DataFrame({'feature': list(feature_imp_dict.keys()),
                                'importance': list(feature_imp_dict.values())})
    feature_imp["feature"] = feature_imp["feature"].apply(lambda x: name[x])
    feature_imp = feature_imp.sort_values("importance")
    if plot == "yes":
        ppt = feature_imp.set_index("feature").plot(kind='barh',
                                                    figsize=(8, 8),
                                                    fontsize=12)
        ppt.set_title("Feature Importance", fontsize=14)
        ppt.set_xlabel("Feature Importance Score", fontsize=14)
        ppt.set_xlabel("Feature Name", fontsize=14)
    return feature_imp


def filter_feature_list(feature_imp, threshold):
    new_feature = feature_imp[feature_imp["importance"] >
                              0.01].feature.values.tolist()
    return new_feature
