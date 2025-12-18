import signUpUser from './4-user-promise'
import uploadPhoto from './5-photo-reject'

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [signUpUser(firstName, lastName), uploadPhoto(fileName)];
  return Promise.allSettled(promises).then(results => results.map(result => {
    if (result.status === 'fulfilled') {
      return {'status': result.status, 'value': result.value}
    }
    return {'status': result.status, 'value': result.reason.toString()}
  }))
}

// allSettled retourne... une promesse !
// A t0 quand le programme s'execute, allSettled est pending : pas encore résolu
// Les deux promesses à l'intérieure vont se résoudre ou se rejeter. 
// allSettled passera résolu avec en valeur un array contenant le statut
// et la valeur de chaque promesse. 
// Une promesse est donc retournée, et sa valeur est automatiquement,
// car c'est ainsi que fonction allSettled, un array de résultat de promesses.