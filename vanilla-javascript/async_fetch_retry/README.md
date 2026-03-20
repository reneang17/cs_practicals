# Async Fetch & Retry

This project demonstrates core Asynchronous JavaScript programming concepts essential for junior frontend roles.

## Objective

- Use **Promises**, `async/await`, and the native `fetch` API to retrieve data from a remote public API endpoint (`JSONPlaceholder`).
- Implement an **Exponential Backoff Retry Mechanism** to automatically retry failed requests with increasing delays.
- Handle potential Promise rejections/errors gracefully in `try...catch` blocks.
- Use Node.js's native `fs.promises` module to perform asynchronous file system writes.

## Usage

Simply run the demo script using Node:
```bash
node demo.js
```

This will fetch a list of users and save a sample to a newly generated `output.json` file. You can uncomment the failing API URL in `demo.js` to observe the retry logic working!
