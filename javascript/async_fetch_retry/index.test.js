const fs = require('fs').promises;

// Determine which file to test based on environment variable or fallback to index.js
const targetFile = process.env.FILE_TARGET === 'solution' ? './solution.js' : './index.js';
const { fetchWithRetry, saveToFile } = require(targetFile);

describe(`Async Fetch Retry (${targetFile})`, () => {

  beforeEach(() => {
    // Clear all mocks before each test
    jest.clearAllMocks();
  });

  describe('fetchWithRetry', () => {
    it('should implement exponential backoff and retry 3 times', async () => {
      // 1. Mock global fetch
      const mockFetch = jest.fn()
        .mockResolvedValueOnce({ ok: false, status: 500 }) // Attempt 1 fails
        .mockResolvedValueOnce({ ok: false, status: 500 }) // Attempt 2 fails
        .mockResolvedValueOnce({ 
          ok: true, 
          json: async () => ({ success: true }) 
        }); // Attempt 3 succeeds

      global.fetch = mockFetch;

      // 2. Execute the function (with a tiny 10ms base delay to speed up the test)
      const startTime = Date.now();
      const result = await fetchWithRetry('http://mock.url', {}, 3, 10);
      const timeElapsed = Date.now() - startTime;

      // 3. Assertions
      expect(mockFetch).toHaveBeenCalledTimes(3);
      expect(result).toEqual({ success: true });
      
      // Delay should roughly be: 10ms + 20ms = 30ms total wait time (exponential backoff)
      expect(timeElapsed).toBeGreaterThanOrEqual(25);
    });

    it('should throw an error if all retries fail', async () => {
      global.fetch = jest.fn().mockResolvedValue({ ok: false, status: 500 });

      // We expect the promise to reject after 2 attempts
      await expect(fetchWithRetry('http://mock.url', {}, 2, 5))
        .rejects
        .toThrow(/Failed to fetch after 2 attempts/i);

      expect(global.fetch).toHaveBeenCalledTimes(2);
    });
  });

  describe('saveToFile', () => {
    it('should correctly stringify and save data using fs.promises.writeFile', async () => {
      const mockWriteFile = jest.spyOn(fs, 'writeFile').mockResolvedValue(true);
      const testData = { a: 1, b: 2 };

      await saveToFile('test_output.json', testData);

      expect(mockWriteFile).toHaveBeenCalledTimes(1);
      
      // Check the arguments passed to fs.writeFile
      const [filePath, content] = mockWriteFile.mock.calls[0];
      expect(filePath).toMatch(/test_output\.json$/);
      
      const parsedContent = JSON.parse(content);
      expect(parsedContent).toEqual(testData);
    });
  });
});
