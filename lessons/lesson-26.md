# Lesson 26 · Microseconds

**Topic:** Algorithmic trading and market microstructure  
**Style & Register:** Technical journalism — fast, concrete, short sentences, scene and number  
**Level:** C1–C2

---

## Reading Passage

A microsecond is one millionth of a second. Light travels about three hundred metres in that time. A nerve impulse gets roughly nowhere. You cannot perceive one, and neither can anything you have ever built with your hands.

There are firms whose entire competitive position is measured in them.

**What is actually being raced**

Start with the object at the centre of it all: the order book.

For any given instrument, an exchange maintains two queues. On one side, everyone willing to buy, ranked by price. On the other, everyone willing to sell. The highest bid and the lowest offer face each other across a gap — the spread — and when the two meet, a trade occurs. The book is public, it updates continuously, and it is the closest thing modern finance has to a physical marketplace.

Most of the resting orders in it now belong to market makers: firms that simultaneously quote a price to buy and a price to sell, intending to capture the spread rather than to hold a view. They are, functionally, the people standing behind the counter. They do not care which direction the price moves so long as they buy slightly below the midpoint and sell slightly above it, repeatedly, all day.

And here is the problem their entire business exists to manage.

A market maker's quote is an open offer to anyone. Most of the people who take it are trading for their own ordinary reasons — a pension fund rebalancing, a retail order, a company hedging a currency exposure. Those are good trades to be on the other side of. But some of the people who take it know something the market maker does not: the price is about to move, and it is about to move through the quote. Every one of those trades is a loss.

This is adverse selection, and it dictates everything. The market maker must set a spread wide enough to profit from the uninformed flow by more than they lose to the informed flow — and must withdraw their quote, fast, the instant the picture changes.

*Fast* is the operative word. That is what is being raced. Not the ability to predict the market over minutes or days, which is a different business entirely, but the ability to update a quote before somebody hits it at a price that has already become wrong.

**The physical layer**

Because the constraint is physical, the solutions are physical.

Exchanges lease rack space inside their own data centres, and firms pay to place their machines there. Cable lengths between the exchange's matching engine and every customer rack are deliberately equalised to the metre, so that the advantage is sold rather than inherited by whoever is nearest the door.

Between cities, geometry matters. Fibre optic cable does not run in straight lines; it follows rights of way, railways and roads, and light travels through glass at about two-thirds of its speed in vacuum. Microwave signals, by contrast, travel through air at very nearly the full speed of light, and a chain of towers can be built approximately straight. On the route between the major American exchange centres, microwave transmission cut round-trip latency from roughly six and a half milliseconds to just over four. The links cost tens of millions, carry a trickle of data compared with fibre, and fail in heavy rain. They were built anyway, and then rebuilt for further increments.

Inside the machines, the same logic. General-purpose processors were abandoned for programmable logic chips that implement the strategy directly in hardware, because an operating system's scheduler introduces delays measured in microseconds and a microsecond is the unit of competition. Firms now quote their tick-to-trade times — signal in, order out — in double-digit nanoseconds.

**What it cost, and what it bought**

Two things are true at once, and most commentary picks one.

The first: trading has become dramatically cheaper for ordinary investors. In the 1990s the spread on a liquid stock was quoted in fractions of a dollar. Today it is frequently a single cent, and often less on the most active names. Commissions have fallen towards zero. Whatever else the arms race produced, the cost of executing a normal transaction collapsed, and that saving accrues to every pension and every index fund.

The second: the competition is largely zero-sum. A microwave link that lets one firm see a price update two hundred microseconds sooner does not add information to the world. It reallocates a profit from one participant to another, and the capital spent doing so is a cost the system bears for no aggregate gain. Serious economists have described the resulting expenditure as a socially wasteful arms race, and the argument is difficult to answer on its own terms.

**Where it breaks**

Speed changes the character of failure.

On an afternoon in May 2010, a large automated sell programme executed into a market already thin. Market makers, seeing an imbalance they could not interpret, withdrew — exactly as their models instruct. Liquidity evaporated in seconds. Individual shares printed at a penny and at a hundred thousand dollars. The index fell hundreds of points and recovered most of it within about half an hour. Nothing had happened in the world. The book had simply emptied faster than anyone could refill it.

Two years later, a firm deployed a software update to its trading servers and missed one of eight machines. Dormant code on that machine reactivated under a flag reused for the new system and began sending orders at full speed. The firm lost roughly four hundred and forty million dollars in about forty-five minutes — more than its market capitalisation — and was sold within days. The error was not a trading error. It was a deployment error, of a kind that occurs in ordinary software teams weekly, executing at a rate no human process could interrupt.

The regulatory response has been structural rather than prohibitive: automatic pauses when a price moves too far too fast, bands outside which orders cannot execute, mandatory risk checks before an order reaches the exchange. At least one venue introduced a deliberate delay — a few hundred microseconds of coiled fibre in front of its matching engine — on the reasoning that if everyone is slowed equally, the advantage of being marginally faster disappears.

**The honest ledger**

The market is faster, cheaper and more fragile than it was. Spreads are historically narrow; liquidity is abundant in calm conditions and can vanish in seconds in disorderly ones, because most of it is now provided by participants under no obligation to provide it.

There is no plausible route back. The interesting question was never whether machines should intermediate markets — they do, and reversing it would raise costs for everyone. It is whether a system in which the binding constraint is the speed of light through glass has optimised for anything a saver would recognise as valuable.

---

## Key Vocabulary

**instrument** *(n.)* — a tradable financial asset or contract.
**queue** *(n.)* — an ordered line of waiting items.
**bid** *(n.)* — the highest price a buyer is offering.
**spread** *(n.)* — the gap between the best buying and selling prices.
**resting** *(adj.)* — of an order, waiting in the book to be matched.
**quote** *(v./n.)* — to state a price at which one will trade.
**midpoint** *(n.)* — the value halfway between two prices.
**hedge** *(v.)* — to take a position offsetting an existing risk.
**adverse selection** *(n. phr.)* — the tendency to transact disproportionately with better-informed parties.
**withdraw** *(v.)* — to remove an offer from the market.
**operative** *(adj.)* — most significant; carrying the essential meaning.
**rack** *(n.)* — a frame housing computing equipment in a data centre.
**inherit** *(v.)* — to receive by circumstance rather than payment.
**latency** *(n.)* — the delay between sending and receiving.
**increment** *(n.)* — a small additional amount of improvement.
**scheduler** *(n.)* — the component of an operating system allocating processor time.
**zero-sum** *(adj.)* — describing a situation where one party's gain equals another's loss.
**reallocate** *(v.)* — to shift from one holder to another without creating new value.
**aggregate** *(adj.)* — combined across the whole system.
**thin** *(adj.)* — of a market, having little available liquidity.
**dormant** *(adj.)* — inactive but capable of being reactivated.
**prohibitive** *(adj.)* — here, taking the form of a ban.

## Phrases & Collocations

**hold a view** — to take a position based on an opinion about future prices.
**on the other side of** — acting as counterparty to a given trade.
**rights of way** — legally permitted routes across land.
**tick-to-trade** — the interval between receiving a price signal and issuing an order.
**two things are true at once** — a framing device introducing a genuine tension.
**difficult to answer on its own terms** — a concession that an argument is internally sound.
