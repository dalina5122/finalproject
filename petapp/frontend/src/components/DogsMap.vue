<template>
    <h1>DOGS MAP HERE</h1>
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