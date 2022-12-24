import os
import re
import subprocess
import time

command = ['nvidia-smi', '--query-gpu=name,utilization.gpu,fan.speed,memory.total,memory.used,temperature.gpu', '--format=csv']
reset_color = '\033[0m'
while True:
    os.system('clear')
    t = time.time()
    p = subprocess.check_output(command)
    data = p.decode('utf-8').split('\n')[1].split(',')
    name = data[0]
    util = int(re.findall(r'\d+', data[1])[0])
    fan = int(re.findall(r'\d+', data[2])[0])
    ram_total = int(re.findall(r'\d+', data[3])[0])
    ram_used = int(re.findall(r'\d+', data[4])[0])
    temp = int(re.findall(r'\d+', data[5])[0])
    ram_percent = int(ram_used) / int(ram_total)
    if 0 < ram_percent < .5:
        ram_color = '\033[32m'
    elif ram_percent < .75:
        ram_color = '\033[33m'
    else:
        ram_color = '\033[31m'
    if util < 50:
        gpu_color = '\033[32m'
    elif util < 90:
        gpu_color = '\033[33m'
    else:
        gpu_color = '\033[31m'
    if fan < 50:
        fan_color = '\033[32m'
    elif fan < 75:
        fan_color = '\033[33m'
    else:
        fan_color = '\033[31m'
    if temp > 65:
        tempcolor = '\033[33m'
    elif temp > 75:
        tempcolor = '\033[31m'
    else:
        tempcolor = '\033[32m'

    print(reset_color+name)
    print(f'Fan: {fan_color}{fan}%{reset_color}, Temp: {tempcolor}{temp}C')
    print(f'{reset_color}Memory-Usage[{ram_color}{"|"*int(ram_percent/2*100)}{" "*(50-int(ram_percent/2*100))}\033[0m]: {ram_used}/{ram_total}')
    print(f'{reset_color}GPU-Util    [{gpu_color}{"|"*int(util/2)}{" "*(50-int(util/2))}\033[0m]: {util}%')
    time.sleep(1-(time.time()-t))
