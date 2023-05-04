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

        <!-- SIDE MENU -->
        <div class="container-fluid">
            <div class="row flex-nowrap">

                <!-- DOGS LIST -->
                <div>
                    <table class="table cat-table">
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
                            <template v-for="cat in cats" :key="cat.id">
                                <tr>
                                    <td class="cat-picture">
                                        <img :src="getPicture(cat.picture_c)" alt="Cat picture" loading="auto">
                                    </td>

                                    <td>{{ cat.name_c }}</td>
                                    <td>{{ cat.age_c }}</td>
                                    <td>{{ cat.county_c }}</td>
                                    <td>{{ cat.color_c }}</td>
                                    <td>{{ cat.description_c }}</td>
                                    <td>{{ cat.date_c }}</td>
                                    <td>{{ cat.breed_c }}</td>
                                    <td>{{ cat.gender_c }}</td>
                                    <td>{{ cat.status_c }}</td>
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
    import axios from 'axios';

    export default{
        data(){
            return{
                catIconSrc: '/media/caticon.png',
                catIconSrcHover: '/media/dogicon.png',
                showForm: false,
                cats: [],
            }
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
    width: 100px;
    height: 100px;
    object-fit: cover;
}

.cat-picture img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>