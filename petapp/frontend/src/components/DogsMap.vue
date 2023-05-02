<template>
    <div id="tab">

        <!-- TOP BAR -->
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <!-- DOG ICON -->
            <a class="navbar-brand">
                <div>
                    <img loading="auto" src="/media/dogicon.png" width="75">
                </div>
            </a>

            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <!-- POST BUTTON -->
            <div class="collapse navbar-collapse">
                <div class="nav navbar-nav">
                     <button class="btn btn-outline-success my-2 my-sm-0" @click="showForm=true">NEW POST</button>
                </div>
            </div>   
        </nav>

        <!-- SIDE MENU -->
        <div class="container-fluid">
            <div class="row flex-nowrap">
                <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-light">
                    <div class="d-flex flex-column align-items-center align-items-sm-start px-3 pt-2 text-black min-vh-50">

                        <a href="/" class="d-flex align-items-center pb-3 mb-md-0 me-md-auto text-black text-decoration-none">
                            <span class="fs-5 d-none d-sm-inline">MENU</span>
                        </a>

                        <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start" id="menu">
                            <li class="nav-item nav-link">
                                <a href="#" class="nav-link align-middle px-0">
                                    <i class="fs-4 bi-house"></i> <span class="ms-1 d-none d-sm-inline">Home</span>
                                </a>
                            </li>

                            <li class="nav-item nav-link">
                                <a href="#" class="nav-link px-0 align-middle">
                                    <i class="fs-4 bi-table"></i> <span class="ms-1 d-none d-sm-inline">Pet Care</span></a>
                            </li>

                        </ul>
                    </div>
                </div>

                <!-- LIST OF DOGS -->
                <div>
                    <li v-for="dog in dogs" :key="dog.id" class="dog-list">
                        <div class="dog-item">
                            <div class="dog-picture">
                                <img :src="getPicture(dog.picture_d)" alt="Dog picture" loading="auto">
                            </div>
                            <div class="dog-details">
                                {{ dog.name_d }} - {{ dog.age_d }} - {{ dog.county_d }} - {{ dog.color_d }} - {{ dog.description_d }} - {{ dog.date_d }} - {{ dog.breed_d }} - {{ dog.gender_d }} - {{ dog.status_d }}
                            </div>
                        </div>
                    </li>
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
        },

        components:{
            AddDog
        }
    }
</script>

<style scoped>
.dog-item {
    display: flex;
    flex-wrap: nowrap;
    align-items: center;
    gap: 1rem;
    padding: 0.5rem;
    border-bottom: 1px solid #ccc;
}

.dog-details {
    flex-grow: 1;
}

.dog-picture {
    width: 100px;
    height: 100px;
}

.dog-picture img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.dog-list{
    list-style: none;
}
</style>