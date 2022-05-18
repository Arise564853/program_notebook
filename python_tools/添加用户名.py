import os


os.chdir(r'G:\2021年起重工地')
for dirs in os.listdir('.'):
    if dirs in ['2021朱卫平(吴健)']:
        for sub_dir in os.listdir(f'./{dirs}'):
            if dirs[4:] in sub_dir:
                old_name = f'./{dirs}/{sub_dir}'
                new_name = f"./{dirs}/{sub_dir.replace(dirs[4:], '')}"
                os.renames(old_name, new_name)


