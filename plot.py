from threeviz.api import plot_3d, plot_pose, plot_line_seg
import json
data = json.load(open('map.json', 'r'))

def get_midpoint_for_loc(i, j):
    return i + 0.5, j + 0.5

def main ():
    z = -0.1
    
    
    for i in range(len(data)):
        for j in range(len(data)):
            block_value = data[i][j]
            if block_value == 0:
                plot_3d(*get_midpoint_for_loc(j, j), z, 'tile blue {0}'.format(j), color='blue', size=1)
            elif block_value == 1:
                plot_3d(*get_midpoint_for_loc(j, j), z, 'tile green {0}'.format(j), color='green', size=1)
    #             0 k nam wali tile liga do
    #             else if (jsonp[i][j] == 1)
    #             1 k nam wali tile liga do

    

main()