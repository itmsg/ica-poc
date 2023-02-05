from dwave.system import DWaveSampler, EmbeddingComposite
import dimod

import config
import utils
from Decoder import Decoder

problems_to_solve= Decoder().get_list_of_problems_from_csv(config.inputfilename)

qpu = DWaveSampler()
sampler= EmbeddingComposite(qpu)

for problem in problems_to_solve:
    qubo_as_dict = utils.get_input_for_qbsolv(problem.qubo_as_array)
    print ("TEST", qubo_as_dict)

    bqm= dimod.binary.BinaryQuadraticModel.from_qubo(qubo_as_dict)
    result= sampler.sample(bqm, label=problem.id)
    print("#########################")
    print("result:" ,result)
    print("#########################")
    print("result.info:" ,result.info)
    print("#########################")
    print("result.data_vectors:" ,result.data_vectors)
    print("#########################")
    print("result.record:" ,result.record)
    print("#########################")
    print("result.first:" ,result.first)
    print("#########################")
    print("result.variables:" ,result.variables)
    print("#########################")
    print("result.samples:" ,result.samples())
    print("#########################")
    print("result.lowest:" ,result.lowest())
    print("#########################")