export default function setFromArray(array) {
  const newSet = new Set();
  for (const element of array) {
    newSet.add(element);
  }
  return newSet;
}