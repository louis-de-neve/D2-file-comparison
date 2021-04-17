import settings
import os

def generate_old_list():

    old = f'D:/{settings.old_dir}/'
    old_sub_folders = os.listdir(old)[::-1]

    for folder in old_sub_folders:
        path = f'{old}{folder}'
        bin_list = os.listdir(path)[::-1]
        with open(f'{settings.file_temp}old/{folder}.txt', 'w') as f:
            for bin in bin_list:
                size = os.path.getsize(f'{path}/{bin}')
                f.write(bin + " " + str(size) + '\n')

def generate_new_list():

    new = f'D:/{settings.new_dir}/'
    new_sub_folders = os.listdir(new)[::-1]

    for folder in new_sub_folders:
        path = f'{new}{folder}'
        bin_list = os.listdir(path)[::-1]
        with open(f'{settings.file_temp}new/{folder}.txt', 'w') as f:
            for bin in bin_list:
                size = os.path.getsize(f'{path}/{bin}')
                f.write(bin + " " + str(size) + '\n')

generate_old_list()
generate_new_list()