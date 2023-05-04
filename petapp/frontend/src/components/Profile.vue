<template>
    <h1>MY PROFILE</h1>
    <div class="user-profile">
      <img :src="user.profile_image" alt="Profile Image" />
      <p>Username: {{ user.username }}</p>
      <p>Email: {{ user.email }}</p>
      <p>Date of Birth: {{ user.date_of_birth }}</p>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        user: {},
      };
    },
    async created() {
      try {
        const headers = {
          "Content-Type": "application/json",
          Authorization: `Token ${localStorage.getItem("token")}`,
        };
        const response = await axios.get("http://127.0.0.1:8000/petapp/getuserdetails/", {
          headers: headers,
        });
        this.user = response.data.user;
      } catch (error) {
        console.error("Error fetching user details: ", error);
      }
    },
  };
  </script>