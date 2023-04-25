<template>
    <!-- <form @submit.prevent="login">
      <input type="text" v-model="username" required>
      <input type="password" v-model="password" required>
      <button type="submit">Login</button>
    </form> -->
    <h1>LOGIN</h1>
</template>
  
<!-- <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
       login() {
            const data = new FormData();
            data.append('username', this.username);
            data.append('password', this.password);

            axios.post('http://localhost:8000/login/', data)
            .then(response => {
                console.log(response.data);
                // Redirect the user to the main page or do whatever you need to do with the user data
            })

            .catch(error => {
                console.log(error.response.data);
            });
        }
      }
    
  }
</script> -->