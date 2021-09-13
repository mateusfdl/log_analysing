import json
import pandas as pandas
from pandas.io.json import json_normalize

class Analysis:
    def __init__(self, path):
        self.file = open(path)
        self.lines = self.file.read().split('\n')
        self.data = []

    def export(self):
        self.append_parsed_data()
        data_frame = pandas.DataFrame(self.data, columns=['authenticated_entity', 'latencies', 'route'])

        data_frame['route'].apply(lambda route: route['service']['id']).value_counts().to_csv(r'./request_per_service.csv', sep='\t', encoding='utf-8')
        data_frame['authenticated_entity'].apply(lambda authenticated_entity: authenticated_entity['consumer_id']['uuid']).value_counts().to_csv(r'./request_per_consumer.csv', sep='\t', encoding='utf-8')
        avg_latencie = pandas.concat([pandas.json_normalize(data_frame['latencies']), data_frame.route.apply(lambda route: route['service']['id']).apply(pandas.Series)], axis=1).groupby(0)[['kong', 'request', 'proxy']].agg(['mean'])
        avg_latencie.to_csv(r'./avg_latencies.csv', sep='\t', encoding='utf-8')
        pass

    def append_parsed_data(self):
        for line in self.lines:
            self.data.append(json.loads(line))


