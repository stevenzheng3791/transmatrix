#!/bin/bash

if [ "$#" -eq 1 ]
then
	echo "Testing standard translation matrix..."
	python test_tm.py $1 data/OPUS_en_it_europarl_test.txt data/EN.200K.cbow1_wind5_hs0_neg10_size300_smpl1e-05.txt data/IT.200K.cbow1_wind5_hs0_neg10_size300_smpl1e-05.txt

elif [ "$1" = "--pos" ]
then
	echo "Testing translation matrix with pos augmented word embeddings..."
	python test_tm.py $2 data/OPUS_en_it_europarl_test.txt data/EN.200K.cbow1_wind5_hs0_neg10_size300_smpl1e-05_POS.txt data/IT.200K.cbow1_wind5_hs0_neg10_size300_smpl1e-05_POS.txt

else
	echo "Invalid command"
fi