import os
import random
import requests
import sh
from pdr.formats import DATA_EXTENSIONS
from importlib import import_module

headers = {
    'User-Agent': 'MillionConcepts-PDART-pdrtestsuitespider (sierra@millionconcepts.com)'}


class TemporaryNameUntilMyBrainWorks:
    def __init__(self, mission_name, destination_folder=None):
        rules_module = import_module(f"selection_rules.{mission_name}")
        self.file_information = getattr(rules_module, "file_information")
        self.mission_name = mission_name
        self.destination_folder = destination_folder
        """Destination_folder should be an os.path or it will create a folder with that name inside of the place this
        script is run. By not providing a destination it will execute in the current folder."""
        self.select_and_scrape()

    def create_product_lists(self):
        for key in self.file_information:
            database = self.file_information[key]['database_file']
            product_list = self.mission_name + '_' + self.file_information[key] + '.csv'
            with open(database, 'r') as in_file, open(product_list, 'w+') as out_file:
                for line in in_file:
                    line_list = line.split(',')
                    url = line_list[0]
                    filename = url.split('/')[-1]
                    size = line_list[2]
                    if int(size) != 0:
                        if all(val in filename for val in self.file_information[key]['filename_must_contain']) and \
                                'thumbnail' not in filename.lower():
                            try:
                                if all(val in url for val in self.file_information[key]['url_must_contain']):
                                    out_file.write(line)
                            except KeyError:
                                out_file.write(line)
            in_file.close()
            out_file.close()

    def random_picks(self, product_list: str):
        with open(product_list) as pl:
            line_count = 0
            for _ in pl:
                line_count += 1
        pl.close()
        dataset_type = product_list.lstrip(self.mission_name+'_').rstrip('.csv')
        if self.destination_folder:
            folder = os.path.join(self.destination_folder, dataset_type)
        else:
            folder = dataset_type
        if line_count < 200:
            with open(product_list, 'r') as pl, open(product_list.rstrip('.csv') + '_subset.csv', 'w+') as subset_list:
                for line in pl:
                    line_list = line.split(',')
                    url = line_list[0]
                    # filename = url.split('/')[-1]
                    size = line_list[2]
                    if int(size) / (1 * 10 ** 9) < 8:
                        self.download_file(url, folder, dataset_type)
                        subset_list.write(url+'\n')
        else:
            subset_indices = []
            files_downloaded = 0
            while files_downloaded < 200 and len(subset_indices) < line_count-1:
                ind = random.randint(0, line_count-1)
                if ind not in subset_indices:
                    subset_indices = subset_indices + [ind]
                with open(product_list, 'r') as pl, \
                        open(product_list.rstrip('.csv') + '_subset.csv', 'w+') as subset_list:
                    count = 0
                    for line in pl:
                        line_list = line.split(',')
                        url = line_list[0]
                        # filename = url.split('/')[-1]
                        size = line_list[2]
                        if count in subset_indices and int(size) / (1 * 10 ** 9) < 8:
                            self.download_file(url, folder, dataset_type)
                            files_downloaded += 1
                            subset_list.write(url+'\n')
                        count += 1

    def download_file(self, url: str, folder: str, dataset_type):
        if not os.path.exists(folder):
            os.makedirs(folder)
        filename = url.rstrip('\n').split('/')[-1]
        file_path = os.path.join(folder, filename)

        if self.file_information[dataset_type]['label'] == 'D':
            for val in DATA_EXTENSIONS:
                lbl_path = file_path.rstrip(val) + '.LBL'
                lbl_url = url.rstrip(val) + '.LBL'
            with requests.get(lbl_url, headers=headers) as lbl_response:
                if lbl_response.ok:
                    with open(lbl_path, 'wb+') as lp:
                        lp.write(lbl_response.content)
                else:
                    print(f'Download of label at {lbl_url} failed.')
        if self.file_information[dataset_type]['label'] == 'A':
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

    def select_and_scrape(self):
        self.create_product_lists()
        files_in_folder = os.listdir(self.destination_folder)
        data_types = []
        for k in self.file_information:
            data_types = data_types+[self.file_information[k]['dataset']]
        for file in files_in_folder:
            if any(val in file for val in data_types) and '.csv' in file:
                self.random_picks(file)
