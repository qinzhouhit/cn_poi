import pickle
import os
import sys
import collections


def city_poi_extract(argv):
    # TODO: have POI formatted into pickle
    """
    file header: 0)address, 1)adname, 2)page_publish_time, 3)adcode, 4)pname,
    5)cityname, 6)name, 7)location, 8)_id, 9)type,
    e.g., 0)丰城市,1)丰城市,2)2017-06-19 02:26:39,3)360981,4)江西省,5)宜春市,
    6)怡丰花园15号楼,7)115.768309，28.152627,8)j#20170619#6d2ee48230dd6861879e5ac8c8434933,
    9)地名地址信息;门牌信息;楼栋号,
    :return: k: (lng, lat), v: a list of categories
    """
    
    data_path = "some_path"
    files = []
    for i in os.listdir(data_path):
        if i.startswith("poi"):
            try:
                for j in os.listdir(os.path.join(data_path, i)):
                    if j.endswith("csv"):
                        files.append(os.path.join(data_path, i, j))
            except NotADirectoryError:
                continue
    res = collections.defaultdict(list)
    for file in files:
        print (file)
        try:
            for line in open(file, encoding="gbk"):
                attrs = line.split(",")
                if attrs[5] == argv[0]: #
                    coords = attrs[7].split("，")
                    categories = attrs[-2].split(";")
                    res[(float(coords[0]), float(coords[1]))] = categories
        except UnicodeDecodeError:
            # for line in open(file, encoding="ISO-8859-1"):
            #     print (line)
            continue
    pickle.dump(res, open(argv[1] + "_poi_pku.p", "wb"))

    
if __name__=="__main__":
    city_poi_extract(sys.argv[1:])
