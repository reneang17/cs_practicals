# Async Fetch & Retry Exercise

## Objective

- Use **Promises**, `async/await`, and the native `fetch` API to retrieve data from a remote public API endpoint.
- Implement an **Exponential Backoff Retry Mechanism** to automatically retry failed requests with increasing delays.
- Handle potential Promise rejections/errors gracefully in `try...catch` blocks.
- Use Node.js's native `fs.promises` module to perform asynchronous file system writes.

## Instructions
1. Open `index.js` and complete the `fetchWithRetry` and `saveToFile` functions according to the comments.
2. Run `node demo.js` to test your implementation. If written correctly, it will fetch JSONPlaceholder users and save them to `output.json`.
3. You can reference `solution.js` if you get stuck!
```bash
node demo.js
```

This will fetch a list of users and save a sample to a newly generated `output.json` file. You can uncomment the failing API URL in `demo.js` to observe the retry logic working!
