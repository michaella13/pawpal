# PawPal+ Project Reflection

## 1. System Design

-Enter owner + pet info — provide basic details about themselves and their pet
- Add/edit tasks — create and modify care tasks with at minimum a duration and priority
-Generate a daily plan — trigger the scheduler to produce a prioritized daily schedule with reasoning

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design centered around five classes that mirror how pet care actually works in real life.

Owner holds the person's info — their name, how much free time they have per day, and any preferences like preferring morning walks. It can update its available time.

Pet represents the animal with basic details like name, species, breed, age, and any special needs. It's responsible for holding the list of care tasks.

CareTask is the building block of the whole system — it stores what the task is, how long it takes, how important it is, and what category it falls under (walk, feeding, meds, etc.). It can mark itself as completed.

DailySchedule holds the final ordered list of tasks for the day along with the total time used and a human-readable explanation of why the plan was built that way. It can display the plan and return a summary.

Scheduler is the brain. It takes the owner and pet as inputs, sorts tasks by priority, filters out anything that doesn't fit within the owner's available time, and produces a DailySchedule with reasoning attached.

The core relationship is: an Owner has a Pet, a Pet has many CareTasks, and the Scheduler reads both to produce a DailySchedule.



**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Pet.add_task / get_tasks — I wired these to actually use self._tasks. They were just pass before, so the task list was being created but never written to or read from.

CareTask priority — I added a VALID_PRIORITIES tuple and a check on init that raises an error if you pass anything outside "low", "medium", "high". Without this, a typo would silently break sorting later.

Scheduler — I removed pet as a separate parameter and instead pull it from owner.pet. This way you can't accidentally pass a pet that doesn't belong to the owner

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

find_conflicts() reports that two tasks overlap but leaves it entirely up to the user to fix it. A more complete scheduler would suggest an alternative time, automatically reschedule the shorter task, or prioritize by frequency. The tradeoff is simplicity over automation — the code stays easy to read and understand, but the user has to manually reorganize conflicting tasks.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

## 6 Demo

<a href="/apprun.png" target="_blank"><img src=''>
