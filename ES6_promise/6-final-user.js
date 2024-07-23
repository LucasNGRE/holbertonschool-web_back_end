import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, filename) {
  const user = signUpUser(firstName, lastName);
  const photo = uploadPhoto(filename);

  return Promise.allSettled([user, photo])
    .then((values) => values.map((value) => ({
      status: value.status,
      value: value.status === 'fulfilled' ? value.value : value.reason,
    })));
}
