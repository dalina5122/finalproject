<template>
    <div>
        <form @submit="postDog" enctype="multipart/form-data">
            <input type="file" id="picture_d2" required>
            <input type="text" id="name_d2" placeholder="Name" required>
            <input type="number" id="age_d2" placeholder="Age" required>
            <input type="date" id="date_d2" placeholder="Date" required>
            <select id="county_d2" required>
                <option disabled value="Select a County"></option>
                <option v-for="option in countyOptions" :value="option.value">
                    {{ option.label }}
                </option>
            </select>
            <input type="text" id="color_d2" placeholder="Color" required>
            <input type="text" id="description_d2" placeholder="Description" required>
            <input type="text" id="breed_d2" placeholder="Breed" required>
            <select id="gender_d2" required>
                <option v-for="option in genderOptions" :value="option.value">
                    {{ option.label }}
                </option>
            </select>            
            <select id="status_d2" required>
                <option v-for="option in statusOptions" :value="option.value">
                    {{ option.label }}
                </option>
            </select>  

            <button class='btn btn-outline-success my-2 my-sm-0' type="submit">Post</button>
        </form>
    </div>
</template>

<script>
  import {defineComponent} from 'vue';

  export default defineComponent({
    data() {
    return {
        countyOptions: [{value: 'AB', label: 'Alba'}, {value: 'AR', label: 'Arad'}, {value: 'AG', label: 'Arges'}, {value:'BC', label: 'Bacau'}, {value: 'BH', label: 'Bihor'}, {value: 'BN', label:'Bistrita-Nasaud'}, {value: 'BT', label: 'Botosani'},
        {value: 'BV', label: 'Brasov'}, {value: 'BR', label: 'Braila'}, {value: 'BZ', label: 'Buzau'}, {value: 'CS', label: 'Caras-Severin'}, {value: 'CL', label: 'Calarasi'}, {value: 'CJ', label: 'Cluj'},
        {value: 'CT', label: 'Constanta'}, {value: 'CV', label: 'Covasna'}, {value: 'DB', label: 'Dambovita'}, {value: 'DJ', label: 'Dolj'}, {value: 'GL', label: 'Galati'}, {value: 'GR', label: 'Giurgiu'}, {value: 'GJ', label: 'Gorj'},
        {value: 'HR', label: 'Harghita'}, {value: 'HD', label: 'Hunedoara'}, {value: 'IL', label: 'Ialomita'}, {value: 'IS', label: 'Iasi'}, {value: 'MM', label: 'Maramures'}, {value: 'MH', label: 'Mehedinti'}, {value: 'MS', label: 'Mures'},
        {value: 'OT', label: 'Olt'}, {value: 'PH', label: 'Prahova'}, {calue: 'SM', label: 'Satu Mare'}, {value: 'SJ', label: 'Salaj'}, {value: 'SB', label: 'Sibiu'}, {value: 'SV', label: 'Suceava'}, {value: 'TR', label: 'Teleorman'},
        {value: 'TM', label: 'Timis'}, {value: 'TL', label: 'Tulcea'}, {value: 'VS', label: 'Vaslui'}, {value: 'VL', label: 'Valcea'}, {value: 'VN', label: 'Vrancea'}],
        genderOptions: [{value: 'M', label: 'Male'}, {value:'F', label: 'Female'}, {value:'O', label: 'Other'}],
        statusOptions: [{value: 'L', label:'Lost'}, {value: 'F', label: 'Found'}, {value:'A', label: 'Adoption'}],
      }
    },

    methods:{
      async postDog(event){
        event.preventDefault();
        let dogFormData=new FormData();

        var input=document.getElementById('picture_d2');
        var new_picture_d=input.files[0];

        let new_picture_d_base64 = null;
        if (new_picture_d) {
          new_picture_d_base64 = await new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onloadend = () => resolve(reader.result);
            reader.onerror = reject;
            reader.readAsDataURL(new_picture_d);
          });
        }

        let new_name_d=document.getElementById('name_d2').value;
        let new_age_d=document.getElementById('age_d2').value;
        let new_date_d=document.getElementById('date_d2').value;
        let new_county_d=document.getElementById('county_d2').value;
        let new_color_d=document.getElementById('color_d2').value;
        let new_description_d=document.getElementById('description_d2').value;
        let new_breed_d=document.getElementById('breed_d2').value;
        let new_gender_d=document.getElementById('gender_d2').value;
        let new_status_d=document.getElementById('status_d2').value;

        let new_entry={
          name_d: new_name_d,
          age_d: new_age_d,
          date_d: new_date_d,
          county_d: new_county_d,
          color_d: new_color_d,
          description_d: new_description_d,
          breed_d: new_breed_d,
          gender_d: new_gender_d,
          status_d: new_status_d,
          picture_d: new_picture_d_base64,
        };
        console.log(new_entry)

        console.log("Sending data:", new_entry);
        let response=await fetch('http://127.0.0.1:8000/newdog/',{
          method: 'POST',
          headers: {
            "Authorization": `Token ${localStorage.getItem("token")}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(new_entry),
        });
        
        if(response.ok){
          document.getElementById('name_d2').value="",
          document.getElementById('age_d2').value="",
          document.getElementById('date_d2').value="",
          document.getElementById('county_d2').value="",
          document.getElementById('color_d2').value="",
          document.getElementById('description_d2').value="",
          document.getElementById('breed_d2').value="",
          document.getElementById('gender_d2').value="",
          document.getElementById('status_d2').value="",
          document.getElementById('picture_d2').value=""
          this.$router.push('/newdog');
        }
        else
          alert('Dog cannot be added');
      }
    }
  })
</script>