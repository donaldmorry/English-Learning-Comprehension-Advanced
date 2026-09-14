# Lesson 22 · The Ghost in the Ledger

**Topic:** Stablecoins and the settlement layer of digital asset markets  
**Style & Register:** Investigative financial analysis — forensic, sceptical, question-driven  
**Level:** C1–C2

---

## Reading Passage

Begin with the question that organises everything else: when you hold a token that claims to be worth one dollar, what exactly do you own?

It is not a rhetorical question. There are at least four structurally different answers, they carry entirely different risks, and the tokens are traded interchangeably by people who could not tell you which they hold.

**The four architectures**

*Fiat-backed.* An issuer accepts dollars, holds them in reserve, and issues tokens against them. The token is a liability of that issuer — a claim, redeemable in principle, whose value depends wholly on whether the reserves exist, whether they are liquid, and whether redemption is honoured promptly. This is by far the dominant form by volume, and it is, in every meaningful respect, a money market fund with a blockchain interface and a different regulatory history.

*Crypto-collateralised.* A user locks volatile assets worth substantially more than the tokens issued against them — typically 150 per cent or above — and the excess absorbs price movement. Collateral falling towards the threshold is liquidated automatically. The mechanism is transparent and capital-inefficient by construction. Its vulnerability is correlated collapse: liquidations arriving simultaneously into a falling market, each sale pushing the price lower and triggering the next.

*Algorithmic.* No meaningful collateral at all. The peg is defended by an arbitrage relationship with a second, freely floating token, the supply of each expanding or contracting to restore the price. It works precisely as long as participants believe it works, which is a description of a confidence game rather than a mechanism, and in 2022 a system of this design holding tens of billions in nominal value unwound to approximately zero over four days. The failure mode was neither surprising nor novel: the arbitrage that defends the peg on the way up destroys the floating token on the way down, and once holders understand that, the rational move is to exit first.

*Tokenised deposits and funds.* The most recent category — regulated institutions issuing on-chain claims on conventional instruments, subject to existing supervision. The structure is old; only the settlement rail is new.

**The word doing the heavy lifting**

For the dominant fiat-backed category, everything reduces to a single verifiable question: are the reserves there?

The industry's answer is the *attestation*, and the distinction between an attestation and an audit is the single most important piece of vocabulary in this entire market.

An attestation is a report in which an accounting firm confirms that, at a specified moment, the issuer's stated figures agree with records the issuer provided. It is a snapshot. It does not test internal controls, verify that the assets are unencumbered, cover the period between snapshots, or express an opinion on whether the financial statements as a whole are fairly presented. An audit does all of those things, and carries a correspondingly different liability for the firm signing it.

Most attestations here are conducted at a single month-end date, announced in advance. Whether the assets were present continuously, and whether any were pledged elsewhere in the interval, is not a question an attestation is designed to answer.

**Composition, and why it is not a detail**

Assume the reserves exist. The next question is what they consist of, and the published breakdowns repay close reading.

Short-dated government bills are cash-equivalent and can be sold at scale in a crisis. Overnight repurchase agreements are similar. Bank deposits are not equivalent: they are unsecured claims on individual banks, insured only to modest limits, and they introduce precisely the counterparty risk the structure was supposed to avoid. This is not hypothetical. In March 2023 a major issuer disclosed that several billion dollars of its reserves sat at a bank that had entered resolution over a weekend. The token traded at eighty-seven cents before recovering when the deposits were made whole. The reserves had been real, adequate and inaccessible — a combination that a headline figure cannot express.

Longer-dated holdings raise a different issue. A portfolio can be fully backed at face value and still fail to meet redemptions at par if it must be sold quickly into a falling market. Every run in financial history was a liquidity event before it was a solvency event.

**Who can actually redeem**

Here the retail understanding diverges sharply from the mechanics.

Direct redemption with the issuer is typically available only to verified institutional counterparties, frequently subject to minimums of a hundred thousand dollars or more, and governed by terms that in several cases explicitly reserve the right to suspend redemption or to settle in assets other than cash.

The ordinary holder cannot redeem. They can only sell on the open market, at whatever price is available. The peg they rely on is maintained not by their own redemption right but by arbitrageurs who profit from buying discounted tokens and redeeming them at par — which functions smoothly in normal conditions and depends entirely on those arbitrageurs retaining both the ability and the willingness to act during the precise moments when a peg comes under pressure.

**Who keeps the interest**

A question that receives less attention than it merits.

An issuer holding tens of billions in reserves earns the prevailing short-term rate on those reserves. Holders of the tokens receive nothing. In a period of meaningful interest rates, the resulting revenue is very large relative to the operating cost of the business, and it accrues entirely to the issuer.

This is not concealed and it is not unlawful. It is worth stating plainly nonetheless, because it explains both the sector's profitability and its growth incentives: the business model is to attract non-interest-bearing liabilities and invest them, which is the oldest business model in finance, conducted here without the capital requirements, deposit insurance or supervisory apparatus that were built around it over a century.

**The systemic question**

Stablecoins are now the principal settlement instrument of digital asset markets — the denominator of most trading pairs and the medium in which most positions are held between trades. The exposure is therefore not confined to holders. A failure of a dominant issuer would propagate into every venue and lending protocol that treats its token as cash equivalent, simultaneously, and those systems liquidate automatically.

The largest issuers now rank among the significant holders of short-dated government paper. Sector growth is therefore a source of demand for that paper, and a disorderly contraction would be a forced seller of it, at speed — which is why supervisory interest has intensified.

None of this asserts that any particular issuer is insolvent. The narrower and more durable point is that a claim marketed as equivalent to cash, whose backing is confirmed by point-in-time attestation, whose redemption is available only to institutions, and whose float earns interest for someone other than the holder, is not a dollar. It is a private liability with a dollar-shaped label, and the distinction tends to become apparent only in the week it matters.

---

## Key Vocabulary

**interchangeably** *(adv.)* — as if identical and mutually substitutable.
**liability** *(n.)* — an obligation owed by an issuer to a holder.
**redeemable** *(adj.)* — able to be exchanged back for the underlying asset.
**liquid** *(adj.)* — readily convertible into cash without loss of value.
**collateral** *(n.)* — assets pledged to secure an obligation.
**liquidate** *(v.)* — to sell assets, often forcibly, to close a position.
**correlated** *(adj.)* — moving together rather than independently.
**peg** *(n.)* — a fixed exchange value that a currency is managed to maintain.
**arbitrage** *(n.)* — profiting from a price difference between markets.
**unwind** *(v.)* — to come apart progressively; to reverse a position.
**nominal** *(adj.)* — stated on paper, as opposed to realisable in practice.
**attestation** *(n.)* — a limited confirmation that stated figures match provided records.
**unencumbered** *(adj.)* — free of any claim, pledge or lien by another party.
**counterparty** *(n.)* — the other party to a financial contract.
**resolution** *(n.)* — the formal process of winding up a failing bank.
**made whole** *(phr.)* — fully compensated for a loss.
**at par** *(prep. phr.)* — at exactly the stated face value.
**solvency** *(n.)* — the state of having assets exceeding liabilities.
**diverge** *(v.)* — to move apart; to differ increasingly.
**accrue** *(v.)* — to accumulate to a party over time.
**float** *(n.)* — the pool of funds held by an issuer pending redemption.
**propagate** *(v.)* — to spread through a connected system.

## Phrases & Collocations

**doing the heavy lifting** — carrying the greatest weight of meaning or work.
**repay close reading** — to reward careful examination. *Literary-analytic idiom.*
**point-in-time** — capturing a single instant rather than a period.
**come under pressure** — to be subjected to stress that threatens stability.
**cash equivalent** — an asset treated as being as good as cash.
**a dollar-shaped label** — a coined phrase: the appearance of a thing without its substance.
