# Event Emitter (Pub/Sub) Exercise

## Objective
The **Publish-Subscribe (Pub/Sub) pattern** is immensely popular in frontend frameworks (like React, Vue, Redux) and backend systems. Your objective is to build a custom `EventEmitter` class from scratch using Vanilla JavaScript.

## Instructions
1. Open `index.js` and implement the `EventEmitter` class. It should support:
   - `on(eventName, listener)`: Subscribes to an event.
   - `emit(eventName, ...args)`: Publishes/triggers an event, passing any arguments to the listeners.
   - `off(eventName, listener)`: Unsubscribes a specific listener from an event.
2. Run `node demo.js` to test your class design.
3. If you get stuck with handling the internal map of events to arrays of functions, check `solution.js`.
