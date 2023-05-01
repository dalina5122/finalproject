<template>
    <form @submit.prevent="login($event)" enctype="multipart/form-data">
      <input type="text" v-model="username" required>
      <input type="password" v-model="password" required>
      <button type="submit">Login</button>
    </form>
    <h1>LOGIN</h1>
</template>
  
<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      login(event) {
        event.preventDefault();
        const data = new FormData();
        data.append('username', this.username);
        data.append('password', this.password);

        axios.post('http://localhost:8000/petapp/login/', data)
          .then(response => {
            console.log(response.data);
            const token = response.data.token;
            localStorage.setItem('token', token);
            this.$router.push('/dogsmap');
          })
          .catch(error => {
            console.log(error.response.data);
          });
      }
  }
  }
</script>