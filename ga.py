import random
from deap import creator, base, tools, algorithms
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from plot import vector_plot

def get_genes():
	'''
	returns a tuple of (r,theta,thi) i.e. spherical coordinates
	'''
	return [1,np.random.uniform(0,1)*np.pi,np.random.uniform(0,1)*2*np.pi]

def distance(a,b):
	return np.sqrt(a[0]**2 + b[0]**2 -2*a[0]*b[0]*(np.sin(a[1])*np.sin(b[1])*np.cos(a[2]-b[2]) + np.cos(a[1])*np.cos(b[1])))

def total_distance(individual):
	total = 0
	for i, a in enumerate(individual[:-1]):
		for b in individual[i+1:]:
			total += distance(a,b)
	return total,

def mutate_custom(individual,mR=False,mTheta=True,mThi=True,indp=0.05):
	for g in individual:
		if mR and random.random() < indp:
			print('mutating radius')
			c = np.random.uniform(0.5,1.5)
			g[0] *= g[0]*c
		elif mTheta and random.random() < indp:
			print('mutating Theta')
			g[1] = np.random.uniform(0,1)*np.pi
		elif mThi and random.random() < indp:
			print('mutating Thi')
			g[2] = np.random.uniform(0,1)*2*np.pi



creator.create("FitnessMaxDistance", base.Fitness,weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMaxDistance)

toolbox = base.Toolbox()

toolbox.register("vec_genes",get_genes)
toolbox.register("individual", tools.initRepeat,creator.Individual,toolbox.vec_genes,n=4)
toolbox.register("population",tools.initRepeat,list, toolbox.individual)

toolbox.register("evaluate",total_distance)
toolbox.register("mate",tools.cxOnePoint)
toolbox.register("mutate",mutate_custom)
toolbox.register("select", tools.selTournament, tournsize=3)

if __name__ == '__main__':
	population = toolbox.population(n=100)
	#evaluate the entire population
	fitnesses = list(map(toolbox.evaluate,population))
	for ind, fit in zip(population, fitnesses):
		ind.fitness.values = fit

	#extracting all the fitnesses of 
	fits = [ind.fitness.values[0] for ind  in population]

	g = 0
	nG = 1000
	#Begin the evolution
	while g < nG:
		# A new generation
		g = g + 1
		CXPB = 0.5

		print(f'-- Generation {g} --')
		#select the next generation of individuals
		offspring = toolbox.select(population, len(population))
		#clone selected individuals
		offspring = list(map(toolbox.clone, offspring))

		#apply crossover and mutation on the offspring
		for child1, child2 in zip(offspring[::2], offspring[1::2]):
			if random.random() < CXPB:
				toolbox.mate(child1, child2)
				del child1.fitness.values
				del child2.fitness.values

		for mutant in offspring:
			toolbox.mutate(mutant)
			del mutant.fitness.values			

		#Evaluate individuals with an invalid fitness
		invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
		fitnesses = map(toolbox.evaluate, invalid_ind)
		for ind, fit in zip(invalid_ind, fitnesses):
			ind.fitness.values = fit
		population[:] = offspring

		#Gather all the fitnesses in one list 
		fits = [ind.fitness.values[0] for ind in population]
		#strongest = [ind for ind in population if ind.fitness.values[0] == max(fits)]
		if g == 999:
			for ind in population:
				if ind.fitness.values[0] == max(fits):
					strongest = ind
	
		length = len(population)
		mean = sum(fits) / length
		sum2 = sum(x*x for x in fits)
		std = abs(sum2 / length - mean**2)**0.5

		print("Min %s" % min(fits))
		print("Max %s" % max(fits))
		print("Avg %s" % mean)
		print("Std %s" % std)

vects = [[g[0]*np.sin(g[1])*np.cos(g[2]),g[0]*np.sin(g[1])*np.sin(g[2]),g[0]*np.cos(g[1])] for g in strongest]
print(vects)
print(strongest)
vector_plot(vects)
