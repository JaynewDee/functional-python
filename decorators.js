function timer(func) {
  function wrapper(...args) {
    console.time("JavaScript");
    const result = func(...args);
    console.timeEnd("JavaScript");
    return result;
  }
  return wrapper;
}

function memoize(func) {
  // initialize mutable structure
  let cache = {};

  function wrapper(...args) {
    const key = args.toString();
    // return early with result if it's stored
    if (key in cache) return cache[key];
    const result = func(...args);
    cache[key] = result;
    return result;
  }
  return wrapper;
}

function cpuSpinner(x) {
  return [...Array.from({ length: x }, (x) => x)].reduce(
    (sum, val) => (sum += val),
    0
  );
}

function cpuSpinnerIter(x) {
  const nums = [...Array.from({ length: x }, (x) => x)];
  let total = 0;
  for (let i = 0; i < nums.length; i++) {
    total += nums[i];
  }
}

const timedMemo = timer(memoize(cpuSpinner));

timedMemo(100000000);
timedMemo(100000000);

const timedIterMemo = timer(memoize(cpuSpinnerIter));

timedIterMemo(100000000);
timedIterMemo(100000000);
