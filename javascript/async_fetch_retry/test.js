const fs = require('fs').promises;
const assert = require('assert');
const path = require('path');

// Determine if we are testing index.js or solution.js
const isSolution = process.argv.includes('solution');
const fileToTest = isSolution ? './solution.js' : './index.js';

console.log(`\n🧪 Testing: ${fileToTest}...\n`);

let target;
try {
  target = require(fileToTest);
} catch (e) {
  console.error(`❌ Failed to load ${fileToTest}. Did you create the functions?`);
  process.exit(1);
}

const { fetchWithRetry, saveToFile } = target;

async function runTests() {
  let passed = 0;
  let total = 2;

  // --- Test 1: fetchWithRetry ---
  console.log("Test 1: fetchWithRetry exponential backoff");
  try {
    if (typeof fetchWithRetry !== 'function') throw new Error("fetchWithRetry is not a function.");

    let fetchCalls = 0;
    // Mock global fetch to fail twice, then succeed
    global.fetch = async (url) => {
      fetchCalls++;
      if (fetchCalls < 3) {
        return { ok: false, status: 500, statusText: "Internal Server Error" };
      }
      return { ok: true, json: async () => ({ success: true }) };
    };

    const startTime = Date.now();
    // Use a small delay (e.g., 50ms) to speed up testing
    const result = await fetchWithRetry('http://mock.url', {}, 3, 50);
    const timeElapsed = Date.now() - startTime;

    // Backoff should have waited: attempt 1 failed -> wait 50ms, attempt 2 failed -> wait 100ms. 
    // Total wait > 150ms.
    assert.strictEqual(fetchCalls, 3, "fetch should have been called exactly 3 times");
    assert.deepStrictEqual(result, { success: true }, "Should return the parsed JSON data");
    assert.ok(timeElapsed >= 140, "Should have performed exponential backoff delays");

    console.log("✅ Passed!");
    passed++;
  } catch (e) {
    console.error(`❌ Failed: ${e.message}`);
  }

  // --- Test 2: saveToFile ---
  console.log("\nTest 2: saveToFile writes JSON using fs.promises");
  try {
    if (typeof saveToFile !== 'function') throw new Error("saveToFile is not a function.");

    let writeCalled = false;
    let writtenPath = '';
    let writtenContent = '';

    // Mock fs.promises.writeFile
    const originalWriteFile = fs.writeFile;
    fs.writeFile = async (filePath, content, encoding) => {
      writeCalled = true;
      writtenPath = filePath;
      writtenContent = content;
    };

    await saveToFile('test_output.json', { a: 1 });

    // Restore original
    fs.writeFile = originalWriteFile;

    assert.ok(writeCalled, "fs.promises.writeFile should have been called");
    assert.ok(writtenPath.includes('test_output.json'), "File path should include the filename");
    assert.strictEqual(writtenContent.replace(/\s+/g, ''), '{"a":1}', "Should stringify the JSON payload correctly");

    console.log("✅ Passed!");
    passed++;
  } catch (e) {
    console.error(`❌ Failed: ${e.message}`);
  }

  // --- Summary ---
  console.log(`\n📊 Results: ${passed}/${total} Tests Passed.\n`);
  if (passed === total) {
    console.log("🎉 Congratulations! You have successfully completed this exercise.");
  } else {
    console.log("🛠 Keep trying! Review the failing tests and update your implementation.");
    process.exit(1);
  }
}

runTests();
