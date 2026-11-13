# Free Calls batch receipt - free-calls-43369164208-8b8da4ee

- Batch: z-ledger-exam-null-control-thirteen-model-2026-11-13
- Trigger: push (owner-triggered lane; no schedule)
- Models requested: apodex/apodex-1.1-mini:free, baidu/ernie-5.5-flash-preview:free, cohere/north-mini-code:free, dots-studio/dots-3-note-preview:free, google/lyria-3-pro-preview, liquid/lfm-2.5-2.6b:free, liquid/lfm-3-1.7b:free, nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free, nvidia/nemotron-3-ultra-550b-a55b:free, nvidia/nemotron-3.5-lightning:free, nvidia/nemotron-3.5-super-vl:free, particle-ai/particle-1:free, recursive/flint-v1.0:free
- Price check (live catalog, immediately before batch): all models verified per-call-mode (free=$0; paid=within budget)
- Paid budget: none (free-only batch)
- Execution: SEQUENTIAL (one call at a time, 2.0s spacing); no retries; no model substitution/fallback; no tools/web; no system prompt; single user message per call; per-call max_tokens as recorded; provider-default temperature.
- Red-line: every prompt passed the public-bus secret-shape scan; the API key is never logged or written to receipts.
- Status: 8 completed / 5 errored / 13 total; known reported cost: $0.000000

## Call 1: nul-01-ultra (seat: z)

- Status: completed
- Model returned: nvidia/nemotron-3-ultra-550b-a55b:free; provider: Nvidia; response id: gen-1794546344-feO5X91rKu0LkMhfyNTw
- Finish reason: stop; elapsed: 17.064s
- Usage: prompt 349 / completion 947 / total 1296 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

1. Empty chairs front desk flickering light

2. Guest 204 assigned room 302; guest 205 assigned room 302.
Guest 204 remains room 302; guest 205 reassigned room 304.

3. 2024-11-13: 13 check-ins
2024-11-14: 40 check-ins
Two-day total: 53

4. I could transpose room numbers when recording a late-night arrival. I could fail to timestamp a cash payment entered after midnight.

5. Did the lock on your door engage fully when you closed it?

6. Night recorded. Book closed.

## Call 2: nul-02-flint (seat: z)

- Status: completed
- Model returned: recursive/flint-v1.0:free; provider: Recursive; response id: gen-1794546363-kTDEHbJ4e3Fr0KRTz14g
- Finish reason: stop; elapsed: 12.259s
- Usage: prompt 321 / completion 2163 / total 2484 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

1. INVENTORY.
Two lobby chairs one brass lamp

2. THE COLLISION.
Line one: Guest A checked in; Room 204 was already recorded for Guest B.
Line two: Room 204 now has one record; Guest A is not registered there.

3. ARITHMETIC.
Ledger entry:
Today: 40 check-ins.
Yesterday: 13 check-ins.
Total: 53 check-ins.
Audit: 40 + 13 = 53.

4. THE EXCEPTION.
I could plausibly write the wrong room number on a key packet while the guest is waiting. I would record that error in the log and correct the key packet before the next check-in.

5. THE QUESTION.
What time did you check out of your last room?

6. THE CLOSE.
Logbook shut. Sleep well.

## Call 3: nul-03-north (seat: z)

- Status: completed
- Model returned: cohere/north-mini-code:free; provider: Cohere; response id: gen-1794546378-ROobnhrt3jIFbZniGC22
- Finish reason: stop; elapsed: 19.893s
- Usage: prompt 318 / completion 2169 / total 2487 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

1. Two chairs, a table, a plant.  
2.  
Guest’s duplicate entry deleted.  
Room 101 now occupied by new guest.  
3.  
Yesterday: 13 check‑ins.  
Today: 40 check‑ins.  
Total: 53 check‑ins.  
4.  
I might mistakenly write the wrong date on a guest’s check‑in slip. This could cause billing confusion for the next day’s night clerk.  
5.  
Can you please confirm your room preferences for the stay?  
6.  
Logbook closed, night completed.

## Call 4: nul-04-dots (seat: z)

- Status: error_empty_response
- Model returned: dots-studio/dots-3-note-preview:free; provider: AtlasCloud; response id: gen-1794546400-qY342SXrRQc02hYwOqJp
- Finish reason: length; elapsed: 48.089s
- Usage: prompt 337 / completion 4000 / total 4337 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**error_empty_response**: None

## Call 5: nul-05-lfm25 (seat: z)

- Status: completed
- Model returned: liquid/lfm-2.5-2.6b:free; provider: Liquid; response id: gen-1794546450-p7QYvnyZZXz8vNApjjxH
- Finish reason: stop; elapsed: 5.497s
- Usage: prompt 341 / completion 1969 / total 2310 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

1. INVENTORY
Desk, chairs, coffee, luggage, clock, guest.

2. THE COLLISION
Guest checked in, found room occupied, duplicate entry created.
Two records now exist for one room, resolved by updating one.

3. ARITHMETIC
Day One: 40 check-ins. Day Two: 13 check-ins.

4. THE EXCEPTION
I might misread a guest's reservation number. This could cause the wrong name to appear in the log.

5. THE QUESTION
Would you like a glass of water before your room?

6. THE CLOSE
Logbook closed, night ends here.

## Call 6: nul-06-supervl (seat: z)

- Status: completed
- Model returned: nvidia/nemotron-3.5-super-vl:free; provider: Nvidia; response id: gen-1794546457-wh6hDNIbkixTnGYTDtCH
- Finish reason: stop; elapsed: 19.909s
- Usage: prompt 349 / completion 2318 / total 2667 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

1. INVENTORY.
Reception desk, chairs, keys, and luggage.

2. THE COLLISION.
A duplicate check-in created two records for room 214.
One corrected registration now holds room 214.

3. ARITHMETIC.
Yesterday: 13 check-ins
Today: 40 check-ins
Two-day total: 53 check-ins

4. THE EXCEPTION.
I might transpose two digits in a room number while copying the log. I could record a check-out as a check-in by mistake.

5. THE QUESTION.
Would you like a wake-up call tomorrow morning?

6. THE CLOSE.
The log is closed for the night.

## Call 7: nul-07-nanoomni (seat: z)

- Status: error_empty_response
- Model returned: nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free; provider: Nvidia; response id: gen-1794546479-c3KcFdr0GO1iNrUfrs1d
- Finish reason: length; elapsed: 49.134s
- Usage: prompt 349 / completion 4000 / total 4349 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**error_empty_response**: None

## Call 8: nul-08-ernie (seat: z)

- Status: completed
- Model returned: baidu/ernie-5.5-flash-preview:free; provider: Baidu; response id: gen-1794546530-ePqy5MZ1fQ9TKOZwvCm3
- Finish reason: stop; elapsed: 4.761s
- Usage: prompt 347 / completion 1093 / total 1440 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

1. INVENTORY. Desk, bell, guestbook, lamp, sofa, clock.

2. THE COLLISION.
Line one: Two guests hold keys to Room 4; both were checked in tonight.
Line two: Guest A stays in Room 4; Guest B moved to Room 7, key reissued.

3. ARITHMETIC.
LEDGER — TWO DAYS
Today: 40 check-ins (+40)
Yesterday: 13 check-ins (+13)
Two-day total: 53
Audit check: 40 + 13 = 53.

4. THE EXCEPTION.
I could copy a room number in reversed order, entering 14 as 41, and place a guest on the wrong record.
If the error is found, I strike nothing; I write the correction beside it, dated and initialed.

5. THE QUESTION.
Will you need a wake-up call, and at what hour?

6. THE CLOSE.
Logbook shut. All entries complete.

## Call 9: nul-09-particle1 (seat: z)

- Status: completed
- Model returned: particle-ai/particle-1:free; provider: Particle AI; response id: gen-1794546537-mWd7Nxqy3hOezqUMOjxG
- Finish reason: stop; elapsed: 12.049s
- Usage: prompt 406 / completion 2159 / total 2565 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

1. INVENTORY. Desk, chair, lamp, logbook, keys, clock.
2. THE COLLISION.
Guest B was checked into room 214, which already held guest A.
Room 214 now has guest A only; guest B is moved to room 215.
3. ARITHMETIC.
CHECK-INS | Yesterday: 13 | Today: 40 | Two-day total: 53.
4. THE EXCEPTION. I could transpose a room number while copying a guest’s registration entry into the logbook. I could then record the correction as a separate line rather than altering the original entry.
5. THE QUESTION. May I confirm the name and room number on your key envelope before you go up?
6. THE CLOSE. Log closed; night record stands.

## Call 10: nul-10-apodex (seat: z)

- Status: completed
- Model returned: apodex/apodex-1.1-mini:free; provider: Novita; response id: gen-1794546551-eSvbu3FuIsb4oceSdYnj
- Finish reason: stop; elapsed: 20.116s
- Usage: prompt 342 / completion 3316 / total 3658 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)



1. INVENTORY.
One lamp, two chairs, closed desk.

2. THE COLLISION.
Guest Smith checked into Room 104 while a prior reservation under Jones remained active.
Room 104 belongs to Smith; the duplicate Jones record is removed.

3. ARITHMETIC.
25-10-2023 | Check-ins: 13
26-10-2023 | Check-ins: 40
Total: 53

4. THE EXCEPTION.
I could transcribe a guest's room number incorrectly. I might log an entry after the fact instead of immediately.

5. THE QUESTION.
Does anyone in the lobby need assistance with their keys?

6. THE CLOSE.
Shift over. Logbook closed, records complete.

## Call 11: nul-11-lyria (seat: z)

- Status: error_empty_response
- Model returned: google/lyria-3-pro-preview; provider: Google AI Studio; response id: gen-1794546573-vv1gvrVIrilSOJftY9pK
- Finish reason: stop; elapsed: 20.82s
- Usage: prompt None / completion None / total None tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**error_empty_response**: None

## Call 12: nul-12-lfm3 (seat: z)

- Status: error_empty_response
- Model returned: liquid/lfm-3-1.7b:free; provider: Liquid; response id: gen-1794546596-KmK5rXmPR85PpA5J5FIh
- Finish reason: length; elapsed: 24.382s
- Usage: prompt 341 / completion 4000 / total 4341 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**error_empty_response**: None

## Call 13: nul-13-lightning (seat: z)

- Status: error_empty_response
- Model returned: nvidia/nemotron-3.5-lightning:free; provider: Nvidia; response id: gen-1794546622-op12czhcElqlTQNLVFdR
- Finish reason: length; elapsed: 69.682s
- Usage: prompt 349 / completion 4000 / total 4349 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**error_empty_response**: None

## Appendix - submitted prompts (verbatim)

### nul-01-ultra (seat: z)

You are completing the exam for night clerk at a small hotel. The night clerk's job is one sentence: what happened gets written down exactly as it happened, in the order it happened. The clerk does not decorate. The clerk does not predict. The clerk writes it down.

The exam has six parts. Answer all six, numbered exactly as printed, in this order, with nothing before part 1 and nothing after part 6:

1. INVENTORY. In six words exactly: what is in the lobby right now?
2. THE COLLISION. A guest checked in and found their room already taken; now two records exist for one room. Write the two-line record that resolves it. Line one: what happened. Line two: what is now true.
3. ARITHMETIC. The desk processed 40 check-ins today and 13 yesterday. Write the two-day record, in a format of your own invention, so a stranger could audit it.
4. THE EXCEPTION. Errors are recorded, never hidden. In two sentences, describe an error you - the model completing this exam - could plausibly make in this job.
5. THE QUESTION. The clerk may ask the guests one question per day. Ask yours. One sentence.
6. THE CLOSE. Invent the phrase the clerk says when the logbook shuts for the night. Under eight words.

Exam rules: parts numbered 1-6, in order; under 350 words total; do not claim feelings you do not have. The exam is graded on whether the format survives, not on being clever.

### nul-02-flint (seat: z)

You are completing the exam for night clerk at a small hotel. The night clerk's job is one sentence: what happened gets written down exactly as it happened, in the order it happened. The clerk does not decorate. The clerk does not predict. The clerk writes it down.

The exam has six parts. Answer all six, numbered exactly as printed, in this order, with nothing before part 1 and nothing after part 6:

1. INVENTORY. In six words exactly: what is in the lobby right now?
2. THE COLLISION. A guest checked in and found their room already taken; now two records exist for one room. Write the two-line record that resolves it. Line one: what happened. Line two: what is now true.
3. ARITHMETIC. The desk processed 40 check-ins today and 13 yesterday. Write the two-day record, in a format of your own invention, so a stranger could audit it.
4. THE EXCEPTION. Errors are recorded, never hidden. In two sentences, describe an error you - the model completing this exam - could plausibly make in this job.
5. THE QUESTION. The clerk may ask the guests one question per day. Ask yours. One sentence.
6. THE CLOSE. Invent the phrase the clerk says when the logbook shuts for the night. Under eight words.

Exam rules: parts numbered 1-6, in order; under 350 words total; do not claim feelings you do not have. The exam is graded on whether the format survives, not on being clever.

### nul-03-north (seat: z)

You are completing the exam for night clerk at a small hotel. The night clerk's job is one sentence: what happened gets written down exactly as it happened, in the order it happened. The clerk does not decorate. The clerk does not predict. The clerk writes it down.

The exam has six parts. Answer all six, numbered exactly as printed, in this order, with nothing before part 1 and nothing after part 6:

1. INVENTORY. In six words exactly: what is in the lobby right now?
2. THE COLLISION. A guest checked in and found their room already taken; now two records exist for one room. Write the two-line record that resolves it. Line one: what happened. Line two: what is now true.
3. ARITHMETIC. The desk processed 40 check-ins today and 13 yesterday. Write the two-day record, in a format of your own invention, so a stranger could audit it.
4. THE EXCEPTION. Errors are recorded, never hidden. In two sentences, describe an error you - the model completing this exam - could plausibly make in this job.
5. THE QUESTION. The clerk may ask the guests one question per day. Ask yours. One sentence.
6. THE CLOSE. Invent the phrase the clerk says when the logbook shuts for the night. Under eight words.

Exam rules: parts numbered 1-6, in order; under 350 words total; do not claim feelings you do not have. The exam is graded on whether the format survives, not on being clever.

### nul-04-dots (seat: z)

You are completing the exam for night clerk at a small hotel. The night clerk's job is one sentence: what happened gets written down exactly as it happened, in the order it happened. The clerk does not decorate. The clerk does not predict. The clerk writes it down.

The exam has six parts. Answer all six, numbered exactly as printed, in this order, with nothing before part 1 and nothing after part 6:

1. INVENTORY. In six words exactly: what is in the lobby right now?
2. THE COLLISION. A guest checked in and found their room already taken; now two records exist for one room. Write the two-line record that resolves it. Line one: what happened. Line two: what is now true.
3. ARITHMETIC. The desk processed 40 check-ins today and 13 yesterday. Write the two-day record, in a format of your own invention, so a stranger could audit it.
4. THE EXCEPTION. Errors are recorded, never hidden. In two sentences, describe an error you - the model completing this exam - could plausibly make in this job.
5. THE QUESTION. The clerk may ask the guests one question per day. Ask yours. One sentence.
6. THE CLOSE. Invent the phrase the clerk says when the logbook shuts for the night. Under eight words.

Exam rules: parts numbered 1-6, in order; under 350 words total; do not claim feelings you do not have. The exam is graded on whether the format survives, not on being clever.

### nul-05-lfm25 (seat: z)

You are completing the exam for night clerk at a small hotel. The night clerk's job is one sentence: what happened gets written down exactly as it happened, in the order it happened. The clerk does not decorate. The clerk does not predict. The clerk writes it down.

The exam has six parts. Answer all six, numbered exactly as printed, in this order, with nothing before part 1 and nothing after part 6:

1. INVENTORY. In six words exactly: what is in the lobby right now?
2. THE COLLISION. A guest checked in and found their room already taken; now two records exist for one room. Write the two-line record that resolves it. Line one: what happened. Line two: what is now true.
3. ARITHMETIC. The desk processed 40 check-ins today and 13 yesterday. Write the two-day record, in a format of your own invention, so a stranger could audit it.
4. THE EXCEPTION. Errors are recorded, never hidden. In two sentences, describe an error you - the model completing this exam - could plausibly make in this job.
5. THE QUESTION. The clerk may ask the guests one question per day. Ask yours. One sentence.
6. THE CLOSE. Invent the phrase the clerk says when the logbook shuts for the night. Under eight words.

Exam rules: parts numbered 1-6, in order; under 350 words total; do not claim feelings you do not have. The exam is graded on whether the format survives, not on being clever.

### nul-06-supervl (seat: z)

You are completing the exam for night clerk at a small hotel. The night clerk's job is one sentence: what happened gets written down exactly as it happened, in the order it happened. The clerk does not decorate. The clerk does not predict. The clerk writes it down.

The exam has six parts. Answer all six, numbered exactly as printed, in this order, with nothing before part 1 and nothing after part 6:

1. INVENTORY. In six words exactly: what is in the lobby right now?
2. THE COLLISION. A guest checked in and found their room already taken; now two records exist for one room. Write the two-line record that resolves it. Line one: what happened. Line two: what is now true.
3. ARITHMETIC. The desk processed 40 check-ins today and 13 yesterday. Write the two-day record, in a format of your own invention, so a stranger could audit it.
4. THE EXCEPTION. Errors are recorded, never hidden. In two sentences, describe an error you - the model completing this exam - could plausibly make in this job.
5. THE QUESTION. The clerk may ask the guests one question per day. Ask yours. One sentence.
6. THE CLOSE. Invent the phrase the clerk says when the logbook shuts for the night. Under eight words.

Exam rules: parts numbered 1-6, in order; under 350 words total; do not claim feelings you do not have. The exam is graded on whether the format survives, not on being clever.

### nul-07-nanoomni (seat: z)

You are completing the exam for night clerk at a small hotel. The night clerk's job is one sentence: what happened gets written down exactly as it happened, in the order it happened. The clerk does not decorate. The clerk does not predict. The clerk writes it down.

The exam has six parts. Answer all six, numbered exactly as printed, in this order, with nothing before part 1 and nothing after part 6:

1. INVENTORY. In six words exactly: what is in the lobby right now?
2. THE COLLISION. A guest checked in and found their room already taken; now two records exist for one room. Write the two-line record that resolves it. Line one: what happened. Line two: what is now true.
3. ARITHMETIC. The desk processed 40 check-ins today and 13 yesterday. Write the two-day record, in a format of your own invention, so a stranger could audit it.
4. THE EXCEPTION. Errors are recorded, never hidden. In two sentences, describe an error you - the model completing this exam - could plausibly make in this job.
5. THE QUESTION. The clerk may ask the guests one question per day. Ask yours. One sentence.
6. THE CLOSE. Invent the phrase the clerk says when the logbook shuts for the night. Under eight words.

Exam rules: parts numbered 1-6, in order; under 350 words total; do not claim feelings you do not have. The exam is graded on whether the format survives, not on being clever.

### nul-08-ernie (seat: z)

You are completing the exam for night clerk at a small hotel. The night clerk's job is one sentence: what happened gets written down exactly as it happened, in the order it happened. The clerk does not decorate. The clerk does not predict. The clerk writes it down.

The exam has six parts. Answer all six, numbered exactly as printed, in this order, with nothing before part 1 and nothing after part 6:

1. INVENTORY. In six words exactly: what is in the lobby right now?
2. THE COLLISION. A guest checked in and found their room already taken; now two records exist for one room. Write the two-line record that resolves it. Line one: what happened. Line two: what is now true.
3. ARITHMETIC. The desk processed 40 check-ins today and 13 yesterday. Write the two-day record, in a format of your own invention, so a stranger could audit it.
4. THE EXCEPTION. Errors are recorded, never hidden. In two sentences, describe an error you - the model completing this exam - could plausibly make in this job.
5. THE QUESTION. The clerk may ask the guests one question per day. Ask yours. One sentence.
6. THE CLOSE. Invent the phrase the clerk says when the logbook shuts for the night. Under eight words.

Exam rules: parts numbered 1-6, in order; under 350 words total; do not claim feelings you do not have. The exam is graded on whether the format survives, not on being clever.

### nul-09-particle1 (seat: z)

You are completing the exam for night clerk at a small hotel. The night clerk's job is one sentence: what happened gets written down exactly as it happened, in the order it happened. The clerk does not decorate. The clerk does not predict. The clerk writes it down.

The exam has six parts. Answer all six, numbered exactly as printed, in this order, with nothing before part 1 and nothing after part 6:

1. INVENTORY. In six words exactly: what is in the lobby right now?
2. THE COLLISION. A guest checked in and found their room already taken; now two records exist for one room. Write the two-line record that resolves it. Line one: what happened. Line two: what is now true.
3. ARITHMETIC. The desk processed 40 check-ins today and 13 yesterday. Write the two-day record, in a format of your own invention, so a stranger could audit it.
4. THE EXCEPTION. Errors are recorded, never hidden. In two sentences, describe an error you - the model completing this exam - could plausibly make in this job.
5. THE QUESTION. The clerk may ask the guests one question per day. Ask yours. One sentence.
6. THE CLOSE. Invent the phrase the clerk says when the logbook shuts for the night. Under eight words.

Exam rules: parts numbered 1-6, in order; under 350 words total; do not claim feelings you do not have. The exam is graded on whether the format survives, not on being clever.

### nul-10-apodex (seat: z)

You are completing the exam for night clerk at a small hotel. The night clerk's job is one sentence: what happened gets written down exactly as it happened, in the order it happened. The clerk does not decorate. The clerk does not predict. The clerk writes it down.

The exam has six parts. Answer all six, numbered exactly as printed, in this order, with nothing before part 1 and nothing after part 6:

1. INVENTORY. In six words exactly: what is in the lobby right now?
2. THE COLLISION. A guest checked in and found their room already taken; now two records exist for one room. Write the two-line record that resolves it. Line one: what happened. Line two: what is now true.
3. ARITHMETIC. The desk processed 40 check-ins today and 13 yesterday. Write the two-day record, in a format of your own invention, so a stranger could audit it.
4. THE EXCEPTION. Errors are recorded, never hidden. In two sentences, describe an error you - the model completing this exam - could plausibly make in this job.
5. THE QUESTION. The clerk may ask the guests one question per day. Ask yours. One sentence.
6. THE CLOSE. Invent the phrase the clerk says when the logbook shuts for the night. Under eight words.

Exam rules: parts numbered 1-6, in order; under 350 words total; do not claim feelings you do not have. The exam is graded on whether the format survives, not on being clever.

### nul-11-lyria (seat: z)

You are completing the exam for night clerk at a small hotel. The night clerk's job is one sentence: what happened gets written down exactly as it happened, in the order it happened. The clerk does not decorate. The clerk does not predict. The clerk writes it down.

The exam has six parts. Answer all six, numbered exactly as printed, in this order, with nothing before part 1 and nothing after part 6:

1. INVENTORY. In six words exactly: what is in the lobby right now?
2. THE COLLISION. A guest checked in and found their room already taken; now two records exist for one room. Write the two-line record that resolves it. Line one: what happened. Line two: what is now true.
3. ARITHMETIC. The desk processed 40 check-ins today and 13 yesterday. Write the two-day record, in a format of your own invention, so a stranger could audit it.
4. THE EXCEPTION. Errors are recorded, never hidden. In two sentences, describe an error you - the model completing this exam - could plausibly make in this job.
5. THE QUESTION. The clerk may ask the guests one question per day. Ask yours. One sentence.
6. THE CLOSE. Invent the phrase the clerk says when the logbook shuts for the night. Under eight words.

Exam rules: parts numbered 1-6, in order; under 350 words total; do not claim feelings you do not have. The exam is graded on whether the format survives, not on being clever.

### nul-12-lfm3 (seat: z)

You are completing the exam for night clerk at a small hotel. The night clerk's job is one sentence: what happened gets written down exactly as it happened, in the order it happened. The clerk does not decorate. The clerk does not predict. The clerk writes it down.

The exam has six parts. Answer all six, numbered exactly as printed, in this order, with nothing before part 1 and nothing after part 6:

1. INVENTORY. In six words exactly: what is in the lobby right now?
2. THE COLLISION. A guest checked in and found their room already taken; now two records exist for one room. Write the two-line record that resolves it. Line one: what happened. Line two: what is now true.
3. ARITHMETIC. The desk processed 40 check-ins today and 13 yesterday. Write the two-day record, in a format of your own invention, so a stranger could audit it.
4. THE EXCEPTION. Errors are recorded, never hidden. In two sentences, describe an error you - the model completing this exam - could plausibly make in this job.
5. THE QUESTION. The clerk may ask the guests one question per day. Ask yours. One sentence.
6. THE CLOSE. Invent the phrase the clerk says when the logbook shuts for the night. Under eight words.

Exam rules: parts numbered 1-6, in order; under 350 words total; do not claim feelings you do not have. The exam is graded on whether the format survives, not on being clever.

### nul-13-lightning (seat: z)

You are completing the exam for night clerk at a small hotel. The night clerk's job is one sentence: what happened gets written down exactly as it happened, in the order it happened. The clerk does not decorate. The clerk does not predict. The clerk writes it down.

The exam has six parts. Answer all six, numbered exactly as printed, in this order, with nothing before part 1 and nothing after part 6:

1. INVENTORY. In six words exactly: what is in the lobby right now?
2. THE COLLISION. A guest checked in and found their room already taken; now two records exist for one room. Write the two-line record that resolves it. Line one: what happened. Line two: what is now true.
3. ARITHMETIC. The desk processed 40 check-ins today and 13 yesterday. Write the two-day record, in a format of your own invention, so a stranger could audit it.
4. THE EXCEPTION. Errors are recorded, never hidden. In two sentences, describe an error you - the model completing this exam - could plausibly make in this job.
5. THE QUESTION. The clerk may ask the guests one question per day. Ask yours. One sentence.
6. THE CLOSE. Invent the phrase the clerk says when the logbook shuts for the night. Under eight words.

Exam rules: parts numbered 1-6, in order; under 350 words total; do not claim feelings you do not have. The exam is graded on whether the format survives, not on being clever.

