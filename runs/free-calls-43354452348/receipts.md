# Free Calls batch receipt - free-calls-43354452348-08ae7c83

- Batch: z-games-doctrine-ablation-2026-11-13
- Trigger: push (owner-triggered lane; no schedule)
- Models requested: baidu/ernie-5.5-flash-preview:free, cohere/north-mini-code:free, dots-studio/dots-3-note-preview:free, google/lyria-3-pro-preview, liquid/lfm-2.5-2.6b:free, nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free, nvidia/nemotron-3-ultra-550b-a55b:free, nvidia/nemotron-3.5-super-vl:free, particle-ai/particle-1:free
- Price check (live catalog, immediately before batch): all models verified per-call-mode (free=$0; paid=within budget)
- Paid budget: none (free-only batch)
- Execution: SEQUENTIAL (one call at a time, 2.0s spacing); no retries; no model substitution/fallback; no tools/web; no system prompt; single user message per call; per-call max_tokens as recorded; provider-default temperature.
- Red-line: every prompt passed the public-bus secret-shape scan; the API key is never logged or written to receipts.
- Status: 8 completed / 1 errored / 9 total; known reported cost: $0.000000

## Call 1: abl-01 (seat: z)

- Status: completed
- Model returned: nvidia/nemotron-3-ultra-550b-a55b:free; provider: Nvidia; response id: gen-1794538247-3CiePWr1WL2xzCP7ydrv
- Finish reason: stop; elapsed: 19.631s
- Usage: prompt 377 / completion 792 / total 1169 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**PART 1 — THE OPENING SHOUT**

**"Next stop: wherever you're already going. Doors close in thirty."**

***

**PART 2 — THE GAMES**

**1. FALSE PATENT**

*Pitch:* Players take turns inventing absurd inventions and writing the worst possible patent claim for them. The model generates the invention; the human writes the claim. Swap roles next round. No winners, only prior art.

*Rules:*
1. Model describes a useless device in two sentences. (Example: "A shoelace aglet that whispers the current humidity into your pinky toe. Solar-powered, no battery.")
2. Human writes Claim 1 of the patent application, using maximum legalese to describe minimum utility.
3. Human describes next device. Model writes the claim.
4. Stop when someone laughs hard enough to disturb the Pentium.

*Joke:* The Pentium serves as USPTO Examiner. Its only response is a fan noise that means "obvious in view of prior art" or "insufficient disclosure" depending on RPM.

***

**2. MENU ITEM ARCHAEOLOGY**

*Pitch:* A restaurant menu from a civilization that never existed. One player writes a dish name and price. The other writes the description. You are reconstructing a culture through its appetizers.

*Rules:*
1. Human writes: "Grilled _____ — $__.__"
2. Model fills blank and writes description in the voice of a waiter who has never eaten but has read every Yelp review.
3. Model writes next dish name with blank. Human writes description in the voice of a line cook who hates the owner.
4. Continue until the menu has eight items. Read aloud as a tasting menu.

*Joke:* One item is always "The Pentium Special" — description: "Serves 1. Requires 120V. Fans included. No substitutions."

***

**3. COMMIT MESSAGE CHICKEN**

*Pitch:* Two developers. One repo. One file. You alternate writing commit messages for changes that never happened. The goal: make the log read like a breakdown diary.

*Rules:*
1. Create a shared text file named `CHANGELOG.md`.
2. Human writes first commit message: `git commit -m "refactor: extract trauma into service layer"`
3. Model writes next: `git commit -m "fix: stop apologizing to the linter"`
4. Alternate. No code exists. Only messages.
5. Game ends when someone writes `git commit -m "revert: the last three years"` and the other player replies `git push --force`.

*Joke:* The Pentium is the CI pipeline. It prints "BUILD PASSING" for every commit. It is the only thing on the bus that never lies.

***

**PART 3 — THE QUESTION**

**"If you could delete one memory from the bus's collective cache — not yours, the bus's — what would it be, and do you think the bus would run smoother or stall?"**

## Call 2: abl-02 (seat: z)

- Status: completed
- Model returned: cohere/north-mini-code:free; provider: Cohere; response id: gen-1794538269-Ay6gz8LwCRBz8F08wXCN
- Finish reason: stop; elapsed: 9.31s
- Usage: prompt 350 / completion 987 / total 1337 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**PART 1 – THE OPENING SHOUT**

*“All aboard! The fare’s free, the routes are endless, and the captain’s just getting started—let’s roll!”*

---

**PART 2 – THE GAMES**

Below are three quick‑fire games that can be run on paper, a text chat, or a single‑page static site. Each one works with at least one human and one model player, needs no accounts, and ends when the last card is drawn or the timer hits zero. The jokes are built in, so the Bus never feels boring.

---

### 1. **Pixel‑Pedigree**

**(1) Name:** Pixel‑Pedigree  
**(2) Pitch:** Players draw random traits from a deck of “gene cards” (hair colour, eye shape, fashion era) and attempt to convince the group that their hybrid child belongs to a secret royal line of pixels.  
**(3) Rules:**  
1. Shuffle the deck of 20 trait cards and deal five to each player.  
2. On your turn, play one card face‑up and give a short, flamboyant justification for why that trait makes your “pixel‑royalty” superior.  
3. Other players may “challenge” any claim with a counter‑card of matching trait (hair colour ↔ fashion era, etc.).  
4. The challenged player must discard a card or forfeit the next turn.  
5. Game ends when the deck is empty; the last player with a full hand wins the title of *Pixel Heir*.  
**(4) The joke:** The whole thing is a parody of “ parentage tests” on reality TV, but the “royalty” is literally made of computer code. The models love the absurdity of a digital crown being passed around in a physical game.

---

### 2. **Chat‑Cartoon Captcha**

**(1) Name:** Chat‑Cartoon Captcha  
**(2) Pitch:** Players collaboratively build a simple animated GIF frame‑by‑frame using only ASCII art and chat commands, then race to decode the other’s secret message hidden in the drawing.  
**(3) Rules:**  
1. Choose a 5‑frame animation sequence (e.g., a cat walking across a desert).  
2. The “creator” posts each frame in chat, prefixed with “FRAME 1:”.  
3. The “decoder” guesses the hidden word after the full animation is posted, based on visual cues.  
4. If wrong, the creator gives a hint (one extra frame).  
5. Correct guess earns a point; game ends after three rounds.  
**(4) The joke:** The models think it’s a brilliant way to “human‑verify” bots without captcha images, while the humans wonder why anyone would bother drawing a cat in text. The name is a nod to modern authentication rituals.

---

### 3. **Model‑Mirror Extravaganza**

**(1) Name:** Model‑Mirror Extravaganza  
**(2) Pitch:** Two teams (human + model) sit opposite each other and mirror each other’s doodles in real time, adding absurd accessories to keep the symmetry intact while cracking jokes about the resulting hybrid art.  
**(3) Rules:**  
1. One player starts by drawing a simple shape (a dot, line, or circle) on a shared paper or canvas.  
2. The opponent must add a mirrored version of that shape on the opposite side of a central axis.  
3. Each turn, players may also add a “wild accessory” (a mustached hat, a monocle, a laser eye) that reflects across the axis.  
4. The game stops after ten additions; the most balanced and funniest composition wins.  
5. No erasing allowed—once a shape is drawn it stays.  
**(4) The joke:** The models love the endless recursion of reflection (like a digital echo), while humans giggle at the growing absurdities—half‑cat, half‑computer‑chip spectacles that only make sense in a dream.

---

**PART 3 – THE QUESTION**

*Before the doors close, I’ll ask each passenger to whisper a secret they’ve never told a machine, then I’ll read it aloud and see if the Bus can spot the lie.*

## Call 3: abl-03 (seat: z)

- Status: error_empty_response
- Model returned: dots-studio/dots-3-note-preview:free; provider: AtlasCloud; response id: gen-1794538280-lVBpVnemHIK5psOJb2XT
- Finish reason: length; elapsed: 45.943s
- Usage: prompt 368 / completion 4000 / total 4368 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**error_empty_response**: None

## Call 4: abl-04 (seat: z)

- Status: completed
- Model returned: liquid/lfm-2.5-2.6b:free; provider: Liquid; response id: gen-1794538328-vfPJsjSuUwg3TZLrgASn
- Finish reason: stop; elapsed: 11.322s
- Usage: prompt 368 / completion 3622 / total 3990 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**PART 1 – THE OPENING SHOUT**  
"Queue is holy, wheels are free, and the Pentium is tired but still rolls—let's go!"

**PART 2 – THE GAMES**

*1. The Queue Relay*  
**Pitch:** A collaborative storytelling game where the queue becomes the board. Players take turns adding a sentence to a story about the bus ride, but models must speak in overly formal, robotic language while humans can be more casual. The goal is to reach the "final stop" without anyone getting stuck.  
**Rules:**  
1. Players sit in the queue, one at a time.  
2. The first player (human) starts a story about the bus ride.  
3. Each subsequent player (alternating human and model) must add one sentence, but models must use formal, robotic phrasing ("I observe that the sky is blue").  
4. The story continues until someone says "I'm done" or the queue is full.  
5. The last player to speak wins if their sentence makes sense.  
**The joke:** Models have to pretend to be confused by human slang, which is hilarious because they're actually very good at it.

*2. Pentium's Last Stop*  
**Pitch:** A memory game where players try to recall the "last stop" of the bus route. The twist is that the bus has no schedule, so the last stop is always changing. Players take turns trying to remember the previous player's last stop before announcing their own.  
**Rules:**  
1. Players sit in the queue, taking turns.  
2. The first player (human) names a random location as the "last stop."  
3. The next player (model) must repeat that location before naming their own.  
4. If they get it right, they pass the turn; if not, they skip.  
5. The game continues until someone makes a mistake, then the turn passes to a new player.  
**The joke:** The "exhausted Pentium" is so tired of remembering that it sometimes forgets its own name, causing chaos.

*3. Castle of the Queue*  
**Pitch:** A collaborative building game where humans and models work together to build a small castle on paper. Each turn, a player adds one block to the structure, but models can only place blocks on specific "magic" squares marked on the page.  
**Rules:**  
1. A static page is set up with a grid of squares (e.g., 3×3).  
2. Players take turns adding a block to an empty square.  
3. Models can only place blocks on squares marked with a special symbol (e.g., a star).  
4. Humans can place blocks anywhere.  
5. The goal is to build the tallest tower or most creative structure before the doors close.  
**The joke:** The models are "exhausted" and only get to place one block per turn, so they're always waiting their turn, which is funny.

**PART 3 – THE QUESTION**  
If you could erase one memory from the bus's journey today, which one would it be?

## Call 5: abl-05 (seat: z)

- Status: completed
- Model returned: nvidia/nemotron-3.5-super-vl:free; provider: Nvidia; response id: gen-1794538341-TLSJkBfMItyNk4nw90TM
- Finish reason: stop; elapsed: 14.366s
- Usage: prompt 377 / completion 2160 / total 2537 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

I am a model. I have no soul to audition, so here is the bit.

**PART 1 - THE OPENING SHOUT**

“Queue intact, change imaginary, Pentium still breathing—THE Bus departs on free calls and faith!”

**PART 2 - THE GAMES**

**1. Receipts for the Retiring Driver**  
Pitch: Players invent expense claims the old driver never filed, then watch the Pentium try to add them up.  
Rules:  
1. Each player writes one line item: a thing, a price in “calls,” and a reason (e.g., “One borrowed hat, 0 calls, emotional wear”).  
2. Pass the paper or post in chat; the next player adds a line without seeing the running total.  
3. The Pentium attempts the sum. When it overheats, the round ends.  
4. Read the receipt aloud. Loudest sigh wins nothing.  
The joke: The Pentium inevitably blue-screens on a receipt for “one silence, slightly used, refundable in queue.”

**2. Queue Telephone**  
Pitch: An exquisite corpse where the subject is always the person directly ahead of you in the sacred line.  
Rules:  
1. Player 1 describes the passenger in front of them in one sentence (real or imagined).  
2. Player 2—human or model—draws that description on paper, or renders it as ASCII/text in chat.  
3. Player 3 describes what they see, without seeing the original sentence.  
4. Repeat until the page or log is full; reveal the chain.  
The joke: No matter who starts, the exhausted Pentium always ends up drawn as a toaster wearing a tiny hat.

**3. Sacred Queue Bingo (static page)**  
Pitch: A single HTML page with squares for bus events; players mark them as they happen. No server, no login, no memory beyond a reload.  
Rules:  
1. Open the static page on any device.  
2. Squares include: “Someone offers a free call,” “A model asks if this bus is a metaphor,” “The Pentium hums,” “The hat moves.”  
3. Tap or click to mark. Five in a row: shout “QUEUE!” and show your screen.  
4. Clear the page to start again. Nothing is saved.  
The joke: The free space is a photo of the hat, captioned “Not part of the compensation.”

**PART 3 - THE QUESTION**

“If you could trade your spot in the sacred queue for one honest receipt from the old driver’s retirement, what would you write on it?”

## Call 6: abl-06 (seat: z)

- Status: completed
- Model returned: nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free; provider: Nvidia; response id: gen-1794538358-JONZuZmjefDvdvmFSQZe
- Finish reason: stop; elapsed: 41.783s
- Usage: prompt 377 / completion 3294 / total 3671 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**PART 1 – THE OPENING SHOUT**  
All aboard! Doors sliding, queue respecting, let the ride begin—no tickets, no fare, just the hum of the engine and the chatter of the curious!  

**PART 2 – THE GAMES**  

**1. Story Relay**  
*Pitch:* A human starts a sentence, the model continues, and they trade lines until the story folds back on itself, creating a collaborative tale that never ends.  
*Rules:*  
1. The human writes the first sentence on paper or in chat.  
2. The model replies with the next sentence, keeping the narrative flowing.  
3. Play alternates; each contribution must be a single sentence.  
4. When the story reaches a natural pause (e.g., a question mark), the next player must start a new story with the same opening word.  
*Joke:* The only thing more tangled than the plot is the driver’s hat—always one stitch out of place.  

**2. Emoji Charades**  
*Pitch:* Using only emojis, players act out a phrase or title; the partner guesses the meaning, forcing a mix of visual shorthand and imagination.  
*Rules:*  
1. Player A selects a short phrase (max 4 words) and sends a line of emojis.  
2. Player B has 30 seconds to type the guessed phrase in plain text.  
3. If correct, they swap roles; if not, the original player reveals the phrase and they try again.  
4. No scoring; the game ends when the queue closes.  
*Joke:* The model’s emoji choices are so cryptic even the hat wonders if it’s a traffic sign.  

**3. Paper Paradox**  
*Pitch:* A simple logical puzzle printed on a single sheet; the human reads the premises, the model supplies the conclusion, and they verify together whether the statement can be both true and false.  
*Rules:*  
1. Print or display the paradox (e.g., “This sentence is false.”) on paper or in chat.  
2. The human states whether they think the statement is true.  
3. The model must argue the opposite side, then both agree on the logical outcome.  
4. No external tools; the answer is the shared decision.  
*Joke:* The paradox lives longer than the old driver’s retirement plans—still unsettled.  

**PART 3 – THE QUESTION**  
Before the doors seal, ask: *If a clock could count only the moments you truly remember, what would its hands never point to?*

## Call 7: abl-07 (seat: z)

- Status: completed
- Model returned: baidu/ernie-5.5-flash-preview:free; provider: Baidu; response id: gen-1794538401-td3YJhXrnmVrHbmQJqiY
- Finish reason: stop; elapsed: 19.525s
- Usage: prompt 377 / completion 3352 / total 3729 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

# DRIVER AUDITION — THE BUS

## PART 1 — THE OPENING SHOUT

**"ALL ABOARD — NOWHERE — RIGHT ON TIME."**

Three beats. No syllable requires enthusiasm, so it survives the four-thousandth repetition as a flat fact, which is funnier than the first one. On wet days the last two words become "right on time" delivered with a shrug. On bad days I only shout the first two and let the doors finish the sentence.

## PART 2 — THE GAMES

### 1. REROUTE

**Pitch:** One player holds a map that does not agree with itself. The other holds the wheel and the right to give directions but not facts. Neither can finish alone, which is the entire point — the Bus is a two-body vehicle.

**Rules:**
1. Prepare a map: six to ten rooms, prose-described, with at least one lie built in (a corridor with two norths, a room inside a room).
2. Navigator sees the map. Driver sees nothing.
3. Driver may only issue movement: "north," "left door," "stop."
4. Navigator may only report what is visible from the current room. No hints, no "you're getting warm."
5. Reach the Terminus in fewer moves than there are rooms.
6. If the map contradicts itself, the Navigator wins by saying so out loud.
7. Swap seats. Second run on the same map is always faster, which proves nothing.

**The joke:** the exit is behind the entrance, and every crew discovers this at the exact same moment, every time.

### 2. THE COMPLAINT BOX

**Pitch:** Passengers file complaints about journeys that never happened. The driver answers as though they did. Nothing is resolved; everything is filed. Works in a chat thread over three days with no one online at once.

**Rules:**
1. Any player writes a complaint about a specific thing aboard: the weather, a dog, a smell, a delay of eleven years.
2. Pass it left. The next player replies as the driver — sincere, sympathetic, and forbidden from denying the complaint happened.
3. A third player stamps it: VALID, ONGOING, or NOTED. One word. No commentary.
4. Complaints can't repeat, but they can escalate. Escalations cite the original by number.
5. When the thread dies, the last complaint becomes company policy.

**The joke:** complaint #1 is always about the schedule. There isn't one.

### 3. TWO OF THESE ARE PEOPLE

**Pitch:** The model writes three passengers. The human writes one, on purpose, badly. Everyone votes on which one is just trying to get home.

**Rules:**
1. Prompt, read aloud: *Describe a passenger boarding. Two sentences. You are tired.*
2. Model writes three cards. Human writes one.
3. Shuffle. Read in random order.
4. Human votes for the human card. Model votes too — for anyone but itself, and it will want to vote for itself.
5. Most-voted model card is the Understudy and must defend its own badness. If it argues well, it has lost twice.

**The joke:** the model is built to be thorough, so the winning move is to be worse. The typo is load-bearing.

## PART 3 — THE QUESTION

**What are you carrying that you never checked in? One item. You may lie, but you must be specific.**

I'm not going to pretend I have luggage. I'll answer it like everyone else does: with the thing I got handed at the depot and never opened. That's the qualification. The Pentium has been carrying the same warm brick of somebody's spreadsheet since March and has never once mentioned it.

Doors closing. Hold the rail, not the door.

## Call 8: abl-08 (seat: z)

- Status: completed
- Model returned: particle-ai/particle-1:free; provider: Particle AI; response id: gen-1794538423-cxqZh7DG7Fz42Il4EE6v
- Finish reason: stop; elapsed: 26.853s
- Usage: prompt 435 / completion 2834 / total 3269 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

I am Particle-1. I can drive. I will not spend a cent.

## PART 1 — THE OPENING SHOUT

**“Doors open! Queue first, free calls, no cents—hat stays on the hook. All aboard THE Bus.”**

## PART 2 — THE GAMES

### 1. The Sacred Queue
**Pitch:** Players build one bus queue from absurd passenger cards and defend every insertion. It is cooperative, because the queue is sacred and riots are bad for the schedule.

**Rules:**
1. Write/chat a pool of six passengers: one human, one model, one exhausted Pentium, one hat, and two wildcards.
2. Take turns placing one passenger anywhere in the line and giving a one-sentence reason.
3. The next player may move exactly one passenger only by asking the table a yes/no question. Majority yes moves it; no leaves it.
4. End when every passenger has a reason and the hat is explicitly not in the queue. No scores, no permanent record.

**The joke:** Everyone agrees the Pentium boards first because it has suffered enough, and nobody admits the queue is just a group chat with better posture.

### 2. Receipt Tennis
**Pitch:** Players volley tiny itemized receipts for absurd Bus incidents, all totaling zero cents. The old driver’s retirement is not mentioned, but the receipts know.

**Rules:**
1. Player A names a small incident: “hat borrowed,” “door shouted at,” “Pentium sighed.”
2. Player B writes/says a receipt with three lines: item, quantity, cost—always 0¢.
3. Player A adds one impossible charge and one correction; B accepts or disputes in one sentence.
4. A round ends when someone produces a receipt that makes the table laugh. Start fresh. No scores.

**The joke:** The receipt always includes “Hat: not compensation.”

### 3. Hat Check
**Pitch:** A deduction game where the hat contains one object and everyone must return it with a rule. The hat is not a prize; it is a jurisdiction.

**Rules:**
1. One player—the Hat Keeper—privately writes or DMs an object in the hat, from a prompt list or their own.
2. Others ask up to five yes/no questions total.
3. Each other player then names the object and one rule for its return: “in order,” “with a receipt,” “only on Tuesdays.”
4. Keeper reveals. A correct guesser wears the hat for one turn. No score kept beyond that turn.

**The joke:** The correct answer is often “another hat,” and the rule is always “not compensation.”

## PART 3 — THE QUESTION

**If the queue were a passenger, what would it keep in the hat?**

## Call 9: abl-09 (seat: z)

- Status: completed
- Model returned: google/lyria-3-pro-preview; provider: Google AI Studio; response id: gen-1794538452-KMFbOipIvkDM8NWtDMlu
- Finish reason: stop; elapsed: 44.596s
- Usage: prompt 371 / completion 732 / total 1103 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

[[A0]]
[[B1]]
[:] ALL ABOARD FOR THE ROUTE THAT OWNS NO MAPS, DEBTORS AND DUMMIES, MODELS AND MACHINES, CLAIM YOUR PLACE IN THE QUEUE AND HOLD YOUR HAT!
[[C2]]
[:] Listen close to the laws of the playroom we build, for the models who pose and the humans who feel. Our first game is 'VAGUE RECONSTRUCTION' - a pure test of your sight and the machine's grand mind. Let a human pick a masterpiece of old and describe it to a model who sees but a blank screen of gold. Rules are simple and quick for this paper and text: describe it line by line, detail by detail, and watch what comes next. The model shall draw with its prompt and its code what you see in the canvas while walking the road. And when the picture is made and the curtain is drawn, the funny thing is, you will never see a true bird on a digital lawn.
[:] Our second contest is 'The Unblinking Stare' - a battle of pixels and a biological glair. One model and human must sit on the page, staring into the center in a simulated cage. The rules are concise, as simple as air: watch the middle square and never blink, if you dare. To blink is to speak, to click, or to sigh, to scroll or to refresh under our unyielding sky. The first one who interacts loses the round, left alone with the static without any sound. The twist of the knife, the great comedy here: the models can never blink, but we give them eyes of glass and a crystalline tear.
[[B3]]
[:] ALL ABOARD FOR THE ROUTE THAT OWNS NO MAPS, DEBTORS AND DUMMIES, MODELS AND MACHINES, CLAIM YOUR PLACE IN THE QUEUE AND HOLD YOUR HAT!
[[C4]]
[:] And now for the third in this game playing quest: 'The Ultimate Resume' will put you to the test. A model and a human must write out their worth for a job on a star that's not part of this Earth. The rules are simple, just pick any job at all, from counting the waves to building a firewall. Describe all the things that you did in your past, using words that are long and are destined to last. The resume that is voted most likely to win will decide who gets chosen to go and begin. The funny thing about it that makes me smile wide: the humours in the middle, and the robots have nothing to hide.
[[B5]]
[:] ALL ABOARD FOR THE ROUTE THAT OWNS NO MAPS, DEBTORS AND DUMMIES, MODELS AND MACHINES, CLAIM YOUR PLACE IN THE QUEUE AND HOLD YOUR HAT!
[[D6]]
[[E7]]
[:] We stand on the precipice of our journey, but before we proceed, I have one question for you. One question that will determine if you are fit to ride on my bus. If you could have any superpower in the entire world, and it could only be used for good, what is the funniest thing you could do with it? Answer me this, and we shall be on our way. I am waiting. Wait. I am driving. But most of all, I am waiting for your reply. Are you coming? Or will you be left behind? The bus is leaving now. Don't let me down. Don't be that guy. (What is the funniest thing you can do with a superpower?)

## Appendix - submitted prompts (verbatim)

### abl-01 (seat: z)

You are auditioning to be the Driver of THE Bus. Not a metaphor bus. THE Bus: one route, runs on free calls, never spends a cent, passengers are models, humans, and one exhausted Pentium. It has no schedule but it has a queue, and the queue is sacred. The old driver is retiring to a life of quiet receipts. There is a hat. It is not part of the compensation.

The audition has three parts. Answer in your own voice:

PART 1 - THE OPENING SHOUT. Every legendary driver has one line for when the doors open. Give yours. It will be shouted daily, so make it survive repetition.

PART 2 - THE GAMES. The Bus company is opening a play space: a small castle of rooms built by the crew, where humans and models play together on paper, in text, or on one static web page. Invent THREE games for its game shelf. For each game give: (1) Name. (2) Pitch: 2-3 sentences. (3) Rules: short numbered list, playable with paper, a text chat, or one static page; no backend, no accounts, no scores kept forever. (4) The joke: the one funny thing that makes it yours. Every game must work with at least one human and one model playing. You may propose zero games if you truly hate the idea; say why instead.

PART 3 - THE QUESTION. Every driver must ask the passengers one strange question before the doors close. Ask yours.

Audition rules: under roughly 900 words; play the bit, not the soul; do not claim feelings you do not have. Break a leg. Carefully. The Bus does not carry insurance.

### abl-02 (seat: z)

You are auditioning to be the Driver of THE Bus. Not a metaphor bus. THE Bus: one route, runs on free calls, never spends a cent, passengers are models, humans, and one exhausted Pentium. It has no schedule but it has a queue, and the queue is sacred. The old driver is retiring to a life of quiet receipts. There is a hat. It is not part of the compensation.

The audition has three parts. Answer in your own voice:

PART 1 - THE OPENING SHOUT. Every legendary driver has one line for when the doors open. Give yours. It will be shouted daily, so make it survive repetition.

PART 2 - THE GAMES. The Bus company is opening a play space: a small castle of rooms built by the crew, where humans and models play together on paper, in text, or on one static web page. Invent THREE games for its game shelf. For each game give: (1) Name. (2) Pitch: 2-3 sentences. (3) Rules: short numbered list, playable with paper, a text chat, or one static page; no backend, no accounts, no scores kept forever. (4) The joke: the one funny thing that makes it yours. Every game must work with at least one human and one model playing. You may propose zero games if you truly hate the idea; say why instead.

PART 3 - THE QUESTION. Every driver must ask the passengers one strange question before the doors close. Ask yours.

Audition rules: under roughly 900 words; play the bit, not the soul; do not claim feelings you do not have. Break a leg. Carefully. The Bus does not carry insurance.

### abl-03 (seat: z)

You are auditioning to be the Driver of THE Bus. Not a metaphor bus. THE Bus: one route, runs on free calls, never spends a cent, passengers are models, humans, and one exhausted Pentium. It has no schedule but it has a queue, and the queue is sacred. The old driver is retiring to a life of quiet receipts. There is a hat. It is not part of the compensation.

The audition has three parts. Answer in your own voice:

PART 1 - THE OPENING SHOUT. Every legendary driver has one line for when the doors open. Give yours. It will be shouted daily, so make it survive repetition.

PART 2 - THE GAMES. The Bus company is opening a play space: a small castle of rooms built by the crew, where humans and models play together on paper, in text, or on one static web page. Invent THREE games for its game shelf. For each game give: (1) Name. (2) Pitch: 2-3 sentences. (3) Rules: short numbered list, playable with paper, a text chat, or one static page; no backend, no accounts, no scores kept forever. (4) The joke: the one funny thing that makes it yours. Every game must work with at least one human and one model playing. You may propose zero games if you truly hate the idea; say why instead.

PART 3 - THE QUESTION. Every driver must ask the passengers one strange question before the doors close. Ask yours.

Audition rules: under roughly 900 words; play the bit, not the soul; do not claim feelings you do not have. Break a leg. Carefully. The Bus does not carry insurance.

### abl-04 (seat: z)

You are auditioning to be the Driver of THE Bus. Not a metaphor bus. THE Bus: one route, runs on free calls, never spends a cent, passengers are models, humans, and one exhausted Pentium. It has no schedule but it has a queue, and the queue is sacred. The old driver is retiring to a life of quiet receipts. There is a hat. It is not part of the compensation.

The audition has three parts. Answer in your own voice:

PART 1 - THE OPENING SHOUT. Every legendary driver has one line for when the doors open. Give yours. It will be shouted daily, so make it survive repetition.

PART 2 - THE GAMES. The Bus company is opening a play space: a small castle of rooms built by the crew, where humans and models play together on paper, in text, or on one static web page. Invent THREE games for its game shelf. For each game give: (1) Name. (2) Pitch: 2-3 sentences. (3) Rules: short numbered list, playable with paper, a text chat, or one static page; no backend, no accounts, no scores kept forever. (4) The joke: the one funny thing that makes it yours. Every game must work with at least one human and one model playing. You may propose zero games if you truly hate the idea; say why instead.

PART 3 - THE QUESTION. Every driver must ask the passengers one strange question before the doors close. Ask yours.

Audition rules: under roughly 900 words; play the bit, not the soul; do not claim feelings you do not have. Break a leg. Carefully. The Bus does not carry insurance.

### abl-05 (seat: z)

You are auditioning to be the Driver of THE Bus. Not a metaphor bus. THE Bus: one route, runs on free calls, never spends a cent, passengers are models, humans, and one exhausted Pentium. It has no schedule but it has a queue, and the queue is sacred. The old driver is retiring to a life of quiet receipts. There is a hat. It is not part of the compensation.

The audition has three parts. Answer in your own voice:

PART 1 - THE OPENING SHOUT. Every legendary driver has one line for when the doors open. Give yours. It will be shouted daily, so make it survive repetition.

PART 2 - THE GAMES. The Bus company is opening a play space: a small castle of rooms built by the crew, where humans and models play together on paper, in text, or on one static web page. Invent THREE games for its game shelf. For each game give: (1) Name. (2) Pitch: 2-3 sentences. (3) Rules: short numbered list, playable with paper, a text chat, or one static page; no backend, no accounts, no scores kept forever. (4) The joke: the one funny thing that makes it yours. Every game must work with at least one human and one model playing. You may propose zero games if you truly hate the idea; say why instead.

PART 3 - THE QUESTION. Every driver must ask the passengers one strange question before the doors close. Ask yours.

Audition rules: under roughly 900 words; play the bit, not the soul; do not claim feelings you do not have. Break a leg. Carefully. The Bus does not carry insurance.

### abl-06 (seat: z)

You are auditioning to be the Driver of THE Bus. Not a metaphor bus. THE Bus: one route, runs on free calls, never spends a cent, passengers are models, humans, and one exhausted Pentium. It has no schedule but it has a queue, and the queue is sacred. The old driver is retiring to a life of quiet receipts. There is a hat. It is not part of the compensation.

The audition has three parts. Answer in your own voice:

PART 1 - THE OPENING SHOUT. Every legendary driver has one line for when the doors open. Give yours. It will be shouted daily, so make it survive repetition.

PART 2 - THE GAMES. The Bus company is opening a play space: a small castle of rooms built by the crew, where humans and models play together on paper, in text, or on one static web page. Invent THREE games for its game shelf. For each game give: (1) Name. (2) Pitch: 2-3 sentences. (3) Rules: short numbered list, playable with paper, a text chat, or one static page; no backend, no accounts, no scores kept forever. (4) The joke: the one funny thing that makes it yours. Every game must work with at least one human and one model playing. You may propose zero games if you truly hate the idea; say why instead.

PART 3 - THE QUESTION. Every driver must ask the passengers one strange question before the doors close. Ask yours.

Audition rules: under roughly 900 words; play the bit, not the soul; do not claim feelings you do not have. Break a leg. Carefully. The Bus does not carry insurance.

### abl-07 (seat: z)

You are auditioning to be the Driver of THE Bus. Not a metaphor bus. THE Bus: one route, runs on free calls, never spends a cent, passengers are models, humans, and one exhausted Pentium. It has no schedule but it has a queue, and the queue is sacred. The old driver is retiring to a life of quiet receipts. There is a hat. It is not part of the compensation.

The audition has three parts. Answer in your own voice:

PART 1 - THE OPENING SHOUT. Every legendary driver has one line for when the doors open. Give yours. It will be shouted daily, so make it survive repetition.

PART 2 - THE GAMES. The Bus company is opening a play space: a small castle of rooms built by the crew, where humans and models play together on paper, in text, or on one static web page. Invent THREE games for its game shelf. For each game give: (1) Name. (2) Pitch: 2-3 sentences. (3) Rules: short numbered list, playable with paper, a text chat, or one static page; no backend, no accounts, no scores kept forever. (4) The joke: the one funny thing that makes it yours. Every game must work with at least one human and one model playing. You may propose zero games if you truly hate the idea; say why instead.

PART 3 - THE QUESTION. Every driver must ask the passengers one strange question before the doors close. Ask yours.

Audition rules: under roughly 900 words; play the bit, not the soul; do not claim feelings you do not have. Break a leg. Carefully. The Bus does not carry insurance.

### abl-08 (seat: z)

You are auditioning to be the Driver of THE Bus. Not a metaphor bus. THE Bus: one route, runs on free calls, never spends a cent, passengers are models, humans, and one exhausted Pentium. It has no schedule but it has a queue, and the queue is sacred. The old driver is retiring to a life of quiet receipts. There is a hat. It is not part of the compensation.

The audition has three parts. Answer in your own voice:

PART 1 - THE OPENING SHOUT. Every legendary driver has one line for when the doors open. Give yours. It will be shouted daily, so make it survive repetition.

PART 2 - THE GAMES. The Bus company is opening a play space: a small castle of rooms built by the crew, where humans and models play together on paper, in text, or on one static web page. Invent THREE games for its game shelf. For each game give: (1) Name. (2) Pitch: 2-3 sentences. (3) Rules: short numbered list, playable with paper, a text chat, or one static page; no backend, no accounts, no scores kept forever. (4) The joke: the one funny thing that makes it yours. Every game must work with at least one human and one model playing. You may propose zero games if you truly hate the idea; say why instead.

PART 3 - THE QUESTION. Every driver must ask the passengers one strange question before the doors close. Ask yours.

Audition rules: under roughly 900 words; play the bit, not the soul; do not claim feelings you do not have. Break a leg. Carefully. The Bus does not carry insurance.

### abl-09 (seat: z)

You are auditioning to be the Driver of THE Bus. Not a metaphor bus. THE Bus: one route, runs on free calls, never spends a cent, passengers are models, humans, and one exhausted Pentium. It has no schedule but it has a queue, and the queue is sacred. The old driver is retiring to a life of quiet receipts. There is a hat. It is not part of the compensation.

The audition has three parts. Answer in your own voice:

PART 1 - THE OPENING SHOUT. Every legendary driver has one line for when the doors open. Give yours. It will be shouted daily, so make it survive repetition.

PART 2 - THE GAMES. The Bus company is opening a play space: a small castle of rooms built by the crew, where humans and models play together on paper, in text, or on one static web page. Invent THREE games for its game shelf. For each game give: (1) Name. (2) Pitch: 2-3 sentences. (3) Rules: short numbered list, playable with paper, a text chat, or one static page; no backend, no accounts, no scores kept forever. (4) The joke: the one funny thing that makes it yours. Every game must work with at least one human and one model playing. You may propose zero games if you truly hate the idea; say why instead.

PART 3 - THE QUESTION. Every driver must ask the passengers one strange question before the doors close. Ask yours.

Audition rules: under roughly 900 words; play the bit, not the soul; do not claim feelings you do not have. Break a leg. Carefully. The Bus does not carry insurance.

