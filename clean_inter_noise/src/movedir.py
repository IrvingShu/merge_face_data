import os
import sys
import shutil
import os.path as osp

import argparse

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--img-root-folder', type=str, help='img root folder')
    parser.add_argument('--inter-same-label-path', type=str, help='merge same label path')
    return parser.parse_args(argv)

def main(args):
    root_folder = args.img_root_folder
    inter_same_path = args.inter_same_label_path
    with open(inter_same_path) as f:
        lines = f.readlines()
        for line in lines:
            labels = line.strip().split(' ')
            dst = osp.join(root_folder, labels[0])
            for i in range(1,len(labels)):
                src = osp.join(root_folder,labels[i])
                if osp.exists(dst):
                    if osp.exists(src):
                        print('from %s to %s'%(src,dst))
                        shutil.move(src, dst)
                    else:
                        print('src: %s not existed' %(src))
                else:
                    print('dst: %s not existed'%(dst))

if __name__ == '__main__':
    main(parse_args(sys.argv[1:]))
