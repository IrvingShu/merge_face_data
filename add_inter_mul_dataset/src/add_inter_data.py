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


def get_label_center_fea_dict(root_folder, feature_path, fea_dims):
    print('Start load feature')
    label_featurelist_dict = get_label_featurelist_dict(feature_path)

    print('Finished load feature')
    label_center_dict = dict()
    # Calulate feature center
    for key in label_featurelist_dict:
        feature_sum = np.zeros(fea_dims, dtype=np.float64)
        cur_fea_list = label_featurelist_dict[key]
        for i in range(len(cur_fea_list)):
            full_path = os.path.join(root_folder, cur_fea_list[i])
            x_vec = load_feat(full_path) # matio.load_mat(full_path).flatten()
            feature_sum += x_vec
        feature_center = feature_sum / len(cur_fea_list)
        label_center_dict[key] = feature_center
    print('Finishe cal center')
    return label_center_dict



def load_npy(npy_file):
    mat = None
    if os.path.exists(npy_file):
        mat = np.load(npy_file)
    else:
        err_info = 'Can not find file: ' + npy_file
        raise Exception(err_info)
    return mat

def load_feat(feat_file, flatten=True):
    feat = None
    if feat_file.endswith('npy'):
        feat = load_npy(feat_file)
    elif feat_file.endswith('bin'):
        feat =matio.load_mat(feat_file)
    else:
        raise Exception(
            'Unsupported feature file. Only support .npy and .bin (OpenCV Mat file)')
    if flatten:
        feat = feat.flatten()
    return feat

#merge 
def get_extra_inter_class(from_data, to_data, inter_threshold, intra_threshold):
    inter_result = []
    intra_result = []
    for key in from_data:
        cur_fea_center = from_data[key]
        max_sim = -1.0
        max_sim_label = ''
        for key2 in to_data:
            com_fea_center = to_data[key2]
            sim = np.dot(cur_fea_center, com_fea_center) / (np.linalg.norm(cur_fea_center, ord=2) * np.linalg.norm(com_fea_center, ord=2))
            if sim > max_sim:
                max_sim = sim
                max_sim_label = key2
        if max_sim < inter_threshold:
            print(key + ' ' +  max_sim_label + ' ' + str(max_sim))
            inter_result.append(key)
        else:
            pass    
 
        if max_sim >= intra_threshold:
            print(key + ' ' +  max_sim_label + ' ' + str(max_sim))
            intra_result.append(key + ' ' +  max_sim_label + ' ' + str(max_sim)) 
        else:
            pass
        
    return inter_result, intra_result
            

def parse_args(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--from-feature-root-folder', type=str, help='feature root folder')
    parser.add_argument('--from-feature-list-path', type=str, help='feature list path') 
    parser.add_argument('--to-feature-root-folder', type=str, help='feature root folder')
    parser.add_argument('--to-feature-list-path', type=str, help='feature list path')
    parser.add_argument('--feature-dims', type=int, help='feature dims', default=512)
 
    parser.add_argument('--inter-threshold', type=float, help='less threshold will merge it as new label') 
    parser.add_argument('--intra-threshold', type=float, help='above threshold will merge it as existed label') 
    parser.add_argument('--save-inter-path', type=str, help='save inter path')
    parser.add_argument('--save-intra-path', type=str, help='save intra path')
    
    return parser.parse_args(argv)

def main(args):
    print('===> args:\n', args)
    from_fea_root_folder = args.from_feature_root_folder
    from_fea_list_path = args.from_feature_list_path

    to_fea_root_folder = args.to_feature_root_folder
    to_fea_list_path = args.to_feature_list_path

    fea_dims = args.feature_dims
    inter_threshold = args.inter_threshold
    intra_threshold = args.intra_threshold
        
    #cal class center
    to_fea_root_folder_list = to_fea_root_folder.split(',')
    to_fea_list_path_list = to_fea_list_path.split(',')
    if len(to_fea_root_folder_list) != len(to_fea_list_path_list):
        print('The num of root floder must equal to the num of path list')
        return -1 
    #read all input feture
    #
    print('read from feature:')
    from_data = get_label_center_fea_dict(from_fea_root_folder, from_fea_list_path, fea_dims)    
    print('read to feature:')
    to_data = {}
    for i in range(len(to_fea_root_folder_list)):
        tmp_to_data = get_label_center_fea_dict(to_fea_root_folder_list[i], to_fea_list_path_list[i], fea_dims)
        to_data.update(tmp_to_data)

    #
    extra_inter_data, extra_intra_data = get_extra_inter_class(from_data, to_data, inter_threshold, intra_threshold)
    save_inter_path = args.save_inter_path
    save_intra_path = args.save_intra_path

    with open(save_inter_path , 'w') as f, open(save_intra_path, 'w') as f1:
        for i in range(len(extra_inter_data)):
            f.write(extra_inter_data[i]+ '\n')
        for j in range(len(extra_intra_data)):
            f1.write(extra_intra_data[j] + '\n')        
    print('Finished merge inter label')
if __name__ == '__main__':
    main(parse_args(sys.argv[1:]))
    
