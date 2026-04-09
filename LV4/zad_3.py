import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y

def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
    return y_noisy

broj_uzoraka = 50
x = np.linspace(1,10,broj_uzoraka)
y_true = non_func(x)
y_measured = add_noise(y_true)
x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis]

degrees = [2, 6, 15]

for degree in degrees:
    # make polynomial features
    poly = PolynomialFeatures(degree=degree)
    xnew = poly.fit_transform(x)
    
    np.random.seed(12)
    indeksi = np.random.permutation(len(xnew))
    indeksi_train = indeksi[0:int(np.floor(0.7*len(xnew)))]
    indeksi_test = indeksi[int(np.floor(0.7*len(xnew)))+1:len(xnew)]

    xtrain = xnew[indeksi_train,]
    ytrain = y_measured[indeksi_train]

    xtest = xnew[indeksi_test,]
    ytest = y_measured[indeksi_test]

    linearModel = lm.LinearRegression()
    linearModel.fit(xtrain,ytrain)

    ytest_p = linearModel.predict(xtest)
    MSE_test = mean_squared_error(ytest, ytest_p)
    ytrain_p = linearModel.predict(xtrain)
    MSE_train = mean_squared_error(ytrain, ytrain_p)
    print('MSE_test for degree', degree, ':', MSE_test)
    print('MSE_train for degree', degree, ':', MSE_train)

    plt.figure(degree)
    plt.plot(xtest[:,1],ytest_p,'og',label='predicted')
    plt.plot(xtest[:,1],ytest,'or',label='test')
    plt.legend(loc = 4)
    plt.show()
    
    plt.figure(degree)
    plt.plot(x,y_true,label='f')
    plt.plot(x, linearModel.predict(xnew),'r-',label='model')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(xtrain[:,1],ytrain,'ok',label='train')
    plt.legend(loc = 4)
    plt.show()

"""
Za model sa degree 2 i 15 uzoraka model prati predikciju koja je daleko od funkcije.
Za model sa degree 6 i 15 uzoraka model je dobar odnosno po krivulji vidimo da prati predikciju i funkciju kako treba.
Za model sa degree 15 i 15 uzoraka model je neznam kako opisati.
Za model sa degree 2 i 100 uzoraka model prati predikciju koja je daleko od funkcije.
Za model sa degree 6 i 100 uzoraka model je dobar odnosno po krivulji vidimo da prati predikciju i funkciju kako treba.
Za model sa degree 15 i 100 uzoraka model je dobar odnosno po krivulji vidimo da prati predikciju i funkciju kako treba.
Za model sa degree 2 i 50 uzoraka model prati predikciju ali od funkcije je daleko.
Za model sa degree 6 i 50 uzoraka model je dobar odnosno po krivulji vidimo da prati predikciju i funkciju kako treba.
Za model sa degree 15 i 50 uzoraka model je dobar odnosno po krivulji vidimo da prati predikciju i funkciju malo odstupa od funkcije.
"""