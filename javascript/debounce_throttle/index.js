/**
 * Creates a debounced function that delays invoking `func` until after `wait` milliseconds
 * have elapsed since the last time the debounced function was invoked.
 * @param {Function} func The function to debounce.
 * @param {number} wait The number of milliseconds to delay.
 * @returns {Function} Returns the new debounced function.
 */
function debounce(func, wait) {
  // TODO: Implement Debounce (Return a function that uses setTimeout and clearTimeout)
  return function(...args) {
    // Add logic here
  };
}

/**
 * Creates a throttled function that only invokes `func` at most once per every `limit` milliseconds.
 * @param {Function} func The function to throttle.
 * @param {number} limit The number of milliseconds to throttle invocations to.
 * @returns {Function} Returns the new throttled function.
 */
function throttle(func, limit) {
  // TODO: Implement Throttle (Keep track of the last time the function was called)
  return function(...args) {
    // Add logic here
  };
}

module.exports = { debounce, throttle };
