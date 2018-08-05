'''
Created on 2018年7月4日
@author: Charles

'''

# Step 1.匯入 keras 程式，下載並讀取mnist資料
import tensorflow as tf
import keras
import pandas as pd
from keras.utils import np_utils

# Step 2.匯入 keras 模組
from keras.datasets import mnist
from matplotlib.cm import cmap_d

# Step 3. 第一次執行下載 mnist 資料
(X_train_image, y_train_label),\
(X_test_image, y_test_label) = mnist.load_data()

# Step 4. 查看下載的 mnist 資料檔案
# ./res/imgs/mnist.npz

# Step 5. 讀取 mnist 資料
(X_train_image, y_train_label),\
(X_test_image, y_test_label) = mnist.load_data()

# Step 6. 查看 mnist 資料
print('train data=', len(X_train_image))
print(' test data=', len(X_test_image))

# 查看訓練資料
# Step 1. 訓練資料是由images與labels所組成
print('X_train_image:', X_train_image.shape)
print('y_train_image:', y_train_image.shape)

# Step 2. 定義 plot_image 函數顯示數字影像
import matplotlib.pyplot as plt

def plot_image(image):
    fig = plt.gcf()
    fig.set_size_inches(2,2)
    plt.imshow(image, cmap = 'binary')
    plt.show()
    
# Step 3. 執行 plot_image 函數查看第0筆數字影像
plot_image(X_train_image[0])

# Step 4. 查看第0筆 labels 資料

# 查看多筆訓練資料 images 與 labels
# Step 1. 建立plot_image_labels_prediction函數，可以顯示多筆 mnist 資料的 images 與 labels
# 因為後續我們希望能方便查看數字圖形，真實數字與預測結果，所以我們建立下列函數。
import matplotlib.pyplot as plt
def plot_image_labels_prediction(images,labels,prediction,idx,num=10):
    fig = plt.gcf()
    fit.set_size_inches(12,14)
    if num > 25: num = 25
    for i in range(0,num):
        ax = plt.subplot(5, 5, 1+i)              #建立 subgraph 子圖形為5行5列
        ax.imshow(images[idx], cmap = 'binary')
        title = "label=" + str(labels[idx])
        if len(prediction)>0:
            title+= "label" + str(labels[idx])
        ax.set_title(title,fontsize=10)
        ax.set_xticks([]);ax.set_yticks([])
        idx+=1
    plt.show()

# Step 2. 查看訓練資料前 10 筆資料
plot_image_labels_prediction(X_train_image,y_train_label,[],0,20)

# Step 3. 查看 test 測試資料
print('X_test_image:',X_test_image.shape)
print('y_test_label:',y_test_label.shape)     

# Step 4. 執行 show_image_labels() 顯示測試資料前 10 筆資料
plot_image_labels_prediction(X_test_image,y_test_label,[],0,10)

# 多層感知器模型資料預處理
# feature (數字影像的特徵值) 資料預處理
# 1.將原本28x28數字影像，以reshape轉換成1維的向量，其長度是784，並轉換為float
# 2.數字影像image的數字標準化
# Step 1. 查看資料的 shape
print('X_train_image:',X_train_image.shape)
print('y_train_label:',y_train_label.shape)

# Step 2. 將 image 以 reshape 轉換
# 將原本28x28的2維數字影像，以reshape轉換為1維的向量，再以astype轉換為float，共784個float數字
x_Train = X_train_image.reshape(60000, 784).astype('float32')
x_Test = X_test_image.reshape(10000, 784).astype('float32')

# Step 3. 查看轉換為1維的向量的shape
print('x_train:',x_Train.shape)
print('x_Test:',x_Test.shape)

# Step 4. 查看image影像的內容 (0->256;0->FF)
X_train_image[0]

# Step 5. 將數字影像image的數字標準化
x_Train_normalize = x_Train/255
x_Test_normalize = x_Test/255

# Step 6. 查看數字影像image的數字標準化後的結果
x_Train_normalize[0]

# 將資料類別轉換成 One-hot encoding
# Step 1. Labels (數字影像真實的值) 資料預處理
# 查看原本的label標籤欄位
y_train_label[:5]

# Step 2. Label標籤欄位執行 One-hot encoding 轉換 (真實為1、其餘為0)
y_TrainOneHot = np_utils.to_categorical(y_train_label)
y_TestOneHot = np_utils.to_categorical(y_test_label)

# 匯入所需要的模組
from keras.models import Sequential
from keras.layers import Dense

# Step 3. 建立模型
model = Sequential()

# Step 4. 建立｢輸入層｣、「隱藏層」、「輸出層」
model.add(Dense(units=256,                   # 定義隱藏層神經元個數256
                input_dim=784,               # 設定輸入層的神經元個數784(784個float數字)
                kernel_initializer='normal', # 使用常態分配分布的亂數，初始化 weight 、 bias
                activation='relu'))          # 定義激活函數為 relu
model.add(Dense(units=10,
                kernel_initializer='normal',
                activation='softmax'))

# Step 5.查看模型的摘要
print(model.summary())

# 進行訓練
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 開始訓練
train_history = model.fit(x=x_Train_normalize,
                          y=y_TrainOneHot,
                          validation_split=0.2,
                          epochs=10,
                          batch_size=200,
                          verbose=2)

# 建立show_train_history 顯示訓練過程
import matplotlib.pyplot as plt
def show_train_history(train_history,train,validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.xlabel('Epoch')
    plt.ylabel(train)
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()

# 顯示訓練資料正確率
show_train_history(train_history,'acc','val_acc')

# 顯示訓練資料錯誤率
show_train_history(train_history,'loss','val_loss')

scores = model.evaluate(x_Test_normalize, y_TestOneHot)
print()
print('accuracy=',scores[1])

# 執行預測
prediction = model.predict_classes(x_Test)

prediction

# 顯示10筆預測結果
plot_image_labels_prediction(X_test_image,y_test_label,prediction,idx=340)

# 顯示混淆矩陣(可以看出哪幾個數字分不好)
import pandas as pd
pd.crosstab(y_test_label,prediction,rownames=['label'],colnames=['predict'])

# 查詢每個實際類別與預測類別
df = pd.DataFrame({'label':y_test_label, 'predict':prediction})
df[:2]

# 找出模型分錯的數字圖形編號
df[(df.label==5)&(df.predict==3)]

# 畫圖
plot_image_labels_prediction(X_test_image,y_test_label,prediction,idx=340,num=1)

