nohup python -u ./src/clean_intra_noise_version2.py \
     --feature-root-folder=/workspace/data/blueface_ansia_95660/feature/model-r100-spa-m2.0-4gpu-faceemore-asian-91926-ep156 \
     --feature-list-path=/workspace/data/blueface_ansia_95660/feature/feature.lst \
     --feature-dims=512 \
     --threshold=0.3 \
     --noise-save-path=./log/0.3-blueface_ansia_95660-intra-noise.txt \
     > ./0.3-blueface_ansia_95660-intra-noise.log 2>&1 &
 
