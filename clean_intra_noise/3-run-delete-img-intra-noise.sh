nohup python -u ./src/delete_intra_img_noise.py \
     --img-root-folder=/workspace/data/qyc/data/MeGlass_ori_align/below10 \
     --intra-noise-path=./log/0.3-below10-MeGlass-result-clean-noise.txt \
     --threshold=0.3 \
     > ./img_delete.log 2>&1 &
 
