nohup python -u ./src/gen_train_merge_inter.py \
     --prefix-from-img='blue' \
     --from-img-root-folder=/workspace/data/qyc/data/face_asian_and_blueface \
     --from-img-list-path=/workspace/data/qyc/data/face_asian_and_blueface.lst \
     --prefix-to-img='msra,cele' \
     --to-img-root-folder=/workspace/data/trillion_pairs/msra_align_112x112/aligned_imgs/msra,/workspace/data/trillion_pairs/celebrity_align_112x112/aligned_imgs/celebrity \
     --to-img-list-path=/workspace/data/trillion_pairs/msra_align_112x112/aligned_imgs/img.lst,/workspace/data/trillion_pairs/celebrity_align_112x112/aligned_imgs/celebrity_align_112x112.lst \
     --inter-merge-list-path=./result/0.5-inter-result-add-blue-ansia-to-deepint-ansia.txt \
     --keep-above-img=0 \
     --save-path=./train_0_inter_blue_deepint.lst \
     > ./logs/run-merge-above0-inter.log 2>&1 &
