function found(set, value) {
  const result = set.has(value);
  return result;
  }

export default function hasValuesFromArray(set, array) {
  const bool = array.every(element => found(set, element));
  return bool;
}