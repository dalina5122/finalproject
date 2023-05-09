<template>
  <div>
    <!-- TITLE -->
    <div>
      <img loading="auto" src="/media/signuptitle.png" width="200">
    </div>

    <!-- SIGNUP FORM -->
    <form @submit.prevent="submitForm" enctype="multipart/form-data">
      <div class="rounded p-2">
        <input type="text" v-model="username" placeholder="Username" required>
      </div>

      <div class="rounded p-2">
        <input type="email" v-model="email" placeholder="Email" required>
      </div>

      <div class="rounded p-2">
        Date of Birth: 
        <input type="date" v-model="date_of_birth" placeholder="Date of Birth" required>
      </div>

      <div class="rounded p-2">
        Picture: 
        <input type="file" v-on:change="onFileChange" ref="fileInput">
      </div>

      <div class="rounded p-2">
        <input type="password" v-model="password1" placeholder="Password" required>
      </div>

      <div class="rounded p-2">
        <input type="password" v-model="password2" placeholder="Confirm Password" required>
      </div>

      <div class="rounded p-4">
        <button type="submit">Sign up</button>
      </div>
    </form>

    <div>
      Already have an account?
      <router-link to="/log-in">
        <button class="btn btn-outline-info my-2 my-sm-0">Log In</button>
      </router-link>
    </div>
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

      axios.post('http://localhost:8000/petapp/signup/', data)
        .then(response => {
          console.log(response.data);
          this.$router.push('/menupage');
        })
        .catch(error => {
          console.log(error.response.data);
        });
    }
  }
}
</script>