#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp 
# @Time: 2021/5/23 18:49
# @File: yaml_util.py
import yaml


class YamlUtil:
    def __init__(self, yaml_file):
        """
        传入yaml文件
        :param yaml_file:
        """
        self.yaml_file = yaml_file

    def read_yaml(self):
        with open(self.yaml_file, 'r', encoding='utf8')as fp:
            yaml_data = yaml.load(fp, Loader=yaml.FullLoader)

        return yaml_data


if __name__ == '__main__':
    uaml = YamlUtil('../data/data_file.yaml')
    aa = uaml.read_yaml()
    print(aa[0]['name'])
