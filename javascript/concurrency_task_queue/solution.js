class TaskQueue {
  constructor(concurrencyLimit) {
    this.concurrencyLimit = concurrencyLimit;
    this.activeCount = 0;
    this.queue = [];
  }

  add(task) {
    this.queue.push(task);
    this.runNext();
  }

  async runNext() {
    if (this.activeCount >= this.concurrencyLimit || this.queue.length === 0) {
      return; // Can't run anything right now
    }

    // Unqueue next item
    const task = this.queue.shift();
    this.activeCount++;

    try {
      await task();
    } catch (error) {
      console.error("Task failed:", error);
    } finally {
      this.activeCount--;
      // Regardless of success or failure, try to run the next task
      this.runNext();
    }
  }
}

module.exports = TaskQueue;
