<template>
    <img loading='auto' src="media/profiletitle.png" width="400">

    <div class="row border border-secondary rounded">

      <div class="col-sm-4">
        <img :src="user.profile_image" alt="Profile Image" width="200" class="rounded"/>
        <button @click="showImageUpdate=!showImageUpdate" class="btn btn-outline-info my-2 my-sm-0">EDIT PICTURE</button>

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

    <div class="updateimage" v-if="showImageUpdate">
      <h4>Change your Picture</h4>
      <form @submit.prevent="updateImage">
        <input type="file" @change="onFileSelected" />
        <button class="btn btn-outline-info my-2 my-sm-0" type="submit">Change</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        user: {},
        showImageUpdate: false,
      };
    },

    methods:{
      onFileSelected(event) {
        this.selectedFile = event.target.files[0];
      },

      async updateImage() {
        if (!this.selectedFile) {
          alert("Please select an image file to upload.");
          return;
        }

        const formData = new FormData();
        formData.append("image", this.selectedFile);

        try {
          const headers = {
            Authorization: `Token ${localStorage.getItem("token")}`,
          };
          const response = await axios.post(
            "http://127.0.0.1:8000/petapp/updateimage/",
            formData,
            { headers: headers }
          );
          this.user = response.data.user;
          alert("Profile image updated successfully.");
        } catch (error) {
          console.error("Error updating profile image: ", error);
        }
        },
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