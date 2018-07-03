import os
import sys
import argparse
def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--img-root-folder', type=str, help='img root folder')
    parser.add_argument('--intra-noise-path', type=str, help='noise  path')
    parser.add_argument('--threshold', type=float, help='less threshold will remove')
    return parser.parse_args(argv)

def main(args):
    print('===> args:\n', args)
    root_folder = args.img_root_folder
    del_list = args.intra_noise_path
    threshold = args.threshold
    with open(del_list) as f:
        lines = f.readlines()
        for line in lines:
            score = float(line.strip().split(' ')[1])
            if score < threshold:

                dir_list = line.strip().split(' ')[0].split('_')
                tmp_name = dir_list[0]
                for i in range(1,len(dir_list) -1):
                    tmp_name = tmp_name + '_'+dir_list[i]

                img_name = tmp_name

                path = os.path.join(root_folder, img_name)
                if os.path.exists(path):
                    os.remove(path)
                    print('remove: '+ path )
                else:
                    print('not existed: ' + path)
            
if __name__ == '__main__':
    main(parse_args(sys.argv[1:]))             
