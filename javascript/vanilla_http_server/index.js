const http = require('http');

const PORT = 3000;

// Dummy data for our API
const users = [
  { id: 1, name: 'Alice' },
  { id: 2, name: 'Bob' }
];

const server = http.createServer((req, res) => {
  const { method, url } = req;

  // 1. Handle "GET /" (Return HTML)
  if (method === 'GET' && url === '/') {
    // TODO: Set status code to 200
    // TODO: Set header 'Content-Type' to 'text/html'
    // TODO: Send HTML string and end the response
  } 
  
  // 2. Handle "GET /api/users" (Return JSON)
  else if (method === 'GET' && url === '/api/users') {
    // TODO: Set status code 200, header 'Content-Type' to 'application/json'
    // TODO: Send back the stringified users array
  }
  
  // 3. Handle "POST /api/users" (Parse body and return JSON)
  else if (method === 'POST' && url === '/api/users') {
    let body = '';
    
    // Listen for incoming data chunks
    req.on('data', chunk => {
      // TODO: Append the chunk to the body string
    });

    // When the entire request body is received
    req.on('end', () => {
      // TODO: Parse the body string into JSON
      // TODO: Respond with a success message and the parsed data
    });
  } 
  
  // 4. Handle 404 Not Found
  else {
    // TODO: Handle any unknown route by returning a 404 status
  }
});

if (require.main === module) {
  server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
  });
}

module.exports = server;
