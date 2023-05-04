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
                            <template v-for="dog in dogs" :key="dog.id">
                                <tr>
                                    <td class="dog-picture">
                                        <img :src="getPicture(dog.picture_d)" alt="Dog picture" loading="auto">
                                    </td>

                                    <td>{{ dog.name_d }}</td>
                                    <td>{{ dog.age_d }}</td>
                                    <td>{{ dog.county_d }}</td>
                                    <td>{{ dog.color_d }}</td>
                                    <td>{{ dog.description_d }}</td>
                                    <td>{{ dog.date_d }}</td>
                                    <td>{{ dog.breed_d }}</td>
                                    <td>{{ dog.gender_d }}</td>
                                    <td>{{ dog.status_d }}</td>
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
    import axios from 'axios';

    export default{
        data(){
            return{
                dogIconSrc: '/media/dogicon.png',
                dogIconSrcHover: '/media/caticon.png',
                showForm: false,
                dogs: [],
            }
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