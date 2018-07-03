nohup python -u ./src/delete_intra_feature_noise.py \
     --feature-root-folder=/workspace/data/qyc/data/MeGlass_ori_align/above10_feature \
     --intra-noise-path=./log/0.3-above10-MeGlass-result-clean-noise.txt \
     --threshold=0.3 \
     > ./feature_delete.log 2>&1 &
 
