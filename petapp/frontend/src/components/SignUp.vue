<template>
    <div>
      <form>
        <label>Username</label>
        <input type="text" v-model="form.username">
        <label>Email</label>
        <input type="email" v-model="form.email">
        <label>Date of Birth</label>
        <input type="date" v-model="form.date_of_birth">
        <label>Profile Image</label>
        <input type="file" v-on:change="handleFileChange">
        <label>Password</label>
        <input type="password" v-model="form.password1">
        <label>Confirm Password</label>
        <input type="password" v-model="form.password2">
        <button type="button" v-on:click="submitForm">Sign Up</button>
      </form>
    </div>
</template>
  
<script>
  export default {
    props: ['csrfToken'],
    data() {
      return {
        form: {
          username: '',
          email: '',
          date_of_birth: '',
          profile_image: null,
          password1: '',
          password2: ''
        }
      }
    },

    methods: {
        handleFileChange(event) {
            this.form.profile_image = event.target.files[0];
        },

        submitForm() {
            const formData = new FormData();
            formData.append('username', this.form.username);
            formData.append('email', this.form.email);
            formData.append('date_of_birth', this.form.date_of_birth);
            formData.append('profile_image', this.form.profile_image);
            formData.append('password1', this.form.password1);
            formData.append('password2', this.form.password2);

            fetch('/petapp/getsignup/', {
                method: 'POST',
                headers: {
                  'X-CSRFToken': this.csrfToken, // Replace with your CSRF token
                },
                body: formData,
            })

            .then(response => response.json())

            .then(data => {
                this.form.username = data.username;
                this.form.email = data.email;
                this.form.date_of_birth = data.date_of_birth;
                this.form.password1 = data.password1;
                this.form.password2 = data.password2;
            })
            // .catch(error => console.error(error));
        }
    }
  }
</script>