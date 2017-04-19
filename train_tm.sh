#!/bin/bash

if [ "$#" -eq 1 ]
then
	echo "Training standard translation matrix..."
	python train_tm.py -o $1 data/OPUS_en_it_europarl_train_5K.txt data/EN.200K.cbow1_wind5_hs0_neg10_size300_smpl1e-05.txt data/IT.200K.cbow1_wind5_hs0_neg10_size300_smpl1e-05.txt
elif [ "$1" = "--pos" ]
then
	echo "Training translation matrix with pos augmented word embeddings..."
	python train_tm.py -o $2 data/OPUS_en_it_europarl_train_5K.txt data/EN.200K.cbow1_wind5_hs0_neg10_size300_smpl1e-05_POS.txt data/IT.200K.cbow1_wind5_hs0_neg10_size300_smpl1e-05_POS.txt
else
	echo "Invalid command"
fi