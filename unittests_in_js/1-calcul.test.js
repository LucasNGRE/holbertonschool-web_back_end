const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should return 6 when adding 1.4 and 4.5', function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should return -2 when adding -1.4 and -0.6', function () {
      assert.strictEqual(calculateNumber('SUM', -1.4, -0.6), -2);
    });

    it('should return 5 when adding 2.6 and 2.5', function () {
      assert.strictEqual(calculateNumber('SUM', 2.6, 2.5), 5);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 when subtracting 1.4 and 4.5', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should return 0 when subtracting 2.4 and 2.5', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 2.4, 2.5), 0);
    });

    it('should return 3 when subtracting 5.6 and 2.5', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 5.6, 2.5), 3);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 when dividing 1.4 by 4.5', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return "Error" when dividing 1.4 by 0.2', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.2), 'Error');
    });

    it('should return 3 when dividing 8.5 by 2.5', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 8.5, 2.5), 3);
    });
  });
});
