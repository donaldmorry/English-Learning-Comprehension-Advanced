# Lesson 47 · Secrets with an Expiry Date

**Topic:** Cryptography, from mechanical ciphers to post-quantum standards  
**Style & Register:** Narrative history — suspense structure, short paragraphs, delayed revelation  
**Level:** C1–C2

---

## Reading Passage

Every secret ever kept has had a shelf life. The only question worth asking about a cipher is not whether it will be broken, but when — and whether that will be soon enough to matter.

For most of recorded history, the answer was: sooner than the user hoped.

---

**I. The machine that was too good**

The German Enigma machine was, by the standards of the 1930s, an outstanding piece of engineering. An operator pressed a key; current ran through a plugboard, then through three rotating wheels, bounced off a reflector, and returned through the wheels by a different path to illuminate a lamp. The rotors advanced after every keystroke, so that pressing the same letter twice produced two different outputs. The number of possible configurations exceeded a hundred and fifty million million million.

Its operators believed it unbreakable, and they had the arithmetic to support the belief. What the arithmetic did not capture was that a cipher is not merely a machine. It is a machine plus the procedures of the people using it, and procedures leak.

The first breaks came from Polish mathematicians in the early 1930s, working from intercepted traffic and an insight about structure rather than brute force: the reflector guaranteed that no letter could ever be encrypted as itself. This sounds like a triviality. It is catastrophic, because it lets an analyst slide a guessed fragment of plaintext along a message and eliminate every position where a letter aligns with itself. Combine that with operators who began messages with predictable formulae — weather reports, ranks, the same three-letter key typed twice out of laziness — and the hundred and fifty million million million collapses into something a machine can search.

The lesson has been relearned in every generation since. Systems are almost never broken through their mathematics. They are broken through their edges: implementation, habit, reuse, and the human preference for doing today what one did yesterday.

---

**II. The impossible requirement**

After the war, the theory caught up with the practice. It was established rigorously that perfect secrecy is achievable — a message encrypted with a truly random key as long as itself, used exactly once, cannot be broken by any amount of computation, because every possible plaintext of that length remains equally consistent with the ciphertext. There is no information to extract. The proof is airtight.

It is also nearly useless, and the reason is the difficulty that dominated the entire field for the next thirty years.

To use such a scheme, both parties need the key. To share the key, they need a secure channel. If they had a secure channel, they would not need the cipher. Every practical system therefore reduced to the same logistical nightmare: distributing keys in advance, by courier, in locked cases, to every party who might ever need to communicate. Navies and diplomatic services did exactly this, at vast expense. For commerce between strangers, it was hopeless.

The problem was widely regarded as fundamental. Encryption required a shared secret; sharing a secret required encryption. There was no obvious way out of the circle, and serious people had stopped looking.

---

**III. The way out**

The resolution, published in 1976, is one of the few ideas in applied mathematics that can be conveyed accurately to a non-specialist in a paragraph, and it is worth the paragraph.

Suppose two people each begin with a pot of identical yellow paint, in full public view. Each privately selects a secret colour and mixes some into their pot. They then exchange pots openly. Anyone watching sees two mixtures. Each party now adds their own secret colour to the pot they received. Both end up with a pot containing yellow plus both secrets — the same colour, arrived at independently. The observer, holding both intermediate mixtures, cannot produce it, because separating a colour back into its components is far harder than mixing it.

Replace paint with modular arithmetic and the analogy becomes a protocol. Certain operations are cheap in one direction and prohibitively expensive to reverse: multiplying two large primes is trivial, factoring their product is not. Two strangers who have never met, communicating over a channel their adversary is reading, can establish a shared secret the adversary cannot compute.

Nearly every secure transaction you have ever conducted rests on this. It is the reason commerce over an open network is possible at all.

---

**IV. The announcement**

And then, in 1994, a proof arrived that undid the foundation.

The security of these schemes rests not on impossibility but on difficulty — on the claim that factoring and discrete logarithms are computationally infeasible at scale. The proof demonstrated that on a quantum computer, a machine operating on principles no one had built at useful size, both problems become efficiently solvable. Not faster. Structurally different: the algorithm converts the search into a question about periodicity, which quantum interference answers directly.

The mathematics is not in dispute. What is in dispute is the engineering — whether a machine of sufficient scale and stability can be built, and when. Estimates from credible groups range across decades.

Here is why that uncertainty does not license patience.

An adversary does not need a quantum computer today in order to benefit from one tomorrow. Encrypted traffic can be recorded now and stored indefinitely, awaiting a machine capable of opening it. For a message whose value expires in a week this is irrelevant. For medical records, industrial designs, diplomatic archives and identity documents with a thirty-year life, the threat is not future. It is present, and it is silent.

---

**V. The replacement, and the warning inside it**

A multi-year international competition was accordingly held to select replacement algorithms — systems based on mathematical problems with no known efficient quantum solution, principally the difficulty of finding short vectors in high-dimensional lattices. The first standards were finalised in 2024. Migration of global infrastructure is now under way and will take most of a decade, because cryptography is embedded in hardware, in devices that cannot be updated, in protocols agreed between parties who must all move together.

One episode from that competition deserves to be remembered.

A candidate scheme built on a different and elegant branch of mathematics reached the final rounds. It had been studied for years by capable people. Then, in 2022, two researchers published an attack that recovered its key using a decades-old theorem from a neighbouring field. The demonstration ran on a single ordinary computer. It took approximately an hour.

No quantum machine was involved. The scheme was not defeated by the future. It was defeated by a piece of nineteenth-century mathematics that nobody had thought to point at it.

Every secret has a shelf life, and you are never told the date.

---

## Key Vocabulary

**shelf life** *(n. phr.)* — the period during which something remains usable or valid.
**cipher** *(n.)* — a method of transforming a message to conceal its meaning.
**illuminate** *(v.)* — to light up.
**intercepted** *(adj.)* — captured in transit before reaching its destination.
**brute force** *(n. phr.)* — solving by exhaustive trial rather than insight.
**triviality** *(n.)* — something of no importance. *Here: deceptively so.*
**catastrophic** *(adj.)* — causing complete failure or ruin.
**collapse** *(v.)* — here, to reduce suddenly to a much smaller size.
**rigorously** *(adv.)* — with strict logical precision.
**airtight** *(adj.)* — admitting no flaw or exception; used of arguments and proofs.
**logistical** *(adj.)* — concerning the practical organisation of resources.
**courier** *(n.)* — a person who carries documents or goods by hand.
**convey** *(v.)* — to communicate an idea successfully.
**protocol** *(n.)* — an agreed set of rules governing an exchange.
**prohibitively** *(adv.)* — to an extent that makes something impractical.
**adversary** *(n.)* — an opponent; in security, the assumed attacker.
**infeasible** *(adj.)* — not practically achievable.
**periodicity** *(n.)* — the property of repeating at regular intervals.
**license** *(v.)* — to justify or permit. *"Does not license patience"* = gives no excuse for delay.
**indefinitely** *(adv.)* — for an unlimited period.
**lattice** *(n.)* — a regular grid of points; in mathematics, a structure in many dimensions.
**recover** *(v.)* — here, to extract a secret value by cryptanalysis.

## Phrases & Collocations

**by the standards of** — judged according to the norms of a particular time or place.
**catch up with** — to reach the same level as something ahead.
**there was no obvious way out of the circle** — the problem appeared logically self-defeating.
**rest on** — to depend for support upon.
**under way** — in progress, already begun.
**nobody had thought to point at it** — no one had considered applying it. *Understated.*
