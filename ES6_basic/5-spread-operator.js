export default function concatArrays(array1, array2, string) {
  const newArray = array1.concat(array2, Array.from(string));
  return newArray;
}
