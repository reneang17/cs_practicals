const EventEmitter = require('./index.js'); // User edits index.js

console.log("--- Starting Event Emitter Pub/Sub Demo ---\n");

const myEmitter = new EventEmitter();

// 1. Subscribe to an event
const onUserLogin = (user) => {
  console.log(`[Listener 1] User Logged In: ${user.name} (${user.email})`);
};

const sendWelcomeEmail = (user) => {
  console.log(`[Listener 2] Sending welcome email to ${user.email}...`);
};

console.log("Subscribing listeners to 'login' event...");
myEmitter.on('login', onUserLogin);
myEmitter.on('login', sendWelcomeEmail);

// 2. Publish the event
console.log("\nSimulating user login...");
myEmitter.emit('login', { name: 'Alice', email: 'alice@example.com' });

// 3. Unsubscribe a listener
console.log("\nUnsubscribing Listener 2 ('sendWelcomeEmail')...");
myEmitter.off('login', sendWelcomeEmail);

// 4. Publish the event again
console.log("\nSimulating another user login...");
myEmitter.emit('login', { name: 'Bob', email: 'bob@example.com' });

console.log("\nDemo complete. Listener 2 should not have fired for Bob.");
