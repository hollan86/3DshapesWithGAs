# Creating Basic 3D-Shapes using a Genetic algorithm

## Introduction
A genetic algorithm(GA) is an optimization technique inspired by natural selection. There are numerous applications of GAs. In this project I attempt to create basic 3D shapes using a GA. To achieve this, I have used positional vectors in spherical coordinates system to represent similarly charged points in space. Then I used a simple fitness function that computes the total between all the point charges. 

![](https://github.com/hollan86/3DshapesWithGAs/blob/main/fitness.png )

A genetic algorithm based on the [DEAP](https://github.com/deap/deap) framework is then used to maximize this fitness. The genome used in initial experiments is a list containing random charge locations in spherical coordinates. Initial experiments show that it is possible to obtain optimum shapes using this setup. As seen below, if the genome is of length 2, the optimum shape is a straight line connecting the two point charges. If the genome is of length 3, optimum shape is an equilateral triangel connecting the three point charges. If the genome length is 4, the optimal shape is a tetrahedron. See the interactive plots below.

[Genome length=2](https://plotly.com/~hollan86/1/)

<div>
    <a href="https://plotly.com/~hollan86/1/?share_key=Y624lSWV6rlYvd6JbyN2Um" target="_blank" title="gdp_per_cap" style="display: block; text-align: center;"><img src="https://plotly.com/~hollan86/1.png?share_key=Y624lSWV6rlYvd6JbyN2Um" alt="gdp_per_cap" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plotly.com/404.png';" /></a>
    <script data-plotly="hollan86:1" sharekey-plotly="Y624lSWV6rlYvd6JbyN2Um" src="https://plotly.com/embed.js" async></script>
</div>

