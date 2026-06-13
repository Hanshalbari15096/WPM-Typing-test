# WPM Typing Test

A terminal-based typing speed tester written in pure Python.

## Requirements

- Python 3.x
- No external libraries needed

## Run

```bash
python WPM_Test.py
```

## How It Works

1. A randomly generated sentence appears on screen
2. Press **Enter** to start the timer
3. Type the sentence and press **Enter**
4. See your **WPM**, **accuracy**, and a performance message

## Sentence Generation

Sentences are built by randomly combining:

- **Subject** — e.g. `A swift programmer`, `The clever AI`
- **Verb** — e.g. `quickly debugged`, `optimized the code of`
- **Object** — e.g. `the entire database.`, `a complex puzzle.`

Every run gives a unique sentence.

## Metrics

| Metric | How It's Calculated |
|---|---|
| WPM | `(characters typed / 5) / minutes elapsed` |
| Accuracy | `correct characters / total characters × 100` |

## Performance Feedback

| Condition | Message |
|---|---|
| Accuracy = 100% and WPM > 40 | `Good job` |
| Accuracy < 70% | `Focus more on accuracy next time` |

## Example Output

```
=== WELCOME TO THE WPM TYPING TEST ===

Your sentence to type is:
"A sneaky cat explored a complex puzzle."

Press ENTER as soon as you are ready to start typing!

Start Typing Now
> A sneaky cat explored a complex puzzle.

--- RESULTS ---
Time Taken: 6.42 seconds
Your Speed: 62 WPM
Accuracy: 100%
Good job
```

## File Structure

```
WPM_Test.py   # main script, everything in one file
README.md     # this file
```
