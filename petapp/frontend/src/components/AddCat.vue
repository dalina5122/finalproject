<template>
    <div>
        <!-- FORM FOR POSTING A NEW CAT -->
        <form @submit="postCat" enctype="multipart/form-data">
            <input type="file" id="picture_c2" required>
            <input type="text" id="name_c2" placeholder="Name" required>
            <input type="number" id="age_c2" placeholder="Age" required>
            <input type="date" id="date_c2" placeholder="Date" required>
            <select id="county_c2" required>
                <option disabled value="Select a County"></option>
                <option v-for="option in countyOptions" :value="option.value">
                    {{ option.label }}
                </option>
            </select>
            <input type="text" id="color_c2" placeholder="Color" required>
            <input type="text" id="description_c2" placeholder="Description" required>
            <input type="text" id="breed_c2" placeholder="Breed" required>
            <select id="gender_c2" required>
                <option v-for="option in genderOptions" :value="option.value">
                    {{ option.label }}
                </option>
            </select>            
            <select id="status_c2" required>
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
        // OPTIONS FOR COUNTY, GENDER AND STATUS
        countyOptions: [{value: 'AB', label: 'Alba'}, {value: 'AR', label: 'Arad'}, {value: 'AG', label: 'Arges'}, {value:'BC', label: 'Bacau'}, {value: 'BH', label: 'Bihor'}, {value: 'BN', label:'Bistrita-Nasaud'}, {value: 'BT', label: 'Botosani'},
        {value: 'BV', label: 'Brasov'}, {value: 'BR', label: 'Braila'}, {value: 'BZ', label: 'Buzau'}, {value: 'CS', label: 'Caras-Severin'}, {value: 'CL', label: 'Calarasi'}, {value: 'CJ', label: 'Cluj'},
        {value: 'CT', label: 'Constanta'}, {value: 'CV', label: 'Covasna'}, {value: 'DB', label: 'Dambovita'}, {value: 'DJ', label: 'Dolj'}, {value: 'GL', label: 'Galati'}, {value: 'GR', label: 'Giurgiu'}, {value: 'GJ', label: 'Gorj'},
        {value: 'HR', label: 'Harghita'}, {value: 'HD', label: 'Hunedoara'}, {value: 'IL', label: 'Ialomita'}, {value: 'IS', label: 'Iasi'}, {value: 'IF', label: 'Iflov'}, {value: 'MM', label: 'Maramures'}, {value: 'MH', label: 'Mehedinti'}, {value: 'MS', label: 'Mures'},
        {value: 'NT', label: 'Neamt'}, {value: 'OT', label: 'Olt'}, {value: 'PH', label: 'Prahova'}, {calue: 'SM', label: 'Satu Mare'}, {value: 'SJ', label: 'Salaj'}, {value: 'SB', label: 'Sibiu'}, {value: 'SV', label: 'Suceava'}, {value: 'TR', label: 'Teleorman'},
        {value: 'TM', label: 'Timis'}, {value: 'TL', label: 'Tulcea'}, {value: 'VS', label: 'Vaslui'}, {value: 'VL', label: 'Valcea'}, {value: 'VN', label: 'Vrancea'}],
        genderOptions: [{value: 'M', label: 'Male'}, {value:'F', label: 'Female'}, {value:'O', label: 'Other'}],
        statusOptions: [{value: 'L', label:'Lost'}, {value: 'F', label: 'Found'}, {value:'A', label: 'Adoption'}],
      }
    },

    methods:{
      async postCat(event){
        event.preventDefault();
        let catFormData=new FormData();

        // PICTURE FORMATTING
        var input=document.getElementById('picture_c2');
        var new_picture_c=input.files[0];
        let new_picture_c_base64 = null;
        if (new_picture_c) {
          new_picture_c_base64 = await new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onloadend = () => resolve(reader.result);
            reader.onerror = reject;
            reader.readAsDataURL(new_picture_c);
          });
        }

        let new_name_c=document.getElementById('name_c2').value;
        let new_age_c=document.getElementById('age_c2').value;
        let new_date_c=document.getElementById('date_c2').value;
        let new_county_c=document.getElementById('county_c2').value;
        let new_color_c=document.getElementById('color_c2').value;
        let new_description_c=document.getElementById('description_c2').value;
        let new_breed_c=document.getElementById('breed_c2').value;
        let new_gender_c=document.getElementById('gender_c2').value;
        let new_status_c=document.getElementById('status_c2').value;

        let new_entry={
          name_c: new_name_c,
          age_c: new_age_c,
          date_c: new_date_c,
          county_c: new_county_c,
          color_c: new_color_c,
          description_c: new_description_c,
          breed_c: new_breed_c,
          gender_c: new_gender_c,
          status_c: new_status_c,
          picture_c: new_picture_c_base64,
        };
        console.log(new_entry)

        console.log("Sending data:", new_entry);
        let response=await fetch('http://127.0.0.1:8000/petapp/newcat/',{
          method: 'POST',
          headers: {
            "Authorization": `Token ${localStorage.getItem("token")}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(new_entry),
        });
        
        const responseData = await response.json();

        console.log('Full response object:', response);
        console.log('Response data:', responseData);

        if(response.ok){
          document.getElementById('name_c2').value="",
          document.getElementById('age_c2').value="",
          document.getElementById('date_c2').value="",
          document.getElementById('county_c2').value="",
          document.getElementById('color_c2').value="",
          document.getElementById('description_c2').value="",
          document.getElementById('breed_c2').value="",
          document.getElementById('gender_c2').value="",
          document.getElementById('status_c2').value="",
          document.getElementById('picture_c2').value="",
          this.$emit('cat-added', responseData.cat);        
        }
        
        else
          alert('Cat cannot be added');
      }
    }
  })
</script>