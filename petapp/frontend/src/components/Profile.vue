<template>
    <img loading='auto' src="media/profiletitle.png" width="400">
    <div class="row">

      <div class="col-sm-4">
        <img :src="user.profile_image" alt="Profile Image" width="200"/>
        <button class="btn btn-outline-info my-2 my-sm-0">EDIT PICTURE</button>

      </div>

      <div class="col-sm-6">
        <p style="font-weight: bold;">Username:</p>
        <p> {{ user.username }}</p>

        <p style="font-weight: bold;">Email:</p>
        <p> {{ user.email }}</p>

        <p style="font-weight: bold;">Date of Birth:</p>
        <p> {{ user.date_of_birth }}</p>
      </div>

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