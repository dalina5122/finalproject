<template>
    <div>
        <form @submit.prevent="submitForm" enctype="multipart/form-data">
            <input type="file" v-on:change="onFileChange" ref="fileInput">
            <input type="text" v-model="name_d" placeholder="Name" required>
            <input type="number" v-model="age_d" placeholder="Age" required>
            <input type="date" v-model="date_d" placeholder="Date" required>
            <input type="text" v-model="county_d" placeholder="County" required>
            <input type="text" v-model="color_d" placeholder="Color" required>
            <input type="text" v-model="description_d" placeholder="Description" required>
            <input type="text" v-model="breed_d" placeholder="Breed" required>
            <input type="text" v-model="gender_d" placeholder="Gender" required>
            <input type="text" v-model="status_d" placeholder="Status" required>
            <button class='btn btn-outline-success my-2 my-sm-0' type="submit">Post</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
        age_d: '',
        name_d: '',
        picture_d: null,
        county_d: '',
        color_d: '',
        description_d: '',
        date_d: '',
        breed_d: '',
        gender_d: '',
        status_d: ','
    }
  },
  methods: {
    onFileChange(event) {
      this.picture_d = event.target.files[0];
    },

    submitForm() {
      const data = new FormData();
      data.append('age_d', this.age_d);
      data.append('name_d', this.name_d);
      data.append('county_d', this.county_d);
      data.append('picture_d', this.picture_d);
      data.append('color_d', this.color_d);
      data.append('description_d', this.description_d);
      data.append('date_d', this.date_d);
      data.append('breed_d', this.breed_d);
      data.append('gender_d', this.gender_d);
      data.append('status_d', this.status_d)

      axios.post('http://localhost:8000/newdog/', data)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error.response.data);
        });
    }
  }
}
</script>