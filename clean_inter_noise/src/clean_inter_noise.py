import os
import sys

import matio
import numpy as np
import argparse


def get_label_featurelist_dict(path):
    with open(path) as f:
        lines = f.readlines()
        label_img_dict = dict()

        current_label = ''
        pre_label = ''
        img_list = []
        i = 0
        for line in lines:
            i = i + 1
            label = line.strip().split('/')[0]
            if label != current_label:
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
        return label_img_dict


def clean_inter_noise(root_folder, feature_path, fea_dims,threshold):
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
    print('Finished Cal class center')
    label_visited_dict = dict()
    for key in lable_center_dict:
        label_visited_dict[key] = 0
    print('Start merge same class')
    #same_class = []
    out_result = []
    for key in lable_center_dict:
        tmp_class = []
        if label_visited_dict[key] == 0:
            tmp_class.append(key)
            label_visited_dict[key] = 1
            cur_fea_center = lable_center_dict[key]

            for key2 in lable_center_dict:
                if key != key2 and label_visited_dict[key2] == 0:
                    #label_visited_dict[key2] = 1
                    com_fea_center = lable_center_dict[key2]
                    dist = np.dot(cur_fea_center, com_fea_center) / (np.linalg.norm(cur_fea_center, ord=2) * np.linalg.norm(com_fea_center, ord=2))
                    #print(str(key)+'  ' +str(key2) + '  ' + str(dist))
                    if dist > threshold:
                        print(str(key)+'  ' +str(key2) + '  ' + str(dist))
                        label_visited_dict[key2] = 1
                        tmp_class.append(key2)
                        out_result.append(str(key)+'  ' +str(key2) + '  ' + str(dist))
    return out_result

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

    result = clean_inter_noise(fea_root_folder, fea_list_path, fea_dims, threshold)

    save_path = args.noise_save_path
    with open(save_path , 'w') as f:
        for i in range(len(result)):
            f.write(result[i]+ '\n')
    print('Finised clean')

if __name__ == '__main__':
    main(parse_args(sys.argv[1:]))
