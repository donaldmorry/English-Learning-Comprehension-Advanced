# Lesson 03 · Easy Is Hard

**Topic:** Humanoid robots and Moravec's paradox  
**Style & Register:** Analytical essay — contrarian, paradox-driven, rhetorical questions  
**Level:** C1–C2

---

## Reading Passage

Here is a prediction made in 1965 by one of the founders of artificial intelligence, and it is worth quoting because it was not foolish. Machines, he wrote, would within twenty years be capable of doing any work a person can do.

He was wrong, but notice the shape of the error. It was not that he overestimated machines generally. Within his twenty years, computers could do algebra, prove theorems, play excellent chess, diagnose certain diseases and pass examinations that select for elite human capability. What they could not do was walk across an unfamiliar room, pick up a sock, and put it in a drawer.

That inversion — the fact that the work we consider difficult turned out to be easy, and the work we do not consider work at all turned out to be nearly intractable — is the single most reliable finding in the history of the field. Hans Moravec named it in 1988, and it has survived every subsequent wave of progress. It is worth taking seriously, because the industry's current enthusiasm for building machines shaped like people is, in effect, a bet that the paradox is about to resolve.

**Why the ranking is inverted**

The explanation Moravec offered is evolutionary, and it is elegant enough to be worth stating carefully.

Sensorimotor competence — balance, grasping, locomotion, the perception of a cluttered scene — has been under selection for something like five hundred million years. Every ancestor you have ever had, back through mammals and reptiles and fish, was good at it, and the ones who were not are not ancestors. It is the most thoroughly optimised software in the biosphere, refined over a period compared to which all of recorded history is an afternoon.

Abstract reasoning, by contrast, is recent. Deliberate symbolic thought is perhaps a hundred thousand years old and arithmetic considerably younger. It is a thin, slow, effortful layer running on hardware built for something else entirely.

Now add the crucial second point: we have no introspective access to the old system. You do not experience the extraordinary computation involved in standing up, because none of it is available to consciousness. You experience only the effort of the recent, shallow, badly optimised system — which is why we mistake difficulty of *experience* for difficulty of *task*. Chess feels hard. It is, computationally, a narrow problem with clean rules. Picking up a sock feels like nothing at all, and requires the real-time integration of vision, proprioception, force control and material prediction in an environment that was not designed and cannot be enumerated.

We built a hierarchy of intellectual respect that exactly inverts the hierarchy of computational difficulty, and then spent sixty years being surprised by it.

**What the hand actually does**

Consider the specification of the thing being replaced.

The human hand has twenty-seven bones and roughly as many independently controllable degrees of freedom, driven by muscles mostly located in the forearm and transmitted through tendons — an arrangement that keeps mass away from the moving part, which every engineer eventually rediscovers. Its skin contains on the order of seventeen thousand mechanoreceptors of four distinct types, some responding to steady pressure and others exclusively to change.

More importantly, the control loop is fast and largely unconscious. When an object begins to slip, the grip tightens within about seventy milliseconds, which is faster than you can notice the slip. That reflex does not consult you. It has already happened by the time you would have had an opinion.

A robotic hand must reproduce this with actuators whose power-to-weight ratio is broadly comparable to muscle, but whose control bandwidth, sensing density and tolerance of impact are not. This is not a problem that more computation solves. It is partly a materials problem and partly an architecture problem, and progress on it has been real but incremental for thirty years.

**The case for the human shape**

Why, then, build machines shaped like us at all? The standard argument is environmental. The built world — doors, stairs, handles, vehicles, shelf heights, tool grips, the dimensions of a shipping tote — is an enormous accumulated investment in one particular body plan. A machine matching that plan can, in principle, be dropped into existing environments without modifying them, which is exactly what warehouse automation cannot do and what makes it so expensive.

The second argument is data. If manipulation is to be learned from demonstration, a body with human proportions can be taught directly by a person wearing motion capture or operating it remotely, and the enormous corpus of recorded human activity becomes at least partially usable as training material. A machine of different morphology inherits none of it.

Both arguments are serious. Neither is obviously decisive.

**The case against**

The objection is simply that form should follow task, and that the human body is a compromise optimised for a set of constraints — bipedalism freeing the hands, a birth canal, thermoregulation on a savannah — that have nothing to do with moving totes.

Where a task is known and repetitive, a specialised machine beats a general one on every metric that matters: cost, reliability, throughput, energy. A wheeled base is more stable, more efficient and dramatically simpler than legs. A conveyor outperforms any walking machine at moving objects along a fixed path, and always will. The humanoid's advantage appears only when the tasks are numerous, varied, and individually too small to justify dedicated equipment — which is a real and large category, but a narrower one than the current level of investment implies.

There is also a discipline that video does not enforce. A demonstration establishes that a system can perform a task under chosen conditions. Deployment requires it thousands of times, in poor lighting, with unfamiliar objects, safely alongside people, at a competitive cost per hour, with a mean time between failures long enough that maintenance does not consume the saving. The gap between those two claims has historically been measured in years.

**The honest position**

The paradox has not been repealed. It has been narrowed, in the specific sense that learned control has made some previously intractable manipulation tasks tractable, and that the rate of narrowing over the past five years has been faster than the preceding thirty.

Whether that rate continues is the entire investment thesis of a very large industry, and nobody knows the answer, including the people whose statements suggest they do.

What remains certain is the ordering. The last thing these machines will learn to do is the first thing a two-year-old does without instruction — and the fact that this still sounds like a joke is precisely the mistake the paradox is about.

---

## Key Vocabulary

**overestimate** *(v.)* — to judge something as greater than it is.
**inversion** *(n.)* — a reversal of the normal or expected order.
**intractable** *(adj.)* — extremely difficult to solve or manage.
**enthusiasm** *(n.)* — eager and often uncritical interest.
**resolve** *(v.)* — here, to cease to be a contradiction.
**sensorimotor** *(adj.)* — relating to the coordination of sensing and movement.
**selection** *(n.)* — here, the evolutionary process favouring advantageous traits.
**optimised** *(adj.)* — refined to perform as well as possible.
**introspective** *(adj.)* — relating to examination of one's own mental processes.
**enumerate** *(v.)* — to list all members of a set exhaustively.
**hierarchy** *(n.)* — a ranked ordering by importance or status.
**degree of freedom** *(n. phr.)* — an independent direction in which a system can move.
**mechanoreceptor** *(n.)* — a sensory cell responding to mechanical pressure or distortion.
**bandwidth** *(n.)* — the rate at which a system can transmit or respond to information.
**reflex** *(n.)* — an automatic response not requiring conscious decision.
**incremental** *(adj.)* — advancing by small steps rather than leaps.
**morphology** *(n.)* — the form and structure of a body.
**inherit** *(v.)* — to receive from a predecessor without having to re-earn it.
**decisive** *(adj.)* — settling an issue conclusively.
**thermoregulation** *(n.)* — the maintenance of stable body temperature.
**repeal** *(v.)* — to revoke or cancel, as a law. *Here used figuratively.*
**thesis** *(n.)* — here, the central claim on which a position rests.

## Phrases & Collocations

**notice the shape of the error** — an invitation to examine *how* someone was wrong, not merely that they were.
**under selection** — subject to evolutionary pressure over long periods.
**form should follow task** — a design principle: shape must be determined by purpose.
**on every metric that matters** — by all the measures that are relevant.
**mean time between failures** — the average interval between breakdowns. *Engineering term.*
**the honest position** — a formula introducing an author's candid, qualified conclusion.
