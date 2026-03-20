// This file starts the server (either your index.js implementation or the solution)
// and makes a few automated HTTP requests to demonstrate it.

// To run this demo, simply run `node demo.js`
const http = require('http');

// Change this to require('./solution.js') to see the completed version!
const server = require('./index.js'); 

const PORT = 3000;

console.log("--- Starting Vanilla HTTP Server Demo ---\n");

setTimeout(() => {
  console.log("\n1. Testing GET /api/users...");
  http.get('http://localhost:3000/api/users', (res) => {
    let data = '';
    res.on('data', chunk => { data += chunk; });
    res.on('end', () => {
      console.log(`Status: ${res.statusCode} (Expected 200)`);
      console.log(`Content-Type: ${res.headers['content-type']} (Expected application/json)`);
      console.log(`Response: ${data}`);
    });
  }).on('error', err => {
    console.error("Test 1 Failed: ", err.message);
  });
}, 1000);

setTimeout(() => {
  console.log("\n2. Testing POST /api/users...");
  const postData = JSON.stringify({ name: 'Charlie', role: 'Admin' });
  const options = {
    hostname: 'localhost',
    port: 3000,
    path: '/api/users',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(postData)
    }
  };

  const req = http.request(options, (res) => {
    let data = '';
    res.on('data', chunk => { data += chunk; });
    res.on('end', () => {
      console.log(`Status: ${res.statusCode} (Expected 201)`);
      console.log(`Response: ${data}`);
      
      console.log("\nDemo tests triggered. The server is still running...");
      console.log("You can press CTRL+C to stop it, or test it in your browser at http://localhost:3000");
    });
  });

  req.on('error', err => {
    console.error("Test 2 Failed: ", err.message);
  });

  req.write(postData);
  req.end();
}, 2000);
