# Lesson 19 · Who Owns the Commons?

**Topic:** Open-source software, maintenance and governance  
**Style & Register:** Opinion essay — argumentative, concessive, professionally polemical  
**Level:** C1–C2

---

## Reading Passage

In December 2021, a substantial proportion of the world's corporate computing infrastructure was found to contain a vulnerability so severe, and so trivially exploitable, that security teams spent the holiday period patching continuously. The affected component was a logging library — a modest piece of software whose job is to record what a program has done, useful and entirely unglamorous. It was embedded, directly or indirectly, in an astonishing quantity of enterprise software, in many cases without the companies concerned being aware that they depended on it at all.

It was maintained by volunteers. Not a consortium, not a vendor with a support contract: a handful of people who worked on it in the evenings, unpaid, and who now found themselves, over Christmas, fielding demands from Fortune 500 corporations that had never contributed a line of code or a currency unit of funding, and several of whom appear to have regarded the situation as a service failure.

I want to argue that this was not a security incident with an economic footnote. It was an economic failure with a security symptom, and until we treat it that way it will recur, because the incentive structure that produced it remains entirely intact.

**The structure of the problem**

Begin with the scale. Estimates vary in method but converge on a striking figure: somewhere between seventy and ninety per cent of the code in a typical commercial application was not written by the company shipping it. It arrives through dependencies — components pulled in from public repositories, each of which pulls in others, producing a dependency tree that routinely runs to thousands of packages, the great majority of which no engineer at the company has ever examined.

Now consider the economics of that arrangement. The code is free to acquire, and free to use commercially. The producer receives no payment and, in the standard licences, disclaims all warranty. The consumer receives enormous value and incurs no obligation. This is not a market; it is a gift economy operating at industrial scale, and it has produced the fastest accumulation of shared technical capital in history. I do not want to be misread on this point: the model works. Practically everything that has been built in the last twenty years rests on it.

But it has an obvious failure mode, and it is the oldest one in economics. The benefits of using a widely shared resource are captured privately; the costs of maintaining it are borne by whoever happens to feel responsible. Where contribution is voluntary and consumption is not rationed, under-provision is the predictable equilibrium. Everyone would prefer that critical infrastructure be well maintained. Nobody's individual incentive is to maintain it.

The consequence is a pattern familiar to anyone who has looked: components on which billions of dollars of commerce depend are sustained by one or two people, often the original author, who continue out of a sense of obligation long after the pleasure has gone. The volume of requests scales with adoption. The number of maintainers does not. Reported rates of burnout and abandonment among maintainers of widely used projects are not a wellbeing problem in the ordinary corporate sense. They are a supply-chain risk.

**Three responses, and their limits**

The industry has offered three answers. Each is partially right, and each is regularly oversold.

*Corporate employment.* Large technology firms now pay engineers to work on projects they depend upon, and this has professionalised the maintenance of major infrastructure — kernels, compilers, container systems. The limitation is selection: the projects that attract sponsorship are the visible ones. Sponsorship follows profile rather than criticality, and the components that cause crises are characteristically obscure. A firm will fund the database it markets a product around. It will not fund a date-parsing utility, right up until the morning the date-parsing utility fails.

*Licence change.* Several companies built on open-source projects have relicensed under terms restricting commercial redistribution, typically in response to cloud providers monetising their work without contributing to it. The grievance is legitimate. The remedy has repeatedly failed to achieve its purpose: the affected communities have forked the last freely licensed version, placed it under neutral foundation governance, and continued, so that the company has succeeded principally in donating its user base to a competitor it now cannot influence. The episode has recurred often enough to constitute evidence rather than anecdote.

*Public funding.* Several governments have begun funding maintenance directly, on the explicit reasoning that this software is infrastructure in the same sense as a bridge. The approach is promising and the sums so far are trivial relative to the dependency. Meanwhile regulation is arriving independently, with new obligations for software suppliers to document their components and remediate defects — a development that will do more to change corporate behaviour than a decade of appeals to conscience, since it converts a diffuse moral duty into a specific legal liability.

**What I think follows**

The objection I expect is that maintainers chose this, that nobody was conscripted, and that a gift carries no obligation to keep giving. As a matter of principle this is unanswerable. As a matter of practice it is beside the point. We are not discussing whether maintainers are wronged. We are discussing whether a civilisation should run its payment systems, its hospitals and its power grids on components whose continuity depends on the goodwill of individuals under no obligation to provide it. Reasoning about fairness does not resolve that; reasoning about risk does.

Three measures seem to me defensible and overdue.

First, criticality must be measured rather than assumed. We now have the tooling to map dependency graphs at ecosystem scale and identify components that are simultaneously deeply embedded and thinly maintained. That list should be public, and it should be uncomfortable reading.

Second, funding should follow that list rather than following visibility. Pooled funds administered by neutral foundations already exist; what they lack is money proportionate to the exposure being insured.

Third, organisations above a certain size should be expected to report their dependencies as a matter of routine disclosure. Not because transparency is inherently virtuous, but because an organisation that cannot enumerate what it depends on cannot manage the risk, and will therefore be surprised again.

None of this is radical. It is ordinary infrastructure stewardship, applied belatedly to the one category of infrastructure we acquired by accident, for nothing, and have never once been sent a bill for.

---

## Key Vocabulary

**vulnerability** *(n.)* — a weakness that can be exploited to cause harm.
**exploitable** *(adj.)* — able to be taken advantage of, especially maliciously.
**patch** *(v.)* — to apply a corrective update to software.
**consortium** *(n.)* — an association of organisations acting jointly.
**field** *(v.)* — to receive and deal with questions or demands.
**footnote** *(n.)* — a minor supplementary remark; here, dismissively.
**intact** *(adj.)* — undamaged and unchanged.
**converge** *(v.)* — to come together towards a common value or conclusion.
**disclaim** *(v.)* — to formally deny responsibility for something.
**incur** *(v.)* — to become subject to a cost or obligation.
**ration** *(v.)* — to limit the amount each party may consume.
**under-provision** *(n.)* — the supply of less of something than is collectively needed.
**equilibrium** *(n.)* — a stable state that a system settles into.
**burnout** *(n.)* — exhaustion caused by prolonged, unsustainable effort.
**oversold** *(adj.)* — presented as more effective than it is.
**criticality** *(n.)* — the degree to which something is essential to a system.
**obscure** *(adj.)* — little known; not prominent.
**relicense** *(v.)* — to reissue under different legal terms.
**grievance** *(n.)* — a real or perceived cause for complaint.
**fork** *(v.)* — to copy a project and develop it independently thereafter.
**remediate** *(v.)* — to correct a defect or fault.
**diffuse** *(adj.)* — spread out; not concentrated or clearly assigned.

## Phrases & Collocations

**a service failure** — a breakdown in something contractually owed. *Used ironically here.*
**I do not want to be misread on this point** — a concessive formula pre-empting misinterpretation.
**the predictable equilibrium** — the outcome a system will naturally settle into.
**right up until** — continuing only until a sudden reversal.
**beside the point** — irrelevant to the matter actually under discussion.
**as a matter of routine disclosure** — reported regularly as standard practice.
