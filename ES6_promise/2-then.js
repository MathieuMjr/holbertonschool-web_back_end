export default function handleResponseFromAPI(promise) {
  promise.then(() => {
    console.log('Got a response from the API');
    return {'statuts': 200, 'body': 'success'};
  })
  .catch(() => {
    console.log('Got a response from the API');
    return new Error;
  })
}
