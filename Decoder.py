import csv

import csvfile as csvfile
from dwave.system import DWaveSampler, EmbeddingComposite
import dimod
import config
from model.Problem import Problem

class Decoder:

    def __init__(self):
        self.problemCollection =[]
    def get_list_of_problems_from_csv(self, inputfilename):
        with open(inputfilename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                print("ZEILE: ",row)
                #TODO: validate input

                problem = Problem().init_problem_from_csv_line(row)
                self.problemCollection.append(problem)
                print(problem.to_string(False))
            print("problems to solve", str([x.id for x in self.problemCollection]))
        return self.problemCollection

