from dwave.system import DWaveSampler, EmbeddingComposite
import dimod

qpu = DWaveSampler()

sampler= EmbeddingComposite(qpu)
bqm= dimod.binary.BinaryQuadraticModel.from_qubo({('b', 'a'): 2.0, ('a', 'a'): -1.0, ('b', 'b'): -1.0})
result= sampler.sample(bqm, label="Swing-Sample: 1 swing, 2 persons")
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