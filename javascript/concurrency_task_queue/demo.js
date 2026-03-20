const TaskQueue = require('./index.js'); // User edits index.js

console.log("--- Starting Concurrency Task Queue Demo ---\n");

// A helper function to create a dummy async task that takes `duration` ms.
const createAsyncTask = (id, duration) => {
  return () => new Promise((resolve) => {
    console.log(`[▶] Task ${id} started... (will take ${duration}ms)`);
    setTimeout(() => {
      console.log(`[✔] Task ${id} finished.`);
      resolve(id);
    }, duration);
  });
};

// Initialize the queue with a max concurrency of 2.
// This means no more than 2 tasks should be running at the exact same time.
const queue = new TaskQueue(2);

console.log("Adding 5 tasks to a queue with Concurrency Limit = 2.\n");

// Add tasks to the queue. Tasks 1 & 2 should start immediately.
// Task 3 should only start when either 1 or 2 finishes.
queue.add(createAsyncTask(1, 1000));
queue.add(createAsyncTask(2, 500));
queue.add(createAsyncTask(3, 800));
queue.add(createAsyncTask(4, 300));
queue.add(createAsyncTask(5, 1200));

// Explanation:
// T=0ms: Task 1 and Task 2 start.
// T=500ms: Task 2 finishes. Task 3 starts.
// T=1000ms: Task 1 finishes. Task 4 starts.
// T=1300ms: Task 3 finishes (started at 500 + 800). Task 5 starts.
// T=1300ms: Task 4 finishes (started at 1000 + 300).
// T=2500ms: Task 5 finishes (started at 1300 + 1200).
