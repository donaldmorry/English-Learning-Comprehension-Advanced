# Lesson 06 · A Thousand Small Stupidities

**Topic:** Swarm robotics, stigmergy and emergent behaviour  
**Style & Register:** Comparative science writing — playful, structurally patterned, analogical  
**Level:** C1–C2

---

## Reading Passage

A termite mound in savannah country may stand four metres high. It contains ventilation shafts that maintain the internal atmosphere within a narrow range despite an external temperature swinging through thirty degrees each day, a cellar excavated down to the water table, and a fungus garden kept at a temperature the fungus requires and the termites do not. Construction takes years. The finished structure is proportionally taller, relative to its builders, than any building humans have erected.

There is no architect. There is no plan. There is no termite anywhere in that mound with the faintest conception of what a mound is, and none of them can see more than a few millimetres in any direction.

This ought to be impossible, and the resolution of why it is not is one of the more useful ideas available to anyone designing distributed systems.

**The trick is the material**

The mechanism was named in 1959 by a French biologist who observed that termites do not coordinate by communicating with each other. They coordinate by modifying their shared environment, and then responding to the modification.

A termite carrying a pellet of soil deposits it where the local concentration of a particular pheromone is highest — that is, where other pellets have recently been placed. The deposit raises the concentration there, making the spot more attractive to the next termite. Small random accumulations grow into pillars. When two pillars rise near each other, the gradients between them tilt inwards and the builders begin bridging. An arch appears. Nobody built an arch. Every termite executed one rule — *put it where the smell is strongest* — and the arch was that rule interacting with a partially built wall.

This is *stigmergy*, and its defining feature is that the workers do not need to know anything. The memory of the colony is not held in the termites. It is held in the mound. The half-finished structure is the instruction set, continuously updated, readable by anyone who wanders past, requiring no addressing, no message passing and no shared clock.

**A second recipe, and a third**

The same architecture recurs across biology with different implementing chemistry, and the pattern is worth laying side by side.

*Ants and the shortest path.* A foraging ant returning from food lays a trail. Others follow trails probabilistically, preferring stronger ones, and reinforce what they follow. Consider two routes to the same food, one short and one long. Ants on the short route complete the round trip more often per unit time, so they deposit more per unit time, so the short route's signal strengthens faster, so more ants choose it, so it strengthens faster still. Meanwhile the pheromone evaporates, which erases obsolete solutions. The colony converges on the shorter path without any ant having compared the two — indeed without any ant being capable of comparison. Positive feedback finds the answer; evaporation prevents the answer from being permanent.

*Flocking.* In 1986 a computer graphics researcher, attempting to animate birds without keyframing each one, gave every simulated bird three local rules: steer away from neighbours that are too close, match the average heading of nearby neighbours, and move towards the average position of nearby neighbours. Separation, alignment, cohesion. That is the whole specification. The resulting flocks split around obstacles and rejoin on the far side, produce the rolling density waves seen in real starling murmurations, and were never told to do any of it.

*Slime mould.* A single-celled organism with no nervous system, placed in a maze with food at two points, withdraws from the dead ends and maintains a tube along the shortest connecting route. Given food sources arranged to match a country's major cities, it produces a network whose efficiency and redundancy are comparable to the rail system engineers spent a century designing.

Four organisms, four chemistries, one architecture: numerous simple agents, strictly local information, a shared medium that carries the state, and feedback that amplifies what works while decaying what does not.

**Why engineers want this**

Three properties follow from the design, and all three are properties that centralised systems struggle to buy at any price.

*Robustness.* There is no component whose failure stops the system. Remove a third of the ants and the colony forages more slowly. Remove the central controller from a conventional robotic system and it stops entirely. Swarms degrade; they do not fail.

*Scalability.* Because every agent interacts only with its neighbours, the computational and communication load on each individual does not grow as the population grows. A thousand-unit swarm is not a thousand times harder to run than a ten-unit swarm. It is the same difficulty, repeated.

*Flexibility.* The behaviour is specified by local rules rather than by a global plan, so the system does not need to be reprogrammed when the environment changes. It was never programmed for the environment in the first place.

**Why it remains rare**

And yet the number of genuinely swarm-controlled systems in commercial operation is small, which requires explaining.

The difficulty is the inverse problem. Going forwards is easy: give agents rules, run the simulation, observe what emerges. Going backwards is very hard indeed: specify the global behaviour you want, and derive the local rules that will produce it. There is no general method. Emergent outcomes are not linear functions of their rules — a small change to a threshold can produce a qualitatively different collective result — which means design proceeds largely by search, simulation and intuition, and the resulting systems resist the kind of formal guarantee that safety certification requires.

There is also a marketing confusion worth clearing up. Coordinated drone displays, in which hundreds of aircraft form shapes in the sky, are routinely described as swarms. They are the opposite. Every trajectory is computed centrally in advance, and each aircraft flies a prescribed path while reporting its position. It is a beautifully executed orchestra, and an orchestra is precisely the thing a swarm is not: a swarm has no score and no conductor.

Where genuine swarm behaviour has found use, it is in domains matching the biology — distributed environmental sensing, exploration of spaces too large or too dangerous to map first, and experimental construction systems in which simple units add material by local rules until a structure accumulates.

The concluding thought is a discomforting one, and it is the reason the idea keeps returning. Intelligence, in these systems, is not located anywhere. It is not in the agent, which is stupid, and it is not in the rules, which are trivial. It exists only in the interaction, and only while the interaction is running. Take the system apart to find out how it works and you will find nothing at all — just a thousand small stupidities, each of them inadequate, arranged in the one configuration that happens to add up.

---

## Key Vocabulary

**ventilation** *(n.)* — the circulation of air through a structure.
**excavate** *(v.)* — to dig out.
**conception** *(n.)* — a mental grasp or idea of something.
**pellet** *(n.)* — a small compressed ball of material.
**gradient** *(n.)* — a gradual change in concentration across space.
**tilt** *(v.)* — to lean or slope in a direction.
**stigmergy** *(n.)* — coordination through traces left in a shared environment.
**instruction set** *(n. phr.)* — the complete list of commands a system can execute.
**forage** *(v.)* — to search widely for food.
**probabilistically** *(adv.)* — according to chance weighted by likelihood.
**reinforce** *(v.)* — to strengthen by adding to.
**evaporate** *(v.)* — to disperse into vapour and disappear.
**obsolete** *(adj.)* — no longer useful or current.
**converge** *(v.)* — to move towards a single point or solution.
**heading** *(n.)* — the direction in which something is travelling.
**cohesion** *(n.)* — the tendency to stay together as a group.
**redundancy** *(n.)* — deliberate duplication providing tolerance of failure.
**amplify** *(v.)* — to increase in strength or magnitude.
**degrade** *(v.)* — to decline gradually in performance rather than stopping outright.
**threshold** *(n.)* — the value at which a behaviour changes.
**qualitatively** *(adv.)* — in kind rather than merely in amount.
**prescribed** *(adj.)* — laid down in advance as a rule or plan.

## Phrases & Collocations

**with the faintest conception of** — having even the slightest understanding of. *Emphatic negative.*
**lay side by side** — to place together for direct comparison.
**per unit time** — for each equal interval; a standard rate formulation.
**at any price** — under no circumstances obtainable, however much is paid.
**worth clearing up** — deserving to be corrected because it causes confusion.
**add up** — to combine into a coherent or meaningful whole.
