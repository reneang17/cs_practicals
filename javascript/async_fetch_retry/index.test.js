const fs = require('fs').promises;

// We dynamically test either './index.js' or './solution.js' based on the command you ran
const targetFile = process.env.FILE_TARGET === 'solution' ? './solution.js' : './index.js';
const { fetchWithRetry, saveToFile } = require(targetFile);

describe('Async Fetch & Retry Project', () => {

  // This runs before every single test to give us a clean slate!
  beforeEach(() => {
    jest.clearAllMocks();
  });

  // --- 1. Testing fetchWithRetry ---
  describe('fetchWithRetry()', () => {
    
    it('should retry a failed request exactly 3 times before succeeding', async () => {
      // 1. SETUP (Mocking)
      // We don't want to actually hit the real internet!
      // So we "mock" the global fetch API to pretend it failed twice, then succeeded.
      global.fetch = jest.fn()
        .mockResolvedValueOnce({ ok: false, status: 500 }) // Attempt 1 => Fails
        .mockResolvedValueOnce({ ok: false, status: 500 }) // Attempt 2 => Fails
        .mockResolvedValueOnce({ 
          ok: true, 
          json: async () => ({ success: true })            // Attempt 3 => Succeeds!
        });

      // 2. EXECUTION
      // We pass a tiny delay (10ms) so our test runs instantly instead of waiting seconds.
      const result = await fetchWithRetry('http://mock.url', {}, 3, 10);

      // 3. ASSERTION
      // Did it call fetch 3 times like we expected?
      expect(global.fetch).toHaveBeenCalledTimes(3);
      
      // Did it return the final successful JSON data?
      expect(result).toEqual({ success: true });
    });

    it('should throw an error if all retries instantly fail', async () => {
      // Setup fetch to always fail
      global.fetch = jest.fn().mockResolvedValue({ ok: false, status: 500 });

      // We expect the promise to "reject" (throw an error) after 2 attempts
      await expect(fetchWithRetry('http://mock.url', {}, 2, 5)).rejects.toThrow();
    });

  });

  // --- 2. Testing saveToFile ---
  describe('saveToFile()', () => {
    
    it('should call the native file system module to stringify and save data', async () => {
      // Setup: We "spy" on the file system so it doesn't actually write a file to your hard drive
      const mockWriteFile = jest.spyOn(fs, 'writeFile').mockResolvedValue(true);
      
      const testData = { name: "Alice", age: 25 };

      // Execute
      await saveToFile('test_output.json', testData);

      // Assertion: Did your code call fs.promises.writeFile?
      expect(mockWriteFile).toHaveBeenCalledTimes(1);
      
      // Check the exact arguments your code passed to the file system!
      const [passedFilePath, passedContent] = mockWriteFile.mock.calls[0];
      expect(passedFilePath).toMatch(/test_output\.json$/);
      expect(JSON.parse(passedContent)).toEqual(testData);
    });

  });
});
