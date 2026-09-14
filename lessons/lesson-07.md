# Lesson 07 · Everything, All at Once

**Topic:** The transformer architecture and attention mechanisms  
**Style & Register:** Mechanism explainer — precise, step-by-step, diagrammatic  
**Level:** C1–C2

---

## Reading Passage

To understand why one architecture came to dominate machine learning within five years of its publication, it helps to understand precisely what it replaced, and why the thing it replaced was so stubbornly inadequate.

**The problem with reading in order**

Language arrives as a sequence. It was therefore natural, for roughly three decades, to process it with models that consumed one element at a time while maintaining a running summary of everything seen so far. Read a word, update an internal state, read the next word, update again. These recurrent networks were elegant, biologically suggestive, and afflicted by two defects that proved fatal.

The first was informational. Everything the model knew about a sentence had to be squeezed into a single fixed-size vector, updated at every step. For a short phrase this is adequate. For a paragraph it is not: the representation of a word encountered forty tokens ago has been overwritten dozens of times, and the gradients that would allow the model to learn long-range dependencies decay towards nothing as they are propagated backwards through the chain. The model could, in principle, connect a pronoun to a noun three sentences earlier. In practice it rarely did.

The second defect was computational, and it is the one that actually decided the outcome. If the state at step five depends on the state at step four, you cannot compute them simultaneously. The architecture is sequential by construction, which means it cannot exploit hardware whose entire advantage is doing thousands of things at the same time. Graphics processors were becoming cheap and enormously parallel. Recurrent models could not use them properly.

**Attention, stated plainly**

The mechanism that resolved both problems is called self-attention, and beneath the terminology it performs a very simple operation: it allows every position in a sequence to look directly at every other position, and to decide for itself which ones are worth attending to.

Consider the sentence *The bandage would not fit in the case because it was too large.* What does *it* refer to? A human resolves this instantly by reasoning about physical containment. A model must resolve it by weighting: when constructing its internal representation of *it*, it should draw heavily on *bandage* and much less on *case*. Change one word — *because it was too small* — and the correct weighting reverses. No fixed rule of grammar or word order will tell you this. The dependency is semantic, and it must be computed from context.

Self-attention computes it as follows. Each token in the sequence is projected into three separate vectors, conventionally named the query, the key and the value. The query expresses what this position is looking for. The key expresses what this position offers. The value carries the content that will be passed along if the position is selected.

For every pair of positions, the model takes the dot product of one token's query with another token's key. A dot product is a measure of alignment: large when two vectors point in similar directions, small when they do not. This yields a raw compatibility score for every pair. The scores are divided by the square root of the vector dimension — a scaling step that prevents the values from growing so large that the next operation saturates — and then passed through a softmax function, which converts the row of scores into a set of positive weights summing to one. The new representation of each token is simply the weighted average of all the value vectors, using those weights.

That is the entire mechanism. Every position queries every other, compatibility determines influence, and information flows accordingly.

Two consequences follow immediately. The path length between any two tokens is now one step rather than many, so nothing decays with distance. And because every pair can be scored independently, the whole operation reduces to a pair of large matrix multiplications — precisely the workload that parallel hardware executes most efficiently.

**Heads, position and depth**

Three refinements turn the mechanism into a usable architecture.

*Multiple heads.* A single attention operation produces one pattern of relationships, but language contains several simultaneously: syntactic agreement, coreference, topical association. The model therefore runs the operation many times in parallel with independently learned projections, and concatenates the results. Different heads demonstrably specialise, and some are interpretable — one may track subject–verb agreement, another may attend consistently to the previous token.

*Positional information.* Attention as described is permutation-invariant: shuffle the input and the output shuffles identically, since nothing in the computation encodes order. For language this is obviously unacceptable. Position must therefore be injected explicitly, either by adding a positional signal to each token's representation or, in most contemporary systems, by rotating the query and key vectors by an angle proportional to their position, so that the dot product between two tokens depends on their separation.

*Depth.* A single layer mixes information once. Stacking many layers, each with its own attention operation followed by a small position-wise neural network, allows representations to be refined progressively — early layers capturing local and syntactic structure, later layers capturing something closer to meaning. Residual connections, which add each layer's input to its output, keep gradients flowing cleanly through depth that would otherwise be untrainable.

**The cost**

The architecture's defining strength carries a corresponding penalty. Because every position attends to every other, the number of scores computed grows with the square of the sequence length. Double the context and the attention cost quadruples. This quadratic scaling is the reason context windows were initially short, the reason extending them is expensive rather than trivial, and the target of a substantial ongoing research effort in approximation, sparsity and alternative formulations.

**Why it generalised**

The final and least anticipated point is that none of this is specific to language. The mechanism assumes only that the input can be expressed as a set of elements that may be relevant to one another. Divide an image into patches and the same architecture performs image recognition. Feed it amino acid sequences and it predicts protein structure. Feed it audio, or moves in a board game, or sensor readings from a robot, and it works there too.

A technique designed to resolve pronouns turned out to describe something more general: how to let a system decide, for itself and from data, what in its input is worth paying attention to. That, rather than any particular application, is why it won.

---

## Key Vocabulary

**stubbornly** *(adv.)* — persistently and resistant to change.
**inadequate** *(adj.)* — insufficient for the purpose required.
**recurrent** *(adj.)* — occurring repeatedly; here, feeding output back as input.
**afflicted** *(adj.)* — troubled or burdened by something harmful.
**fatal** *(adj.)* — decisive in causing failure.
**vector** *(n.)* — an ordered list of numbers representing a point or direction.
**overwrite** *(v.)* — to replace existing information with new information.
**decay** *(v.)* — to diminish progressively towards zero.
**exploit** *(v.)* — to make full and effective use of a resource.
**resolve** *(v.)* — to determine the correct interpretation of something ambiguous.
**containment** *(n.)* — the state of holding something inside.
**semantic** *(adj.)* — relating to meaning rather than form.
**project** *(v.)* — here, to transform data into a different representational space.
**alignment** *(n.)* — the degree to which two things point in the same direction.
**saturate** *(v.)* — to reach a limit beyond which a function stops responding.
**refinement** *(n.)* — a small improvement that increases precision.
**concatenate** *(v.)* — to join sequences end to end.
**interpretable** *(adj.)* — capable of being understood or explained by a human.
**permutation-invariant** *(adj.)* — producing the same result regardless of input order.
**inject** *(v.)* — to introduce something into a system deliberately.
**quadratic** *(adj.)* — growing in proportion to the square of a quantity.
**sparsity** *(n.)* — the property of having mostly zero or absent values.

## Phrases & Collocations

**by construction** — as an unavoidable consequence of how something is built.
**beneath the terminology** — setting jargon aside; looking at the underlying idea.
**it follows immediately that…** — a formal marker of a direct logical consequence.
**a corresponding penalty** — a cost that arises directly from an advantage.
**the least anticipated point** — the most surprising of several observations.
**turned out to describe** — proved on reflection to be an account of something broader.
