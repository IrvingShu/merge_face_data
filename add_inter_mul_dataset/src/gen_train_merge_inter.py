import os
import sys

import matio
import numpy as np
import argparse
import random

def get_label_imglist_dict(root_folder,path,prefix):
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
            label = prefix+line.strip().split('/')[0]
            if label != current_label:
                count_label = count_label + 1
                if len(img_list) > 0:
                    label_img_dict[pre_label] = img_list
                    img_list = []
                current_label = label
                img_list.append(os.path.join(root_folder,line.strip()))
            else:
                img_list.append(os.path.join(root_folder,line.strip()))
                pre_label = current_label
                if i == len(lines):
                    label_img_dict[pre_label] = img_list
        print('label num: %d'%count_label)
        return label_img_dict
            

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--prefix-from-img', type=str, help='prefix from img') 
    parser.add_argument('--from-img-root-folder', type=str, help='img list path') 
    parser.add_argument('--from-img-list-path', type=str, help='img list path')
 
    parser.add_argument('--prefix-to-img', type=str, help='prefix to img')
    parser.add_argument('--to-img-root-folder', type=str, help='img list path')
    parser.add_argument('--to-img-list-path', type=str, help='img list path')
    
    parser.add_argument('--inter-merge-list-path', type=str, help='merge img list path')
    
    parser.add_argument('--keep-above-img', type=int, help='keep image above the num you want')
    
    parser.add_argument('--save-path', type=str, help='noise save path')
    return parser.parse_args(argv)

def main(args):
    print('===> args:\n', args)

    from_img_list_path = args.from_img_list_path
    from_img_root_folder = args.from_img_root_folder
    prefix_from_img = args.prefix_from_img 

    to_img_list_path = args.to_img_list_path
    to_img_root_folder = args.to_img_root_folder
    prefix_to_img = args.prefix_to_img

    to_img_list_path_list = to_img_list_path.split(',')
    to_img_root_folder_list = to_img_root_folder.split(',')    
    prefix_to_img_list = prefix_to_img.split(',')

    keep_above_img = args.keep_above_img

    if len(to_img_list_path_list) != len(to_img_root_folder_list):
        print('The num of root floder must equal to the num of path list')
        return -1    

    to_label_img_dict = {}
    for i in range(len(to_img_list_path_list)):
        tmp_to_label_img_dict = get_label_imglist_dict(to_img_root_folder_list[i] ,to_img_list_path_list[i], prefix_to_img_list[i])
        to_label_img_dict.update(tmp_to_label_img_dict)

    from_label_img_dict = get_label_imglist_dict(from_img_root_folder ,from_img_list_path, prefix_from_img) 
    #
    inter_merge_list_path = args.inter_merge_list_path

    save_path = args.save_path
    with open(inter_merge_list_path) as f, open(save_path , 'w') as f2:
        label = -1
        count = 0
        save_to_label_dict = dict()
        result_label_img = dict()
        for key in to_label_img_dict:
            label = label + 1
            for i in range(len(to_label_img_dict[key])):
                count = count + 1
                f2.write('1' + '\t' + to_label_img_dict[key][i] + '\t' + str(label) + '\n')
        
        print('to data: %d' %(label))
        lines = f.readlines()
        count2 = 0
 
        #merge inter
        merge_label_num = 0
        below_20_lable_num = 0
        all_merge_label_num = 0
        for line in lines:
            all_merge_label_num = all_merge_label_num + 1
            key = prefix_from_img+line.strip()
            random.shuffle(from_label_img_dict[key])
            sample_num = len(from_label_img_dict[key])
            if len(from_label_img_dict[key]) > 300:
                sample_num = sample_num 
            elif len(from_label_img_dict[key]) > 200 and len(from_label_img_dict[key]) <= 300:
                sample_num = sample_num 
            elif len(from_label_img_dict[key]) > 100 and len(from_label_img_dict[key]) <= 200:
                sample_num = sample_num
            
            #
            elif len(from_label_img_dict[key]) < keep_above_img:
                below_20_lable_num = below_20_lable_num + 1
                continue
            else:
                sample_num = sample_num
            img_list = []
            label = label + 1
            merge_label_num = merge_label_num + 1 
            for i in range(sample_num):
                count = count + 1
                count2 = count2 + 1
                f2.write('1' + '\t' + from_label_img_dict[key][i] + '\t' + str(label) + '\n')
        
        print('below %d label num: %d' %(keep_above_img ,below_20_lable_num))
        print('add inter id num: %d' %(merge_label_num))
        print('all inter id num: %d' % all_merge_label_num)

        print('max label: %d' %label)
        print('add inter image: %d'%count2)
        print('all image: %d'%count)      

if __name__ == '__main__':
    main(parse_args(sys.argv[1:]))
     
