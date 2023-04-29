<template>
  <div>
    <h2>Sign up</h2>
    <form @submit.prevent="submitForm" enctype="multipart/form-data">
      <input type="text" v-model="username" placeholder="Username" required>
      <input type="email" v-model="email" placeholder="Email" required>
      <input type="date" v-model="date_of_birth" placeholder="Date of Birth" required>
      <input type="file" v-on:change="onFileChange" ref="fileInput">
      <input type="password" v-model="password1" placeholder="Password" required>
      <input type="password" v-model="password2" placeholder="Confirm Password" required>
      <button type="submit">Sign up</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      date_of_birth: '',
      profile_image: null,
      password1: '',
      password2: '',
    }
  },
  methods: {
    onFileChange(event) {
      this.profile_image = event.target.files[0];
    },

    submitForm() {
      const data = new FormData();
      data.append('username', this.username);
      data.append('email', this.email);
      data.append('date_of_birth', this.date_of_birth);
      data.append('profile_image', this.profile_image);
      data.append('password1', this.password1);
      data.append('password2', this.password2);

      axios.post('http://localhost:8000/signup/', data)
        .then(response => {
          console.log(response.data);
          this.$router.push('/newdog');
        })
        .catch(error => {
          console.log(error.response.data);
        });
    }
  }
}
</script>