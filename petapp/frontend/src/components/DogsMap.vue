<template>
    <!-- TOP BAR -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <!-- dog icon-click to switch to cat map -->
        <a class="navbar-brand">
            <div>
                <img loading="auto" src="/media/dogicon.png" width="75"> Filter By:
            </div>
        </a>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <!-- filters -->
        <div class="collapse navbar-collapse">
            <div class="nav navbar-nav">
                <a class="nav-item nav-link">X</a>
                <a class="nav-item nav-link">Y</a>
                <a class="nav-item nav-link">Z</a>

                <button class="btn btn-outline-success my-2 my-sm-0">Done</button>
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

            <!-- map -->
            <div class="col-auto">
                <img loading="auto" src="/media/map.png" width="800">
            </div>
        </div>
    </div>


</template>


<script lang="ts">
    import {defineComponent} from 'vue'

    export default defineComponent({
        data(){
            return{
                pet: [] as any,
                pets: [] as {id: number, age: string, name: string, location: string, color: string, description: string, date: string, breed: string, user: string} [],
                allowUpload: false,
            }
        },

        props: {
            user_id: Number,
        },

        methods: {
            async fetchPets(){
                let response = await fetch("http://localhost:8000/petapp/api/dogs/",{
                        credentials: "include",
                        mode: "cors",
                        referrerPolicy: "no-referrer",
                });

                let data = await response.json()
                console.log(data)
                this.pets = data.pets
            },


            async fetchPet(pet_id: number){
                let response = await fetch("http://localhost:8000/petapp/api/dog/" + pet_id);
                let data = await response.json()
                this.pet = data
            },
        }


    });

</script>