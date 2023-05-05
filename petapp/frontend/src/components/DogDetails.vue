<template>
    <div>
      <h1>{{ dog.name_d }}</h1>
      <!-- Add more details about the dog here -->
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        dog: {},
      };
    },
    async created() {
      try {
        const headers = {
          'Content-Type': 'application/json',
          Authorization: `Token ${localStorage.getItem('token')}`,
        };
        const response = await axios.get(`http://127.0.0.1:8000/petapp/dogdetails/${this.$route.params.id}/`, {
          headers: headers,
        });
  
        this.dog = response.data.dog;
      } catch (error) {
        console.error('Error fetching dog details:', error);
      }
    },
  };
  </script>