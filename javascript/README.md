# Vanilla JavaScript Projects

Welcome to the JavaScript section of the `cs_practicals` repository! 

This directory contains a series of individual vanilla JavaScript projects (using Node.js). They are structured as exercises designed to help you practice and demonstrate fundamental computer science and frontend development skills. These are specifically tailored to concepts frequently asked in junior to mid-level frontend interviews.

## 🚀 Projects (In Order of Incremental Difficulty)

We recommend working through these exercises in the following order:

### 1. [Async Fetch & Retry (`async_fetch_retry/`)](./async_fetch_retry)
- **Concepts:** Promises, `async/await`, API fetching, exponential backoff, file system.
- **Description:** Implement a custom `fetch()` wrapper that automatically retries failed HTTP requests before saving the payload to disk.

### 2. [Debounce & Throttle (`debounce_throttle/`)](./debounce_throttle)
- **Concepts:** Closures, Timing (`setTimeout`), `this` binding, performance optimization.
- **Description:** Build your own `debounce()` and `throttle()` higher-order functions from scratch.

### 3. [Event Emitter Pub/Sub (`event_emitter_pubsub/`)](./event_emitter_pubsub)
- **Concepts:** Publish-Subscribe design pattern, Object-Oriented JS, callbacks.
- **Description:** Create an `EventEmitter` class with `.on()`, `.emit()`, and `.off()` methods to manage state notifications.

### 4. [Virtual DOM Builder (`virtual_dom_builder/`)](./virtual_dom_builder)
- **Concepts:** Recursion, UI State representation, string manipulation, Tree traversal.
- **Description:** Parse a nested JavaScript object representing UI elements into a valid HTML string (the foundation of frameworks like React).

### 5. [Concurrency Task Queue (`concurrency_task_queue/`)](./concurrency_task_queue)
- **Concepts:** Advanced Promises, the Node.js Event Loop, Queue data structures.
- **Description:** Write an asynchronous task runner that receives jobs but strictly executes a maximum of `N` tasks concurrently.

### 6. [Vanilla HTTP Server (`vanilla_http_server/`)](./vanilla_http_server)
- **Concepts:** HTTP Protocol, Node Streams, Routing, backend concepts.
- **Description:** Build a completely functional API server from scratch using Node's native `http` module, handling both `GET` requests and streaming `POST` bodies without external libraries.

---

## 🛠 How to Start
Each project folder is self-contained. To begin an exercise:
1. Navigate into the folder: `cd javascript/project_name`
2. Run `npm install` (if you added any dependencies)
3. Follow the instructions in that project's specific `README.md`.
4. Write your implementation inside `index.js` and test it with `npm start` or `npm run demo`.
5. If you get stuck, peek into `solution.js` or run it with `npm run solution`!
