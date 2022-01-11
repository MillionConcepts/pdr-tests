import os
import random
import requests
import sh

headers = {
    'User-Agent': 'MillionConcepts-PDART-pdrtestsuitespider (sierra@millionconcepts.com)'}


def create_product_lists(file_information: dict, mission_name):
    for key in file_information:
        database = file_information[key]['database_file']
        product_list = mission_name + '_' + file_information[key]['dataset'] + '.csv'
        with open(database, 'r') as in_file, open(product_list, 'w+') as out_file:
            for line in in_file:
                line_list = line.split(',')
                url = line_list[0]
                filename = url.split('/')[-1]
                size = line_list[2]
                if size != 0:
                    if all(val in filename for val in file_information[key]['filename_must_contain']) and \
                            'thumbnail' not in filename.lower():
                        try:
                            if all(val in url for val in file_information[key]['url_must_contain']):
                                out_file.write(url+'\n')
                        except KeyError:
                            out_file.write(url+'\n')
        in_file.close()
        out_file.close()


def random_picks(product_list: str, mission_name, destination_folder):
    with open(product_list) as pl:
        line_count = 0
        for _ in pl:
            line_count += 1
    pl.close()
    folder = product_list.lstrip(mission_name+'_').rstrip('.csv')
    if destination_folder:
        folder = os.path.join(destination_folder, folder)
    if line_count < 200:
        with open(product_list) as pl:
            for line in pl:
                line = line.rstrip('\n')
                download_file(line, folder)
    else:
        subset_indices = []
        while len(subset_indices) < 200:
            ind = random.randint(0, line_count-1)
            if ind not in subset_indices:
                subset_indices = subset_indices + [ind]
        with open(product_list) as pl:
            count = 0
            for line in pl:
                if count in subset_indices:
                    line = line.rstrip('\n')
                    download_file(line, folder)
                count += 1
        chosen_files = os.listdir(folder)
        with open(product_list, 'r') as pl, open(product_list.rstrip('.csv') + '_subset.csv', 'w+') as subset_list:
            for line in pl:
                filename = line.split('/')[-1]
                if any(val in filename for val in chosen_files):
                    subset_list.write(line)


def download_file(url: str, folder: str):
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = url.rstrip('\n').split('/')[-1]
    file_path = os.path.join(folder, filename)
    if '.TIF' or '.tif' in filename:
        lbl_path = file_path.rstrip('.TIF').rstrip('.tif') + '.LBL'
        lbl_url = url.rstrip('.TIF').rstrip('.tif') + '.LBL'
        with requests.get(lbl_url, headers=headers) as lbl_response:
            if lbl_response.ok:
                with open(lbl_path, 'wb+') as lp:
                    lp.write(lbl_response.content)
            else:
                print(f'Download of label at {lbl_url} failed.')
    with requests.get(url, stream=True, headers=headers) as response:
        if response.ok:
            # if you don't want to download to home and then move change to: with open(filename, 'wb+') as fp:
            # and comment out the sh.mv line.
            with open("/home/ubuntu"+filename, 'wb+') as fp:
                for chunk in response:
                    fp.write(chunk)
            sh.mv("/home/ubuntu/"+filename, file_path, _bg=True)
        else:
            print(f'Download of {url} failed.')


def select_and_scrape(file_information, mission_name, destination_folder=None):
    """Destination_folder should be an os.path or it will create a folder with that name inside of the place this
    script is run. By not providing a destination it will execute in the current folder. Mission_name is a string."""
    create_product_lists(file_information, mission_name)
    files_in_folder = os.listdir(destination_folder)
    data_types = []
    for k in file_information:
        data_types = data_types+[file_information[k]['dataset']]
    for file in files_in_folder:
        if any(val in file for val in data_types) and '.csv' in file:
            random_picks(file, mission_name, destination_folder)
