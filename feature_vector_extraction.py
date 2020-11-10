from os import listdir, scandir
from os.path import isfile, isdir, join
import string
import statistics
import json

weeks = [('./Processed/'+ d) for d in listdir('./Processed') if isdir(join('./Processed', d))]

feature_vectors = {}
for week in weeks:
    feature_vectors[week] = {}
    rolls = [d for d in listdir(week) if isdir(join(week, d))]
    for roll in rolls:
        try:
            feature_vectors[week][roll]
        except KeyError:
            feature_vectors[week][roll] = {}
            feature_vectors[week][roll]['hold_time'] = {}
            feature_vectors[week][roll]['latencies'] = {}
            alpha_list = list(string.ascii_uppercase)
            for alpha in alpha_list:
                feature_vectors[week][roll]['hold_time'][alpha] = []
            for alpha in alpha_list:
                for alpha1 in alpha_list:
                    feature_vectors[week][roll]['latencies'][alpha + alpha1] = []

        path = week + '/' + roll + '/Train data/hold_time'
        files = [f for f in listdir(path) if isfile(join(path, f))]
        for file in files:
            with open(path + '/' + file) as f:
                content = f.readlines()
            f.close()
            content = [float(x.strip()) for x in content]
            feature_vectors[week][roll]['hold_time'][file.replace('.txt', '')].extend(content)

        path = week + '/' + roll + '/Train data/latencies'
        files = [f for f in listdir(path) if isfile(join(path, f))]
        for file in files:
            with open(path + '/' + file) as f:
                content = f.readlines()
            f.close()
            content = [float(x.strip()) for x in content]
            feature_vectors[week][roll]['latencies'][file.replace('.txt', '')].extend(content)

mean_feature_vector = {}
for week in weeks:
    mean_feature_vector[week] = {}
    for roll in feature_vectors[week]:
        mean_feature_vector[week][roll] = []
        for file in feature_vectors[week][roll]['hold_time']:
            if len(feature_vectors[week][roll]['hold_time'][file]) != 0:
                mean_feature_vector[week][roll].append(statistics.mean(feature_vectors[week][roll]['hold_time'][file]))
            else:
                mean_feature_vector[week][roll].append(0)
        for file in feature_vectors[week][roll]['latencies']:
            if len(feature_vectors[week][roll]['latencies'][file]) != 0:
                mean_feature_vector[week][roll].append(statistics.mean(feature_vectors[week][roll]['latencies'][file]))
            else:
                mean_feature_vector[week][roll].append(0)

mean_feature_vector_1 = {}
for week in mean_feature_vector:
    t = week
    mean_feature_vector_1[t.replace('./Processed/', '')] = mean_feature_vector[week]

# print(mean_feature_vector_1)
# print(len(mean_feature_vector_1[week.replace('./Processed/', '')][roll]))

with open("mean_feature_vector_splitted_new.json", "w") as outfile:
    json.dump(mean_feature_vector_1, outfile)
