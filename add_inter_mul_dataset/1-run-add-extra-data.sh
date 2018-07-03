
nohup python -u ./src/add_inter_data.py \
     --from-feature-root-folder="/workspace/data/shiyongjie/data/megaface_challenge2_features" \
     --from-feature-list-path="/workspace/data/shiyongjie/code/megaface_challenge2_features_filelist.txt" \
     --to-feature-root-folder="/workspace/data/faceemore-asian-91926/featuremodel-r100-spa-m2.0-6gpu-ep96" \
     --to-feature-list-path="/workspace/data/faceemore-asian-91926/feature.lst"  \
     --feature-dims=512 \
     --inter-threshold=0.4 \
     --intra-threshold=0.8 \
     --save-inter-path=./result/0.4-inter-result-add-megaface-challenge2.txt \
     --save-intra-path=./result/0.4-intra-result-add-megaface-challenge2.txt \
     > ./logs/0.4_0.8_train_celebrity-to-megaface-challenge2.log 2>&1 &

#nohup python -u ./src/add_inter_data.py \
#     --from-feature-root-folder=/workspace/data/trillion_pairs/celebrity_align_112x112/feature/model-r100-spa-m2.0-6gpu-ep96 \
#     --from-feature-list-path=/workspace/data/trillion_pairs/celebrity_align_112x112/feature/feature_list.lst \
#     --to-feature-root-folder=/workspace/data/qyc/feature/face_asian_mtcnn_simaligned_112x112_merge_faceemore \
#     --to-feature-list-path=/workspace/data/qyc/feature/face_asian_mtcnn_simaligned_112x112_merge_faceemore.lst \
#     --feature-dims=512 \
#     --inter-threshold=0.5 \
#     --intra-threshold=0.8 \
#     --save-inter-path=./result/0.5-inter-result-add-train_celebrity-to-Andansian.txt \
#     --save-intra-path=./result/0.8-inter-result-add-train_celebrity-to-Andansian.txt \
#     > ./logs/0.5_0.8_train_celebrity-to-faceemoreAndansian.log 2>&1 &


#nohup python -u ./src/add_inter_data.py \
#     --from-feature-root-folder=/workspace/data/trillion_pairs/celebrity_align_112x112/feature/model-r100-spa-m2.0-6gpu-ep96 \
#     --from-feature-list-path=/workspace/data/trillion_pairs/celebrity_align_112x112/feature/feature_list.lst \
#     --to-feature-root-folder=/workspace/data/insightface_color_imgV2/feature/model-r100-spa-m2.0-6gpu-ep96,/workspace/data/qyc/feature/face_asian_mtcnn_simaligned_112x112_merge_faceemore \
#     --to-feature-list-path=/workspace/data/insightface_color_imgV2/feature/feature_list.txt,/workspace/data/qyc/feature/face_asian_mtcnn_simaligned_112x112_merge_faceemore.lst \
#     --feature-dims=512 \
#     --threshold=0.4 \
#     --save-path=./result/0.4-result-add-train_celebrity-to-faceemoreAndansian.txt \
#     > ./logs/0.4_train_celebrity-to-faceemoreAndansian.log 2>&1 &

