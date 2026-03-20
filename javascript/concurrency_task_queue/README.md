# Concurrency Task Queue Exercise

## Objective
Advanced Promises and concurrency control are standard advanced interview questions. This exercise requires you to build a `TaskQueue` that processes asynchronous tasks, but strictly limits the number of tasks running at once to a maximum concurrency limit (`N`).

## Instructions
1. Open `index.js` and implement the `TaskQueue` class.
2. The queue should be initialized with a specific concurrency limit: `const queue = new TaskQueue(3)`.
3. It should have an `add(task)` method, where `task` is an asynchronous function (returning a Promise).
4. If there are fewer than `concurrency` tasks running, it should run the `task` immediately.
5. If the limit is reached, it should queue the `task`. When a running task finishes, the next queued task should begin.
6. Run `node demo.js` to see a simulation of jobs arriving and finishing at different times!
7. Check `solution.js` for an example of how event-driven promises can manage this beautifully.
