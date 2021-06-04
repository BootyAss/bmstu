function matMult(a, b) {
  let rowsA = a.length;
  let colsA = a[0].length;
  let rowsB = b.length;
  let colsB = b[0].length;

  let result = [rowsA];

  for (let i = 0; i < rowsA; i++) {
    result[i] = [colsB];
  }

  if (colsA != rowsB) {
    print("rows and cols");
    return null;
  }

  for (let i = 0; i < rowsA; i++) {
    for (let j = 0; j < colsB; j++) {
      let sum = 0;
      for (let k = 0; k < colsA; k++) {
        sum += a[i][k] * b[k][j];
      }
      result[i][j] = sum;
    }
  }
  
  return result;
}
