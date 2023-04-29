<template>
    <div>
        <form @submit.prevent="submitForm" enctype="multipart/form-data">
            <input type="file" v-on:change="onFileChange" ref="fileInput">
            <input type="text" v-model="name_d" placeholder="Name" required>
            <input type="number" v-model="age_d" placeholder="Age" required>
            <input type="date" v-model="date_d" placeholder="Date" required>
            <select v-model="county_d" required>
                <option disabled value="Select a County"></option>
                <option v-for="option in countyOptions" :value="option.value">
                    {{ option.label }}
                </option>
            </select>
            <input type="text" v-model="color_d" placeholder="Color" required>
            <input type="text" v-model="description_d" placeholder="Description" required>
            <input type="text" v-model="breed_d" placeholder="Breed" required>
            <select v-model="gender_d" required>
                <option v-for="option in genderOptions" :value="option.value">
                    {{ option.label }}
                </option>
            </select>            
            <select v-model="status_d" required>
                <option v-for="option in statusOptions" :value="option.value">
                    {{ option.label }}
                </option>
            </select>  

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
        status_d: '',
        countyOptions: [{value: 'AB', label: 'Alba'}, {value: 'AR', label: 'Arad'}, {value: 'AG', label: 'Arges'}, {value:'BC', label: 'Bacau'}, {value: 'BH', label: 'Bihor'}, {value: 'BN', label:'Bistrita-Nasaud'}, {value: 'BT', label: 'Botosani'},
        {value: 'BV', label: 'Brasov'}, {value: 'BR', label: 'Braila'}, {value: 'BZ', label: 'Buzau'}, {value: 'CS', label: 'Caras-Severin'}, {value: 'CL', label: 'Calarasi'}, {value: 'CJ', label: 'Cluj'},
        {valu: 'CT', label: 'Constanta'}, {value: 'CV', label: 'Covasna'}, {value: 'DB', label: 'Dambovita'}, {value: 'DJ', label: 'Dolj'}, {value: 'GL', label: 'Galati'}, {value: 'GR', label: 'Giurgiu'}, {value: 'GJ', label: 'Gorj'},
        {value: 'HR', label: 'Harghita'}, {value: 'HD', label: 'Hunedoara'}, {value: 'IL', label: 'Ialomita'}, {value: 'IS', label: 'Iasi'}, {value: 'MM', label: 'Maramures'}, {value: 'MH', label: 'Mehedinti'}, {value: 'MS', label: 'Mures'},
        {value: 'OT', label: 'Olt'}, {value: 'PH', label: 'Prahova'}, {calue: 'SM', label: 'Satu Mare'}, {value: 'SJ', label: 'Salaj'}, {value: 'SB', label: 'Sibiu'}, {value: 'SV', label: 'Suceava'}, {value: 'TR', label: 'Teleorman'},
        {value: 'TM', label: 'Timis'}, {value: 'TL', label: 'Tulcea'}, {value: 'VS', label: 'Vaslui'}, {value: 'VL', label: 'Valcea'}, {value: 'VN', label: 'Vrancea'}],
        genderOptions: [{value: 'M', label: 'Male'}, {value:'F', label: 'Female'}, {value:'O', label: 'Other'}],
        statusOptions: [{value: 'L', label:'Lost'}, {value: 'F', label: 'Found'}, {value:'A', label: 'Adoption'}],
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
          const newDogId = response.data.id;
          console.log(`New dog created with ID: ${newDogId}`);
          
          this.age_d = '';
          this.name_d = '';
          this.picture_d = null;
          this.county_d = '';
          this.color_d = '';
          this.description_d = '';
          this.date_d = '';
          this.breed_d = '';
          this.gender_d = '';
          this.status_d = '';

          alert('Dog created successfully!');
        })
        .catch(error => {
          console.log(error.response.data);
          alert('Error creating dog. Please try again later.');
        });
    }
  }
}
</script>