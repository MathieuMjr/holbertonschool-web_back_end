import {uploadPhoto, createUser} from './utils'

export default function handleProfileSignup() {
  const photo = uploadPhoto();
  return photo.then(result1 => createUser().then(result2 => {
    console.log(`${result1.body} ${result2.firstName} ${result2.lastName}`)
  }))
  .catch(() => console.log('Signup system offline'))
}
// use Promise.all instead