const { fetchWithRetry, saveToFile } = require('./index.js');

// Public JSON API to fetch from
const API_URL = 'https://jsonplaceholder.typicode.com/users';
// Try uncommenting the line below to test the retry mechanism with a failing URL
// const API_URL = 'https://httpstat.us/500';

async function runDemo() {
  console.log("--- Starting Async Fetch with Retry Demo ---\n");
  
  try {
    // 1. Fetch the data
    const data = await fetchWithRetry(API_URL, {}, 3, 1000);
    console.log(`\nSuccessfully fetched ${data.length} users!`);
    
    // 2. Save the top 2 users to a local JSON file to demonstrate basic parsing
    const topData = data.slice(0, 2);
    await saveToFile('output.json', topData);
    
  } catch (error) {
    console.error(`\nDemo stopped with error: ${error.message}`);
  }
}

runDemo();
