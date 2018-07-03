import os
import sys
import argparse

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--inter-noise-list', type=str, help='inter noise list')
    parser.add_argument('--same-label-list', type=str, help='output same label list')
    return parser.parse_args(argv)

def main(args):
    print('===> args:\n', args)
    inter_noise_list = args.inter_noise_list
    same_label_list = args.same_label_list

    with open(inter_noise_list) as f, open(same_label_list,'w') as f1:
        lines = f.readlines()
        from_label_list = []
        for line in lines:
            from_label = line.strip().split('  ')[0]
            from_label_list.append(from_label)
        from_label_set = set(from_label_list)
        result = []
        for item in from_label_set:
            tmp = []
            tmp.append(item)
            for line in lines:
                from_label = line.strip().split('  ')[0]
                if item == from_label:
                    to_label = line.strip().split('  ')[1]
                    tmp.append(to_label)
            result.append(tmp)
        for i in range(len(result)):
            for j in range(len(result[i])):
                f1.write(result[i][j]+' ')
            f1.write('\n')

if __name__ == '__main__':
    main(parse_args(sys.argv[1:]))















