nohup python -u ./src/gen_train_list.py \
     --prefix-from-img='ansia' \
     --from-img-root-folder=/workspace/data/trillion_pairs/celebrity_align_112x112/aligned_imgs/celebrity \
     --from-img-list-path=/workspace/data/trillion_pairs/celebrity_align_112x112/aligned_imgs/celebrity_align_112x112.lst \
     --prefix-to-img='facemore' \
     --to-img-root-folder=/workspace/data/faceemore-asian-91926/faceemore-asian-91926-img \
     --to-img-list-path=/workspace/data/faceemore-asian-91926/faceemore-asian-91926-img.lst \
     --inter-merge-list-path=./result/0.5-inter-result-add-blue-ansia-to-deepint-ansia.txt \
     --intra-merge-list-path=./result/inter-result-add-blue-ansia-to-deepint-ansia.txt \
     --keep-above-img=0 \
     --save-path=./train_0_inter_intra_blue_deepint.lst \
     > ./logs/run-merge-above0-inter.log 2>&1 &
