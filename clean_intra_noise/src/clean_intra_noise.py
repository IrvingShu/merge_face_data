import os
import sys

import matio
import numpy as np
import argparse

def get_label_featurelist_dict(path):
    with open(path) as f:
        lines = f.readlines()
        label_img_dict = dict()
        print('all image nums: %d' %len(lines))
        current_label = ''
        pre_label = ''
        img_list = []
        i = 0
        count_label = 0
        for line in lines:
            i = i + 1
            label = line.strip().split('/')[0]
            if label != current_label:
                count_label = count_label + 1
                if len(img_list) > 0:
                    label_img_dict[pre_label] = img_list
                    img_list = []
                current_label = label
                img_list.append(line.strip())
            else:
                img_list.append(line.strip())
                pre_label = current_label
                if i == len(lines):
                    label_img_dict[pre_label] = img_list
        print('label num: %d'%count_label)
        return label_img_dict


def clean_intra_noise(root_folder, feature_path, fea_dims, threshold):
    print('Start load feature')
    label_featurelist_dict = get_label_featurelist_dict(feature_path)

    print('Finished load feature')
    lable_center_dict = dict()
    # Calulate feature center
    for key in label_featurelist_dict:
        feature_sum = np.zeros(fea_dims, dtype=np.float64)
        cur_fea_list = label_featurelist_dict[key]
        for i in range(len(cur_fea_list)):
            full_path = os.path.join(root_folder, cur_fea_list[i])
            x_vec = matio.load_mat(full_path).flatten()
            feature_sum += x_vec
        feature_center = feature_sum / len(cur_fea_list)
        lable_center_dict[key] = feature_center

    # compare insta distance
    noise_img = []
    for key in label_featurelist_dict:
        cur_fea_list = label_featurelist_dict[key]
        for i in range(len(cur_fea_list)):
            full_path = os.path.join(root_folder, cur_fea_list[i])
            x_vec= matio.load_mat(full_path).flatten()
            center = lable_center_dict[key]

            sim = np.dot(x_vec, center) / (np.linalg.norm(x_vec, ord=2) * np.linalg.norm(center, ord=2))
            if sim < threshold:
                #print(cur_fea_list[i] + ' ' + str(dist))
                noise_img.append(cur_fea_list[i] + ' ' + str(sim))
    return noise_img

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--feature-root-folder', type=str, help='feature root folder')
    parser.add_argument('--feature-list-path', type=str, help='feature list path') 
    parser.add_argument('--feature-dims', type=int, help='feature dims', default=512) 
    parser.add_argument('--threshold', type=float, help='less threshold will remove') 
    parser.add_argument('--noise-save-path', type=str, help='noise save path')
    return parser.parse_args(argv)

def main(args):
    print('===> args:\n', args)
    fea_root_folder = args.feature_root_folder
    fea_list_path = args.feature_list_path
    fea_dims = args.feature_dims
    threshold = args.threshold
    noise_img = clean_intra_noise(fea_root_folder, fea_list_path, fea_dims, threshold)
    save_path = args.noise_save_path
    with open(save_path , 'w') as f:
        for i in range(len(noise_img)):
            f.write(noise_img[i]+ '\n')        
    print('Finised clean')
if __name__ == '__main__':
    main(parse_args(sys.argv[1:]))
