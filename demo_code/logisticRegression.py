import matplotlib.pyplot as plt 
import numpy as np 

N = 100 # number of points per class
Nx = 2 # dimensionality
K = 2 # number of classes
X = np.zeros((N*K,Nx)) # data matrix (each row = single example)
y = np.zeros(N*K, dtype='uint8') # class labels

Nd=N*K

mean1=[-0.5,-0.5]
mean2=[0.5,0.5]
cov1=[[1,-0.8],[-0.8,1]]
cov1=np.array(cov1)*0.1
cov2=[[1,-0.8],[-0.8,1]]
cov2=np.array(cov2)*0.1

X[0:N,:]=np.random.multivariate_normal(mean1,cov1,(N))
X[N:2*N,:]=np.random.multivariate_normal(mean2,cov2,(N))
y[0:N]=0
y[N:2*N]=1



# lets visualize the data:
# plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.Spectral)
# plt.show()

def sigmoid(x):
    return 1/(1+np.exp(-x))

def oneOrzero(x):
    return np.round(x)

def cost(X,y):
    cost_sum =0
    for i in range(len(X)):
        prob=sigmoid(np.dot(X[i,:],w_pred)+b_pred)
        cost_sum += -1*(y[i]*np.log(prob)+(1-y[i])*np.log(1-prob))
    cost_sum = 0.5*cost_sum/len(X)
    cost_sum += 0.5*reg*np.sum(w_pred*w_pred)
    return cost_sum

w_pred=np.zeros(Nx)
b_pred=0

nloop=500
step=1e0
reg=1e-10

for l in range(nloop):

    delta_w=np.zeros(Nx)
    delta_b=0
    for i in range(Nd):
        # for j in range(Nx):
        delta_w += (y[i]-sigmoid(np.dot(X[i,:],w_pred)+b_pred))*(-X[i,:])
        delta_b += (y[i]-sigmoid(np.dot(X[i,:],w_pred)+b_pred))*(-1)
    w_pred += -step*((1/Nd)*delta_w+reg*w_pred)
    b_pred += -step*(1/Nd)*delta_b

    if l%50 ==0:
        loss=cost(X,y)
        print('loop {} with loss {}'.format(l,loss))

print('Training is Done!')

# plt.scatter(X[:, 0], X[:, 1], c=oneOrzero(sigmoid(np.dot(X,w_pred)+b_pred)), s=40, cmap=plt.cm.Spectral)
# plt.show()

y_pred=oneOrzero(sigmoid(np.dot(X,w_pred)+b_pred))
print('Accuracy: {}'.format(np.mean(y_pred==y)))



h = 0.01
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Z = oneOrzero(sigmoid(np.dot(np.c_[xx.ravel(),yy.ravel()],w_pred)+b_pred))
Z = Z.reshape(xx.shape)
fig = plt.figure()
plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.Spectral)
# plt.scatter(X[:, 0], X[:, 1], c=oneOrzero(sigmoid(np.dot(X,w_pred)+b_pred)), s=40, cmap=plt.cm.Spectral)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.show()