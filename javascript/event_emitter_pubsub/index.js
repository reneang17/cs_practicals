class EventEmitter {
  constructor() {
    // TODO: Initialize a data structure to hold event names and their corresponding listeners
    this.events = {};
  }

  /**
   * Subscribe to an event
   * @param {string} eventName The name of the event
   * @param {Function} listener The callback function
   */
  on(eventName, listener) {
    // TODO: Add the listener to the specified event
  }

  /**
   * Publish an event
   * @param {string} eventName The name of the event
   * @param {...any} args Arguments to pass to the listeners
   */
  emit(eventName, ...args) {
    // TODO: Loop through all listeners of the event and invoke them with args
  }

  /**
   * Unsubscribe from an event
   * @param {string} eventName The name of the event
   * @param {Function} listener The callback function to remove
   */
  off(eventName, listener) {
    // TODO: Remove the specific listener from the event's array
  }
}

module.exports = EventEmitter;
