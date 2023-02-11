# Quantum-Assisted LDPC Decoding Augmented with Classical Post-Processing for AWGN Channels


## Abstract
Utilizing present and futuristic Quantum Computers to solve difficult problems in different domains has become one of the main endeavors at this moment. Of course, in arriving at the requisite solution both quantum and classical computers work in conjunction. With the continued popularity of Low Density Parity Check (LDPC) codes and hence their decoding, this paper looks into the latter as a Quadratic Unconstrained Binary Optimization (QUBO) and utilized D-Wave 2000Q Quantum Annealer to solve it. The outputs from the Annealer are classically postprocessed using simple minimum distance decoding to further improve the performance. We evaluated and compared this implementation against the decoding performance obtained using Simulated Annealing (SA) and belief propagation (BP) decoding with classical computers. The results show that implementations of annealing (both simulated and quantum) are superior to BP decoding and suggest that the advantage becomes more prominent as block lengths increase. Reduced Bit Error Rate (BER) and Frame Error Rate (FER) are observed for simulated annealing and quantum annealing, at useful SNR range - a trend that persists for various codeword lengths.


## Model Explanation
![Model-Diagram](Assets/datasetDivision.png)

Here we are displaying the dataset composition for our experiments. For our machine learning models, we have used:
* Linear Regressor
* Random Forest Regressor
* Simple Artificial Neural Network (with one hidden layer)
* Multilayer Perceptron
* Gradient Bossting Regressor

## Results
![Model-Diagram](Assets/resultTable.png)

## Conclusion and Future Plans
Our model outperforms existing statistical estimators of bond percolation threshold as described in the article. We have introduced these models for site and explosive percolation thresholds and have obtained siginificant results. 
Out of the five models, Gradient Boosting Regressor performs the best, followed by Multilayer Perceptron and Random Forest Rregressor.
