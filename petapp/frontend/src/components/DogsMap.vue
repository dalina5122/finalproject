<template>
    <div id="tab">

        <!-- TOP BAR -->
        <nav class="navbar navbar-expand-lg navbar-light bg-light">

            <!-- DOG ICON -->
            <a class="navbar-brand">
                <div>
                    <router-link to="/catsmap">
                        <img loading="auto" :src="dogIconSrc" @mouseover="dogIconSrc = dogIconSrcHover" @mouseout="dogIconSrc = '/media/dogicon.png'" width="75">
                    </router-link>
                </div>
            </a>

            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse">

                <!-- POST BUTTON -->
                <div class="nav navbar-nav">
                    <button class="btn btn-outline-success my-2 my-sm-0" @click="showForm=true">NEW POST</button>
                </div>

                <!-- LOG OUT BUTTON -->
                <div class="ms-auto">
                    <router-link to="/">
                        <img loading="auto" src="media/logout.png" @click="logout" width="75">
                    </router-link>
                </div>

                <!-- PROFILE BUTTON -->
                <div class="ms-auto">
                    <router-link to="/profile">
                        <img loading="auto" src="media/profile.png" width="75">
                    </router-link>
                </div>
            </div>   
        </nav>

        <CountyFilter :counties="counties" @county-selected="selectedCounty = $event" />


        <div class="container-fluid">
            <div class="row flex-nowrap">

                <!-- DOGS LIST -->
                <div>
                    <table class="table dog-table">
                        <thead>
                            <tr>
                                <th>Picture</th>
                                <th>Name</th>
                                <th>Age</th>
                                <th>County</th>
                                <th>Color</th>
                                <th>Description</th>
                                <th>Date</th>
                                <th>Breed</th>
                                <th>Gender</th>
                                <th>Status</th>
                            </tr>
                        </thead>

                        <tbody>
                            <template v-for="dog in filteredDogs" :key="dog.id">
                                <tr>
                                    <td class="dog-picture" @click="$router.push(`/dogdetails/${dog.id}`)" style="cursor: pointer;">
                                        <img :src="getPicture(dog.picture_d)" alt="Dog picture" loading="auto">
                                    </td>

                                    <td @click="$router.push(`/dogdetails/${dog.id}`)" style="cursor: pointer;">{{ dog.name_d }}</td>
                                    <td @click="$router.push(`/dogdetails/${dog.id}`)" style="cursor: pointer;">{{ dog.age_d }}</td>
                                    <td @click="$router.push(`/dogdetails/${dog.id}`)" style="cursor: pointer;">{{ dog.county_d }}</td>
                                    <td @click="$router.push(`/dogdetails/${dog.id}`)" style="cursor: pointer;">{{ dog.color_d }}</td>
                                    <td @click="$router.push(`/dogdetails/${dog.id}`)" style="cursor: pointer;">{{ dog.description_d }}</td>
                                    <td @click="$router.push(`/dogdetails/${dog.id}`)" style="cursor: pointer;">{{ dog.date_d }}</td>
                                    <td @click="$router.push(`/dogdetails/${dog.id}`)" style="cursor: pointer;">{{ dog.breed_d }}</td>
                                    <td @click="$router.push(`/dogdetails/${dog.id}`)" style="cursor: pointer;">{{ dog.gender_d }}</td>
                                    <td @click="$router.push(`/dogdetails/${dog.id}`)" style="cursor: pointer;">{{ dog.status_d }}</td>
                                </tr>
                            </template>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div v-if="showForm">
            <AddDog @dog-added="onDogAdded"/>
        </div>
    </div>
</template>


<script>
    import AddDog from '../components/AddDog.vue';
    import CountyFilter from '../components/CountyFilter.vue';
    import axios from 'axios';

    export default{
        data(){
            return{
                dogIconSrc: '/media/dogicon.png',
                dogIconSrcHover: '/media/caticon.png',
                showForm: false,
                dogs: [],
                selectedCounty: '',
                counties: [
                    {code: 'SM', name: 'Satu Mare', image: '/media/judete/satu-mare.png'},
                    {code: 'MM', name: 'Maramures', image: '/media/judete/maramures.png'},
                    {code: 'SV', name: 'Suceava', image: '/media/judete/suceava.png'},
                    {code: 'BT', name: 'Botosani', image: '/media/judete/botosani.png'},

                    {code: 'BH', name: 'Bihor', image: '/media/judete/bihor.png'},
                    {code: 'SJ', name: 'Salaj', image: '/media/judete/salaj.png'},
                    {code: 'BN', name: 'Bistrita-Nasaud', image: '/media/judete/bistrita-nasaud.png'},
                    {code: 'CJ', name: 'Cluj', image: '/media/judete/cluj.png'},
                    {code: 'MS', name: 'Mures', image: '/media/judete/mures.png'},
                    {code: 'HR', name: 'Harghita', image: '/media/judete/harghita.png'},
                    {code: 'NT', name: 'Neamt', image: '/media/judete/neamt.png'},
                    {code: 'IS', name: 'Iasi', image: '/media/judete/iasi.png'},
                    {code: 'BC', name: 'Bacau', image: '/media/judete/bacau.png'},
                    {code: 'VS', name: 'Vaslui', image: '/media/judete/vaslui.png'},

                    {code: 'AR', name: 'Arad', image: '/media/judete/arad.png'},
                    {code: 'AB', name: 'Alba', image: '/media/judete/alba.png'},
                    {code: 'TM', name: 'Timis', image: '/media/judete/timis.png'},
                    {code: 'HD', name: 'Hunedoara', image: '/media/judete/hunedoara.png'},
                    {code: 'SB', name: 'Sibiu', image: '/media/judete/sibiu.png'},
                    {code: 'BV', name: 'Brasov', image: '/media/judete/brasov.png'},
                    {code: 'CV', name: 'Covasna', image: '/media/judete/covasna.png'},
                    {code: 'VN', name: 'Vrancea', image: '/media/judete/vrancea.png'},
                    {code: 'GL', name: 'Galati', image: '/media/judete/galati.png'},

                    {code: 'CS', name: 'Caras-Severin', image: '/media/judete/caras-severin.png'},
                    {code: 'GJ', name: 'Gorj', image: '/media/judete/gorj.png'},
                    {code: 'VL', name: 'Valcea', image: '/media/judete/valcea.png'},
                    {code: 'AG', name: 'Arges', image: '/media/judete/arges.png'},
                    {code: 'DB', name: 'Dambovita', image: '/media/judete/dambovita.png'},
                    {code: 'PH', name: 'Prahova', image: '/media/judete/prahova.png'},
                    {code: 'BZ', name: 'Buzau', image: '/media/judete/buzau.png'},
                    {code: 'BR', name: 'Braila', image: '/media/judete/braila.png'},
                    {code: 'TL', name: 'Tulcea', image: '/media/judete/tulcea.png'},

                    {code: 'MH', name: 'Mehedinti', image: '/media/judete/mehedinti.png'},
                    {code: 'DJ', name: 'Dolj', image: '/media/judete/dolj.png'},
                    {code: 'OT', name: 'Olt', image: '/media/judete/olt.png'},
                    {code: 'TR', name: 'Teleorman', image: '/media/judete/teleorman.png'},
                    {code: 'IF', name: 'Ilfov', image: '/media/judete/ilfov.png'},
                    {code: 'IL', name: 'Ialomita', image: '/media/judete/ialomita.png'},
                    {code: 'GR', name: 'Giurgiu', image: '/media/judete/giurgiu.png'},
                    {code: 'CL', name: 'Calarasi', image: '/media/judete/calarasi.png'},
                    {code: 'CT', name: 'Constanta', image: '/media/judete/constanta.png'},
                ]

            }
        },

        computed: {
            filteredDogs() {
                if (this.selectedCounty) {
                return this.dogs.filter((dog) => dog.county_d === this.selectedCounty);
                }
                return this.dogs;
            },
        },

        async created(){
            try{
                const headers={
                        "Content-Type": "application/json",
                        Authorization: `Token ${localStorage.getItem("token")}`,
                };
                const response=await axios.get('http://127.0.0.1:8000/petapp/getdogs/',{
                    headers: headers
                });

                this.dogs=response.data.dogs.slice();
                console.log('Fetched dogs:', this.dogs);
                console.log(response.data);


            }
            catch(error){
                console.error("Error fetching dogs: ", error);
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

            onDogAdded(newDog) {
                this.dogs.push(newDog);
            },

            logout(){
                localStorage.removeItem("token");
            },
        },

        components:{
            AddDog,
            CountyFilter,
        }
    }
</script>

<style scoped>
.dog-table {
    width: 100%;
    table-layout: fixed;
}
.dog-table th,
.dog-table td {
    white-space: normal;
    word-wrap: break-word;
}
.dog-item {
    display: flex;
    flex-wrap: nowrap;
    align-items: center;
    gap: 1rem;
    padding: 0.5rem;
    border-bottom: 1px solid #ccc;
}

.dog-picture {
    width: 100px;
    height: 100px;
    object-fit: cover;
}

.dog-picture img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>