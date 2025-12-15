export default function createInt8TypedArray(length, position, value) {
  if (position >= length || position < 0) {
    throw new Error('Position outside range');
  }
  const typedArray = new ArrayBuffer(length);
  const dataView = new DataView(typedArray);
  dataView.setInt8(position, value);
  return dataView;
}
