<template>
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

    <div class="container">
        <div>
            <img loading="auto" src="/media/map.png" width="800">
        </div>

        <!-- <div>
            <svg width="400" height="110">
                <rect width="300" height="100" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
            </svg>
        </div> -->
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