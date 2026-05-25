1/**
2 * @param {string} val
3 * @return {Object}
4 */
5var expect = function(val) {
6    return {
7        toBe: function(other) {
8            if (val === other) return true;
9            throw new Error("Not Equal");
10        },
11
12        notToBe: function(other) {
13            if (val !== other) return true;
14            throw new Error("Equal");
15        }
16    };
17};
18
19/**
20 * expect(5).toBe(5); // true
21 * expect(5).notToBe(5); // throws "Equal"
22 */