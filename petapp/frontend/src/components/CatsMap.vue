<template>
    <div id="tab">

        <!-- TOP BAR -->
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <!-- CAT ICON -->
            <a class="navbar-brand">
                <div>
                    <router-link to="/dogsmap">
                        <img loading="auto" :src="catIconSrc" @mouseover="catIconSrc = catIconSrcHover" @mouseout="catIconSrc = '/media/caticon.png'" width="75">
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

                <!-- CATS LIST -->
                <div>
                    <table class="table cat-table">
                        <thead>
                            <tr>
                                <th>Picture</th>
                                <th>Name</th>
                                <th>Date</th>
                                <th>Breed</th>
                                <th>Status</th>
                            </tr>
                        </thead>

                        <tbody>
                            <template v-for="cat in filteredCats" :key="cat.id">
                                <tr>
                                    <td class="cat-picture" @click="$router.push(`/catdetails/${cat.id}`)" style="cursor: pointer;">
                                        <img :src="getPicture(cat.picture_c)" alt="Cat picture" loading="auto">
                                    </td>

                                    <td @click="$router.push(`/catdetails/${cat.id}`)" style="cursor: pointer;">{{ cat.name_c }}</td>
                                    <td @click="$router.push(`/catdetails/${cat.id}`)" style="cursor: pointer;">{{ cat.date_c }}</td>
                                    <td @click="$router.push(`/catdetails/${cat.id}`)" style="cursor: pointer;">{{ cat.breed_c }}</td>
                                    <td @click="$router.push(`/catdetails/${cat.id}`)" style="cursor: pointer;">{{ cat.status_c }}</td>
                                </tr>
                            </template>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div v-if="showForm">
            <AddCat @cat-added="onCatAdded"/>
        </div>
    </div>
</template>


<script>
    import AddCat from '../components/AddCat.vue';
    import CountyFilter from '../components/CountyFilter.vue';
    import axios from 'axios';

    export default{
        data(){
            return{
                catIconSrc: '/media/caticon.png',
                catIconSrcHover: '/media/dogicon.png',
                showForm: false,
                cats: [],
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
            filteredCats() {
                if (this.selectedCounty) {
                    return this.cats.filter((cat) => cat.county_c === this.selectedCounty);
                }
                return this.cats;
            },
        },

        async created(){
            try{
                const headers={
                        "Content-Type": "application/json",
                        Authorization: `Token ${localStorage.getItem("token")}`,
                };
                const response=await axios.get('http://127.0.0.1:8000/petapp/getcats/',{
                    headers: headers
                });

                this.cats=response.data.cats.slice();
                console.log('Fetched cats:', this.cats);
                console.log(response.data);


            }
            catch(error){
                console.error("Error fetching cats: ", error);
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

            onCatAdded(newCat) {
                this.cats.push(newCat);
            },

            logout(){
                localStorage.removeItem("token");
            },
        },

        components:{
            AddCat,
            CountyFilter,
        }
    }
</script>

<style scoped>
.cat-table {
    width: 100%;
    table-layout: fixed;
}
.cat-table th,
.cat-table td {
    white-space: normal;
    word-wrap: break-word;
}
.cat-item {
    display: flex;
    flex-wrap: nowrap;
    align-items: center;
    gap: 1rem;
    padding: 0.5rem;
    border-bottom: 1px solid #ccc;
}

.cat-picture {
    width: 50px;
    height: 100px;
    object-fit: cover;
}

.cat-picture img {
    width: 150px;
    height: 150px;
    object-fit: cover;
}
</style>