nohup python -u ./src/clean_inter_noise.py \
     --feature-root-folder=/workspace/data/blueface_ansia_95660/feature/model-r100-spa-m2.0-4gpu-faceemore-asian-91926-ep156 \
     --feature-list-path=/workspace/data/blueface_ansia_95660/feature/feature.lst \
     --feature-dims=512 \
     --threshold=0.9 \
     --noise-save-path=./0.9-blueface_ansia_95660-result-clean-noise.txt \
     > ./logs/noise_clean.log 2>&1 &
 
