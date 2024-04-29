

#pip install pgmpy

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure of the Bayesian Network
model = BayesianModel([('Rain', 'Sprinkler')])

# Define the Conditional Probability Distributions (CPDs)
cpd_rain = TabularCPD(variable='Rain', variable_card=2, values=[[0.2], [0.8]])
cpd_sprinkler = TabularCPD(variable='Sprinkler', variable_card=2, 
                            values=[[0.4, 0.9], [0.6, 0.1]],
                            evidence=['Rain'], evidence_card=[2])

# Add CPDs to the model
model.add_cpds(cpd_rain, cpd_sprinkler)

# Check the model for consistency
print("Model is valid:", model.check_model())

# Perform variable elimination to get conditional probability
inference = VariableElimination(model)
prob_sprinkler_given_rain = inference.query(variables=['Sprinkler'], evidence={'Rain': 1})
print(prob_sprinkler_given_rain)
