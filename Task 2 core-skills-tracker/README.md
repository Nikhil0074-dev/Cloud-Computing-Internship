# Skill Tracker

A small command line tool that tracks learning progress during the
**Core Concepts and Skills** phase of my internship.

It matches the phase goals: study concepts, practise them, build small
projects, take quizzes, and act on mentor feedback.

## What it does

- **Concepts:** save each concept with the reason it matters (the "why").
- **Practice:** log practice sessions with notes and minutes.
- **Small projects:** link a project to a concept. The concept is then marked done.
- **Quiz:** a self-assessment that shows your weak topics.
- **Mentor feedback:** record feedback and mark it fixed when done.
- **Summary:** see your progress in numbers.

## Requirements

- Python 3.8 or newer
- No other packages needed

## How to run

```bash
git clone https://github.com/<your-username>/core-skills-tracker.git
cd core-skills-tracker

python -m skilltracker add-concept "Testing" "Finds errors early"
python -m skilltracker practice "Testing" "Wrote 5 unit tests" 45
python -m skilltracker add-project "Calculator tests" "Testing"
python -m skilltracker feedback "Add more comments"
python -m skilltracker fix-feedback 1
python -m skilltracker quiz
python -m skilltracker summary
```

Your progress is saved in `data/progress.json` (ignored by Git).

## Run the tests

```bash
python -m unittest discover tests
```

## Project structure

```
skilltracker/
  cli.py        command line commands
  tracker.py    main logic
  quiz.py       quiz scoring and weak topics
  storage.py    save and load JSON
tests/          unit tests
data/           quiz questions
```

## Best practices used

- Small files, each with one job.
- Clear names and short notes in the code.
- Input checks with clear error messages.
- Unit tests for the logic.
- Git commits in small steps.

## What I learned

- Planning the steps before writing code saves time.
- Tests catch mistakes early.
- Splitting code into small parts makes it easier to fix and read.

## Possible next steps

- Add a weekly report.
- Add more quiz topics.
- Add a simple web page.

## License

MIT
