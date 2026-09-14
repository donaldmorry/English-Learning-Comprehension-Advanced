# Lesson 38 · The Butterfly and the Supercomputer

**Topic:** Weather forecasting, chaos and the limits of prediction  
**Style & Register:** Explanatory narrative — historical, elegant, quietly dramatic  
**Level:** C1–C2

---

## Reading Passage

In 1922 an English mathematician published a book proposing that the weather could be calculated.

The claim was not mystical. Lewis Fry Richardson's argument was that the atmosphere obeys known physical laws — the conservation of mass, momentum and energy — and that if one knew its present state with sufficient precision, one could divide the globe into cells, apply those laws numerically, and step forward in time. The future weather was not a matter of signs and intuition. It was an arithmetic problem with an enormous number of terms.

To demonstrate it, he had already attempted a calculation by hand, working in intervals between ambulance duty during the war, using observations from a single day in central Europe. It took him something close to six weeks to produce a six-hour forecast. The forecast was spectacularly wrong: it predicted a pressure change many times larger than anything the atmosphere has ever produced.

The method, it later emerged, was sound. The failure lay in the initial data, which contained small inconsistencies that the equations amplified into a violent and entirely fictitious storm.

Richardson was undeterred. At the end of his book he sketched what would be required to keep pace with the weather rather than fall six weeks behind it: a vast hall, he suggested, shaped like a theatre, in which sixty-four thousand human computers each worked on one cell of the globe, coloured signals coordinating their pace, a conductor on a central dais directing the whole calculation like an orchestra. He estimated that this would be just sufficient to compute the weather as fast as it actually happened.

The proposal was received as a charming absurdity. It was, in every respect that matters, a specification for the machines that now do exactly this — and the number of cells he proposed is modest by modern standards.

---

The first electronic forecast was produced in 1950 on one of the earliest computers, which took approximately twenty-four hours to generate a twenty-four-hour prediction. That is the break-even point, and after it the arithmetic improved rapidly. Within a decade, operational numerical forecasting had begun. Within two, it had displaced the older methods.

And then, in 1961, a meteorologist at an American university encountered something that no one had expected and that turned out to be more important than any improvement in the calculation.

Edward Lorenz was running a simplified atmospheric model on a small machine and wanted to re-examine a particular sequence. Rather than begin again, he restarted the run partway through, typing in the numbers from an earlier printout. He went for coffee. When he returned, the new run had diverged from the old one so completely that the two bore no resemblance.

The explanation was banal and its implication was not. The machine held numbers to six decimal places internally but printed three. The value he had entered differed from the value the machine had been using by about one part in ten thousand — a discrepancy far smaller than any conceivable error in a real weather observation. That difference had doubled, and doubled again, until it dominated the solution entirely.

This is sensitive dependence on initial conditions, and Lorenz spent the following decade establishing that it was not an artefact of his simplifications but a property of the underlying equations. The system is entirely deterministic: no randomness enters, and the same input produces the same output every time. It is nevertheless unpredictable in the long run, because the precision required to forecast a given distance ahead grows exponentially with that distance, and exact precision is unobtainable.

The talk in which he presented this carried a title that has escaped into general language and is now mostly used to mean something he did not intend. *Does the flap of a butterfly's wings in Brazil set off a tornado in Texas?* The point was not that small causes have large effects, which is unremarkable. It was that in such a system, error at any scale propagates upward into every larger scale, so that microscopic uncertainty places an absolute ceiling on how far ahead the atmosphere can be predicted at all.

For weather, that ceiling appears to lie at about two weeks. It is not a limit of computing power or of observation, and no future advance will remove it. It is a property of the equations.

---

What is remarkable is how much was achieved after this discovery, and how the profession's response changed the meaning of a forecast.

If error growth is unavoidable, then a single prediction is a poor product, because it conveys no information about its own reliability. The response, developed through the 1990s, was to stop making one forecast. An ensemble forecast runs the model dozens of times from slightly perturbed starting conditions, each within observational uncertainty. If the members stay close together, the atmosphere is in a predictable state and confidence is high. If they diverge within two days, it is not, and no amount of insistence will make it so.

This is why forecasts are now expressed as probabilities. A thirty per cent chance of rain is not evasion. It is the proportion of ensemble members that produced rain, and it carries more information than any single deterministic statement could.

Meanwhile the inputs improved beyond anything Richardson could have assembled. Satellite instruments measure radiation at many wavelengths from which temperature and humidity profiles are inferred; commercial aircraft report continuously; buoys, balloons and ground stations feed in. These observations are irregular, of varying quality, and never sufficient to specify the atmosphere completely. They are combined with a short forecast from the previous cycle, in a procedure that weights each by its estimated error, to produce the best available estimate of the present state. Half the skill of modern forecasting lies in this step, and it receives almost none of the attention.

The cumulative gain has been steady and is easy to overlook. A five-day forecast today is about as accurate as a three-day forecast was in the early 1990s — roughly one additional day of useful skill per decade, sustained for forty years. There are few technologies that have improved so consistently while being so widely regarded as unreliable.

---

Richardson's hall of sixty-four thousand clerks was never built. What replaced it computes more cells than he imagined, with physics he did not have, on observations he could not have obtained.

It still cannot see past a fortnight, and it never will, and that limit was discovered not by failure but by a man retyping three decimal places instead of six and going out for a cup of coffee.

---

## Key Vocabulary

**mystical** *(adj.)* — relying on the inexplicable rather than on reason.
**conservation** *(n.)* — the principle that a quantity remains constant in a closed system.
**momentum** *(n.)* — the quantity of motion of a body, mass times velocity.
**inconsistency** *(n.)* — a conflict between two pieces of data.
**amplify** *(v.)* — to increase in magnitude.
**fictitious** *(adj.)* — not real; produced by the method rather than by nature.
**undeterred** *(adj.)* — not discouraged by a setback.
**dais** *(n.)* — a raised platform for a speaker or conductor.
**absurdity** *(n.)* — something ridiculous or manifestly unreasonable.
**break-even point** *(n. phr.)* — where cost and benefit exactly balance.
**displace** *(v.)* — to take the place of and push out.
**diverge** *(v.)* — to move progressively further apart.
**banal** *(adj.)* — dull and unremarkable.
**discrepancy** *(n.)* — a small difference between two values that should agree.
**deterministic** *(adj.)* — producing a fixed output from a given input, without randomness.
**exponentially** *(adv.)* — at a rate that multiplies rather than adds.
**ceiling** *(n.)* — an upper limit that cannot be exceeded.
**propagate** *(v.)* — to spread from one part of a system to another.
**perturbed** *(adj.)* — slightly altered from an original state.
**evasion** *(n.)* — an avoidance of giving a direct answer.
**infer** *(v.)* — to deduce from indirect evidence.
**cumulative** *(adj.)* — accumulating through successive additions.

## Phrases & Collocations

**keep pace with** — to proceed as fast as something else.
**in every respect that matters** — in all the important ways.
**bear no resemblance** — to be completely unlike.
**one part in ten thousand** — a precise way of expressing a tiny proportion.
**escape into general language** — of a technical phrase, to enter common speech with altered meaning.
**place a ceiling on** — to impose an absolute upper limit upon.
