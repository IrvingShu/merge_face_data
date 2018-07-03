nohup python -u ./src/get_same_label_img.py \
    --inter-noise-list=./0.7-asian-and-blueface-result-clean-noise.txt \
    --same-label-list=./0.7-asian-and-blueface-result-clean-merge-label.txt \
    > ./merge.log 2>&1 &
 
