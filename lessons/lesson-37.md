# Lesson 37 · The Machine That Wrote the Machine

**Topic:** Compilers and the history of abstraction  
**Style & Register:** Historical essay — long periodic sentences, dry wit, understatement  
**Level:** C1–C2

---

## Reading Passage

There is a persistent temptation, when writing the history of computing, to organise it around machines — around the successive generations of valve, transistor and integrated circuit, each faster and smaller than the last. It is a defensible way to tell the story, and it has the advantage of producing good photographs. It is also, I would suggest, the less interesting half. The hardware has improved by something on the order of a trillion-fold. What has changed more profoundly is the distance between the person issuing an instruction and the machine that carries it out, and that distance is measured not in nanometres but in layers of abstraction, almost every one of which was introduced over the confident objections of serious people.

Consider the situation in about 1950. A computer was programmed in the only language it possessed: binary instructions, entered as numbers, each specifying an operation and the memory addresses it acted upon. A programmer kept track of every location by hand, on paper. Inserting a single instruction into the middle of a working program shifted every subsequent address, which meant recalculating the lot. Errors were not merely common but effectively guaranteed, and the discipline attracted, as one might expect, a particular sort of person — meticulous, tolerant of tedium, and in possession of a very good eraser.

Assembly language was the first concession to human frailty, and it was a modest one: instead of writing the numeric code for an addition, one wrote a short mnemonic, and instead of tracking addresses, one attached names to them and let a small program substitute the numbers. This program — the assembler — did nothing clever. It performed a mechanical translation that a patient clerk could have performed. It was nonetheless resisted, on the grounds that machine time was scarce and expensive while programmer time was neither, an argument which was perfectly correct at the time and has aged spectacularly badly.

The genuinely radical proposition arrived shortly afterwards, and it was this: that a computer might be given instructions in something resembling ordinary notation, and might work out the machine code for itself. Grace Hopper, who developed the first compiler of this general kind in the early 1950s, later recalled that her difficulty was not technical. It was that nobody believed a computer could write programs, and she spent a considerable period being told, by people who had every reason to know better, that the thing she had already done was impossible.

The objection that actually mattered, however, was not philosophical but economic, and it deserves more respect than it usually receives. Hand-written assembly, produced by an expert who understood the specific machine, was fast. Code generated automatically by a translator would surely be worse — clumsier, more wasteful of registers, slower in execution. Since computers cost more per hour than a small team of engineers, a translator that produced code even twenty per cent slower was not a labour-saving device. It was an extravagance.

This is the context in which the FORTRAN project, begun in 1954 and delivered in 1957, set itself an unusually severe requirement: the compiler had to produce code approximately as efficient as a competent human would write by hand, because anything less would be rejected by the very users it was meant to serve. Most of the effort went not into the language, which is comparatively simple, but into optimisation — into an analytical apparatus capable of noticing that a calculation inside a loop does not depend on the loop variable and may therefore be performed once outside it, or that a value already sitting in a register need not be fetched again from memory. The project overran substantially. When it finally shipped, it met the requirement, and the argument was over. Within a few years, programming directly in assembly had become a specialist activity rather than the ordinary condition of the field.

What followed was a sequence of the same manoeuvre, executed repeatedly at higher altitudes, and greeted each time with the same scepticism from people who had mastered the layer below. Structured programming was said to be an unnecessary restriction on capable engineers. Automatic memory management was said to be an unaffordable luxury, and for certain applications remained one for a long while. Dynamic languages were said to be unsuitable for serious work. Each objection was true when raised and false within a decade, which may be the closest thing to a law that the discipline possesses.

The compiler itself became a curious object along the way. A translator must be written in some language, and for a new language the obvious candidate is an existing one — but once a rudimentary version exists, the compiler may be rewritten in the language it compiles and then used to compile itself. This procedure, known as bootstrapping, has the pleasing property of being circular without being paradoxical, and it means that the lineage of a modern compiler can often be traced back, through successive self-compilations, to some long-forgotten program written by hand in the 1970s. Ken Thompson observed in 1984 that this circularity carries an unsettling implication: a modification introduced into a compiler could, in principle, teach that compiler to reinsert the modification into its own successors indefinitely, remaining invisible in every version of the source code anyone might subsequently inspect. The observation was made as a caution about trust, and it remains the most elegant argument in the literature for taking the provenance of tools seriously.

Meanwhile the layers have continued to accumulate, quietly and beyond the notice of almost everyone. A single line of a modern scripting language may be parsed into an intermediate representation, interpreted by a runtime that was itself compiled from a systems language by a compiler using a shared optimisation framework, translated into instructions for a processor architecture that then decodes them internally into still smaller operations executed out of order across several pipelines, and finally realised as voltages across structures a few dozen atoms wide. Between the intention and the electron there are perhaps a dozen translation steps, no individual having full command of more than two or three.

We tend to describe this as complexity, generally in a tone of complaint. It is more accurately described as the largest and least celebrated act of delegation in industrial history: an enormous, cumulative decision to hand the tedious parts to the machine, taken one contested step at a time, by people who were assured on each occasion that this particular step was a step too far.

---

## Key Vocabulary

**persistent** *(adj.)* — continuing to exist despite resistance or correction.
**defensible** *(adj.)* — able to be justified, though not necessarily best.
**abstraction** *(n.)* — a simplified representation that hides underlying detail.
**objection** *(n.)* — a stated reason for disagreement.
**meticulous** *(adj.)* — extremely careful about detail.
**tedium** *(n.)* — the quality of being tediously long and dull.
**concession** *(n.)* — something granted in response to a demand or weakness.
**frailty** *(n.)* — weakness; liability to error.
**mnemonic** *(n.)* — a short code or device that aids memory.
**substitute** *(v.)* — to put one thing in place of another.
**scarce** *(adj.)* — available in insufficient quantity.
**extravagance** *(n.)* — unjustifiable expenditure.
**severe** *(adj.)* — demanding; strict in requirement.
**apparatus** *(n.)* — an organised set of methods or equipment for a purpose.
**overrun** *(v.)* — to exceed an allotted time or budget.
**manoeuvre** *(n.)* — a skilful or calculated move.
**altitude** *(n.)* — height; here, figuratively, a level of abstraction.
**rudimentary** *(adj.)* — basic and undeveloped; a first rough version.
**lineage** *(n.)* — a line of descent from an ancestor.
**unsettling** *(adj.)* — causing quiet unease.
**provenance** *(n.)* — the record of origin and ownership.
**delegation** *(n.)* — the transfer of a task to another party.

## Phrases & Collocations

**on the order of** — approximately, to within a factor of ten.
**has aged spectacularly badly** — has come to look very wrong in retrospect. *Ironic.*
**every reason to know better** — was in a position to understand, and failed to.
**a step too far** — an extension beyond what is prudent or acceptable.
**beyond the notice of** — unobserved by; escaping the attention of.
**in a tone of complaint** — in a manner expressing dissatisfaction.
