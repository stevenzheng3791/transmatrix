import sys
import getopt
import numpy as np
from space import Space
from utils import read_dict, train_tm


from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

import numpy as np

#Loading word embeddings
dict_file = sys.argv[0]
source_file = sys.argv[1]	
target_file = sys.argv[2]

print "Reading the training data"
train_data = read_dict(dict_file)

#we only need to load the vectors for the words in the training data
#semantic spaces contain additional words
source_words, target_words = zip(*train_data)

print "Reading: %s" % source_file
source_sp = Space.build(source_file, set(source_words))
source_sp.normalize()

print "Reading: %s" % target_file
target_sp = Space.build(target_file, set(target_words))
target_sp.normalize()

sp1,sp2,data = source_sp,target_sp,train_data
data = get_valid_data(sp1, sp2, data)
data = data[:1250]
print "Training using: %d word pairs" % len(data)

els1, els2 = zip(*data)
m1 = sp1.mat[[sp1.row2id[el] for el in els1],:]
m2 = sp2.mat[[sp2.row2id[el] for el in els2],:]

model = Sequential()
model.add(Dense(300, activation='linear', input_dim=300))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='mean_squared_error',
              optimizer=sgd,
              metrics=['mae'])

print "Learning the translation matrix"
model.fit(x_train, y_train,
          epochs=10000,
          batch_size=100)
#score = model.evaluate(x_test, y_test, batch_size=1)

tm = np.array(model.get_weights()[0])
print "Printing the translation matrix"
#out_file = "./tm"
out_file = sys.argv[3]
np.savetxt("%s.txt" % out_file, tm)

# python train.py data/OPUS_en_it_europarl_train_5K.txt data/EN.200K.cbow1_wind5_hs0_neg10_size300_smpl1e-05.txt data/IT.200K.cbow1_wind5_hs0_neg10_size300_smpl1e-05.txt tm