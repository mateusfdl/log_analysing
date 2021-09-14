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
        self.export_average_latencie()
        self.export_request_per_consumer()
        self.export_request_per_service()

    def append_parsed_data(self):
        for line in self.lines:
            if line: 
                self.data.append(json.loads(line))
            else:
                pass
    
    def data_frame(self):
        return pandas.DataFrame(self.data, columns=['authenticated_entity', 'latencies', 'route'])

    def export_average_latencie(self):
        avg_latencie = pandas.concat([
            pandas.json_normalize(self.data_frame()['latencies']), 
            self.data_frame().route.apply(lambda route: route['service']['id'])
            .apply(pandas.Series)], axis=1).groupby(0)[['kong', 'request', 'proxy']].agg(['mean'])

        avg_latencie.to_csv(r'./logs/avg_latencies.csv', sep='\t', encoding='utf-8')

    def export_request_per_service(self):
        self.data_frame()['route'].apply(lambda route: 
                route['service']['id']).value_counts().to_csv(
                        r'./logs/request_per_service.csv', sep='\t', encoding='utf-8')

    def export_request_per_consumer(self):
       self.data_frame()['authenticated_entity'].apply(lambda authenticated_entity: 
                authenticated_entity['consumer_id']['uuid']).value_counts().to_csv(
                        r'./logs/request_per_consumer.csv', sep='\t', encoding='utf-8')
