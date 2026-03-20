class TaskQueue {
  /**
   * @param {number} concurrencyLimit Maximum number of concurrent tasks.
   */
  constructor(concurrencyLimit) {
    this.concurrencyLimit = concurrencyLimit;
    // TODO: Initialize required state variables properties (queue array, activeCount, etc.)
  }

  /**
   * Adds an async task to the queue and runs it if under limit.
   * @param {Function} task An async function returning a Promise.
   */
  add(task) {
    // TODO: Add the task to the queue
    // TODO: Trigger a method to evaluate and execute tasks
  }

  /**
   * Internal method to run tasks from the queue if there's capacity.
   */
  async runNext() {
    // TODO: Check if activeCount is below concurrencyLimit and if the queue is not empty
    // TODO: Dequeue the next task, increment activeCount
    // TODO: Await the execution of the task
    // TODO: After the task finishes (either pass or fail): decrement activeCount, then try to runNext() again
  }
}

module.exports = TaskQueue;
