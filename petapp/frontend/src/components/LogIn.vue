<template>
    <!-- TITLE -->
    <div>
      <img loading="auto" src="/media/logintitle.png" width="200">
    </div>

    <!-- LOGIN FORM -->
    <form @submit.prevent="login($event)" enctype="multipart/form-data">

      <div class="rounded p-4">
        <input type="text" v-model="username" placeholder="Username" required>
      </div>

      <div class="rounded">
        <input type="password" v-model="password" placeholder="Password" required>
      </div>

      <div class="rounded p-4">
        <button type="submit">Login</button>
      </div>

    </form>

    <div>
      No account?
      <router-link to="/signup">
        <button class="btn btn-outline-info my-2 my-sm-0">Sign Up</button>
      </router-link>
    </div>
    
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