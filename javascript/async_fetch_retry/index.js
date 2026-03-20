const fs = require('fs').promises;
const path = require('path');

/**
 * Perform a fetch request with exponential backoff retries.
 * @param {string} url - The URL to fetch.
 * @param {object} options - Fetch options.
 * @param {number} retries - Number of total retries (Attempt 1 + N retries).
 * @param {number} delay - Base delay in milliseconds.
 * @returns {Promise<any>}
 */
async function fetchWithRetry(url, options = {}, retries = 3, delay = 1000) {
  // TODO: Implement fetch logic with async/await
  // TODO: Implement exponential backoff retry on failure
  // TODO: Return parsed JSON data
}

/**
 * Save data to a JSON file.
 * @param {string} filename - Name of the output file.
 * @param {object|array} data - The data to save.
 */
async function saveToFile(filename, data) {
  // TODO: Construct the file path using __dirname
  // TODO: Use fs.promises.writeFile to save the data as a JSON string
  // TODO: Handle potential errors
}

module.exports = { fetchWithRetry, saveToFile };
