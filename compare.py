import settings
import os
location = settings.file_temp

removed_folders = []
added_folders = []
added_files = []
removed_files = []

def compare_folders():
    old_folders = os.listdir(f'{location}old/')
    new_folders = os.listdir(f'{location}new/')



    for folder in new_folders:
        if folder not in old_folders:
            added_folders.append(folder)

    for folder in old_folders:
        if folder not in new_folders:
            removed_folders.append(folder)

def compare_files():
    old_folders = os.listdir(f'{location}old/')
    new_folders = os.listdir(f'{location}new/')

    for file in new_folders:
        if file not in added_folders:
            temp_add = []
            temp_remove = []
            with open(f'{location}new/{file}', 'r') as f:
                new_bins = []
                for line in f:
                    bin_and_length = line.rsplit(' ')
                    bin = bin_and_length[0]
                    new_bins.append(bin)

            with open(f'{location}old/{file}', 'r') as f:
                old_bins = []
                for line in f:
                    bin_and_length = line.rsplit(' ')
                    bin = bin_and_length[0]
                    old_bins.append(bin)

            for bin in new_bins:
                if bin not in old_bins:
                    temp_add.append(bin)

            for bin in old_bins:
                if bin not in new_bins:
                    temp_remove.append(bin)
            temp = []
            temp.append(file)
            temp.append(temp_add)
            added_files.append(temp)

            temp = []
            temp.append(file)
            temp.append(temp_remove)
            removed_files.append(temp)

def output():
    with open(f'{location}summary.txt', 'w') as f:
        f.write(f"""
Summary:

=========================================================

These folders have been added: {added_folders}

=========================================================

These folders have been removed: {removed_folders}

=========================================================

These bin files have been added:
""")
        for file in added_files:
            f.write(f'\n\nIn {file[0]}:\n')
            for i in range(len(file[1])):
                f.write(file[1][i] + "\n")
        f.write('\n=========================================================\nThese bin files have been removed:\n')
        for file in removed_files:
            f.write(f'\n\nIn {file[0]}:\n')
            for i in range(len(file[1])):
                f.write(file[1][i] + "\n")

compare_folders()
compare_files()

#print("removed folders",removed_folders)
#print("added folders",added_folders)
#print("removed files",removed_files)
#print("added files",added_files)

output()
