<template>
    <!-- TITLE -->
    <h1>LOGIN</h1>

    <!-- LOGIN FORM -->
    <form @submit.prevent="login($event)" enctype="multipart/form-data">
      <input type="text" v-model="username" required>
      <input type="password" v-model="password" required>
      <button type="submit">Login</button>
    </form>
    
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
        axios.post('http://localhost:8000/petapp/login/', {
          username: this.username,
          password: this.password,
        })
          .then(response => {
            console.log(response.data);
            const token = response.data.token;
            localStorage.setItem('token', token);
            this.$router.push('/menupage');
          })
          .catch(error => {
            console.log(error.response.data);
          });
      }
  }
  }
</script>