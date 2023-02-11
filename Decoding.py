# Import the functions and packages that are used
from dwave.system import EmbeddingComposite, DWaveSampler
from dimod import BinaryQuadraticModel #ConstrainedQuadraticModel
from dimod.reference.samplers import ExactSolver
import neal
import math
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)
pd.set_option('display.max_rows',None)
# Setup the problem
n = 20
k = 6
R = (n-k)/n
SNR = 1
W1 = 1
W2 = 1
variance = 10**(-SNR/10)
sigma = math.sqrt(variance)
def prob(z):
 return 1/(1+math.exp(-2*z/(sigma**2)))
x = [i+1000 for i in range(n)]
parity_check =
[[1,0,1,1,0,1,1,0,1,0,0,1,1,1,1,1,1,1,0,1],[0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1
],[1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0],[1,1,0,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,
1],[0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,1,1,0],[0,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0
,0]]
encoded_message = [1,0,1,1,1,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1]
print("Encoded message is {}".format(encoded_message))
bpsk_encoded = [2*t-1 for t in encoded_message]
print("BPSK message is {}".format(bpsk_encoded))
noise = math.sqrt(variance)*np.random.randn(1,n)
print("Noise Vector is {}".format(noise))
received = bpsk_encoded + noise
received = np.array(received).flatten()
print("Noisy signal is {}".format(received))
intrinsic = [prob(i) for i in received] # to be discussed
# Define QUBO variables
codeword = [f'codeword_{i}' for i in x]
# Initialize BQM
bqm = BinaryQuadraticModel('BINARY')
# Objective
for i in (x):
 bqm.add_variable(codeword[i-1000],W1*(1-2*intrinsic[i-1000]))
anc_count = 0
# Parity Check Constraint
for i in range(k):
 cnt = 0
 eligible_codewords = []
 for j in range(n):
 if(parity_check[i][j]==1):
 bqm.add_linear(codeword[j],1)
 eligible_codewords.append(codeword[j])
 cnt = cnt + 1
 num_anc = math.floor(math.log2(math.floor(cnt/2)))+1
 for _ in range(num_anc+anc_count,anc_count,-1):

bqm.add_variable('ancillary_{}'.format(_),W2*math.pow((math.pow(2,_-anc_count)),2))
 # Add quadratic terms
 for a in eligible_codewords:
 for b in range(num_anc+anc_count,anc_count,-1):

bqm.add_quadratic(a,'ancillary_{}'.format(b),-2*W2*(math.pow(2,b-anc_count)))
 for a in range(len(eligible_codewords)-1):
 for b in range(a+1,len(eligible_codewords),1):
 bqm.add_quadratic(eligible_codewords[a],eligible_codewords[b],2*W2)
 for a in range(num_anc+anc_count,anc_count+1,-1):
 for b in range(a-1,anc_count,-1):

bqm.add_quadratic('ancillary_{}'.format(a),'ancillary_{}'.format(b),2*W2*(math.pow(
2,a-anc_count))*(math.pow(2,b-anc_count)))
 anc_count = anc_count + num_anc
#qubo = bqm.to_qubo()
#print(qubo)
# Define the sampler that will be used to run the problem
#sampler = ExactSolver()
sampler = neal.SimulatedAnnealingSampler()
#sampler = EmbeddingComposite(DWaveSampler())
# Run the problem on the sampler and print the results
#sampleset = sampler.sample(bqm)
num_reads = 100
sampleset = sampler.sample(bqm,num_reads=num_reads)
frame = sampleset.to_pandas_dataframe()
s_frame = frame.sort_values(by='energy')
for t in range(anc_count):
 s_frame.drop(['ancillary_{}'.format(t+1)],axis=1,inplace=True)
#s_frame.columns = s_frame.columns.astype(int)
print(s_frame)
for i in range(num_reads):
 temp = list(s_frame.iloc[i])
 temp = temp[0:n]
 if(encoded_message==temp):
 print("String found at row no {}".format(i))
 break
 
