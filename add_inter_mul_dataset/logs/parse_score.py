import os
import sys

if __name__ == '__main__':
    with open("./0.6_0.85_trill-celeb-to-blueface95660.log") as f, open('./0.45_inter_trill-celeb-to-blueface95660.txt','w') as f1:
        lines = f.readlines()
        for line in lines:
            score = float(line.strip().split(' ')[2])
            if score <= 0.45:
                f1.write(line.split(' ')[0] + '\n')
    
    
