import os
import sys
'''
def getImgList(path):
    with open(path) as f:
        lines = f.readlines()
        label_img_dict = dict()

        current_label = ''
        pre_label = ''
        img_list = []
        i = 0
        for line in lines:
            i = i + 1
            label = line.strip().split('\t')[2]
            if label != current_label:
                if len(img_list) > 0:
                    label_img_dict[pre_label] = img_list
                    img_list = []
                current_label = label
                img_list.append(line.strip()+'\n')
            else:
                img_list.append(line.strip()+'\n')
                pre_label = current_label
                if i == len(lines):
                    label_img_dict[pre_label] = img_list
        return label_img_dict
'''
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
            label = line.strip().split('\t')[2]
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
        return label_img_dict


if __name__ == '__main__':
    img_dict = get_label_featurelist_dict('/workspace/data/qyc/train-rec/faceemore-asian-train-celebrity-up0-175273/train.lst')
   
    count_list = [0 for i in range(10)]
    for key in img_dict:
        if len(img_dict[key]) > 0 and len(img_dict[key]) <= 10:
            count_list[0] += 1
        elif len(img_dict[key]) > 10 and len(img_dict[key]) <= 20:
            count_list[1] += 1
        elif len(img_dict[key]) > 20 and len(img_dict[key]) <= 50:
            count_list[2] += 1
        elif len(img_dict[key]) > 50 and len(img_dict[key]) <= 80:
            count_list[3] += 1
        elif len(img_dict[key]) > 80 and len(img_dict[key]) <= 100:
            count_list[4] += 1
        elif len(img_dict[key]) > 100 and len(img_dict[key]) <= 150:
            count_list[5] += 1
        elif len(img_dict[key]) > 150 and len(img_dict[key]) <= 200:
            count_list[6] += 1
        elif len(img_dict[key]) > 200 and len(img_dict[key]) <= 250:
            count_list[7] += 1
        elif len(img_dict[key]) > 250 and len(img_dict[key]) <= 300:
            count_list[8] += 1
        else :
            count_list[9] += 1
    print(count_list)    
