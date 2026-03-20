const fs = require('fs').promises;
const path = require('path');

/**
 * Perform a fetch request with exponential backoff retries.
 * @param {string} url - The URL to fetch.
 * @param {object} options - Fetch options.
 * @param {number} retries - Number of total retries.
 * @param {number} delay - Base delay in milliseconds.
 * @returns {Promise<any>}
 */
async function fetchWithRetry(url, options = {}, retries = 3, delay = 1000) {
  for (let i = 0; i <= retries; i++) {
    try {
      console.log(`[Attempt ${i + 1}/${retries + 1}] Fetching ${url}...`);
      const response = await fetch(url, options);
      
      if (!response.ok) {
        throw new Error(`HTTP Error: ${response.status} ${response.statusText}`);
      }
      
      const data = await response.json();
      return data;
      
    } catch (error) {
      console.error(`Attempt ${i + 1} failed: ${error.message}`);
      
      if (i < retries) {
        const timeout = delay * Math.pow(2, i); // Exponential backoff
        console.log(`Retrying in ${timeout}ms...\n`);
        await new Promise(resolve => setTimeout(resolve, timeout));
      } else {
        throw new Error(`Failed to fetch after ${retries} retries. Last error: ${error.message}`);
      }
    }
  }
}

/**
 * Save data to a JSON file.
 * @param {string} filename - Name of the output file.
 * @param {object|array} data - The data to save.
 */
async function saveToFile(filename, data) {
  try {
    const filePath = path.join(__dirname, filename);
    await fs.writeFile(filePath, JSON.stringify(data, null, 2), 'utf8');
    console.log(`\n✅ Data successfully saved to: ${filePath}`);
  } catch (error) {
    console.error(`\n❌ Failed to save file: ${error.message}`);
    throw error;
  }
}

module.exports = { fetchWithRetry, saveToFile };
