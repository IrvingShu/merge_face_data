nohup python -u ./src/movedir.py \
     --img-root-folder=/workspace/data/qyc/data/face_asian_and_blueface \
     --inter-same-label-path=./0.7-asian-and-blueface-result-clean-merge-label.txt \
     > ./nohup_move.log 2>&1 &
 
