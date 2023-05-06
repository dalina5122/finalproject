<template>
    <div class="row border border-secondary rounded">

      <div class="col-sm-4">
      <div class="image-container">
        <img :src="getPicture(dog.picture_d)" alt="Picture" width="200" class="rounded"/>
      </div>
    </div>

      <div class="col-sm-6">
        <dl class="row">
          <dt class="col-sm-3">Name: </dt>
          <dd class="col-sm-9"> {{ dog.name_d }} </dd>

          <dt class="col-sm-3">Age: </dt>
          <dd class="col-sm-9"> {{ dog.age_d }} </dd>

          <dt class="col-sm-3">County: </dt>
          <dd class="col-sm-9"> {{ dog.county_d }} </dd>

          <dt class="col-sm-3">Color: </dt>
          <dd class="col-sm-9"> {{ dog.color_d }} </dd>

          <dt class="col-sm-3">Description: </dt>
          <dd class="col-sm-9"> {{ dog.description_d }} </dd>

          <dt class="col-sm-3">Date: </dt>
          <dd class="col-sm-9"> {{ dog.date_d }} </dd>

          <dt class="col-sm-3">Breed: </dt>
          <dd class="col-sm-9"> {{ dog.breed_d }} </dd>

          <dt class="col-sm-3">Gender: </dt>
          <dd class="col-sm-9"> {{ dog.gender_d }} </dd>

          <dt class="col-sm-3">Status: </dt>
          <dd class="col-sm-9"> {{ dog.status_d }} </dd>
        </dl>
      </div>

    </div>

  </template>
  
<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        dog: {},
        ownerId: null,
      };
    },

    async created() {
      try {
        const headers = {
          'Content-Type': 'application/json',
          Authorization: `Token ${localStorage.getItem('token')}`,
        };

        console.log('Request headers:', headers);

        const response = await axios.get(`http://127.0.0.1:8000/petapp/dogdetails/${this.$route.params.id}`, {
          headers: headers,
        });

        this.dog = response.data.dog;

        console.log('Fetched dog:', this.dog);


        const userResponse = await axios.get('http://127.0.0.1:8000/petapp/getuserid/', {
          headers: headers,
        });

        this.ownerId = userResponse.data.id;
        console.log('Logged-in user ID:', this.ownerId);
        console.log('Dog owner ID:', this.dog.owner);
      } 

      catch (error) {
        console.error('Error fetching dog details:', error);
      }
    },

    methods:{
      getPicture(pictureBase64){
        if(pictureBase64){
          return 'data:image/jpeg;base64,' + pictureBase64;
        }

        else{
          return 'petimages';
        }
      },
    }
  };
</script>

<style>
  .image-container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
  }
</style>