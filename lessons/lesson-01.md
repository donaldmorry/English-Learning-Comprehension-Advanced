# Lesson 01 · Money as Software

**Topic:** Central bank digital currency and the architecture of payment systems  
**Style & Register:** Formal policy explainer — neutral, definitional, scrupulously balanced  
**Level:** C1–C2

---

## Reading Passage

**1. Purpose and scope**

This note sets out, in non-technical terms, the design questions raised by the possible issuance of a central bank digital currency, and the trade-offs associated with each. It does not advocate a position. The intention is to make the choices legible, since public discussion frequently treats the proposal as a single undifferentiated thing when it is in fact a family of designs with materially different consequences.

**2. What already exists**

It is necessary to begin with a distinction that is widely misunderstood: most of the money in circulation is not issued by a central bank.

Two forms coexist. The first is central bank money — physical banknotes held by the public, and electronic reserve balances held by commercial banks at the central bank. This is a direct claim on the issuing authority and carries no credit risk in the ordinary sense. The second is commercial bank money — the balance shown in an ordinary current account. This is not a holding of central bank money. It is a liability of a private institution: a promise to pay on demand, backed by that institution's assets, protected up to a statutory limit by deposit insurance.

In most developed economies, commercial bank money constitutes the overwhelming majority of the total. The public generally does not notice the distinction, because the two exchange at par and the promise is almost always honoured. It becomes noticeable only in a crisis.

The relevance is this. Physical cash is presently the only form in which a member of the public may hold central bank money directly, and cash use has declined substantially in many economies over the past fifteen years. A digital currency of this type would restore that direct option in electronic form. It is, in essence, a proposal to issue digital banknotes.

**3. The principal design axes**

*Retail or wholesale.* A wholesale instrument would be available only to financial institutions, largely modernising infrastructure that already exists and raising comparatively few public questions. A retail instrument would be available to households and businesses, and it is this variant that generates nearly all the debate. The two should not be discussed interchangeably.

*Direct or intermediated.* In a direct model, the central bank maintains accounts for every user — an operational undertaking of considerable scale, requiring customer service, identity verification and dispute resolution functions that central banks do not currently possess. In the intermediated, or two-tier, model, the claim remains on the central bank while private firms handle distribution, onboarding and interfaces. Nearly every serious proposal has adopted the intermediated form, on the reasoning that the public sector should define the rails and the private sector should compete on the services running over them.

*Account-based or token-based.* An account-based system identifies the holder and transfers value by adjusting balances. A token-based system transfers an object that carries its own validity, more closely resembling cash, and can in principle function without the payer and payee being identified to each other. The choice determines what offline operation and privacy are technically capable of.

**4. Motivations advanced**

Four arguments are made in favour, and they are of unequal strength.

*Payment resilience.* A publicly operated settlement option provides an alternative should privately operated networks fail, which they occasionally do.

*Cost and competition.* Retail payment fees in several markets are set within concentrated networks. A neutral public option could exert competitive pressure, though this depends on adoption reaching a level sufficient for merchants to treat it as a genuine alternative.

*Inclusion.* Where a meaningful share of the population lacks access to banking services, a low-cost public instrument may extend participation. Where banking access is already near-universal, this argument carries correspondingly less weight.

*Cross-border cost.* Remittance corridors frequently carry charges of five to eight per cent with settlement measured in days. Interoperable wholesale systems address this more directly than retail instruments do.

**5. Risks and constraints**

Three difficulties are common to all designs and are the subject of continuing technical work.

*Disintermediation.* If the public may hold central bank money directly, deposits may migrate out of commercial banks, particularly during periods of stress, when the incentive to move is strongest and the consequence most damaging. Since bank lending is funded substantially by deposits, a large migration would reduce credit availability. Proposed mitigations include holding limits per individual, tiered or zero remuneration, and automatic transfer of balances above a threshold back into a linked commercial account. Each mitigation reduces the risk and simultaneously reduces the instrument's usefulness — a trade-off that has no clean resolution.

*Privacy.* Cash is anonymous by construction. Any electronic ledger records something, and the question is what, retained for how long, and accessible to whom. Several proposals specify tiered arrangements in which small transactions are handled with minimal data collection while larger ones meet standard financial-crime requirements. The technical means to enforce such tiers exist. Whether a given legal framework binds a future administration is a question of law and constitutional design rather than of engineering, and it is the point on which public reaction has most consistently turned.

*Programmability.* A digital instrument can in principle carry conditions restricting how, where or by when it may be spent. Proponents note straightforward applications in conditional disbursement and automated settlement. Others observe that the same capability would permit restrictions on individual spending that physical cash does not allow. Most published central bank proposals have explicitly disclaimed any intention to impose such conditions on general-purpose money, while acknowledging that the capability is inherent in the technology and that the safeguard is therefore necessarily legal rather than technical.

**6. Evidence from implementation**

Several jurisdictions have issued retail instruments and the results are instructive. Adoption has generally been low relative to projection. The recurring finding is that where existing electronic payment options are already cheap, fast and universally accepted, the public has little incentive to adopt an additional instrument, however well designed. Adoption has been more meaningful where existing infrastructure was weak or expensive.

**7. Summary**

The technical questions are largely tractable. The decisive questions are institutional: what limits are placed on holdings, what data is recorded and who may see it, and whether those limits are durable. These are matters of law and public legitimacy rather than of system architecture, and no engineering choice can resolve them on its own.

---

## Key Vocabulary

**issuance** *(n.)* — the act of officially putting something into circulation.
**advocate** *(v.)* — to argue publicly in favour of.
**legible** *(adj.)* — here, clear and comprehensible.
**undifferentiated** *(adj.)* — treated as one thing when it contains distinct types.
**liability** *(n.)* — a financial obligation owed by an institution.
**statutory** *(adj.)* — established by law.
**at par** *(prep. phr.)* — at exactly equal value, one for one.
**honoured** *(adj.)* — of a promise, fulfilled as agreed.
**variant** *(n.)* — a form that differs from others of the same kind.
**intermediated** *(adj.)* — conducted through a third party rather than directly.
**onboarding** *(n.)* — the process of registering and verifying new customers.
**rails** *(n. pl.)* — the underlying infrastructure over which transactions run.
**resilience** *(n.)* — the ability to withstand and recover from failure.
**concentrated** *(adj.)* — dominated by few participants.
**remittance** *(n.)* — money sent home by a person working abroad.
**interoperable** *(adj.)* — able to work together across different systems.
**disintermediation** *(n.)* — the removal of an intermediary from a process.
**migrate** *(v.)* — to move from one place or system to another.
**mitigation** *(n.)* — a measure reducing the severity of a risk.
**remuneration** *(n.)* — payment; here, interest paid on a balance.
**disclaim** *(v.)* — to formally deny an intention or responsibility.
**tractable** *(adj.)* — capable of being solved with available means.

## Phrases & Collocations

**sets out** — presents formally and in order. *Standard in official documents.*
**it is necessary to begin with** — a formal framing move establishing prerequisites.
**of unequal strength** — varying in how well supported they are.
**carries correspondingly less weight** — is proportionally less persuasive.
**has no clean resolution** — cannot be settled without accepting a loss somewhere.
**turn on** — to depend decisively upon. *"The point on which reaction has turned."*
