# Vanilla Node HTTP Server Exercise

## Objective
Frameworks like Express or NestJS hide the complexity of routing, parsing bodies, and handling headers. In this exercise, you must build a functional HTTP Web Server completely from scratch using only Node's native `http` module.

## Instructions
1. Open `index.js`. You will find a basic `http.createServer` skeleton.
2. Implement routing logic for:
   - `GET /`: Should return a classic HTML string (e.g. `<h1>Hello Node!</h1>`) with the correct `Content-Type: text/html`.
   - `GET /api/users`: Should return a stringified JSON array of users with the correct `Content-Type: application/json`.
   - `POST /api/users`: Should read the incoming stream of chunks in the `req`, parse the JSON body, and return a success message replicating the parsed data.
3. Run `node index.js` (or `node demo.js`). It will start the server on port 3000.
4. Open your browser to `http://localhost:3000/` or use tools like `curl` or Postman to test your endpoints.
5. Check `solution.js` if you are confused about listening to the `data` and `end` events on the Request readable stream!
