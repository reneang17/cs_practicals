const { debounce, throttle } = require('./index.js'); // User edits index.js

console.log("--- Starting Debounce & Throttle Demo ---\n");

// 1. Test Debounce
console.log("Testing debounce (should only log 'Debounced Function' once at the end)...");
const myDebouncedFunc = debounce(() => console.log('✅ Debounced Function Executed!'), 500);

myDebouncedFunc();
myDebouncedFunc();
myDebouncedFunc(); // Only this one should actually fire after 500ms
setTimeout(myDebouncedFunc, 200); // Resets the timer
setTimeout(myDebouncedFunc, 400); // Resets the timer again. Will execute at ~900ms.

// 2. Test Throttle
setTimeout(() => {
  console.log("\nTesting throttle (should log 'Throttled Function' approximately every 300ms)...");
  const myThrottledFunc = throttle(() => console.log('✅ Throttled Function Executed!'), 300);

  // Call it rapidly
  const interval = setInterval(myThrottledFunc, 100);

  setTimeout(() => {
    clearInterval(interval);
    console.log("\nDemo complete. Try running it with the solution file to compare output!");
  }, 1000); // Run for 1 second

}, 1200); // Start after debounce finishes
