# Lesson 31 · The Cost of Agreeing

**Topic:** Blockchain consensus mechanisms — proof of work and proof of stake  
**Style & Register:** Comparative technical analysis — problem-first, rigorous  
**Level:** C1–C2

---

## Reading Passage

Strip away the terminology and every distributed ledger is attempting to solve one problem, stated as follows: a group of participants who do not know each other, cannot verify each other's identities, and have no shared authority to appeal to, must nevertheless agree on a single ordered history of events — while some unknown fraction of them are actively lying.

This is harder than it sounds, and the reason is worth establishing before any solution makes sense.

**Why ordering is the whole game**

A digital token is information, and information can be copied perfectly. If I hold one unit and send it to two different people simultaneously, each recipient sees a valid, correctly signed transfer. Cryptographic signatures prove that I authorised both. They cannot prove which came first.

Traditional finance resolves this with an authority. A bank maintains the definitive record; if two instructions conflict, the bank's ordering is the ordering, and the question of truth reduces to the question of whose ledger is official.

Remove the authority and the problem becomes genuinely difficult, because "first" has no meaning in a network where messages travel at different speeds and participants may deliberately misreport their own timestamps. What is required is not a clock but a procedure by which mutually suspicious strangers converge on one history — and, crucially, a reason why attacking that procedure costs more than it yields. Consensus, in this setting, is not primarily a computer science problem. It is an economics problem wearing a computer science costume.

**Mechanism one: make writing expensive**

The first working answer inverted the usual approach. Rather than restricting who may write to the ledger, it allowed anyone to write, and made writing costly.

Participants compete to find a number which, when combined with the block of transactions they propose and passed through a cryptographic hash function, yields an output below a target threshold. Hash functions are one-way and their outputs are effectively random, so there is no method superior to guessing. The only way to guess faster is to own more hardware and consume more electricity. The target adjusts automatically so that, whatever the total computing power on the network, a solution is found on average at a fixed interval.

Participants extend the chain containing the most accumulated work. This is what makes rewriting history expensive: an attacker wishing to reverse a transaction must reproduce all the work done since it occurred and outpace the honest network while doing so. With less than half the total power, the attacker falls further behind with every block. Security is therefore probabilistic and strengthens with depth — a transaction six blocks deep is not certain, merely expensive beyond reason to reverse.

The design's elegance is that it requires no knowledge of identity whatsoever. It does not matter who you are or how many network addresses you create, because influence is purchased in a currency that cannot be faked: energy already spent.

That is also its cost. The expenditure is the security, which means it cannot be optimised away. A network of this type consumes electricity on the scale of a mid-sized country, permanently and by design.

**Mechanism two: make writing conditional on a deposit**

The alternative substitutes capital for energy. Participants lock a quantity of the network's own token as a bond and are selected, with probability proportional to their stake, to propose and attest to blocks. Correct behaviour earns a modest yield. Misbehaviour — signing two conflicting blocks, or contradicting one's own earlier attestation — is detectable by anyone, and results in the automatic destruction of a portion of the bond.

The shift is from external cost to internal collateral. Under the first mechanism, an attacker buys hardware and electricity in the outside world, retains the hardware afterwards, and can reuse it. Under the second, an attacker must acquire a large fraction of the token supply, which bids up its price during accumulation, and then watch that holding be destroyed by the very attack it funds. Attacking becomes self-punishing rather than merely unprofitable.

A conceptual objection was raised early and deserves mention because it is frequently repeated as though unanswered. If signing costs nothing, a rational validator should sign every competing version of history, guaranteeing a reward on whichever prevails. This is the *nothing-at-stake* problem, and it is solved precisely by making signing cost something: the penalty for equivocation is applied automatically on evidence submitted by any observer. The apparent flaw was an artefact of the earliest designs, not of the approach.

A second difficulty is more subtle and has not been eliminated. A participant who acquires keys that were valid long ago could, in principle, construct an alternative history from that point. The defence is that new participants must obtain a recent reference point from a trusted source when joining — a requirement known as weak subjectivity, and a genuine, if modest, departure from the ideal of a system that trusts nothing.

**The comparison that actually matters**

Energy consumption is the difference most often cited, and it is real: the transition of one major network in 2022 reduced its consumption by more than ninety-nine per cent overnight. But energy is a consequence of the security model rather than the model itself, and treating it as the whole comparison obscures the structural differences.

*Finality.* The first mechanism offers probabilistic settlement: confidence rises with depth and never reaches certainty. The second can offer deterministic finality — after a defined interval, a block is irreversible unless a large fraction of bonded capital is destroyed. For institutional settlement, the distinction is significant.

*Barriers to participation.* Mining requires access to cheap electricity, specialised hardware and industrial premises, which concentrates it geographically and among those with capital. Staking requires only tokens and an ordinary machine. Both, however, exhibit strong pooling tendencies, because participants prefer smooth income to lumpy income, and both have consequently seen influence accumulate among a modest number of large operators. The centralising pressure is economic rather than technical, and it appears under either mechanism.

*Cost structure.* Proof of work is an operating expense, paid continuously and in an external currency. Proof of stake is a capital commitment, held in the system's own token. The first cannot be attacked without external resources; the second cannot be attacked without exposure to the value of the thing being attacked.

Neither is straightforwardly superior. What both demonstrate is the underlying insight: agreement among strangers is not free, and every such system is a decision about what form the bill should take.

---

## Key Vocabulary

**strip away** *(phr. v.)* — to remove surface layers to reveal what is underneath.
**ledger** *(n.)* — a record of transactions.
**definitive** *(adj.)* — final and authoritative.
**converge** *(v.)* — to arrive at a common point or agreement.
**suspicious** *(adj.)* — distrustful of others' intentions.
**invert** *(v.)* — to reverse the usual order or approach.
**threshold** *(n.)* — a boundary value that must be crossed.
**one-way** *(adj.)* — computable in one direction but not reversible.
**outpace** *(v.)* — to move faster than and get ahead of.
**probabilistic** *(adj.)* — expressed as a likelihood rather than a certainty.
**expenditure** *(n.)* — the spending of resources.
**bond** *(n.)* — a sum deposited as a guarantee of good behaviour.
**stake** *(n.)* — an amount committed and placed at risk.
**attest** *(v.)* — to declare formally that something is true.
**collateral** *(n.)* — an asset pledged and forfeit on default.
**bid up** *(phr. v.)* — to raise a price through competitive purchasing.
**equivocation** *(n.)* — here, signing two contradictory statements.
**artefact** *(n.)* — an incidental by-product of a method, mistaken for a real feature.
**finality** *(n.)* — the point at which a transaction becomes irreversible.
**deterministic** *(adj.)* — producing a definite, guaranteed outcome.
**lumpy** *(adj.)* — irregular and unevenly distributed over time.
**exposure** *(n.)* — vulnerability to loss from a particular risk.

## Phrases & Collocations

**appeal to** — to turn to for authority or resolution.
**the whole game** — the decisive element on which everything depends. *Informal emphasis.*
**beyond reason** — to an extent no rational actor would accept.
**optimised away** — eliminated through efficiency improvements. *"Cannot be optimised away."*
**as though unanswered** — as if no response had ever been given. *Used to dismiss a stale objection.*
**what form the bill should take** — in which currency a necessary cost will be paid. *Figurative.*
