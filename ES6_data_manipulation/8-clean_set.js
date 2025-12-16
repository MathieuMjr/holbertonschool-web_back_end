export default function cleanSet(set, startString) {
  if (!startString) {
    return '';
  }
  let string = '';
  const len = startString.length;
  for (const element of set) {
    if (element.startsWith(startString)) {
      string += element.slice(len) + '-'
    }
  }
  string = string.slice(0, -1);
  return string;
}