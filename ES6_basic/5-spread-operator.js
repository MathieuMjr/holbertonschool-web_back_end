export default function concatArrays(array1, array2, string) {
  let newArray = array1.concat(array2);
  newArray = newArray.concat(Array.from(string));
  return newArray;
}
